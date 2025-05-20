import gdb

class VfioGetSectionIovaRangeBreakpoint(gdb.Breakpoint):
    def __init__(self):
        super(VfioGetSectionIovaRangeBreakpoint, self).__init__("vfio_get_section_iova_range", internal=False)
        self.silent = True

    def stop(self):
        frame = gdb.selected_frame()
        print("\n=== vfio_get_section_iova_range ENTRY ===")

        # Print all arguments
        print("Arguments:")
        try:
            gdb.execute("info args")
        except Exception as e:
            print(f"Error getting args: {e}")

        # Print local variables
        print("\nLocal variables at entry:")
        try:
            gdb.execute("info locals")
        except Exception as e:
            print(f"Error getting locals: {e}")

        # Continue execution but set a finish breakpoint
        finishBp = gdb.FinishBreakpoint(internal=True)
        return False

class VfioGetSectionIovaRangeFinishBreakpoint(gdb.FinishBreakpoint):
    def __init__(self):
        super(VfioGetSectionIovaRangeFinishBreakpoint, self).__init__(internal=True)
        self.silent = True

    def stop(self):
        print("\n=== vfio_get_section_iova_range EXIT ===")

        # Get return values
        print("Return values:")
        try:
            result = gdb.parse_and_eval("$_")
            print(f"Return value: {result}")

            # Try to extract start and end values
            try:
                start = gdb.parse_and_eval("*start")
                print(f"*start: 0x{int(start):x}")
            except Exception as e:
                print(f"Error getting start: {e}")

            try:
                end = gdb.parse_and_eval("*end")
                print(f"*end: 0x{int(end):x}")
            except Exception as e:
                print(f"Error getting end: {e}")

        except Exception as e:
            print(f"Error getting return value: {e}")

        # Print backtrace
        print("\nCalled from:")
        gdb.execute("backtrace 3")

        return False

class VfioListenerRegionAddBreakpoint(gdb.Breakpoint):
    def __init__(self):
        super(VfioListenerRegionAddBreakpoint, self).__init__("vfio_listener_region_add", internal=False)
        self.silent = True

    def stop(self):
        frame = gdb.selected_frame()
        print("\n=== vfio_listener_region_add ===")

        # Print all arguments
        print("Arguments:")
        try:
            gdb.execute("info args")
        except Exception as e:
            print(f"Error getting args: {e}")

        # Try to get specific values we're interested in
        try:
            section = frame.read_var("section")
            print(f"\nSection details:")
            print(f"  section->offset_within_address_space: 0x{int(section['offset_within_address_space']):x}")

            mr = section['mr']
            print(f"  Memory region: {mr}")
            print(f"  Memory region name: {mr['name'].string()}")
            print(f"  Memory region size: 0x{int(mr['size']):x}")
            print(f"  Memory region addr: 0x{int(mr['addr']):x}")
            print(f"  Memory region offset: 0x{int(mr['offset']):x}")

            offset_within_region = frame.read_var("offset_within_region")
            print(f"  offset_within_region: 0x{int(offset_within_region):x}")

            try:
                iova = frame.read_var("iova")
                print(f"  iova: 0x{int(iova):x}")
            except:
                print("  iova not yet calculated")

        except Exception as e:
            print(f"Error accessing section details: {e}")

        # Continue execution
        return False

class VfioAddressSpaceSetup(gdb.Command):
    """Command to examine VFIO address space setup"""
    def __init__(self):
        super(VfioAddressSpaceSetup, self).__init__("vfio-as-setup", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        print("=== VFIO Address Space Setup ===")

        # Try to find and print VFIOAddressSpace structures
        try:
            gdb.execute("p vfio_address_spaces")
        except:
            print("Could not find vfio_address_spaces")

        # Try to find and print IOMMU info
        try:
            print("\nIOMMU Type:")
            gdb.execute("p vfio_host_iommu_type")
        except:
            print("Could not find vfio_host_iommu_type")

        # Try to find DMA mapping info
        try:
            print("\nDMA mapping info:")
            gdb.execute("info variables vfio_dma")
        except:
            print("Could not find vfio_dma variables")

class VfioTraceInvalidIova(gdb.Command):
    """Command to trace IOVA calculation and detect invalid values"""
    def __init__(self):
        super(VfioTraceInvalidIova, self).__init__("vfio-trace-invalid-iova", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        # Set up breakpoints for key functions
        VfioGetSectionIovaRangeBreakpoint()
        VfioListenerRegionAddBreakpoint()

        # Add a conditional watchpoint for large IOVA values
        try:
            # This is a heuristic - we're assuming IOVAs above this threshold might be invalid
            threshold = 0x100000000000  # 2^44
            cmd = f"watch iova if iova > {threshold}"
            gdb.execute(cmd)
            print(f"Watchpoint set for iova > 0x{threshold:x}")
        except Exception as e:
            print(f"Could not set watchpoint: {e}")

        print("IOVA tracing enabled. Run the program to collect data.")

def register_vfio_commands():
    VfioAddressSpaceSetup()
    VfioTraceInvalidIova()
    print("VFIO IOVA tracing helpers loaded")

register_vfio_commands()
import gdb

def analyze_vfio_get_section_iova_range():
    """Analyze the vfio_get_section_iova_range function to understand IOVA calculation"""
    print("=== Analyzing vfio_get_section_iova_range implementation ===")

    # Get the function source code
    try:
        gdb.execute("list vfio_get_section_iova_range")
    except Exception as e:
        print(f"Could not list function source: {e}")

    # Set a breakpoint at the function
    try:
        bp = gdb.Breakpoint("vfio_get_section_iova_range", internal=True)
        print("Breakpoint set. Run the program until it hits this function.")
        print("Then use 'step' to walk through the calculation.")
    except Exception as e:
        print(f"Could not set breakpoint: {e}")

class VfioIovaCalculationAnalysis(gdb.Command):
    """Command to analyze IOVA calculation"""
    def __init__(self):
        super(VfioIovaCalculationAnalysis, self).__init__("vfio-analyze-iova-calc", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        analyze_vfio_get_section_iova_range()

VfioIovaCalculationAnalysis()
print("VFIO IOVA calculation analysis command added")

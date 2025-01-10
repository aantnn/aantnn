# 👨‍💻 Валишин Антон

📱 **Telegram:** [https://t.me/antnn1](https://t.me/antnn1)  
🏠 **Проживает:** Москва  
🌍 **Гражданство:** Россия, есть разрешение на работу: Россия  
🏢 **Не готов к переезду, не готов к командировкам**

---
## 💼 Желаемая должность и зарплата
**DevOps/SRE**

### 🔧 Специализации:
- 🛠️ DevOps-инженер
- 💻 Программист, разработчик
- 🖥️ Системный администратор
- 🎯 Специалист технической поддержки

**Занятость:** полная занятость, частичная занятость, проектная работа  
**График работы:** удаленная работа  
**Желательное время в пути до работы:** не более часа  


## 🚀 Проекты
### 🔄 GitLab Test Pipeline 
- Исследовав исходники GitLab Auto DevOps, реализовал простое тестовое приложение с использованием Auto DevOps для автоматической сборки и развертывания, применяя файл `values.yaml` и `KUBE_CONTEXT`.
- Настроил GitLab Kubernetes Agent, предоставив доступ через файл конфигурации `config.yaml`.  
  [Ссылка на конфигурацию](https://gitlab.com/cicdantnn/kube-agent/-/blob/main/.gitlab/agents/k8s-agent/config.yaml?ref_type=heads)
- Установил GitLab Runner, зарегистрировал его и настроил для работы с Docker.
- Решил проблему с подключением к Docker Daemon, добавив необходимые параметры в конфигурацию `config.toml`.  
  [Ссылка на проект](https://gitlab.com/cicdantnn/flask-test)

---
### ⚙️ Ansible Action Plugin
**Технологии:** Python, PowerShell, C#, Win32, COM, IaC  
- Плагин для генерации файла ответов `unattend.xml` для автоустановки Windows и автоустановки драйверов.
- Генерация golden-образа Windows с базовыми настройками, которые вы задали, установка драйверов, программ, настройка IP, выбор редакции ОС в режиме автоустановки через Ansible playbook.  
  [Ссылка на проект](https://github.com/antnn/win-setup-action-ansible)
- Полностью самостоятельно решена проблема с неправильной инициализацией COM интерфейса.  
  При вызове `this` рантаймом присваивалось `category`, следовательно, терялся указатель на объект, и я получал ошибку:  
  ```
  INetwork::SetCategory(category)
  this=category -> 0x800706F4
  ```
  Решение в этой [строчке](https://github.com/antnn/win-setup-action-ansible/blob/9fc6809b9f6c502e4462af076a35a1197b5170c3/action_plugins/templates/main.cs#L1273) без Reflection.  </br>Мой issue по `COM` `C#` `0x800706F4`, в котором, я не получил ответа, но я смог решить задачу сам
без Reflection [learn.microsoft.com/en-us/answers/](https://learn.microsoft.com/en-us/answers/questions/1467985/(answered)-inetwork-setcategory(-networkcategory-p))


---
### 📱 Android Port of SoftEther VPN
- Разработка порта SoftEther VPN для Android.
- Использование CMake для сборки проекта и всех зависимостей.
- Решена непростая проблема с очередью зависимостей при сборке Ninja.  
  Можно погуглить `ExternalProject_Add` и `Ninja`.  
- Стала возможна кодогенерация заголовочных файлов без полной предварительной сборки проекта, примерно:  
  ```bash
   make build_generated  # отыскал подходящий target
  ```
- [Issue `cmake` и кодогенерация при конфигурации](https://discourse.cmake.org/t/design-cmake-projects-with-autocode-generators/9011/2)</br>
- [Как я решил эту задачу](https://github.com/antnn/SimpleVirtualNetwork/blob/d04943e1d1fbd892d5d751e884c6a86ddd84c117/nativevpn/src/main/cpp/cmake/modules/FindOpenSSL.cmake#L80)
  </br>
  [Ссылка на проект](https://github.com/antnn/SimpleVirtualNetwork)


---
### 🔒 Libvirt and Docker Test 
**Технологии:** `IaC`, `Docker`, `PowerShell`, `LibVirt`, `Serial PTY`, `Active Directory` 
- Контейнер для автоматизированного тестирования сценария, в котором все настраивается с
нуля с чистых образов автоматически из кода:
- Автоматическая настройка Mikrotik с использованием serial pty консоли `console.py`:
Mikrotik Cloud Hosted Router с SSTP VPN выступает маршрутизатором для `Windows Server AD`
сервер
- Автонастройка через серийную [консоль](https://github.com/antnn/ad-winserv-ros/blob/main/console.py)
- Первоначальная настройка `Windows AD`, через `PowerShell` <br>
  [Ссылка на проект](https://github.com/antnn/SimpleVirtualNetwork)

---
### 📧 Postfix в контейнере (podman)
- На своем ПК, localhost: `MTA`, `SMTP` для отправки писем со своего домена. 
- Настроены `SPF`, `DNS`, `PTR`, `DKIM` и `ARC`. 
- Схема: `localhost -> [ sshtun 0.0.0.0/0 via tun0 -> VPS/VDS ] -> gmail/outlook/etc`
- Успешно проходит спам проверки Gmail.com, Outlook.com. 
- Для входящей почты Cloudflare Email Routing
  [Ссылка на проект](https://github.com/antnn/gists/blob/main/postfix/)

---
### 🔐 E2E зашифрованная форма 
- `Webcrypto`, `webworker`, `RSA-OAEP` Сообщение приходит мне на email, код для дешифровки в конце скрипта (ключ не подойдет)
  https://valishin.ru/script.js

---
### 📢 Git notifier
- Уведомления об изменениях в репах (поллинг).<br>
https://github.com/antnn/git-notifier/blob/main/src/main.rs

---
### 🧮 Калькулятор погрешностей
- Справа будет превью-демо, Webcontainer <br>
https://stackblitz.com/edit/angularcalc2022?file=src%2Fapp%2Fmodel%2FInstrument.ts


---
### 🌟 Участие в opensource
- Комментарий для воспроизведения бага при использовании учетного токена (credential) в
PowerShell <br> https://github.com/microsoft/CSS-Exchange/issues/1917#issuecomment-2379227093
- Различные баг репорты в Redhat, etc. Установка маршрута до сервера через default GW,
ошибочно игнорируя существующие маршруты. В результате разрыв VPN соединения. Смог
обнаружить участок кода с ошибкой. Для тестирования сценария использовал `docker`,
`nsenter`, `VETH` (virtual Ethernet)
https://github.com/antnn/gists/blob/main/network-manager-bug-1641.sh

---

## 🎓 Образование
**Уровень:** Среднее образование  

---
## 🛠️ Навыки
**Языки:**  
- 🇷🇺 Русский — Родной  
- 🇬🇧 Английский — B2 (Средне-продвинутый)  

**Технические навыки:**  
Linux, Bash, Docker, PowerShell, Ansible, Python, Windows API, Windows, CMake, C/C++, Rust, GitLab, DevOps, Git, CI/CD  

---

## Дополнительная информация
## 🔑 Ключевые навыки:
- ✨ Самостоятельность в решении задач
- 🔄 Адаптация под существующий code-style
- 👥 Взаимодействие с командой
---

## 💻 Языки программирования:
C/C++, Rust, JavaScript, TypeScript, C#, Python, PowerShell  

---

### 💡 Почему именно ИТ?
  Очень часто спрашивают почти каждый раз: "почему именно ИТ?"...
<br>До того как решил перейти, поскольку разочаровался качеством образования по физике, в
качестве хобби, для себя с 15 лет ставил и настраивал виртуальные серверы VPS с `FreeBSD` от
`ISP Systems`, т.е был знаком с контейнерами уже много лет тому назад (2005-2006).... когда
никакого `docker` и не было.... 
<br>Устанавливал чат-бота `Sulci` для `Jabber` конференций на той же
FreeBSD, собирая из портов настраивал сервер и привязку доменного имени для своего
сайта (Joomla), с помощью панели `ISPManager` и `VDSManager`, `phpmyadmin`. 
<br>И все это я делал
с телефона с `J2ME` (Siemens C75), купив книгу по `FreeBSD`, через `Opera Mini mod` и `SSH`
клиенты на `J2ME`, поскольку тогда у меня не было ПК.... <br>
Пытался что-то разузнать, касаемо
вопросов по `FreeBSD` или книги по ассемблеру для `ARM` под Siemens (`IAR`, `V_Klay`, `ELF`) у
сообществ в чатах... 
<br>Надеюсь, я заранее ответил на ваш вопрос почему именно ИТ?

---

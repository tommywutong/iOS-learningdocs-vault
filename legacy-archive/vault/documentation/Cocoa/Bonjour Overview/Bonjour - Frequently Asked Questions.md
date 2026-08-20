---
title: Bonjour 概述
apple_id: 10000119i
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Articles/faq.html
archived_at: '2026-07-15T07:17:14.976781Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Bonjour 概述](About%20Bonjour.md)


[下一页](Document%20Revision%20History.md)[上一页](Bonjour%20Operations.md)

# Bonjour - 常见问题

本附录介绍关于 Bonjour 的常见问题。

Bonjour 又称零配置联网，它让 IP 网络上的计算机、设备和服务能被自动发现。Bonjour 使用业界标准的 IP 协议，让设备无需录入 IP 地址或配置 DNS 服务器就能自动互相发现。具体来说，Bonjour 让 IP 地址无需 DHCP 服务器即可自动分配，让名称到地址的转换无需 DNS 服务器，让服务发现无需目录服务器。Bonjour 是一个开放协议，Apple 已将其提交给 IETF，作为标准制定工作的一部分。要了解更多信息，请查阅 [Bonjour 协议规范](https://developer.apple.com/networking/bonjour/specs.html)，其中详细说明了构成链路本地 Bonjour 和广域 Bonjour 的各项技术。

mDNSResponder 是一项 Bonjour 系统服务，它实现了用于发现本地网络上服务的多播 DNS 服务发现，以及用于发现世界任意角落服务的单播 DNS 服务发现。mDNSResponder 内置于 [OS X 和 iOS](http://www.apple.com/support/bonjour/)，也可以作为 [Bonjour for Windows](https://developer.apple.com/downloads/index.action?q=Bonjour%20SDK%20for%20Windows) 的一部分下载。iTunes、iPhoto、Messages、Safari 等应用程序都借助 mDNSResponder 实现零配置的网络音乐分享、照片分享、聊天和文件共享，以及发现打印机、网络摄像头等硬件设备的远程用户界面。mDNSResponder 还用于发现 Bonjour 打印机和连接在 AirPort Extreme 与 Express 基站上的 USB 打印机并向其打印。mDNSResponder 是开源的，我们鼓励硬件设备厂商把 [mDNSResponder 源代码](https://developer.apple.com/opensource)直接嵌入自己的产品，以享受零配置联网带来的好处。

是的。OS X 上首个版本的 DNS 服务发现（[DNS-SD](http://files.dns-sd.org/draft-cheshire-dnsext-dns-sd.txt)）把重点放在面向单链路网络的多播 DNS（[mDNS](http://files.multicastdns.org/draft-cheshire-dnsext-multicastdns.txt)）上，因为这是当时 IP 软件支持得最差的环境。Bonjour 使用动态 DNS 更新（[RFC 2316](http://www.ietf.org/rfc/rfc2136.txt)）和单播 DNS 查询来实现广域服务发现。

会的，会持续一段时间。最终，这条 DNS 记录会到达它的生存时间上限并消失。作为应用开发者，如果你用 Bonjour 连接某台主机而连接失败，可以要求 Bonjour 重新确认该记录。这个过程在 _[NSNetServices and CFNetServices Programming Guide](../../Networking/NSNetServices%20and%20CFNetServices%20Programming%20Guide/About%20NSNetServices%20and%20CFNetServices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomzw)_ 中有更详细的说明。

在 iOS 5 及更高版本中，应用必须显式选择加入才能通过蓝牙进行服务发现，并且必须使用低层的 DNS Service Discovery C API 来解析服务。更多信息请参阅 _[Bonjour over Bluetooth on iOS 5 and Later](https://developer.apple.com/library/archive/qa/qa1753/_index.html#//apple_ref/doc/uid/DTS40011315)_。

服务浏览器会消耗资源，所以如果你根本不打算用到这些数据，就不该让它一直跑着。不过，在连接某个服务的过程中保持服务浏览器运行通常是个好主意。如果那次连接失败了，正在运行的浏览器会促使 Bonjour 更积极地重新验证可能已经失效的服务条目，从而让服务列表更准确。

一般来说，如果你没有显示任何包含该列表的用户界面元素，也没有正在主动连接任何服务，那么多半就应该停掉浏览器。不过这只是一条通用建议；无论何种情况，你都应该以给用户带来最佳体验为准。

可以。Bonjour 定义了一种新的服务发现协议（[DNS-SD](http://files.dns-sd.org/draft-cheshire-dnsext-dns-sd.txt)），但它对你所发现的服务类型不作任何限制。因此，你发现 SOAP 服务和发现 Messages 好友、iTunes 音乐库一样容易。换句话说，Bonjour 既支持 SOAP over HTTP，也支持其他任何构建在 TCP/IP 或 UDP/IP 之上的应用协议。

是的。很多人似乎没意识到 Bonjour 也能做通知，原因大概在于这本来就是服务发现协议的一个内在属性。在设计良好的发现协议里，你用来发现某项信息的协议，同样可以用来发现该信息的变化。发现静态信息、发现可变信息，以及发现可变信息何时改变，只不过是同一条谱系上的不同位置而已。想看使用 Bonjour "通知"的应用实例，可以看看 Messages。当你把状态从"在线"改成"离开"或输入一条状态消息时，本地网络上所有其他 Messages 客户端都会收到这一变化的通知。

这项技术在 _[NSNetServices and CFNetServices Programming Guide](../../Networking/NSNetServices%20and%20CFNetServices%20Programming%20Guide/About%20NSNetServices%20and%20CFNetServices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomzw)_ 中有更详细的说明。

默认情况下，你应该选一个人类可读、能唯一描述该服务的名称。以 iTunes 为例，它把本机用户的名和姓组合起来作为音乐分享的默认名称，例如 "Isaac Newton's Music"。对大多数硬件设备而言，默认服务名应当是产品完整的品牌和型号，例如 "Apple MacBook Pro" 之类。请记住，这只是开箱即用的默认名称，你应该允许用户自定义服务名，以便区分网络上的多台设备或多个服务。

对于要注册服务的 OS X 应用开发者来说，在一台电脑上只保留该服务的一个实例往往是合理的做法（而不是在多个账户下运行的每个应用实例各有一个）。这种情况下，与其让你的应用自己弹出界面让用户输入所通告服务的名称，不如直接用系统提供的默认名称来注册，也就是"共享"偏好设置面板中的"电脑名称"，这样更省事。如果你在注册时把服务名传成空字符串（""），系统就会自动使用"电脑名称"。传空字符串还会自动处理名称冲突，做法是在名称末尾追加一个数字。

不过，也有些服务会在同一台电脑上托管多个实例。例如，带三台打印机的打印服务器应当把每台打印机都作为一等实体来通告。每台打印机都应该用一个描述性的名称来通告，让人一看就知道是哪台打印机。这一点很重要，因为那台叫 "Marketing's Transparency Printer"（市场部胶片打印机）的打印机将来可能会被挪到另一台打印服务器上，而用户不应该需要了解这些运维细节。即使打印机现在挂在另一台打印服务器上，他们看到的仍应是网络上以同一名称通告的同一个服务。

你必须传入形如 `"_applicationprotocol._transportprotocol"` 的字符串。目前 `"_transportprotocol"` 必须是 `"_tcp"` 或 `"_udp"` 之一。你的 `"applicationprotocol"` 必须_不超过 15 个字符_，并且应当到 [IANA](http://www.iana.org/form/ports-services) 登记，以便被列入已登记的[协议名称与端口号](http://www.iana.org/assignments/port-numbers)列表。OS X 所用的服务类型清单请参阅 [QA1312](https://developer.apple.com/qa/qa2001/qa1312.html)。

如果你传入空字符串（`""`），那么你的服务会用链路本地多播注册，在适用的情况下也会注册到用户选定的单播 DNS 域中。

如果你传入 `"local"`，那么你的服务只用链路本地多播注册，不会注册到任何用户选定的单播 DNS 域中。

除 `"local"` 域之外，只有当你有某种特殊理由想把服务注册到某个特定的远程域时，才需要传入具体的字符串。

在极少数发生名称冲突的情况下，你的设备应当在名称末尾加一个数字，例如：

"Apple Mac mini (2)"

调用 DNSServiceRegister、CFNetServiceRegisterWithOptions 等 Bonjour API 的应用程序和设备，在发生名称冲突时会自动获得这种改名行为。对于带屏幕且能接受用户输入的设备，你也可以不追加数字，而是选择提示用户输入一个更独特的名称。

TXT 记录的具体性质及其用法取决于服务类型。每种服务类型会定义零个或多个名/值对，用来存放关于各个服务的元数据。这些名/值对应当按 [DNS-Based Service Discovery](http://files.dns-sd.org/draft-cheshire-dnsext-dns-sd.txt) 第 6 节所述的方式格式化。使用 OS X 和 iOS 的 API 时 TXT 记录应如何格式化，请参阅 [QA1306](https://developer.apple.com/qa/qa2001/qa1306.html)。另外，[DNS-SD 网站](http://www.dns-sd.org/ServiceTypes.html)上有常见服务类型当前已定义的名/值对信息。

错。这是一个常见的错误认识。在使用 DHCP（以及链路本地编址）的情况下，假定服务实例明天还是同一个 IP 地址是不安全的。地址是会变的。服务名才是为服务实例设计的稳定标识符。请把实例名（名称、类型和域）保存到应用程序的偏好设置文件中，然后在用户每次访问该服务时按需解析。另外要注意，你不应该保存主机名和端口号，因为不能假定服务实例明天还跑在同一个端口号上。不要保存主机名，而要保存服务实例名（名称、类型和域），这样在使用时解析服务实例名，就一定能拿到最新的 IP 地址和端口号。

应该。你应当把设备上运行的每一个服务都注册进去，例如 HTTP、FTP、SSH、Telnet。在 OS X 上，Safari 浏览器能发现用 Bonjour 通告的 Web 服务器；在 Windows 上，只要装了 [Bonjour for Windows](https://developer.apple.com/downloads/index.action?q=Bonjour%20SDK%20for%20Windows)，Internet Explorer 也能发现 Web 服务器。此外，OS X 的"终端"应用能发现 FTP、SSH 和 Telnet 服务器。

[下一页](Document%20Revision%20History.md)[上一页](Bonjour%20Operations.md)


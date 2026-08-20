---
title: Bonjour 概述
apple_id: 10000119i
resource_type: Guide
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Articles/domainnames.html
archived_at: '2026-07-15T07:17:13.471154Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Bonjour 概述](About%20Bonjour.md)


[下一页](Bonjour%20API%20Architecture.md)[上一页](Bonjour%20Concepts.md)

# 域名命名约定

Bonjour 中服务实例和服务类型的名称与域名系统（DNS）的域名密切相关。本节介绍 DNS 域名、Bonjour 的本地"域"，以及 Bonjour 服务实例和服务类型的命名规则。

DNS 的域名采用从具体到一般的命名方案。最一般的域是 `.`（"点"），称为_根域_（root domain），相当于 UNIX 文件系统中的根目录 `/`。其他所有域都处在根域之下的层级结构中。例如，名称 `www.apple.com.` 位于_二级域_（second-level domain）`apple.com.` 之内，后者位于_顶级域_（top-level domain）`com.` 之内，而顶级域又是 `.`（"点"，即根域）的一部分。图 2-1 展示了这一层级结构的简化版本。

__图 2-1__  互联网域名系统的一部分，并针对 Bonjour 作了增补

!

这棵倒置树的顶端是根域。其下是一些顶级域：`com.`、`edu.`、`org.`，以及 Bonjour 的本地"域" `local.`（详见 [Bonjour 与本地链路](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3teljsgazdkmzx)）。顶级之下是几个二级域：`apple`、`darwin` 和 `zeroconf`。这棵树可以无限向下延伸，例如第三级上的 `www`。

你可能注意到，大多数域名都省略了末尾的点。不过这个末尾的点是有意义的。以点结尾的域名，例如 `www.apple.com.`，称为_完全限定域名_（fully qualified domain name），就像 UNIX 文件系统里的绝对路径（例如 `/usr/bin`）一样。

如果你在 Web 浏览器里输入 `wibble.apple.com`（末尾不带点），系统会把它当作未限定的（部分）名称，并依次追加你的搜索域列表中的名称，例如 `example.com.`、`example.edu` 等等。系统首先尝试追加 `.`（"点"，即根域），但如果 `wibble.apple.com.` 这个名称不存在，它就会沿着列表继续尝试 `wibble.apple.com.example.com.`、`wibble.apple.com.example.edu.`，以此类推。搜索域这个特性通常很有用，但在这种情况下多半不是你想要的结果。

Bonjour 协议在很大程度上是围绕网络中称为_本地链路_（local link）的部分展开的。一台主机的本地链路，或称_链路本地网络_（link-local network），包括它自己以及所有能与它交换数据包而不修改 IP 首部数据的其他主机。实际上，这包括所有未被路由器隔开的主机。

在 Bonjour 系统上，`local.` 用于表明某个名称应当通过在本地 IP 网络上发起 IP 多播查询来解析。

注意，`local.` 并不是一个真正的域。你可以把 `local.` 看作一个伪域。它与传统的 DNS 域有一个根本区别：其他域内的名称在全球范围内是唯一的，而链路本地域名不是。全世界名为 `www.apple.com.` 的逻辑 DNS 条目只有一个，而且按照 DNS 的工作方式，也只可能有一个。另一方面，以 `local.` 结尾的主机名由本地网络上的一组多播 DNS 响应程序管理，因此其命名作用域正如其名：仅限本地。全世界，甚至同一栋楼里，完全可能存在两台名为 `meow.local.` 的主机，只要它们不在同一个本地网络上就行。

全局唯一的名称既重要又有用——事实上这是互联网的重大成就之一——但它们需要投入一定的管理成本来建立和维护。本地名称只在本地网络上有用，但在本地名称已经够用的场合，它们提供了一种用名称（而不是 IP 编号）来指代网络设备的方式，而且协调起来显然比全局唯一名称省事、省钱。

局部唯一的名称在两类网络上尤其有用：一是因为设计使然或线路中断而与全球互联网没有连接的网络，二是小型临时网络，例如用交叉线连起来的两台电脑，或者几个人在家里或咖啡馆的无线网络上用笔记本电脑玩联机游戏。

如果本地网络上发生名称冲突，Bonjour 主机会自动找一个新名称（对于 iOS 或任何没有屏幕的设备而言），或者询问用户（对于个人电脑而言）。

除多播 DNS 之外，Bonjour 还支持通过广域 Bonjour，在传统的单播 DNS 上通告和发现服务。单播 DNS 超出了本文档的范围。要了解如何配置单播域名服务器以配合 Bonjour 使用，请参阅 [DNS-SD 网站](http://www.dns-sd.org/ServerSetup.html)。

Bonjour 服务按照现有的 IP 服务互联网标准命名（该标准见 [RFC 2782](http://www.ietf.org/rfc/rfc2782.txt)）。Bonjour 服务名把服务类型和传输协议组合起来，构成一个注册类型（registration type）。注册类型用于注册服务并为其创建 DNS 资源记录。为了在 DNS 资源记录中把注册类型和域名区分开，注册类型用下划线前缀来分隔构成它的各个部分。格式如下：

`_`_ServiceType_`._`_TransportProtocolName_`.`

服务类型是该服务在 IANA 正式登记的名称，例如 `ftp`、`http` 或 `printer`。传输协议名根据服务所用的传输协议取 `tcp` 或 `udp`。一个跑在 TCP 上的 FTP 服务，其注册类型为 `_ftp._tcp`.，它会向所在主机的多播 DNS 响应程序注册一条名为 `_ftp._tcp.local.` 的 DNS PTR 记录。

如果你正在设计一种新协议并打算把它作为 Bonjour 网络服务通告出去，应当到 [IANA](http://www.iana.org/form/ports-services) 登记。

IANA 目前要求每个已登记的服务都关联一个"知名端口"或一段知名端口范围。例如，`http` 被指派了端口 `80`，因此每当你在 Web 浏览器中访问网站时，程序都会假定 HTTP 服务跑在端口 `80` 上，除非你另行指定。这样一来，只有当网站以非标准方式配置时，你才需要记住它的端口号。

不过有了 Bonjour，你根本不必关心端口号。因为客户端程序只需针对服务类型发起一次简单查询就能发现你的服务，所以知名端口就没有必要了。

服务实例名的用意是作为人类可读的字符串。因此，你应当给它起一个描述性的名字，并允许用户覆盖你提供的默认名称。由于它们本来就是用来浏览而不是用来输入的，服务实例名可以是任何以 UTF-8 编码的 Unicode 字符串，长度上限为 63 个八位组（字节）。

例如，一个在网络上分享音乐的应用程序，默认可能用本机用户的名字来命名音乐分享服务，例如 `Émille's Music Library`。用户可以覆盖这个默认值，把服务命名为 `Zealous Lizard's Tune Studio`，于是应用程序会注册一条名为 `Zealous Lizard's Tune Studio._music._tcp.local.` 的 DNS SRV 记录——这里假定该应用的音乐分享协议关联的名称是 `music`。

[图 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinrqfvjvomq) 展示了 Bonjour 服务实例名的组织方式。树的最上层是域，例如代表本地网络的 `local.`。域之下是注册类型，它由带下划线前缀的服务类型（`_music`）和同样带下划线前缀的传输协议（`_tcp`）构成。树的最下层是人类可读的服务实例名，例如 `Zealous Lizard’s Tune Studio`。完整名称就是沿着这棵树自下而上的一条路径，各部分之间用点分隔。

__图 2-2__  Bonjour 服务名的组织方式

!

[下一页](Bonjour%20API%20Architecture.md)[上一页](Bonjour%20Concepts.md)


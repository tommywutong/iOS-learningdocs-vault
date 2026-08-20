---
title: 使用现代网络技术提升性能与安全性
session_id: 10111
collection: wwdc2020
year: 2020
duration: '13:42'
topics: [System Services]
group: I · 系统服务、进程与安全底层
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2020/10111/'
content_hash: 'sha256:3a432f0c099eacd1'
translated: true
---

# 使用现代网络技术提升性能与安全性

<sub>WWDC2020 · 13:42 · 系统服务</sub>

利用现代网络 API 加快你的 App 运行速度，让它更灵活、更私密、更安全。了解 IPv6 等网络协议……

> [!note] 归档理由
> 现代网络 API 的性能与安全默认值

## 相关资源

- [HD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10111/5/4F35F04B-7EDA-43C3-84B5-C05765126AD4/wwdc2020_10111_hd.mp4?dl=1)
- [SD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10111/5/4F35F04B-7EDA-43C3-84B5-C05765126AD4/wwdc2020_10111_sd.mp4?dl=1)
- [启用加密 DNS](https://developer.apple.com/videos/play/wwdc2020/10047)
- [在你的 App 中支持本地网络隐私](https://developer.apple.com/videos/play/wwdc2020/10110)
- [网络技术进展，第 1 部分](https://developer.apple.com/videos/play/wwdc2019/712)
- [Network.framework 简介：Socket 的现代替代方案](https://developer.apple.com/videos/play/wwdc2018/715)
- [为当今互联网优化你的 App](https://developer.apple.com/videos/play/wwdc2018/714)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎参加 WWDC。

大家好。我是 Jiten Mehta，今天我们将探讨一些在 App 和服务器两端都需要做的重要事情，以提供最佳的用户体验。我们会谈到最大化网络操作性能的方法。

充分利用内置于所有 Apple 平台的坚如磐石的安全能力。在设备在不同网络之间移动时，提供稳健的移动体验。并保护用户的隐私。开始前先简单说一句。我们将要讨论的许多技术都需要客户端设备以及它所连接的服务器同时支持。在客户端，如果你已经在使用 Apple 平台的现代网络 API——URLSession 和 Network.framework，那么你已经具备了所有条件，因为这些技术会自动获得支持。

让我们从性能开始深入探讨。

第一步，IPv6，互联网协议的最新一代版本，也是支撑互联网的基础协议。

Apple 平台原生支持 IPv6 已有多年，包括对纯 IPv6 网络的支持。

在网络上使用 IPv6 的连接延迟更低，通常性能优于 IPv4，部分原因是 NAT 更少，以及使用了更现代的网络设备。

请测试你的 App 是否能在纯 IPv6 网络上正常工作，方法是使用你 Mac 上互联网共享中的 NAT64 支持，因为这是 App Store 提交的要求。好消息是，如果你使用现代网络 API，这应该能直接正常工作。

互联网上 IPv6 的使用呈增长趋势。如果查看过去一个月 Apple 设备在全球发起的连接，我们发现 IPv6 目前已占所有连接的 26%。有 20% 的情况下，连接本可以使用 IPv6，但服务器没有启用它。而在使用 IPv6 时，连接建立的中位数时间比 IPv4 快 1.4 倍。这主要是由于减少的 NAT 使用和改善的路由。请确保你的 App 在客户端使用 URLSession 或 Network.framework 来充分利用 IPv6 带来的改进，这些框架已内建了支持。

我们已经完成了自己的部分。现在轮到你在服务器端勾选这个选项了。因此，请确保你的服务器已启用 IPv6，为用户提供最佳体验。接下来，URLSession 提供了内建的 HTTP/2 支持，这能提升加载性能。

它将发往同一服务器的多个请求复用到单个连接上。这为你节省了时间，因为你不必等待每个响应结束再发送下一个请求。HTTP/2 还通过连接合并提供了性能改进。系统检测到不同请求可以由同一服务器提供服务，并复用现有连接，从而节省了连接建立的开销。头部压缩支持可以实现更好的带宽利用率，因为可以消除请求和响应头部中多余的字节。想了解更多关于 HTTP/2 如何使你的 App 受益，请观看 WWDC 18 的“为当今互联网优化你的 App”。如果查看 Safari 中的 HTTP 使用情况，我们会发现过去一个月中 79% 的请求使用了 HTTP/2，并且使用 HTTP/2 的 URLSession 任务的中位持续时间比使用 HTTP/1.1 的请求快 1.8 倍。如果在客户端使用 URLSession，当服务器端启用 HTTP/2 时，它会默认协商使用 HTTP/2。

因此，请仔细检查你的服务器设置，确保已启用 HTTP/2。

接下来，我们来谈谈保护网络传输安全方面的一些进展。TLS 1.3 是最新、最强大的 TLS 版本，通过从握手过程中减少一次往返来缩短连接建立时间。它通过形式化验证和减少配置错误的可能性提供了更高的安全性。

在 iOS 12 和 macOS Mojave 中，我们提供了一个预览，你可以启用 TLS 1.3 标准的初步版本，并针对你的服务器部署进行测试。

现在该标准已经最终确定，并且自 iOS 13.4 起，URLSession 和 Network.framework 已默认启用 TLS 1.3。

在过去一个月中，我们看到在运行最新 iOS 的设备上，大约 49% 的连接使用了 TLS 1.3。

使用 TLS 1.3 的连接建立速度比使用 TLS 1.2 的快 1.3 倍。

如果服务器端启用了 TLS 1.3，我们的现代网络 API 会默认协商使用 TLS 1.3。

因此，请立即在你的服务器上启用 TLS 1.3，以利用这种更快、更安全的体验。

我们来看看如何让设备在不同网络之间过渡时提供流畅的体验。Multipath TCP 允许你的 App 中的单个 TCP 连接在设备切换网络时持续进行。

这可以防止当连接不稳定或用户移入/移出网络时，你的 App 需要从头开始。

在客户端，你可以通过设置 URLSessionConfiguration 上的 multipathServiceType 属性，或者在 Network.framework 中设置 NWParameters 对象上的该属性，来选择支持 Multipath。Multipath TCP 在我们自己的服务上取得了巨大成功。

去年，我们宣布除了 Siri 之外，我们还将为 Apple Music 启用 Multipath TCP。

自那以后，我们观察到 Music 的播放中断减少了 13%。

而在发生中断的情况下，中断持续时间也减少了 22%。

在 Apple 平台上，你可以轻松地在配置或参数上设置 multipathServiceType 属性来选择 Multipath 协议。要启用服务器端的支持，你需要多做一点工作，所以请访问 multipath-tcp.org，查找在你的服务器部署中启用 Multipath TCP 的说明。接下来，我的同事 Eric 将向大家介绍 iOS 14 中一些重要的新隐私功能。谢谢大家。谢谢，Jiten。iOS 14 通过引入新的本地网络隐私保护来改善用户隐私。

这有助于防止 App 及第三方库或 SDK 利用网络上其他设备的存在来定位或对用户进行指纹识别（fingerprinting）。内建的与本地网络交互的系统服务，如隔空打印、隔空播放和 HomeKit，不会向 App 提供有关网络的任何隐私信息。然而，直接访问任何本地网络资源，包括使用多播和广播，现在都需要明确的用户许可。为了帮助你的用户理解你的 App 如何使用他们的本地网络，你需要在你的 App 的 Info.plist 中提供一个原因字符串。

有关测试你的 App 时的注意事项以及如何确保你准备好提供更具隐私保护体验的更多信息，请务必观看“在你的 App 中支持本地网络隐私”。同样在 iOS 14 和 macOS Big Sur 中新增的是对安全域名解析的支持，包括 DNS-over-TLS 和 DNS-over-HTTPS。这种支持不是为每个 App 或浏览器提供单独的解析服务，而是体现在系统解析器中，因此一旦你配置了安全 DNS，设备上的所有 App 都将受益。除了编写一个使用 NetworkExtension 的 App 来为加密 DNS 传输提供这些系统级设置之外，你还可以在你的 App 中要求使用加密解析。

有关如何利用这些新 API 的详细信息，请参见“启用加密 DNS”讲座。你可以通过编写一个在客户端使用 NetworkExtension 的 App 来为加密解析提供系统级设置，并请你的 DNS 提供商提供 DNS-over-HTTPS 选项（如果他们尚未提供）。我们还希望分享一些即将推出的技术的预览，你现在就可以开始做准备。

即使你已经启用加密 DNS 来使名称解析更加私密，你与服务器进行的每次 TLS 握手都包含一个明文服务器名称指示（SNI），网络上的第三方可以观察到它。我们目前正在与 IETF 合作，推动标准化方法，以加密 TLS 握手的更多部分，从而使第三方无法窥探你的流量。这，尤其是在与加密 DNS 结合时，将是朝着确保你的网络通信仅在你和你正在通信的服务器之间进行的重要一步。

另一个预告，HTTP/3 是下一代的 HTTP，它构建在新的 QUIC 传输协议之上。

这个传输协议内建了 TLS 1.3 安全性，并提供了与 HTTP/2 相同的所有多路复用流支持，但进一步减少了队头阻塞（head-of-line blocking），因此任何单个请求或响应的丢失都不会阻碍其他可能不相关的消息。

基于 QUIC 的 HTTP/3 还拥有更高精度的信息，以提供改进的拥塞控制和丢包恢复。

它还带来了内建的移动性支持，使得网络过渡不会导致正在进行的操作失败。相反，它们可以无缝地在新网络上继续，而不会中断。

HTTP/3 仍然是 IETF 的一项进行中的规范，我们正在那里继续积极合作，以帮助使 HTTP/3 做好全球部署的准备。作为这方面的一个重要第一步，iOS 14 和 macOS Big Sur 包含了对使用 URLSession 的 App 的 HTTP/3 支持的实验性预览，你可以在开发者设置中启用它。

你也可以通过实验性设置在 Safari 中尝试同样的 HTTP/3 支持。

类似地，对于 macOS Big Sur，你可以通过设置 CFNetworkHTTP3Override 用户默认值来为使用 URLSession 的 App 启用实验性 HTTP/3 支持，并且你可以在 Safari 的开发菜单下的实验性功能中启用它。请尝试 HTTP/3，并针对你可能遇到的任何问题提交错误报告。我们非常期待你的反馈。

今天我们讨论了如何利用 IPv6、HTTP/2、TLS 1.3、Multipath TCP 和加密 DNS，为每个人带来性能、安全性、移动性和隐私方面的好处。所有这些技术目前都受到 Apple 平台上现代网络 API 的支持，因此请确保在你的 App 中使用 URLSession 或 Network.framework。接下来，检查你的服务器部署，确保一切保持最新并且已启用这些功能，这样你就能填满这个列表的右侧部分。

最后，启用实验性 HTTP/3 支持并与你的服务器部署进行测试，为下一代网络协议提供反馈。感谢观看。

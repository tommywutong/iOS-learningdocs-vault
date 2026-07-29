---
title: 在 Network framework 中使用结构化并发
session_id: 250
collection: wwdc2025
year: 2025
duration: '21:10'
topics: [System Services]
group: C · 并发、锁与线程
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2025/250/'
content_hash: 'sha256:d388ef78974932f1'
translated: true
---

# 在 Network framework 中使用结构化并发

<sub>WWDC2025 · 21:10 · System Services</sub>

Network framework 是在 Apple 平台上进行底层网络连接的最佳方式——而在 iOS、iPadOS 和 macOS 26 中，它还...

> [!note] 归档理由
> Network 框架的结构化并发用法

## 章节

- [欢迎](/videos/play/wwdc2025/250/?time=0)
- [建立连接](/videos/play/wwdc2025/250/?time=45)
- [发送与接收](/videos/play/wwdc2025/250/?time=442)
- [接受传入连接](/videos/play/wwdc2025/250/?time=862)
- [发现其他设备](/videos/play/wwdc2025/250/?time=965)

## 相关资源

- [欢迎](https://developer.apple.com/videos/play/wwdc2025/250/?time=0)
- [建立连接](https://developer.apple.com/videos/play/wwdc2025/250/?time=45)
- [发送与接收](https://developer.apple.com/videos/play/wwdc2025/250/?time=442)
- [接受传入连接](https://developer.apple.com/videos/play/wwdc2025/250/?time=862)
- [发现其他设备](https://developer.apple.com/videos/play/wwdc2025/250/?time=965)
- [NetworkBrowser](https://developer.apple.com/documentation/Network/NetworkBrowser)
- [NetworkListener](https://developer.apple.com/documentation/Network/NetworkListener)
- [NetworkConnection](https://developer.apple.com/documentation/Network/NetworkConnection)
- [构建自定义点对点协议](https://developer.apple.com/documentation/Network/building-a-custom-peer-to-peer-protocol)
- [Network](https://developer.apple.com/documentation/Network)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2025/250/4/ffac19d6-02fb-4abc-a491-fc009e5d38e3/downloads/wwdc2025-250_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2025/250/4/ffac19d6-02fb-4abc-a491-fc009e5d38e3/downloads/wwdc2025-250_sd.mp4?dl=1)
- [拥抱 Swift 并发](https://developer.apple.com/videos/play/wwdc2025/268)
- [使用 Wi-Fi Aware 提升设备连接性](https://developer.apple.com/videos/play/wwdc2025/228)
- [引入 Network.framework：Socket 的现代替代方案](https://developer.apple.com/videos/play/wwdc2018/715)
- [使用 TLS 建立连接](https://developer.apple.com/videos/play/wwdc2025/250/?time=244)
- [使用 TLS 和 IP 选项建立连接](https://developer.apple.com/videos/play/wwdc2025/250/?time=281)
- [使用自定义参数建立连接](https://developer.apple.com/videos/play/wwdc2025/250/?time=307)
- [在连接上发送和接收数据](https://developer.apple.com/videos/play/wwdc2025/250/?time=450)
- [在连接上发送和接收数据](https://developer.apple.com/videos/play/wwdc2025/250/?time=509)
- [井字棋游戏消息](https://developer.apple.com/videos/play/wwdc2025/250/?time=666)
- [使用 TLV 发送井字棋游戏消息](https://developer.apple.com/videos/play/wwdc2025/250/?time=684)
- [使用 TLV 接收井字棋游戏消息](https://developer.apple.com/videos/play/wwdc2025/250/?time=713)
- [使用 Coder 处理井字棋游戏消息](https://developer.apple.com/videos/play/wwdc2025/250/?time=770)
- [使用 Coder 发送井字棋游戏消息](https://developer.apple.com/videos/play/wwdc2025/250/?time=793)
- [使用 Coder 接收井字棋游戏消息](https://developer.apple.com/videos/play/wwdc2025/250/?time=833)
- [使用 NetworkListener 监听传入连接](https://developer.apple.com/videos/play/wwdc2025/250/?time=916)
- [浏览附近配对的 Wi-Fi Aware 设备](https://developer.apple.com/videos/play/wwdc2025/250/?time=1059)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

嗨，我是 Scott，我非常激动地和大家分享一些改进，这些改进让你的网络代码比以往任何时候都更有趣、更容易编写。如果你从未写过一行网络代码，那你来对地方了。如果你写过，我也有一些令人兴奋的新 API 要和你分享。

我将从如何建立连接开始讲起。然后，我会深入探讨如何使用这些连接来发送和接收数据。

接下来，我将讨论如何监听传入连接。最后，我会介绍如何发现并连接到网络上的其他设备。让我们从建立连接开始。

Network framework 让你能够在 App 中建立安全、可组合且现代化的连接。

Socket、sockaddr、难以记忆的 ioctl 以及阻塞操作的日子已经一去不复返了。Network framework 支持按名称连接（Connect by Name），这意味着它会为你执行名称解析的工作，你无需自己动手。一旦解析了名称，它就会使用一种叫做“快乐眼球（Happy Eyeballs）”的机制，确保高效地选择最佳解析地址，为你动态建立连接。

TLS 提供的内置安全保障，让你无需为了保护用户隐私而将另一个库（通常 API 风格完全不同）集成到你的应用中。它还支持网络接口转换和代理，让你无需任何额外操作就能实现 Wi-Fi Assist 和多路径协议等功能。

它支持如 QUIC 这样的现代传输协议，甚至允许你将自己的协议与内置协议混合搭配使用，让你能够专注于业务逻辑和用户体验，而不是花时间调试消息为何没能从 A 点传送到 B 点。

对于那些同时支持原生 App 和 Web App 的开发者，Network framework 也对 WebSocket 提供了强大的支持，让一台服务器能够服务于各种客户端应用。

Network framework 从设计之初就是可组合的。这意味着，当你使用 Network framework 时，即使网络协议随着时间演进以提升性能和隐私，你也会发现一系列熟悉的 API。

如果你曾经使用 BSD Socket API 通过 TCP 编写过网络代码，你会知道切换到像 QUIC 这样的协议意味着一次重大的重写。而使用 Network framework，在工作午餐时间内就能完成到 QUIC 的切换。在 iOS 和 macOS 26 中，Network framework 与 Swift 对异步操作和结构化并发（structured concurrency）的强大支持紧密结合。现在，你的网络代码能够与你其他的 Swift 代码无缝配合，使你的 App 更易于构建和维护。对于那些刚接触网络编程的开发者，我将在接下来的示例中介绍一些可能不熟悉的概念，但别担心，你最终会明白的。

假设你正在编写你的 App，并想要与 `www.example.com` 服务器的 1029 端口通信。你想使用 TLS，并且只想在非受限网络上建立这个连接。

你的 endpoint 是你要连接的目标。你的 protocol stack 是你连接的方式。你的 parameters 帮助你进一步细化如何到达那里。

你将它们组合起来创建一个 NetworkConnection。

让我们通过一个例子来了解这在实际中是如何运作的。

我通过使用我想要的 endpoint 和 protocol stack 来初始化我的 NetworkConnection 来建立连接。在这个例子中，我指定我的 protocol stack 是 TLS。请注意，TCP 和 IP 是自动推断出来的。我只有在想要自定义某些东西时才需要指定它们，但默认值几乎在大多数时候都是合适的。

当我想修改默认值时，我仍然以声明式（declarative）的方式去做。举个例子，我将为此连接关闭 IP 分片。

首先，我需要在 TLS 下面指定 TCP 和 IP 协议。然后，我可以自定义为 IP 设置的选项来关闭分片。

如果有人启用了低数据模式来最小化网络使用，我想修改我连接的行为，以便禁止使用那些受约束的网络接口。

我更新了代码，这样我就可以修改连接的参数，因为我不再使用自动为我创建的默认参数了。

protocol stack 保持不变，但我添加了自定义参数，这允许我指定：对于此特定连接，我希望 Network framework 只考虑未处于低数据模式的网络接口。太棒了！凭借与 SwiftUI 一样声明式的风格，现在我的网络代码感觉和我的用户界面代码很相似。

虽然网络始终可用是件好事，但网络状况总是在变化。

与 Socket 不同，NetworkConnection 会为你响应这些变化的状态。

当你的连接启动时，它会进入准备中（preparing）状态，同时执行任何协议握手。当这些握手完成时，它会进入就绪（ready）状态。

如果没有连接性，连接将从准备中状态进入等待（waiting）状态。

当 Network framework 检测到网络状况发生变化时，它会回到准备中状态，同时尝试连接到远程 endpoint。当你的连接状态变为就绪时，它就可以发送和接收数据了。

一旦你的连接处于就绪状态，如果遇到错误或连接丢失，它将以错误（error）状态进入失败（failed）状态，并告知你发生了什么。

退出或取消与连接关联的任务（task）会将其移动到已取消（canceled）状态。

这里的好处是，如果你不想，你完全不需要了解任何连接状态。你可以调用 send 和 receive，NetworkConnection 会一直等待，直到其状态变为就绪来完成这些操作。但如果你确实想知道你的连接处于什么状态，比如为了更新你的用户界面，你可以安装一个处理程序，当你的连接状态变化时它会被调用。

好了，现在你知道如何建立连接了。那么让我们开始使用它在网络上发送和接收数据。

Send 和 receive 都是异步函数，并且如果连接尚未启动，它们都会启动连接。

Send 接受一个数据对象，并挂起（suspend）当前任务（task），直到 Network framework 处理完数据。

TLS 和 TCP 都是流协议，所以当你接收数据时，你必须指定你想要多少字节。

在这个例子中，我指定了我要读取的确切字节数。Receive 返回一个包含内容和元数据的元组，但在这个例子中，我指定我只想要内容。

如果连接遇到错误，这两个函数都会抛出错误。例如，如果因为打开了飞行模式而导致网络丢失，你可以使用相关的错误来解释传输被中断的原因。

有时你不知道要接收多少字节的数据。

在这个例子中，我从网络加载一张图片。从连接上接收到的一个 32 位整数告诉我，还有多少字节的图片数据需要接收。利用这个值，我反复调用 receive，直到图片完整接收完毕。

在上一个例子中，我使用了指定确切字节数的 receive 版本。在这个例子中，我使用的 receive 版本允许我指定一个最小和最大字节数来接收。

这样做可以让代码在字节流从网络传入时就解析图片，而不必等待整个图片都传完。像 TLS 这样的字节流协议很棒，但很多时候你会希望对发送和接收的字节进行成帧（frame），这样你就可以处理消息而不是字节。在之前的例子中，我通过从字节流中预先读取一个 32 位值来知道图片有多大，这实际上是用长度来界定图片，以便将其与相邻的图片区分开来。我不得不这样做，因为流协议不保留消息边界。这意味着，传递给单个发送操作的字节数，不一定会是连接另一端从接收操作返回的字节数。

例如，如果你用三个数据块调用 send，另一端可能会一次一个字节地接收，也可能一次性全部接收，或者介于两者之间。

这可能会大大增加编写健壮网络应用的复杂性。

幸运的是，Network framework 可以提供帮助。iOS 和 macOS 26 中新增了一个内置的类型-长度-值（TLV）成帧器（framer），它对消息进行成帧，这样你在连接一端发送的内容，就会是你在另一端接收到的内容。

TLV 是一个简单的消息协议，它对类型（type）进行编码，类型可以用来描述消息中包含的数据；还对长度（length）进行编码，长度是消息中数据的大小。之后是消息的实际内容。常见的网络协议都使用 TLV，所以这可能已经是你的服务器支持的格式了。让我们来试试。在这个例子中，我将发送和接收游戏消息类型。GameMessage 是一个枚举（enum），我将用它作为消息的类型。消息的内容将是一个游戏角色或一个游戏动作。

添加 TLV 就像将其添加到我的 protocol stack 中一样简单。

因为 TLV 会为我成帧消息，所以发送和接收的接口略有不同。

我将使用 JSONEncoder 对我的 GameCharacter 结构体（struct）进行编码，然后发送它。

请注意，我指定了消息的类型以及编码后的数据。

现在让我们看看如何使用 TLV 接收消息。

与之前使用字节流协议的例子不同，当我使用 TLV 时，我不必指定要接收的字节数，因为 TLV 会为我解析消息。因为我想知道我收到的消息类型，所以我接收了内容以及与消息关联的元数据的元组。对于 TLV，元数据包含了类型。

我使用类型来确定我收到了什么类型的内容，然后利用这些信息，我对数据进行解码并打印我所收到的内容。这非常强大，尤其是在与我不控制的现有服务器和协议进行互操作时。所以现在，我不费太多功夫就对字节进行了成帧，并且能够发送和接收消息。与直接使用字节流协议相比，这是一个很好的改进。

但如果我可以直接发送我的对象呢？iOS 和 macOS 26 中新增了对直接发送和接收可编码（codable）类型的支持，这有助于简化部分样板代码。

我可以将角色和动作结构体合并到 GameMessage 枚举本身中。

Coder 是一个协议（protocol），我可以将其添加到我的 protocol stack 中，它会为我成帧消息，并允许我发送和接收可编码类型，而无需自己进行序列化和反序列化。

在这段代码中，我来回发送游戏消息。因此，我将用我正在发送和接收的类型以及我希望 Coder 如何格式化数据来初始化 coder。

Network framework 内置支持 JSON 和属性列表（property list）格式。在这个例子中，我将选择 JSON。

现在，我可以发送游戏消息，而无需自己进行任何编码。

在我的连接上调用 receive 将会直接返回一个游戏消息，而无需进行任何中间的解码步骤来从数据对象转换为 GameMessage 对象。

现在，我可以发送和接收游戏消息，而无需自己做任何额外的工作。我可以专注于我的 App 的业务逻辑和用户界面，而不会被一堆定制的网络代码弄得杂乱无章。

所以现在你已经知道如何创建到一个 endpoint 的连接，并在该连接上发送和接收数据了。你了解了像 TCP 和 TLS 这样的字节流协议，以及如何向你的 protocol stack 添加成帧协议，以便处理消息而不是字节流。但那些需要监听传入连接的应用呢？传入连接由 NetworkListener 处理。

就像 NetworkConnection 一样，我通过声明一个 protocol stack 来初始化它。与连接不同，监听器没有 send 或 receive 方法。

这是因为监听器会监听新的连接，然后将它们传递给调用者。

NetworkListener 有一个 run 方法，它会将新的连接传递给传入的处理程序。让我们看看它是如何工作的。我通过指定一个 protocol stack 来声明式地创建我的 NetworkListener。在这个例子中，我的传入连接将能够发送和接收由 TLS 加密的 GameMessage 对象。

在 NetworkListener 上调用 run 将开始将新的传入连接传递给我在 run 中传入的处理程序。

NetworkListener 会为每一个新连接启动一个新的子任务。因此，我可以在闭包中执行异步操作，而不必担心这会阻止监听器继续传递新的传入连接。当我获得一个新连接时，我使用 NetworkConnection 上的 messages 属性来处理来自客户端的传入消息。

所以现在我已经创建了一个到已知 endpoint 的 NetworkConnection，并且编写了监听新连接的代码。但现在我想创建一个 NetworkConnection，其 endpoint 是我事先不知道的。NetworkBrowser 使我能够发现在创建连接时可以使用的 endpoint。

今年在 iOS 26 中新增的是 Wi-Fi Aware，这是一种跨平台的点对点网络技术，它将允许你发现并连接到各种兼容设备。你可以使用 DeviceDiscoveryUI 框架来通过 Wi-Fi Aware 发现附近的设备并与之配对。或者，你也可以浏览 Bonjour 发布的服务。要了解更多关于 Wi-Fi Aware 的信息，请观看《使用 Wi-Fi Aware 提升设备连接性》。当你想要找到网络上的设备时，无论是通过 Wi-Fi Aware 发现附近的设备，还是通过 Bonjour，你都可以使用 NetworkBrowser。NetworkBrowser 接受浏览描述（browse descriptors），它描述了你要寻找的内容。

与 NetworkConnection 类似，它也接受参数（parameters），这些参数描述了你希望如何找到它。但与 NetworkConnection 和 NetworkListener 不同，NetworkBrowser 不接受 protocol stack。

这是因为 NetworkBrowser 的唯一任务是返回可用于建立连接的 endpoint。

在这个例子中，我创建我的 NetworkBrowser 来使用 Wi-Fi Aware 服务搜索附近的设备，服务名为 Tic-Tac-Toe。在浏览器上调用 run 将使其启动，并开始向我在 run 中传入的处理程序提供 endpoint 集合。

在我的 App 中，我对使用哪个 endpoint 没有偏好，所以我选择了浏览器返回的第一个 endpoint。

使用该 endpoint 返回 `.finish` 将导致浏览器停止运行，并且该 endpoint 会从 run 中返回。

然后，我可以使用这个 endpoint 来初始化一个 NetworkConnection，方式与之前例子中使用 endpoint 初始化 NetworkConnection 的方式完全相同。

不过，这个 endpoint 的巧妙之处在于，浏览器为我发现了它，所以我不必事先知道它。

有了所有这些新的协议，你可能想知道如何在你的 App 中选择使用哪个协议。这是个很好的问题。答案没有你想象的那么复杂。如果你要与一个你不控制的服务器或其他设备通信，你的协议选择已经为你确定了。例如，你可能通过基于 TCP 的 IPP 与打印机通信。

如果你要与另一台设备上你自己的 App 通信，那么在 TLS 或 QUIC 之上使用 Coder 肯定不会错。

请注意，如果你正在进行 HTTP 网络通信并且目前正在使用 URLSession，你不需要更改任何代码。如果你正在使用 Network framework C API，或者在 Swift 中工作并且更倾向于使用完成处理程序（completion handler），你也不需要更改任何代码。无论你以何种形式使用 URLSession 或 Network framework，你仍然会获得一流的按名称连接支持、可组合性、移动性和内置安全性。

让我们快速回顾一下。

iOS 和 macOS 26 中新增了 NetworkConnection、NetworkListener 和 NetworkBrowser。

你了解了如何使用带有 TLV 成帧的 NetworkConnection，以及通过 Coder 协议支持发送和接收可编码类型。

NetworkListener 可用于监听传入连接。NetworkBrowser 可用于浏览网络上的 endpoint。所有这些使得编写网络应用比以往任何时候都更加容易。

就是这样。这些新的 API 从底层开始就是为 Swift 的结构化并发而构建的。它们是以声明式的方式创建的，就像在 SwiftUI 中布局用户界面一样。

它们在任务中运行，并且当其所在的任务被取消时，它们会自动被取消。

尝试这些新的 API，充分利用 Swift 中的结构化并发，让你的代码更简洁，并消除大量的样板代码。

所有这些都同样具备 Network framework 为你提供的在 App 中使用的强大功能和灵活性。感谢观看。

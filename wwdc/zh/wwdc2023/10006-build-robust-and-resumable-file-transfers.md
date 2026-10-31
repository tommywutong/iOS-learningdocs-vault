---
title: 构建稳健且可续传的文件传输
session_id: 10006
collection: wwdc2023
year: 2023
duration: '20:39'
topics: [System Services]
group: H · 持久化与文件系统
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2023/10006/'
content_hash: 'sha256:c3eb5db253e001ec'
translated: true
---

# 构建稳健且可续传的文件传输

<sub>WWDC2023 · 20:39 · System Services</sub>

了解 URLSession 如何帮助你的 App 传输大文件并从中断的网络中恢复。学习如何暂停和恢复……

> [!note] 归档理由
> 可续传文件传输，涉及 URLSession 后台机制

## 章节

- [欢迎](/videos/play/wwdc2023/10006/?time=0)
- [探索 HTTP 中的可续传下载协议](/videos/play/wwdc2023/10006/?time=162)
- [使用 URLSession 暂停和恢复下载](/videos/play/wwdc2023/10006/?time=263)
- [使用 URLSession 暂停和恢复上传](/videos/play/wwdc2023/10006/?time=470)
- [探索 HTTP 中的可续传上传协议](/videos/play/wwdc2023/10006/?time=585)
- [为 SwiftNIO 添加可续传上传](/videos/play/wwdc2023/10006/?time=766)
- [使用后台 URLSession](/videos/play/wwdc2023/10006/?time=971)

## 相关资源

- [欢迎](https://developer.apple.com/videos/play/wwdc2023/10006/?time=0)
- [探索 HTTP 中的可续传下载协议](https://developer.apple.com/videos/play/wwdc2023/10006/?time=162)
- [使用 URLSession 暂停和恢复下载](https://developer.apple.com/videos/play/wwdc2023/10006/?time=263)
- [使用 URLSession 暂停和恢复上传](https://developer.apple.com/videos/play/wwdc2023/10006/?time=470)
- [探索 HTTP 中的可续传上传协议](https://developer.apple.com/videos/play/wwdc2023/10006/?time=585)
- [为 SwiftNIO 添加可续传上传](https://developer.apple.com/videos/play/wwdc2023/10006/?time=766)
- [使用后台 URLSession](https://developer.apple.com/videos/play/wwdc2023/10006/?time=971)
- [用 SwiftNIO 构建可续传上传服务器](https://developer.apple.com/documentation/Foundation/building-a-resumable-upload-server-with-swiftnio)
- [在后台下载文件](https://developer.apple.com/documentation/Foundation/downloading-files-in-the-background)
- [URLSession](https://developer.apple.com/documentation/Foundation/URLSession)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10006/4/62804C33-C167-4D42-9E12-390AED4A4EE1/downloads/wwdc2023-10006_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10006/4/62804C33-C167-4D42-9E12-390AED4A4EE1/downloads/wwdc2023-10006_sd.mp4?dl=1)
- [网络技术进展，第一部分](https://developer.apple.com/videos/play/wwdc2019/712)
- [暂停和恢复 URLSessionDownloadTask](https://developer.apple.com/videos/play/wwdc2023/10006/?time=293)
- [暂停和恢复 URLSessionDownloadTask](https://developer.apple.com/videos/play/wwdc2023/10006/?time=321)
- [暂停和恢复 URLSessionDownloadTask](https://developer.apple.com/videos/play/wwdc2023/10006/?time=371)
- [出错时获取续传数据](https://developer.apple.com/videos/play/wwdc2023/10006/?time=394)
- [暂停和恢复 URLSessionUploadTask](https://developer.apple.com/videos/play/wwdc2023/10006/?time=509)
- [暂停和恢复 URLSessionUploadTask](https://developer.apple.com/videos/play/wwdc2023/10006/?time=517)
- [暂停和恢复 URLSessionUploadTask](https://developer.apple.com/videos/play/wwdc2023/10006/?time=537)
- [出错时获取续传数据](https://developer.apple.com/videos/play/wwdc2023/10006/?time=562)
- [在 Swift NIO 中实现可续传上传之前](https://developer.apple.com/videos/play/wwdc2023/10006/?time=795)
- [在 Swift NIO 中添加可续传上传](https://developer.apple.com/videos/play/wwdc2023/10006/?time=846)
- [URLSession 中的信息性响应](https://developer.apple.com/videos/play/wwdc2023/10006/?time=948)
- [使用后台 URLSession](https://developer.apple.com/videos/play/wwdc2023/10006/?time=1099)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ Jonathan：嗨，我是 Jonathan，是 Internet Technologies 团队的一名工程师。今天我们将探索如何使用 URLSession 构建稳健且可续传的文件传输。大文件传输可能是一个巨大的挑战，因为哪怕一次很小的中断，也可能丢掉你用户的所有进度，迫使他们从头开始。此外，传输越大，耗时就越长；而耗时越长，出问题的机会就越多。

在这段时间里，你的用户可能会离开你的 App、走出 Wi-Fi 覆盖范围，或遇到众多不受他们控制的网络问题。在本场讲座中，我们将探索如何应对这些挑战，为你的用户提供稳健的网络体验。我们的第一站是可续传的 HTTP 协议，它能让用户在连接中断时保留进度。这避免了时间和带宽的浪费，使这些协议成为传输大量数据时的强大工具。我将演示如何在 URLSession 中恢复下载和上传，包括用于可续传上传任务的全新 API。理解这些 API 背后的机制，对调试你的 App、甚至构建你自己的服务器支持都非常有帮助。因此我们还会介绍这些可续传协议本身，让你确切了解你的 App 和服务器是如何通过 HTTP 实现这一点的。

接下来，说到服务器，你将学习如何为任何使用 SwiftNIO 的服务器添加可续传上传支持。

最后，我们将回顾后台 URLSession 如何优雅地处理用户和网络中断，同时高效利用系统资源。

让我们进一步了解 URLSession 中的下载和上传恢复。我正在下载最新版的 Xcode，这个 7 GB 的下载几乎就要完成了。就在这最后关头，我的 Wi-Fi 断了。

但等等，下载暂停了；当 Wi-Fi 恢复在线时，我可以从断掉的地方继续下载。

我刚刚节省了大量时间以及好几个 GB 的带宽。可续传下载真是太棒了。但它们是如何工作的呢？首先，客户端发送一个 GET 请求，从服务器获取下载内容。

在响应中，服务器通过 Accept-Ranges 头来宣告它支持可续传下载。Accept-Ranges: bytes 意味着服务器支持针对该资源特定字节的范围请求（range request）。服务器响应中还包含所谓的 ETag，它在此刻唯一标识这个资源。如果服务器上的内容发生变化，ETag 也会随之改变。

那么，如果这次下载被中断会怎样？客户端已经保存了部分下载数据，所以它只需要最后一部分。为了做到这一点，它可以发送一个范围请求，取回下载中缺失的字节。请求用 Range 字段指明需要哪些字节。但客户端还需要确保资源没有发生变化，否则它就会把新资源的数据追加到已保存的旧资源上。为防止这种情况，If-Range 字段包含上一次响应中收到的 ETag，告诉服务器只有在 ETag 相同时才发送这部分数据。

如果 ETag 相同，服务器就用 206 Partial Content 响应。这里的 Content-Range 字段表示此响应所包含的字节范围，从而完成下载。

从一开始，URLSession 就提供了使用 Range 请求暂停和恢复下载任务的 API。现在，你也可以暂停和恢复上传了。这不仅让你能够手动暂停正在进行的任务，还可以让你执行错误处理，从意外的连接问题中恢复，并从断掉的地方继续传输。让我们先看看下载是如何工作的。想象一下，你正在创建一个让用户手动暂停和恢复下载的 UI。像 Safari 的例子一样，这个 UI 属于你的 App，但在底层，你可以使用 URLSession 处理所有细节，比如跟踪部分下载数据、ETag 和请求头。要开始下载，你像往常一样创建一个下载任务，并调用 resume 启动它。要暂停下载——比如当用户点按暂停按钮时——你可以调用 cancelByProducingResumeData。为了之后恢复这次下载，URLSession 需要关于这次部分下载的信息，比如它的 ETag、当前大小和在磁盘上的位置。这些信息连同其他元数据，都方便地保存在这个函数返回的续传数据（resume data）对象中。再次强调，要注意这份续传数据并不是部分下载数据本身。如果续传数据为 nil，这意味着可续传下载的一项或多项要求没有得到满足，我们很快就会介绍这些要求。另一方面，如果续传数据不为 nil，你就应该把它保存下来以备后用。因为要恢复下载——比如当用户点按恢复按钮时——你需要把这份保存的数据传给 downloadTask withResumeData 方法。就这么简单！这个模式非常适合手动暂停下载，但 URLSession 也提供了从意外连接中断中恢复的方法。

如果你的下载任务因网络问题而失败，你可以检查错误本身中是否带有续传数据。如果下载可以恢复，错误的 userInfo 字典中就会包含那份续传数据。你可以方便地通过 URLError 的 downloadTaskResumeData 属性来获取这份数据。URLSession 的可续传下载有几项要求。下载本质上是获取数据，应当可以安全地重复执行，因此 URLSession 要求下载任务使用 HTTP GET 请求。不支持其他 scheme 或方法。其次，服务器必须支持字节范围请求，并通过 Accept-Ranges 头宣告这一点。服务器必须在响应中为资源提供 ETag 或 Last-Modified 字段，但优先使用 ETag。最后，临时下载文件不能因磁盘空间压力而被系统删除。

有了这些要求，你就可以手动暂停和恢复下载，甚至从连接中断中恢复。没有恢复协议的话，哪怕一次很小的中断也会迫使你从头开始传输。这对上传来说问题更大。上传速度通常比下载速度慢得多，所以重新开始意味着浪费更多的时间和资源。iOS 17 为可续传上传任务引入了全新的支持。我对它们感到超级兴奋。现在，如果服务器支持最新的协议草案，上传任务就是自动可续传的。让我们先探索新的 API，然后深入了解可续传上传协议的细节。和下载任务一样，只需创建一个上传任务并调用 resume 启动它。要暂停的话，上传任务现在支持与下载任务相同的 cancelByProducingResumeData 方法。任务会自动检测服务器是否支持最新的可续传上传协议。如果服务器确实支持，你就可以保存这份续传数据以备后用。

最后，要恢复暂停的上传，使用新的 uploadTask withResumeData 方法。你会注意到这里展示的模式与下载任务完全相同。这意味着，如果你已经为 App 中暂停和恢复下载打造了出色的体验，你也可以轻松地为你的用户实现可续传上传。如果只是一次短暂的网络中断，而服务器仍然可达，URLSession 会自动尝试恢复你的上传。不需要任何额外的代码。但在遇到其他更广泛的连接问题时——比如你的网络或服务器彻底宕机——你可以像检查下载任务那样，从错误中检查续传数据。看到 URLSession 支持可续传上传，我非常高兴，希望你们也会喜欢它们。但要利用这项功能，你的服务器也必须支持最新的可续传上传协议。

该协议目前正在开发中，业界也在 IETF 中努力推动它标准化。在协议中，客户端能够自动发现服务器的支持。这意味着 URLSession 可以在第一个请求上就尝试让所有上传都可续传。如果服务器不支持可续传上传，该请求就简单地作为普通上传继续。让我们看看它在网线上是如何工作的。

客户端首先向一个上传端点发送请求。Upload-Incomplete 字段表示这个客户端支持可续传上传。问号 0 就是所谓的结构化字段布尔值（structured field boolean），它表示 false 这个值。这意味着所有的上传数据都包含在这个请求的正文之中。

如果服务器支持可续传上传，它会检测到客户端的这个头，并用一个 104 信息性响应来宣告自己的支持。104 响应包含一个 location 字段，其中带有一个恢复 URL。这个恢复 URL 用于唯一标识该上传，这样客户端就知道连接中断后该从哪里恢复上传。服务器把它收到的上传数据与这个唯一的恢复 URL 关联起来。

如果上传没有中断就完成了，那就太好了。服务器发送一个 201，事情就结束了。然而，如果上传被中断，客户端和服务器就会执行可续传上传的流程。

服务器已经为该恢复 URL 保存了部分上传数据，但客户端需要一种方法来确定服务器实际收到了多少数据。为此，客户端向恢复 URL 发送一个 HEAD 请求，向服务器询问上传偏移量。这个偏移量就是服务器实际收到的字节数。

然后，服务器针对这个客户端的特定上传，用上传偏移量进行响应。

最后，客户端需要确认服务器的偏移量并发送剩余数据。为此，客户端向恢复 URL 发送一个带有匹配上传偏移量的 PATCH 请求。这个请求的正文包含从给定偏移量开始的上传数据。

至此，客户端终于把所有数据都发送给了服务器，上传完成。你的 App 使用 URLSession 中的上传任务就能免费获得这一切。现在，让我们快速看一看服务器端，探索如何用 SwiftNIO 构建你自己的可续传上传服务器。

对于那些已经在服务器上使用 SwiftNIO 的人来说，这一部分是为你们准备的。可续传上传可以在任何服务器上实现，但如果你的服务器已经在使用 SwiftNIO，有一个新的包能让添加支持变得非常简单。让我们快速看一个例子。如果你不熟悉的话，SwiftNIO 是一个异步网络应用框架，既可用于你的 App，也可用于你的服务器。在这段示例代码中，我们正在搭建一个 HTTP/2 服务器。我们为服务器添加了两个处理器。编解码器把 HTTP/2 帧转换成示例处理器能理解的请求。在另一个方向上，它接收示例处理器的响应，并把它们编码成 HTTP/2 帧。ExampleChannelHandler 为我们服务器执行基本的路由和逻辑。起初，我们只支持普通上传。让我们看看把服务器改造成支持可续传上传有多简单。

首先，我们下载 NIOResumableUpload 项目，把它添加为依赖，并在代码中导入它。然后，我们定义一个可续传上传上下文。这会告诉处理器在生成恢复 URL 时使用哪个上传端点。

最后，我们把当前的处理器包装进 HTTPResumableUploadHandler。它在我们现有逻辑之上执行可续传上传的流程。对于每一次上传，它都会生成一个随机且安全的恢复 URL，并把它与上传数据关联起来。如果连接中断，处理器会保存所有部分数据，并替我们响应所有可续传上传的流程。哇！只用了几行代码，我们就让服务器火力全开，支持了可续传上传。对于那些已经在使用 Swift on Server 的人，去试试吧！无论如何，大家都请务必通过描述中的链接查看这份开源示例代码。这份示例代码还使用了新的 HTTP 类型，它们让你可以在你的 App 和 Swift on Server 项目中使用相同的类型。这些数据类型是与 SwiftNIO 合作以开源包的形式发布的，所以请查看 Swift 博客，了解更多内容并提供你的反馈。

你可能已经注意到，可续传上传协议利用了使用 104 状态码的信息性响应。新的 HTTP 类型让在服务器端支持这些响应变得容易。在你的 App 中，URLSession 会为可续传上传自动处理 104 响应。但除此之外，URLSession 现在还提供了一个委托方法 didReceiveInformationalResponse。这让你的 App 能够处理其他中间响应，比如 102 Processing 或 103 Early Hints。

可续传协议是缓解网络中断、节省带宽的好方法。在处理大文件传输时，后台 URLSession 也很有用。想象一下，你的用户想要上传他们最近一次滑雪之旅拍下的一段巨大的 4K 视频。如果他们的连接中断了，你要确保在可能的情况下恢复上传。你可以自己完成所有的错误处理。或者，你可以让后台会话替你来做。

事实上，如果服务器支持，后台会话会为下载和上传任务自动处理恢复。

如果任务被中断，系统会以逐渐增大的时间间隔尝试恢复该任务。

如果任务无法恢复，系统会自动从头重试该任务。

也许你的用户在滑雪山上失去了蜂窝网络信号，或者一场暴风雪摧毁了他们的 Wi-Fi。后台会话总会等待网络连接，所以任务会在设备重新连接到互联网之后的某个时刻得到调度。

当你的用户正在上传视频时，他们可能会离开你的 App，或把设备收起来。也许他们正准备去滑更多的粉雪，而他们仍然期望上传能够继续。

这正是需要后台会话的场景。后台任务由系统调度，因此它们在你的 App 进程之外运行。这意味着，即使你的 App 被系统挂起或终止，你的网络任务仍能可靠地继续。对于可能耗时很久、且需要在用户离开你的 App 后继续进行的大文件传输，请使用后台会话。

最后，你的用户在你的 App 中时理应获得最佳体验，而这可能意味着把不太紧迫的任务安排到稍后执行。通过使用后台会话，你有若干种方式来高效地调度网络活动，为你的用户节省资源。

对于不需要立即发生的任务，考虑在你的后台配置上把 isDiscretionary 属性设为 true。这允许系统智能地调度你的任务，综合考虑诸如「用户是否在 Wi-Fi 上」「他们的设备是否接通电源」以及「网络是否受限」这样的因素。当下载供以后使用的资源，或者上传每夜备份或分析数据时，这可能是一个很好的选择。

为了在低数据模式下防止使用过多带宽，考虑把 allowsConstrainedNetworkAccess 属性设为 false。观看《网络技术进展》讲座，了解更多在你的 App 中支持低数据模式的技巧。

你还可以把后台任务本身调度到稍后开始——也就是人们不太可能使用系统资源的时候。深夜通常是调度大型备份这类任务的好时机。

为了进一步协助系统调度，我们可以设置 countOfBytesClientExpectsToSend 和 countOfBytesClientExpectsToReceive 属性。利用这些属性，你让系统能够最佳地分配资源，并把这些好处传递给你的用户。后台会话是处理那些不需要立即进行的大文件传输、或需要在你的 App 被挂起后继续的传输的绝佳工具。对于较小的任务，或需要尽快发生的任务，你可以使用标准的 URLSession。把恢复能力带进你的 App，让你的用户拥有可靠的网络体验。去看看 SwiftNIO 和 HTTP Types，让我们一起在 Swift 中打造最好的 HTTP 体验。最后，试试对大型或可自行斟酌时机的文件传输使用后台会话。你会发现许多为你的用户在最需要时节省资源的方法。感谢观看，请务必看看下面这些同样精彩的网络主题讲座。就到这里啦！♪ ♪

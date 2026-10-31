---
title: 认识 AsyncSequence
session_id: 10058
collection: wwdc2021
year: 2021
duration: '14:21'
topics: [Swift]
group: C · 并发、锁与线程
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2021/10058/'
content_hash: 'sha256:23031bf4c6abcc22'
translated: true
---

# 认识 AsyncSequence

<sub>WWDC2021 · 14:21 · Swift</sub>

随着时间推移迭代一串值，现在就像写一个「for」循环一样简单。了解新的 AsyncSequence 协议如何实现……

> [!note] 归档理由
> AsyncSequence 基础

## 相关资源

- [SE-0314: AsyncStream 与 AsyncThrowingStream](https://github.com/apple/swift-evolution/blob/main/proposals/0314-async-stream.md)
- [SE-0298: Async/Await：序列](https://github.com/apple/swift-evolution/blob/main/proposals/0298-asyncsequence.md)
- [The Swift Programming Language：并发](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10058/6/59A23687-3AF9-42AE-A922-079B630ED443/downloads/wwdc2021-10058_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10058/6/59A23687-3AF9-42AE-A922-079B630ED443/downloads/wwdc2021-10058_sd.mp4?dl=1)
- [使用 Create ML Components 组合高级模型](https://developer.apple.com/videos/play/wwdc2022/10020)
- [打造响应更灵敏的媒体 App](https://developer.apple.com/videos/play/wwdc2022/110379)
- [认识 Swift Async Algorithms](https://developer.apple.com/videos/play/wwdc2022/110355)
- [探索 Swift 中的结构化并发](https://developer.apple.com/videos/play/wwdc2021/10134)
- [认识 Swift 中的 async/await](https://developer.apple.com/videos/play/wwdc2021/10132)
- [在 URLSession 中使用 async/await](https://developer.apple.com/videos/play/wwdc2021/10095)
- [Foundation 新变化](https://developer.apple.com/videos/play/wwdc2021/10109)
- [QuakesTool](https://developer.apple.com/videos/play/wwdc2021/10058/?time=37)
- [迭代一个 Sequence](https://developer.apple.com/videos/play/wwdc2021/10058/?time=204)
- [编译器如何处理迭代](https://developer.apple.com/videos/play/wwdc2021/10058/?time=232)
- [编译器如何处理异步迭代](https://developer.apple.com/videos/play/wwdc2021/10058/?time=251)
- [迭代一个 AsyncSequence](https://developer.apple.com/videos/play/wwdc2021/10058/?time=268)
- [通过 break 提前终止迭代](https://developer.apple.com/videos/play/wwdc2021/10058/?time=336)
- [通过 continue 跳过值](https://developer.apple.com/videos/play/wwdc2021/10058/?time=351)
- [AsyncSequence 可能抛出错误](https://developer.apple.com/videos/play/wwdc2021/10058/?time=365)
- [在异步任务中并发迭代](https://developer.apple.com/videos/play/wwdc2021/10058/?time=435)
- [从 FileHandle 读取字节](https://developer.apple.com/videos/play/wwdc2021/10058/?time=476)
- [从 URL 读取行](https://developer.apple.com/videos/play/wwdc2021/10058/?time=496)
- [从 URLSession 读取字节](https://developer.apple.com/videos/play/wwdc2021/10058/?time=529)
- [通知](https://developer.apple.com/videos/play/wwdc2021/10058/?time=552)
- [使用 AsyncStream](https://developer.apple.com/videos/play/wwdc2021/10058/?time=670)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ 低音音乐播放中 ♪ ♪ Philippe Hausler：嗨，我叫 Philippe，我非常兴奋能向你介绍 Swift 中一个很酷的新特性：AsyncSequence。

今天我们将介绍异步序列是什么，以及它们背后的基本原理。

然后我们会讨论如何在你的代码中使用它们，并介绍一些新的 AsyncSequence API。

最后，我们将探索如何构建你自己的异步序列。

让我们直入主题。

这是我编写的一个非常简单的工具，用于说明你可以用 AsyncSequence 做的一些很酷的新事情。

在这个工具中，我们从一个端点的 URL 开始。

它列出了近期的地震。

通常来说，下载东西确实是一项可能需要一些时间的异步任务。

但在这种情况下，我们不想等所有内容都下载完；相反，我们希望内容一边被接收一边展示。

所以我决定做点不一样的尝试，使用新的 async/await 特性来获取这个端点响应的各行内容。

我们获取的数据以逗号分隔的文本格式编排，所以每一行都是一行完整的数据。

由于这个由行组成的异步序列会在每行被接收时就将其发出，这意味着我们眼前可能面临着一次非常大的下载。

但通过在拿到内容时就将其发出，这段代码感觉非常灵敏，而最棒的部分在于，你可以在这个新的异步上下文中使用你在普通序列中已经熟悉的那套东西。

这意味着你可以使用新的 for-await-in 语法来迭代，并使用 map、filter 和 reduce 等函数；或者——就像这个示例中那样——使用 dropFirst 函数来处理这些值。

那么这是如何工作的呢？嗯，我今天要讲的很多内容，其基础都来自 async/await 那场演讲。

但让我们回顾几个要点。

异步函数让你无需回调即可编写并发代码，方法是使用 await 关键字。

调用一个异步函数会使其挂起，然后在产生值或错误时恢复执行。

而 AsyncSequence 会在每个元素上挂起，并在底层迭代器产生值或抛出错误时恢复。

基本上，顾名思义，它们与普通的序列类似，但有几个关键区别。

也就是说，每个元素都是异步送达的。

但由于是异步送达，这意味着失败是完全有可能发生的。

一些异步序列会抛出错误，但如果不会失败，另一些则不会。

就像会抛出错误的函数一样，编译器会帮助确保在迭代或组合时错误得到处理。

一般而言，异步序列是对如何随时间产生值的描述。

因此，一个异步序列可能产生零个或多个值，然后通过其迭代器返回 nil 来表示完成，这与序列一样。

当发生错误时，那也是异步序列进入终止状态的时点，在错误发生之后，对迭代器的任何后续 next 调用都会返回 nil。

那么让我们先从普通迭代开始，深入了解这个定义是如何运作的。

这里有一个我们非常熟悉的模式。

这是一个 for-in 循环。

在这个例子中，它从一个序列迭代 quakes，并在震级超过某个值时调用一个函数。

编译器知道这种迭代应该如何工作，但它所做的并不是什么魔法。

编译步骤实际上只是做一些直截了当的变换。

让我们检视这些变换，以便你理解它的异步形式是什么样的。

这大致就是编译器构建前面代码时所做的事情。

它首先创建一个迭代器变量，然后使用一个 while 循环来获取迭代器在调用 next 时产生的每个地震。

要使用新的 async/await 功能，只需做一个微小的改动。

改动很简单，就是把那个 next 函数变成异步的。

现在，通过等待下一个地震，这次迭代就可以参与到 Swift 并发中了。

让我们倒回去，看看如果循环作用在一个异步序列上会是什么样子。

如前所述，我们需要 await 异步序列产出的每个条目。

这体现在新的 for-await-in 语法中。

这一切意味着，如果你知道如何使用 Sequence，你就已经对如何使用 AsyncSequence 有很好的认识了。

有几种使用异步序列的方式。

正如我们刚刚介绍的，你可以使用新的 for-await-in 语法；如果异步序列会抛出错误，你可以使用新的 for-try-await-in 语法。

这让你能够轻松地迭代异步产生的值——无需摆弄闭包——并使用你已经熟悉的语法来遍历它们。

甚至像 break 和 continue 这样的东西也能直接使用。

现在你已经对异步序列的理论有了很好的入门了解。

让我们进一步探索这种迭代。

给定一个异步序列作为来源，你可以使用 for-await-in 语法等待每一个值。

这意味着它会等待迭代器产生的每个条目，当到达终点时，循环完成。

在迭代异步序列时，break 显然是从循环内部提前终止迭代的好方法。

它的工作方式与普通序列一样。

这里我们在地震缺少位置数据时中断。

或者，如果我们有想要跳过的值，可以使用 continue。

在这个例子中，如果深度大于某个值，我们就跳过它们，继续等待下一个地震。

下载的下一次迭代与之前的工作方式一样，但在这种情况下，我们使用的来源可能会抛出错误。

与会抛出错误的函数一样，当被迭代的 AsyncSequence 可能抛出错误时，处理每个元素都需要 try。

同样与会抛出错误的函数一样，当你漏掉 try 时，编译器会检测出来并提供一个 Fix-it 来纠正错误。

这意味着当异步序列可能产生错误时，你始终是安全的，因为语言强制你要么抛出该错误，要么捕获它。

这第二次迭代会在第一个循环的迭代之后顺序运行。

顺序运行代码并不总是我们想要的。

如果与其他正在进行的事情并发地运行迭代更有用，你可以创建一个新的异步任务来封装这次迭代。

当你知道你使用的异步序列可能会无限期运行时，这会很有用。

现在，尽管那个序列有可能是无限的，但这种情况出现的可能性要小得多。

但在异步行为的世界里，这是更常见得多的事情，也是你在使用它们时需要考虑的事情。

值得庆幸的是，Swift 中的并发设施让这件事变得非常容易和安全。

当你可能希望从外部取消迭代时，这也非常有帮助。

这里我们可以并发地运行这两个迭代，并在稍后终止迭代。

用任务把一个可能无限的迭代的工作范围限定在某个容器的生命周期内是相当容易的。

接下来，让我们浏览一些自 macOS Monterey、iOS 15、tvOS 15 和 watchOS 8 起可用的 AsyncSequence API。

它们有很多，但我将展示其中的一些亮点。

从文件读取通常是异步行为的一个主要用例。

FileHandle 现在有一个新的 bytes 属性，可以访问来自该 FileHandle 的异步字节序列。

它可以与 AsyncSequence 上的新扩展配合使用，后者将异步字节序列转换为行。

但处理文件实在太常见了，以至于我们决定 URL 应当同时拥有 bytes 和 lines 这两个访问器。

这就是我在最初的示例中使用的同一个 API。

它是 URL 上的一个便捷属性，从内容中——无论是文件还是网络——返回一个由行组成的 AsyncSequence。

我确信这会让许多以前非常复杂的任务变得简单而安全。

有时从网络获取内容需要对响应和身份验证有更多的控制。

所以 URLSession 现在有一个 bytes 函数，可以根据给定的 URL 或 URLRequest 获取一个异步字节序列。

如果你想了解更多，你绝对应该观看「在 URLSession 中使用 async/await」这场 session，了解关于这一点以及 URLSession 大量其他新的异步能力的更多细节。

但文件和网络并不是 AsyncSequence 唯一适用的场景。

现在可以使用新的通知 API 来等待通知。

而且迭代并不是与 AsyncSequence 交互的唯一方式。

在这个例子中，我们正在等待第一条具有匹配的存储 UUID 的远程更改通知。

使用诸如 firstWhere 之类的方法，配合通知异步序列，可以实现一些非常巧妙的新设计模式，让以前表达复杂逻辑的代码变得紧凑且更易于阅读。

如果这些还不够酷，还有一大堆新 API 用于异步地处理来自异步序列的值。

它们应该会让你感到似曾相识，因为它们之中有一些与 Sequence 上可用的函数相同。

到目前为止我们已经介绍了一些，例如 dropFirst 和 firstWhere，但远不止这些。

几乎任何你能想到在 Sequence 上使用的操作，现在都有与之对应的异步版本，用于处理 AsyncSequence。

以上内容信息量很大，你可能在想：「嘿，这些新 API 真的很酷，这个语法也超简洁，但我怎样才能创建自己的异步序列呢？」嗯，我们就来做这件事！实现异步序列有几种方式，但我将重点介绍如何改造你现有的代码。

特别值得一提的是，有几种设计模式与 AsyncSequence 配合得非常好，而且我们有一些出色的设施，能让你已有的代码与这个新概念交互。

这些设计模式包括会被多次调用的闭包，也有一些委托（delegate）也能很好地配合。

几乎所有不需要返回响应、只是通报新值产生的模式，都是创建异步序列的理想候选。

这些设计模式非常常见，你今天的 App 里很可能已经有了几个。

这是一个常见的处理程序模式的示例。

它是一个拥有 handler 属性以及 start 和 stop 方法的类。

它看起来像是一个完美的 AsyncSequence 候选者。

现有的用法可能是这样的：创建一个监控器，指定一个获取值的处理程序，然后启动监控器，让地震被发送到处理程序。

之后，监控器可能会被停止，以取消事件的产生。

我们可以使用相同的接口，把用法改造为新的 AsyncStream 类型。

使用它只需要少量代码，并让你能够构建一个异步序列。

构造异步流（async stream）时，需要指定元素类型和一个构造闭包。

该闭包拥有一个 continuation，它可以多次产出值、结束，或处理终止。

这意味着，在这个例子中，监控器可以在构造闭包内部创建。

然后，处理程序可以被指定为向 continuation 产出地震。

接着，onTermination 可以处理取消和清理。

然后我们开始监控。

我们之前拥有的同一个监控器代码可以轻松地被封装进异步流的构造中。

这减少了在每个使用点复刻相同逻辑的需要。

这就是这个异步流的使用方式。

你可以使用强大的转换函数——例如 filter——以及新的 for-await-in 语法。

这让你可以专注于代码的意图，而不必担心复刻那些簿记工作，因为一切都封装在了一个地方。

AsyncStream 在创建你自己的异步序列方面提供了很大的灵活性。

这只是一个例子，在你的代码中可能还有许多其他可以改造的地方。

AsyncStream 是把你的现有代码改造为异步序列的好方法。

它处理你期望异步序列具备的所有事项，例如安全性、迭代和取消；它们还处理缓冲。

AsyncStream 是构建你自己的异步序列的可靠方式，也是你自己 API 的合适返回类型，因为产生元素的唯一来源就是构造过程。

如果你需要表示抛出的错误？嗯，我们有一个专门的类型！AsyncThrowingStream，它与 AsyncStream 类似，但可以处理错误。

它提供与 AsyncStream 相同的灵活性和安全性，但可以通过从迭代中抛出错误来处理失败。

AsyncSequence 是一个非常强大的工具，对于处理多个异步值来说，它既安全又让人熟悉。

如果你知道如何使用 Sequence，你就已经知道如何使用 AsyncSequence。

我们已经介绍了异步序列是什么以及如何使用它们，并带你认识了 AsyncStream。

我们深入探讨了定义它们的原理，介绍了一些新引入的异步序列，最后还讲了如何构建你自己的。

我热切期待着你接下来用它们做出什么。

♪

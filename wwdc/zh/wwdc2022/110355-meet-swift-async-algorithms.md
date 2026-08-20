---
title: 认识 Swift Async Algorithms
session_id: 110355
collection: wwdc2022
year: 2022
duration: '13:01'
topics: [Essentials, Swift]
group: C · 并发、锁与线程
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2022/110355/'
content_hash: 'sha256:6d5e569ab22b4e85'
translated: true
---

# 认识 Swift Async Algorithms

<sub>WWDC2022 · 13:01 · Essentials、Swift</sub>

了解 Apple 最新的开源 Swift 包：Swift Async Algorithms。我们将探讨这个包中的一些算法，它们可以……

> [!note] 归档理由
> Async Algorithms 库

## 相关资源

- [Swift Async Algorithms 包](https://github.com/apple/swift-async-algorithms)
- [Swift 编程语言：并发](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)
- [AsyncSequence](https://developer.apple.com/documentation/Swift/AsyncSequence)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/110355/4/459D7B80-E4A7-428F-ADA8-EF2543CE3350/downloads/wwdc2022-110355_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/110355/4/459D7B80-E4A7-428F-ADA8-EF2543CE3350/downloads/wwdc2022-110355_sd.mp4?dl=1)
- [认识演讲者：认识 Swift Async Algorithms](https://developer.apple.com/videos/play/wwdc2022/110938)
- [问答：Swift 并发](https://developer.apple.com/videos/play/wwdc2022/110480)
- [Swift 新变化](https://developer.apple.com/videos/play/wwdc2022/110354)
- [认识 AsyncSequence](https://developer.apple.com/videos/play/wwdc2021/10058)
- [认识 Swift Algorithms 和 Collections 包](https://developer.apple.com/videos/play/wwdc2021/10256)
- [通讯 App](https://developer.apple.com/videos/play/wwdc2022/110355/?time=121)
- [Zip](https://developer.apple.com/videos/play/wwdc2022/110355/?time=196)
- [Merge](https://developer.apple.com/videos/play/wwdc2022/110355/?time=309)
- [Suspending Clock](https://developer.apple.com/videos/play/wwdc2022/110355/?time=397)
- [Suspending Clock 与 Continuous Clock](https://developer.apple.com/videos/play/wwdc2022/110355/?time=416)
- [控制搜索消息](https://developer.apple.com/videos/play/wwdc2022/110355/?time=514)
- [Debounce](https://developer.apple.com/videos/play/wwdc2022/110355/?time=556)
- [Chunked by](https://developer.apple.com/videos/play/wwdc2022/110355/?time=621)
- [初始化方法中的转换](https://developer.apple.com/videos/play/wwdc2022/110355/?time=682)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ 器乐嘻哈音乐 ♪ 大家好，我叫 Philippe。Swift 拥有一套日益增长的开源包目录。我很高兴向大家介绍其中最新的一个：Swift Async Algorithms。这个包与 Swift Collections 和 Swift Algorithms 等其他包齐头并进。Swift Async Algorithms 包是一组专门专注于使用 AsyncSequence 随时间处理值的算法。但在我们深入探讨之前，让我们花一点时间来回顾一下 AsyncSequence。AsyncSequence 是一个让你描述异步产生的值的协议。基本上，它和 Sequence 很像，但有两点关键区别。它的迭代器的 next 函数是异步的，也就是说它可以使用 Swift 并发（Swift concurrency）来传递值。它还让你能够使用 Swift 的 throw 效果来处理任何潜在的失败。就像 Sequence 一样，你可以使用 for-await-in 语法来遍历它。简而言之，如果你知道如何使用 Sequence，那么你就已经知道如何使用 AsyncSequence 了。当 AsyncSequence 被引入时，我们几乎添加了所有你能期望在 Sequence 中找到的工具，并提供了相应的异步版本。你有像 map、filter、reduce 等算法。Swift Async Algorithms 包则更进一步，融合了更高级的算法，并与时钟（Clock）互操作，为你提供一些非常强大的功能。这是一个开源包，包含一系列增强 Swift 并发的 AsyncSequence 算法。去年我们引入了 Swift Algorithms 包。为了演示这些算法的用途，我们制作了一个通讯 App。这是一个很好的例子，展示了用那个包可以实现的一些丰富而强大的功能。我们认为有很多很好的机会可以利用该 App 迁移到 Swift 并发。为了重点介绍其中几个异步算法，我将带你了解我们使用的一些功能以及它们是如何工作的。首先，我们有一系列用于处理多个输入 AsyncSequence 的算法。这些算法专注于以不同方式将 AsyncSequence 组合在一起。但它们都有一个共同特点：它们接收多个输入 AsyncSequence，并产生一个输出 AsyncSequence。

你可能已经熟悉的一个是 Zip。Zip 算法接收多个输入并对其进行迭代，从而为每个基础序列产生一个结果元组。Zip 的每个输入都是构造 Zip 所依据的基础序列。异步 Zip 算法的工作方式与标准库中的 Zip 算法相同，但它并发地迭代每个基础序列，并且如果迭代其中任何一个发生失败，则会重新抛出错误。现在，实现这种能够重新抛出错误的并发迭代可能相当复杂。但 Swift Async Algorithms 包在我们的通讯 App 中为我们处理了所有这一切。我们之前有大量代码协调异步生成视频录制预览以及将视频转码为多种尺寸以高效存储和传输。通过使用 Zip，我们可以确保在将转码后的视频发送到服务器时，它附带一个预览。由于 Zip 是并发的，转码和预览都不会相互延迟。但这更进一步。Zip 本身并不偏好哪一侧先生成值，因此视频可能先生成，或者预览先生成，无论哪一侧，它都会等待另一侧发送完整的元组。我们可以等待成对的数据，以便它们可以一起上传，因为 Zip 并发地等待每一侧来构造值的元组。我们得出结论，将我们的传入消息建模为 AsyncSequence 非常有意义。因此，我们决定使用 AsyncStream 来处理这些消息，因为它能保持顺序，并将我们的回调转换为一个消息的 AsyncSequence。我们需要处理的一个请求特性是我们希望支持多个帐户。因此，每个帐户创建一个传入消息的 AsyncStream，但在实施时，我们需要将它们作为一个单一的 AsyncSequence 一起处理。这意味着我们需要一种算法来合并这些 AsyncSequence。幸运的是，Swift Async Algorithms 包恰好有这样一个算法，恰如其分地命名为 "Merge"。它在并发迭代多个 AsyncSequence 方面与 Zip 类似。但它不是创建成对的元组，而是要求基础序列共享相同的元素类型，并将这些基础 AsyncSequence 合并成一个单一的元素 AsyncSequence。Merge 的工作原理是取迭代时任意一侧产生的第一个元素。它会持续迭代直到没有更多可以产生的值，具体来说，就是当所有基础 AsyncSequence 的迭代器都返回 nil 时。如果任何一个基础序列产生错误，其他迭代将被取消。这让我们可以获取消息的 AsyncSequence 并合并它们。这些组合算法在值产生时并发工作，但有时与实际时间本身交互也很有用。Swift Async Algorithms 包利用 Swift 中新的 Clock API，引入了一系列与时间交互的算法。时间本身可能是一个非常复杂的话题，而 Swift（5.7）中新增了一组 API 来使其安全且一致：Clock、Instant 和 Duration。

Clock 协议定义了两个原语：一种在给定时刻后唤醒的方法，以及一种产生“现在”概念的方法。有几个内置的时钟。其中比较常见的是 ContinuousClock 和 SuspendingClock。你可以像使用秒表一样使用 ContinuousClock 来测量时间，无论被测量的对象处于什么状态，时间都在前进。另一方面，SuspendingClock 顾名思义，当机器进入睡眠状态时会暂停。我们在 App 中使用新的时钟 API，将现有的回调事件迁移到 clock sleep 函数，以处理在截止时间后关闭提醒。我们能够通过添加一个时长值来创建截止时间，该值专门指示我们想要延迟的秒数。Clock 还有一些方便的方法来测量执行工作的已用时长。这里我们有刚才提到的两个常见时钟：SuspendingClock 和 ContinuousClock。

下方显示的是正在测量的工作的潜在已用时长的展示。这两个时钟之间的关键区别在于机器休眠时的行为。

对于像这样长时间运行的工作，工作可能会暂停，就像我们这里所做的那样，但是当我们恢复执行时，ContinuousClock 在机器休眠期间已经前进了，而 SuspendingClock 则没有。通常，这种区别是确保动画等功能通过暂停执行的时间来按预期工作的关键细节。如果你需要与机器相关的时间进行交互，比如动画，请使用 SuspendingClock。

测量与设备前的用户相关的任务更适合使用 ContinuousClock。因此，如果需要按绝对时长（与人类相关的时间）进行延迟，请使用 ContinuousClock。Swift Async Algorithms 包使用这些新的 Clock、Instant 和 Duration 类型来构建通用算法，用于处理许多关于事件如何随时间处理的概念。在我们的通讯 App 中，我们发现这些对于提供对事件的精确控制非常有帮助。它让我们能够对交互进行速率限制并高效地缓冲消息。

或许我们利用时间最突出的领域是搜索消息。我们创建了一个控制器来管理结果通道。该通道将搜索结果从搜索任务编排回我们的 UI。搜索任务本身需要具有一些与时间相关的特定特性。我们希望确保对服务器上已发送消息的搜索进行速率限制。

算法 Debounce 在迭代时会等待一段静默期，然后才发射下一个值。这意味着事件可能会快速进入，但我们希望确保在安静一段时间后再处理值。当搜索字段的用户输入快速变化时，我们不希望搜索控制器为每次更改都触发搜索请求。相反，我们希望确保等待一个安静期，确定打字很可能已完成。默认情况下，Debounce 算法将使用 ContinuousClock。在这种情况下，我们可以对输入进行防抖，使其在指定时长内没有发生任何事时进行等待。时钟和时长不仅用于防抖，也用于其他算法。我们发现一个非常有用的方面是将消息分批发送到服务器。在 Swift algorithms 包中，有一组用于将值分块的算法。Swift Async Algorithms 包提供了这些算法，还增加了一套与时钟和时长互操作的版本。这一系列分块算法允许按数量、按时间或按内容控制分块。如果其中任何一个发生错误，该错误会被重新抛出，因此我们的代码在失败时是安全的。

我们使用了 `chunked(by:)` API 来确保消息块在指定的已用时长内被序列化和发送。这样，我们的服务器就能从客户端收到高效的数据包。我们能够使用这个 API 每 500 毫秒构建一批消息。这样，如果有人非常兴奋且打字飞快，发送到服务器的请求就会被分组。在处理集合和序列时，惰性处理元素通常是有用且高效的。AsyncSequence 的工作方式与 Swift 标准库中惰性算法的工作方式非常相似。但是，就像那些惰性算法一样，通常会有需要回到集合世界的情况。Swift Async Algorithms 包提供了一组初始化方法，用于使用 AsyncSequence 构造集合。这些初始化方法允许你使用已知是有限的输入 AsyncSequence 来构建字典、集合或数组。集合初始化方法让我们能够在消息的初始化过程中内置转换，并将我们的数据类型保持为 Array。这非常有用，因为我们有许多功能确实可以使用 Swift 并发进行更新。并且通过保留我们现有的数据结构，我们可以逐步迁移 App 的各个部分，并在有意义的地方进行迁移。到目前为止，我们只介绍了 Swift Async Algorithms 包的一小部分亮点。还有比我们今天介绍的更多内容。我们的算法种类繁多，从组合多个 AsyncSequence、按时间进行速率限制、将数据分解成块，但这些只是我们在 App 中大量使用的亮点。这个包拥有的远不止这些。它的范围从缓冲、归约、连接，到间歇性地注入值，等等。Swift Async Algorithms 包将用于处理随时间变化事物的算法集，扩展为广泛的高级功能，可以在你的 App 中为你提供帮助。试试看吧。我们非常期待看到你用这些算法构建的东西，而且这种期待是共同的。这个包正在与你一起开放地开发。感谢观看，并祝你在大会接下来的时间里愉快。♪ 器乐嘻哈音乐 ♪

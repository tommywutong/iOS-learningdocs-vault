---
title: 认识 Swift 中的 async/await
session_id: 10132
collection: wwdc2021
year: 2021
duration: '33:39'
topics: [Swift]
group: C · 并发、锁与线程
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2021/10132/'
content_hash: 'sha256:5524ece7a8c637f6'
translated: true
---

# 认识 Swift 中的 async/await

<sub>WWDC2021 · 33:39 · Swift</sub>

Swift 现在支持异步函数——这种模式通常被称为 async/await。了解新语法能如何让你的代码……

> [!note] 归档理由
> async/await 的语义与挂起点

## 相关资源

- [SE-0310：有副作用的只读属性](https://github.com/apple/swift-evolution/blob/main/proposals/0310-effectful-readonly-properties.md)
- [SE-0300：用 continuation 衔接异步任务与同步代码](https://github.com/apple/swift-evolution/blob/main/proposals/0300-continuation.md)
- [SE-0297：与 Objective-C 的并发互操作性](https://github.com/apple/swift-evolution/blob/main/proposals/0297-concurrency-objc.md)
- [SE-0296：Async/await](https://github.com/apple/swift-evolution/blob/main/proposals/0296-async-await.md)
- [The Swift Programming Language：并发](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10132/5/33A0E99C-1E53-4143-8A63-809D2E6CBA66/downloads/wwdc2021-10132_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10132/5/33A0E99C-1E53-4143-8A63-809D2E6CBA66/downloads/wwdc2021-10132_sd.mp4?dl=1)
- [效率静候：SwiftUI 中的后台任务](https://developer.apple.com/videos/play/wwdc2022/10142)
- [使用 Swift 并发消除数据争用](https://developer.apple.com/videos/play/wwdc2022/110351)
- [使用 Xcode 进行服务器端开发](https://developer.apple.com/videos/play/wwdc2022/110360)
- [可视化并优化 Swift 并发](https://developer.apple.com/videos/play/wwdc2022/110350)
- [把 Core Data 并发引入 Swift 和 SwiftUI](https://developer.apple.com/videos/play/wwdc2021/10017)
- [通过重复测试诊断不可靠的代码](https://developer.apple.com/videos/play/wwdc2021/10296)
- [探索 SwiftUI 中的并发](https://developer.apple.com/videos/play/wwdc2021/10019)
- [探索 Swift 中的结构化并发](https://developer.apple.com/videos/play/wwdc2021/10134)
- [认识 AsyncSequence](https://developer.apple.com/videos/play/wwdc2021/10058)
- [用 Swift Actor 保护可变状态](https://developer.apple.com/videos/play/wwdc2021/10133)
- [Swift 并发：幕后揭秘](https://developer.apple.com/videos/play/wwdc2021/10254)
- [Swift 并发：更新一个示例 App](https://developer.apple.com/videos/play/wwdc2021/10194)
- [在 URLSession 中使用 async/await](https://developer.apple.com/videos/play/wwdc2021/10095)
- [AppKit 的新变化](https://developer.apple.com/videos/play/wwdc2021/10054)
- [CloudKit 的新变化](https://developer.apple.com/videos/play/wwdc2021/10086)
- [Swift 的新变化](https://developer.apple.com/videos/play/wwdc2021/10192)
- [AVFoundation 的新变化](https://developer.apple.com/videos/play/wwdc2021/10146)
- [用完成处理程序编写函数](https://developer.apple.com/videos/play/wwdc2021/10132/?time=223)
- [结合 Result 类型使用完成处理程序](https://developer.apple.com/videos/play/wwdc2021/10132/?time=480)
- [使用 async/await](https://developer.apple.com/videos/play/wwdc2021/10132/?time=510)
- [异步属性](https://developer.apple.com/videos/play/wwdc2021/10132/?time=795)
- [异步序列](https://developer.apple.com/videos/play/wwdc2021/10132/?time=857)
- [使用 XCTestExpectation 测试](https://developer.apple.com/videos/play/wwdc2021/10132/?time=1282)
- [使用 async/await 测试](https://developer.apple.com/videos/play/wwdc2021/10132/?time=1316)
- [从同步桥接到异步](https://developer.apple.com/videos/play/wwdc2021/10132/?time=1350)
- [SDK 中的异步 API](https://developer.apple.com/videos/play/wwdc2021/10132/?time=1556)
- [异步替代方案与 continuation](https://developer.apple.com/videos/play/wwdc2021/10132/?time=1619)
- [为委托回调保存 continuation](https://developer.apple.com/videos/play/wwdc2021/10132/?time=1904)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ 大家好，我是 Nate，Apple Swift 团队的工程师。今天我和同事 Robert 将为大家介绍 Swift 中的 async/await。异步编程对你们中的许多人来说是家常便饭，所以你也知道，异步代码很容易写得又长又复杂，甚至还会出错。Swift 中的 async/await 可以帮上忙：用它，你可以像写普通代码一样轻松地写异步代码，而且这样写出来的代码会更好地体现你的思路，也会更安全。除此之外，SDK 里还有数百个可等待（awaitable）的方法可供使用。举例来说，UIKit 提供了从 UIImage 生成缩略图的功能，而且它同时提供了同步和异步两种函数来完成这个任务。

先简单回顾一下：当你调用一个同步函数——也就是普通的老式函数——你的线程会被阻塞，等待这个函数执行完毕。所以如果你的 fetchThumbnail 函数调用了 preparingThumbnail（UIKit 提供的同步函数），在它执行完之前，你的线程什么别的事都做不了。相比之下，如果你调用 prepareThumbnail(of:completionHandler:)——这个函数的异步版本——在它运行期间，你的线程可以自由地去做别的工作。等它完成后，会通过调用其完成处理程序来通知你。SDK 提供了许多异步函数，它们用几种不同的方式来告诉你它们已经完成了：有些像这样使用完成处理程序，有些依赖委托回调，还有很多标记为 async，直接返回一个值。

这些异步函数的共同点是：当你调用其中一个时，它会很快解除对线程的阻塞，让自己的工作开始运行，这样线程就可以在那项耗时较长的工作完成的同时去做别的事情。为了看清这个区别，我们来看一个大家可能很熟悉的例子。

在 Robert 和我一起构建的这个 App 里，我们有一个条目列表，其中每一行都会显示一张存储在服务器上的图片的缩略图。当需要为列表中的某一行准备好待显示的缩略图时，我们的视图模型里会调用 fetchThumbnail 方法。它通过一系列步骤把一个字符串转换成一个 UIImage：首先，视图模型的 thumbnailURLRequest 方法根据字符串创建一个 URLRequest；接着，URLSession 的 dataTask 方法获取该请求对应的数据；然后 UIImage 的 initWithData 根据这份数据创建一张图片；最后，UIImage 的 prepareThumbnail 方法从原图渲染出一张缩略图。这些操作中的每一个都依赖前一个的结果，这意味着它们必须按顺序执行。

其中一些操作能很快返回结果——从字符串构建 URLRequest、从数据构建 UIImage 都是如此——所以让它们以同步调用的方式，在函数恰好所在的那个线程上运行是没问题的。然而，有一些操作是要花时间的：下载组成一张图片的全部数据需要一段时间，而从中渲染出一张好看的缩略图也需要设备做一些开销不小的工作。这就是为什么 SDK 会提供异步函数来完成这些任务——所以这些调用应该是异步的。

在 Robert 和我尝试用 async/await 之前，我们是用完成处理程序来编写这个函数的。

这个函数接受两个参数：一个字符串，作为第一个操作的输入；还有一个完成处理程序，用来把结果传回给调用方。当 fetchThumbnail 被调用时，我们首先调用 thumbnailURLRequest——这个方法是同步的，所以不需要完成处理程序。接下来我们在共享的 URLSession 实例上调用 dataTask，传入那个 URLRequest 和一个完成处理程序。它会同步地产生一个 URLSessionDataTask，必须调用 resume 才能启动这项异步工作。之后 fetchThumbnail 就返回了，线程可以自由地去做别的工作。这一点非常重要，因为下载一张图片需要时间，你不会想让一个线程阻塞在那里等数据流进来。最终，要么图片下载完成，要么出了什么问题。不管哪种情况，请求都会完成，传给 dataTask 的完成处理程序会被调用，并带上几个可选值：数据、响应和错误。

如果确实出了问题，我们就需要调用完成处理程序并把错误传递出去。如果一切顺利，我们就用 UIImage 的 initWithData 根据数据创建一张图片。因为它是同步的，我们可以写普通的顺序代码来处理结果：如果没有生成图片，我们就结束了；如果生成了图片，那么最后我们就在它上面调用 UIKit 的 prepareThumbnail 方法，并传入一个完成处理程序。在它的工作完成期间，线程是不被阻塞的，可以自由地去做别的工作。

缩略图准备好之后，如果生成缩略图成功，这个完成处理程序会被调用并带上一张图片，否则就是 nil。如果确实成功了，我们就调用自己的完成处理程序，并把图片传递过去。

但正如 Robert 向我指出的那样，这里有个问题：fetchThumbnail 的调用方期望在 fetchThumbnail 完成工作时得到通知，即便失败了也一样。而目前，我们把调用方晾在了一边。我太习惯写 "guard else return" 了，以至于忘了调用完成处理程序，而且忘了两次。所以如果从数据创建 UIImage 失败，或者准备缩略图失败，fetchThumbnail 的调用方将永远不会收到通知，那一行也永远不会更新——它只会一直显示一个转圈的加载指示符。

这就是为什么，作为 fetchThumbnail 的作者，我们必须在任何情况下都通知调用方——所以函数的每一条执行路径都应该通知他们。要做到这一点，我们需要在出错时调用完成处理程序，并把错误传递出去。一个普通函数是通过抛出错误来把错误传给调用方的，而且 Swift 会确保：无论函数的执行路径怎么走，只要没有返回一个值，就一定会抛出一个错误。但在这里我们没法使用 Swift 通常的错误处理机制——我们不能在这些完成处理程序内部，遇到问题时直接抛出一个错误。这很遗憾，因为这意味着 Swift 没法帮我们检查这部分代码：对 Swift 来说，像 fetchThumbnail 里这样的完成处理程序只是一个闭包。虽然我们希望确保它总是会被调用，但在 Swift 里没有办法强制保证这一点。这就是为什么当我从那两个 guard 里直接 return 时，我没有得到编译错误——是 Robert 指出了这个问题，我才去修复它。所以，确保你的完成处理程序最终一定会被调用，这件事得由你自己来保证。当我们俩坐下来写这个函数时，我们只是想按顺序执行几个操作，其中两个是同步的，两个是异步的、需要完成处理程序。我们做到了，但最后写出了大约 20 行代码，里面藏着五处可能出现细微 bug 的机会。我们想要的只是按顺序执行那四个操作，但得到的却是一段难以读懂、难以写对、还遮蔽了我们真实意图的代码。

现在，我们本可以用一些办法让这段代码更安全一点。比如说，我们本可以使用标准库的 Result 类型——虽然这样会更安全一点，但也会增加一些形式上的负担，让代码变得更丑、更长。人们也用过类似 future 这样的技术，从其他角度来改善异步代码。但这些方法都没能给我们提供简单、容易、又安全的代码。有了 async/await，我们可以做得更好。Robert 和我重写了执行那四个步骤的函数，这一次，我们用上了 async/await。

这个函数仍然接受一个字符串作为参数，但上次还需要传入一个完成处理程序，这次函数本身被标记为 async。当你把一个函数标记为 async 时，这个关键字应该写在函数签名里 "throws" 的前面，就像这样；如果函数不会抛出错误，就写在箭头前面。把函数标记为 async，能让函数本身及其签名变得更简单：如果缩略图成功生成，就直接把它返回；如果遇到了错误，就直接抛出。当 fetchThumbnail 被调用时，和之前一样，它一开始会调用 thumbnailURLRequest——这个函数是同步的，所以线程会被阻塞，等它完成工作。

接下来，它通过在共享的 URLSession 上调用 data(for: request) 来开始下载数据。和 dataTask 一样，这个方法也是 Foundation 提供的，也是异步的，但和 dataTask 不同的是，data 方法是可等待的（awaitable）。所以调用它之后，它会很快挂起自己、解除对线程的阻塞，线程接下来就可以自由地去做别的工作了。

这里之所以有 "try"，是因为 data 方法被标记为 "throws"。回想一下早先那个版本，我们不是得检查错误，然后显式调用我们的完成处理程序并把错误传进去吗？而在这个可等待的版本里，所有那些代码都被浓缩成了一个 try 关键字。就像调用标记为 "throws" 的函数需要 "try" 一样，调用标记为 "async" 的函数需要 "await"。如果一个表达式里有多个 async 函数调用，你只需要写一次 "await"，就像一个表达式里有多个会抛错误的函数调用时，你也只需要写一次 "try"。总的来说，这个函数调用被标记为 "try await"。当你处理一个既是 async 又会抛错误的表达式时，你需要把 try 放在 await 前面，就像这样。

最终，当数据下载完成后，data 方法会恢复执行并返回给 fetchThumbnail。这时，data 方法返回的值，或者它抛出的错误，就会流入进来。如果它抛出了一个错误，那么 fetchThumbnail 自己也会依次抛出那个错误；否则，data 和 response 这两个变量就会被赋值。这和早先版本里，传给 URLSession 的 dataTask 方法的完成处理程序被调用时发生的情况是类似的。

在这两个版本里，都有 URLSession 的异步方法产生的值和错误流入进来。但可等待的这个版本要简单得多，它准确地表达了我们的意图：发起这个请求，把拿到的值赋给变量，以便我们使用；如果碰巧遇到了问题，就抛出一个错误。

接下来，fetchThumbnail 会尝试根据下载的数据创建一个 UIImage。如果成功了，就会通过访问它的 thumbnail 属性，为这张图片渲染出一个缩略图。在生成缩略图的过程中，线程是自由的，可以去做别的事情，直到 thumbnail 属性最终恢复执行并返回给 fetchThumbnail。

如果缩略图渲染成功，fetchThumbnail 会把它返回；否则，就会抛出一个错误。

和完成处理程序版本相比，如果没有生成缩略图，Swift 会确保我们要么在这里抛出一个错误，要么返回一个值——我们不能就这么悄无声息地失败。这就是全部了，这就是我们需要的全部代码：这个函数做的事情和之前那个完成处理程序版本完全一样，但它不再是 20 行代码，而只有 6 行，而且全都是顺序执行的代码。

那四个需要按顺序执行的操作被一个接一个地列在这里，而且 Swift 会确保这个函数在完成时总会通知它的调用方，要么是返回，要么是在出问题时抛出错误。这只是使用 async/await 如何改变你的 Swift 异步代码的其中一个例子——让它更安全、更短，也更好地体现你的意图。

我们来深入了解一下 fetchThumbnail 具体是怎么实现的。在倒数第二行，虽然那里没有函数调用，但触发渲染缩略图的这个表达式还是被标记上了 "await"。这是因为 thumbnail 属性是 async 的——不只是函数可以是 async，属性也可以，初始化方法也可以。顺带一提，thumbnail 属性并不是 SDK 的一部分，其实是 Robert 加上去的，我们来看一下它。

他把这个属性定义在 UIImage 的一个 extension 里，实现很简短：先构造一个 CGSize，然后把它传给 byPreparingThumbnail(ofSize) 并等待其结果。顺便说一句，self 上的这个方法就是我们之前用过的那个方法的可等待版本。

这里有几点需要注意。首先，它有一个显式的 getter——要把一个属性标记为 async，这是必须的。从 Swift 5.5 开始，属性的 getter 也可以抛出错误，而且和 async 函数签名一样，如果一个属性既是 async 又会抛错误，async 关键字要写在 throws 前面。

其次，这个属性没有 setter——只有只读属性才能是 async 的。

在函数、属性和初始化方法里，await 都可以用在表达式上，用来表示函数可能在这个点上解除对线程的阻塞。还有一个地方也可以用 await：在 for 循环里遍历异步序列（async sequence）。异步序列就和普通序列一样，只是它是异步地产出各个元素的，所以获取下一个条目必须标注 await 关键字，表示它是 async 的。

当函数一遍又一遍地遍历这个异步序列时，它可能会在等待下一个元素时解除对线程的阻塞，然后要么带着下一个元素恢复执行、进入循环体，要么，如果已经没有剩余元素了，就在循环结束后恢复执行。

想进一步了解 AsyncSequence，请观看 "Meet AsyncSequence" 这场演讲；如果你对并行运行大量异步任务感兴趣，可以看看 "Explore structured concurrency in Swift" 这场演讲。

所以，有很多地方都可以使用 await。这个关键字表示你的 async 函数可能会在那里挂起。一个 async 函数挂起意味着什么呢？为了回答这个问题，我们来想想调用一个函数时会发生什么。

当你调用任何函数时，你会把你的函数所运行的那个线程的控制权交给那个函数。如果你调用的是一个普通函数，比如这里的 thumbnailURLRequest，那么在它完成之前，线程会一直被它占用，为它工作。

这项工作可能就在函数体本身里，也可能在它调用的其他函数里。最终，那个函数会完成——要么返回一个值，要么抛出一个错误。完成之后，它会把控制权交还给你的函数。这是一个普通函数放弃线程控制权的唯一方式：完成自己的工作；而且你的函数是它唯一能把控制权交还的对象。如果你调用的是一个 async 函数，情况就不一样了：和普通函数一样，它完成时也会把控制权还给你的函数；但和普通函数不同的是，它还可以用一种完全不同的方式放弃线程的控制权——挂起。

就像普通函数一样，当你调用一个 async 函数时，你把线程的控制权交给了它。

一旦它开始运行，一个 async 函数就可以挂起。挂起时，它放弃了对线程的控制权，但它并不是把控制权还给你的函数，而是把线程的控制权交给系统。这时，你的函数也随之被挂起。挂起是这个函数告诉系统的一种方式："我知道你还有很多工作要做，你来决定什么最重要。" 这是不是很有协作精神？所以一旦函数把自己挂起，系统就可以自由地用这个线程去做别的工作了。到了某个时刻，系统会判断，眼下最重要的工作就是继续运行那个之前把自己挂起的 async 函数，这时系统就会恢复它。这个 async 函数就重新拿回了线程的控制权，可以继续做自己的工作。

如果它愿意，还可以再次把自己挂起——事实上，它可以按需要挂起自己任意多次。

另一方面，它也完全可能一次都不需要挂起自己：虽然一个 async 函数可能会挂起，但被标记为 async 并不必然意味着它一定会挂起；同样地，你看到一处 "await"，也不代表函数一定会在那里挂起。但最终，不管是从始至终都没挂起过，还是在最后一次恢复之后，这个函数都会完成，把线程的控制权连同一个值或一个错误一起交还给你的函数。

我们再看一遍 fetchThumbnail，看看它挂起时会发生什么。

当 fetchThumbnail 调用 URLSession 的 async data 方法时，data 方法会以只有 async 函数才能使用的这种特殊方式，停止在这个线程上执行——也就是挂起。它把线程的控制权交给系统，并请求系统为 URLSession 的 data 方法安排这项工作。

但此时，控制权在系统手里，那项工作未必会立刻开始，线程反而可以被用来做别的事情。我们来看看这可能是怎么发生的：假设 fetchThumbnail 被调用之后，用户点了一个会上传一些数据的按钮——比如说，他们对一条帖子做出了反应。那么系统就可以自由地先执行"提交用户反应"这项工作，再去处理之前排队等待的工作。

一旦那件临时插入的工作完成，URLSession 的 data 方法就可能会恢复执行；也可能系统会转而去执行别的工作。最终，一旦 data 方法完成，它会返回给 fetchThumbnail。函数被挂起期间，别的工作可以被执行，正是因为这一点，Swift 才坚持要求你用 await 关键字标注 async 调用——你需要意识到，当你的函数挂起时，你 App 的状态可能发生剧烈变化。

其实用完成处理程序的时候，情况同样如此。但因为 async/await 代码没有完成处理程序那一整套形式上的写法和缩进，所以 await 关键字正是你察觉"一段代码不是作为一个整体事务执行的"的方式。函数可能会挂起，而在函数内部各行代码之间，函数挂起期间，别的事情可能已经发生了。

不仅如此，函数还可能恢复到完全不同的另一个线程上。想了解这些问题，可以看看 "Protect mutable state with Swift actors" 这场演讲。这里有几件关于 async/await 需要记住的重要事情。第一，当你把一个函数标记为 async 时，你是在允许它挂起，而且当一个函数把自己挂起时，它也会挂起它的调用方——所以调用方也必须是 async 的。

第二，为了指出一个 async 函数可能在哪里挂起一次或多次，需要使用 await 关键字。

第三，当一个 async 函数被挂起时，线程并没有被阻塞，所以系统可以自由地去调度别的工作，甚至是本应更晚才启动的工作也可能被先执行。这意味着，在函数被挂起期间，你 App 的状态可能会发生很大变化。最后，当一个 async 函数恢复执行时，它所调用的那个 async 函数返回的结果会流回原来的函数，执行会从中断的地方继续下去。你已经看到了 Swift 中 async/await 是怎么工作的，接下来 Robert 会告诉你如何在自己的项目里开始使用它。谢谢，Nate。刚才 Nate 给大家展示了我们一起构建的这个 App。他改造过的那个 thumbnail 函数在好几个地方都有调用，所以我们也需要把这些地方迁移过去、采用并发特性。我们先从对现代软件开发至关重要的一件事说起：测试。我们希望测试异步代码能像测试同步代码一样轻松，所以 XCTest 开箱即支持 async。以前那种繁琐的流程——设置一个 expectation、调用被测的 API、满足这个 expectation，然后还得等待一段不确定的时间——现在只需要给测试函数加上 async 关键字，去掉 XCTest 的 expectation 及其满足调用和显式的 await，转而直接 await 调用 Nate 之前展示的那个新的异步 fetchThumbnail 函数的结果，就变得同样轻松了。

现在测试已经搞定了，我们来看看应用代码本身，尤其是这个列表里每一行缩略图视图背后的 SwiftUI 代码。

创建一个图片单元格时会传入一个 post，每个 post 都有一个 ID，我们把它传给 viewModel，让它异步获取缩略图。你已经在测试代码里见过怎么改造这类调用了，我们来试一下：首先去掉完成处理程序，然后加上 "try" 来处理可能出现的错误，再加上 "await" 来完成对一个 async 函数的调用。但当我们尝试编译这段代码时，出问题了：Swift 编译器告诉我们，不能在本身不是 async 的上下文里调用 async 函数。这里，onAppear 这个修饰符接受的是一个普通的、非 async 的闭包，所以我们需要一种方式，在同步世界和异步世界之间架起一座桥。

解决办法是使用 async task 函数。一个 async task 会把闭包里的工作打包起来，交给系统在下一个可用线程上立即执行——就像在一个全局 dispatch queue 上调用 async 函数一样。

它在这里最大的好处是：可以从同步上下文里调用 async 代码。

再次重新编译后，编译器满意了。Async task 属于一整个系列的 API，能让你用一种熟悉、天然结构化的风格构建丰富的并发 Swift 代码。

想了解更多，可以看看 "Explore structured concurrency in Swift"；想了解如何在 SwiftUI App 里充分利用 async 代码，可以看看 "Discover concurrency in SwiftUI"。我们已经完成了对所有调用 fetchThumbnail 函数的地方的迁移，但我们的 App 里还有很多地方可以采用 async/await。为了能快速上手，我们建议从一个现有 API 的异步替代方案开始入手：SDK 提供了数百个使用完成处理程序的 API，因为它们是以异步方式替你完成工作的。当这些 API 摆在一起对比时，一些模式就会显现出来。

尽管它们可能名字不同、用途各异，但所有这些函数都有同样的核心 API 契约：你调用它们，它们会通过提供的完成处理程序回调你，并把得到的结果传进去。前面 Nate 向你展示过，你可以 await 异步函数的结果，从而写出更自然的代码。如果能把这些回调块转换成这些 async 函数，那该有多棒？从 Swift 5.5 开始，这正是实际发生的事：Swift 编译器会自动查看从 Objective-C 导入的完成处理程序代码，并提供一个 async 替代版本。但我们没有止步于此：许多委托 API 也包含会把完成处理程序传给你的方法，以合作的方式调用这个处理程序，来通知框架某个异步任务已经完成。以这个调用 fetchThumbnail 来为某个 post 显示时间线条目的 ClockKit 复杂功能数据源为例。

和之前一样，我们必须确保在所有路径上都调用了完成处理程序，而这里因为有闭包，会带来不少额外的干扰代码。

有了 async/await，就不再需要这样了：这个委托方法有一个我们可以改用的 async 替代版本。首先，用的是这个 async 替代版本的名字，它去掉了开头的 "get"——我们建议 async 函数省略像 "get" 这样的、用来表示调用结果不是直接返回的开头词，毕竟既然这是一个 async 替代函数，它就是直接返回一个时间线条目的。既然现在已经建立了 async 上下文，我们就调用 fetchThumbnail 的 async 版本。最后，我们从这个方法里返回一个时间线条目，而不是调用现已被删除的那个完成块。

我们在这里重点介绍的这些 async API 只是冰山一角。

想了解更多，可以看看这些场次，它们会更深入地讲解这些 API 本身，以及你在采用 async/await 时该如何使用它们。

所有这些都是 Swift 会替你自动创建 async 替代版本的例子，但在你的代码里，难免会有一些地方，需要你自己创建一个 async 替代版本。

我们来看看这在实践中是什么样子。

在我们的 App 里，我们用这个 getPersistentPosts 函数来获取任何持久化到 Core Data 存储里的 post。这个函数在我们 App 里被调用的地方，比那个 async 版本的 thumbnail 函数要多得多，所以如果到处都直接改成 async，那将是一次很大的改动。而且因为我们用的是 NSAsynchronousFetchRequest，这个函数看起来正好适合做成一个 async 替代版本。首先，我们做一个 async 函数，并转换返回值；由于这个函数可能产生错误，我们同时把它标记为 "throws"。

接着，我们调用 getPersistentPosts 的完成处理程序版本，然后……好吧，现在我们卡住了。

我们需要把回调返回的结果，传回给正在等待调用 async persistentPosts 函数的那些地方。不仅如此，那些调用方还处于挂起状态，我们需要确保在正确的时间点、带着正确的数据恢复它们，让它们能继续完成剩下的工作。

前面 Nate 已经给你展示了 Swift 和系统是怎么协作、替我们处理恢复 async 代码这件事的。我们来更深入地看看这个挂起/恢复的过程具体是怎么运作的，看能不能为我们的问题想出一个类似的解决方案。

当 persistentPosts 的 async 版本被调用时，它会调用进 Core Data。在稍后的某个时刻，Core Data 会调用完成处理程序，并传入这次 fetch 请求的结果。这种情况和 Nate 之前给你展示的那个几乎一模一样：那次是我们的 fetchThumbnail 函数请求系统（而不是 Core Data）来恢复一个被挂起的 async 函数调用。

唯一缺少的，就是一座桥——用来 await 完成处理程序，并带着 fetch 请求的结果恢复执行。

这种模式反复出现，而且它有一个名字：continuation。在这场演讲里，Nate 和我其实已经给你展示过很多 continuation 的例子：那些接受完成块的方法。

方法的调用方等待函数调用的结果，并提供一个闭包来指定接下来要做什么。当函数调用完成时，它会调用完成处理程序，恢复调用方想用结果继续做的任何事情。这种协作式的执行方式，正是 Swift 里 async 函数的工作方式。

为了把这一点显式地表达出来，Swift 提供了一个特性，让你可以用一种高层次、安全的方式创建、管理并恢复 continuation。

我们回到刚才的例子，看看 continuation 能怎么帮我们完成这个 async 替代版本的编写。

withCheckedThrowingContinuation 函数，能把带有错误的回调块，提升为会抛出错误的 async Swift 函数；它还有一个对应版本叫 withCheckedContinuations，用于你确定某个函数永远不会抛错误的场景。这些函数是获取一个 continuation 值的方式，你可以用这个值来恢复一个被挂起的 async 函数。这也搭起了这座桥的第一部分——让我们能够 await 对 getPersistentPosts 的调用。

我们把这座桥搭完。continuation 值提供了一个 resume 函数，我们把完成处理程序里的结果放进去调用它。不仅如此，resume 还提供了我们所缺的那个环节，用来解除任何正在等待 persistentPosts 函数结果的调用的挂起状态。就这样，一整套从完成处理程序到 async 函数的桥，就完工了。

Continuation 提供了一种强大的方式，让你能手动控制一个 async 函数的执行过程，但有几件事需要留意。Continuation 有一个简单但很重要的契约：在每一条路径上，resume 都必须被调用恰好一次。但别担心，Swift 在这一点上会帮你兜底。

如果 continuation 被丢弃却没有调用 resume，Swift 运行时会记录一条警告，因为这会导致 async 调用永远无法解除挂起状态。

然而，如果同一个函数里，一个 continuation 被多次 resume，这是一个更严重的错误，因为它可能损坏程序数据。为了应对这一点，Swift 运行时会检测多次调用 resume 的情况，并确保在第二次 resume 时触发一个致命错误。

记住这一点，我们再来强调一个可能会用到已检查 continuation（checked continuation）的重要场景。

许多 API 是事件驱动的：它们提供委托回调，在特定的关键时刻通知我们的应用程序，并让它做出恰当的响应。为了正确采用 async/await，我们得保存这个 continuation，并在稍后恢复它。像之前一样，我们创建一个 checked continuation。

然后我们保存它，并启动这项工作。

为了遵守 checked continuation 的 API 契约，我们要确保 resume 这个活跃的 continuation，最后再把它置为 nil，这样我们就不会不小心多调用一次。

一定要记住：这里的 checked continuation 值代表着手动恢复对这个 API 的任何 async 调用的能力，所以它必须在所有路径上都被调用。

如果你的委托 API 在某些情况下会被调用很多次，或者一次都不会被调用，那么确保任何活跃的 continuation 都恰好被 resume 一次，就至关重要。

想了解更多关于 Swift 并发底层细节（包括 continuation）的内容，请看 "Swift concurrency: Behind the scenes" 这场演讲。

以上就是对 Swift 中 async/await 的一次快速巡礼。我们向你展示了 async 和 await 这两个关键字在运行时具体是怎么工作的，以及你可以怎样在自己的应用和框架里采用它们。为了帮你上手，我们还展示了 SDK 中一些可用的 async API，并演示了如何把你现有的代码从同步世界桥接到 async 世界。

Async/await 是整个 Swift 并发特性宇宙的基础，我们很期待看到你会用它们构建出什么。感谢观看。

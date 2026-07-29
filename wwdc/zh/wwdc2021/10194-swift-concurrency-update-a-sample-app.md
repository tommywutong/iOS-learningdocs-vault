---
title: 'Swift 并发：更新示例 App'
session_id: 10194
collection: wwdc2021
year: 2021
duration: '61:00'
topics: [Swift]
group: C · 并发、锁与线程
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2021/10194/'
content_hash: 'sha256:58ad54df131aee2c'
translated: true
---

# Swift 并发：更新示例 App

<sub>WWDC2021 · 61:00 · Swift</sub>

> [!note] 归档理由
> 把回调式代码迁到并发的实战

## 相关资源

- [更新 App 以使用 Swift 并发](https://developer.apple.com/documentation/swift/updating_an_app_to_use_swift_concurrency)
- [《Swift 编程语言：并发》](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)
- [HD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10194/12/ED815E9C-D0B9-4B94-ABA6-1EFDCFB2D5D4/downloads/wwdc2021-10194_hd.mp4?dl=1)
- [SD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10194/12/ED815E9C-D0B9-4B94-ABA6-1EFDCFB2D5D4/downloads/wwdc2021-10194_sd.mp4?dl=1)
- [创建更响应式的媒体 App](https://developer.apple.com/videos/play/wwdc2022/110379)
- [使用 Swift 并发消除数据争用](https://developer.apple.com/videos/play/wwdc2022/110351)
- [可视化和优化 Swift 并发](https://developer.apple.com/videos/play/wwdc2022/110350)
- [探索 Swift 中的结构化并发](https://developer.apple.com/videos/play/wwdc2021/10134)
- [认识 Swift 中的 async/await](https://developer.apple.com/videos/play/wwdc2021/10132)
- [使用 Swift Actor 保护可变状态](https://developer.apple.com/videos/play/wwdc2021/10133)
- [Swift 并发：幕后故事](https://developer.apple.com/videos/play/wwdc2021/10254)
- [SwiftUI 的新特性](https://developer.apple.com/videos/play/wwdc2021/10018)
- [在 SwiftUI 中构建复杂功能](https://developer.apple.com/videos/play/wwdc2020/10048)
- [调用 HKHealthKitStore 的 save(_:) 方法的 async 版本](https://developer.apple.com/videos/play/wwdc2021/10194/?time=454)
- [将 save(drink:) 改为 async 函数](https://developer.apple.com/videos/play/wwdc2021/10194/?time=578)
- [创建一个新的异步任务](https://developer.apple.com/videos/play/wwdc2021/10194/?time=615)
- [为 requestAuthorization(completionHandler:) 添加 async 替代方法](https://developer.apple.com/videos/play/wwdc2021/10194/?time=733)
- [更新 requestAuthorization() 的 async 版本](https://developer.apple.com/videos/play/wwdc2021/10194/?time=895)
- [为 loadNewDataFromHealthKit(completionHandler:) 添加 async 替代方法](https://developer.apple.com/videos/play/wwdc2021/10194/?time=943)
- [创建一个使用 continuation 的 queryHealthKit() 辅助函数](https://developer.apple.com/videos/play/wwdc2021/10194/?time=1063)
- [更新 loadNewDataFromHealthKit() 的 async 版本](https://developer.apple.com/videos/play/wwdc2021/10194/?time=1217)
- [使用 @MainActor 注解 updateModel(newDrinks:deletedDrinks:)](https://developer.apple.com/videos/play/wwdc2021/10194/?time=1509)
- [从 updateModel(newDrinks:deletedDrinks:) 的调用点移除 MainActor.run](https://developer.apple.com/videos/play/wwdc2021/10194/?time=1603)
- [将 HealthKitController 改为 Actor](https://developer.apple.com/videos/play/wwdc2021/10194/?time=1764)
- [将 updateModel(newDrinks:deletedDrinks:) 移至 CoffeeData](https://developer.apple.com/videos/play/wwdc2021/10194/?time=1951)
- [更新 updateModel(newDrinks:deletedDrinks:) 的调用点](https://developer.apple.com/videos/play/wwdc2021/10194/?time=1998)
- [将已废弃的完成处理程序方法标记为 nonisolated](https://developer.apple.com/videos/play/wwdc2021/10194/?time=2041)
- [创建一个用于加载和保存的私有 CoffeeDataStore Actor](https://developer.apple.com/videos/play/wwdc2021/10194/?time=2180)
- [为 CoffeeDataStore 添加专用的日志记录器](https://developer.apple.com/videos/play/wwdc2021/10194/?time=2203)
- [将 Actor 的实例添加到 CoffeeData](https://developer.apple.com/videos/play/wwdc2021/10194/?time=2225)
- [将 savedValue 属性从 CoffeeData 移至 CoffeeDataStore](https://developer.apple.com/videos/play/wwdc2021/10194/?time=2317)
- [将 dataURL 属性从 CoffeeData 移至 CoffeeDataStore](https://developer.apple.com/videos/play/wwdc2021/10194/?time=2340)
- [将 currentDrinks 的 didSet 移至一个新的 async 函数](https://developer.apple.com/videos/play/wwdc2021/10194/?time=2562)
- [更新 addDrink(mgCaffeine:onData:) 以调用 drinksUpdated()](https://developer.apple.com/videos/play/wwdc2021/10194/?time=2640)
- [更新 updateModel(newDrinks:deletedDrinks:) 以调用 drinksUpdated()](https://developer.apple.com/videos/play/wwdc2021/10194/?time=2649)
- [将 updateModel(newDrinks:deletedDrinks:) 方法标记为 async](https://developer.apple.com/videos/play/wwdc2021/10194/?time=2657)
- [完成将 save() 方法移入 CoffeeDataStore](https://developer.apple.com/videos/play/wwdc2021/10194/?time=2726)
- [将 load() 方法的上半部分移入 CoffeeDataStore](https://developer.apple.com/videos/play/wwdc2021/10194/?time=2780)
- [更新 CoffeeData 中的 load() 方法以使用 Actor](https://developer.apple.com/videos/play/wwdc2021/10194/?time=2881)
- [更新 CoffeeData 的初始化方法以使用异步任务](https://developer.apple.com/videos/play/wwdc2021/10194/?time=2948)
- [使用 @MainActor 注解 CoffeeData](https://developer.apple.com/videos/play/wwdc2021/10194/?time=3003)
- [替换 ExtensionDelegate 的 handle(_:) 方法中的完成处理程序用法](https://developer.apple.com/videos/play/wwdc2021/10194/?time=3138)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ 贝斯音乐播放中 ♪ ♪ Ben Cohen: 大家好，我是 Swift 团队的 Ben，在这个视频中，我将带您逐步将一个现有应用程序迁移到使用 Swift 的新并发特性。我们将看到这些新特性如何帮助您编写更清晰的异步代码，防范潜在的数据争用（data race），同时也会探讨一些逐步将代码迁移到这种新操作方式的技巧。

我将使用一个名为 Coffee Tracker 的 App，它基于 WWDC 2020 关于创建和更新手表复杂功能的一次演讲。这是一个简单的 App，可以让您追踪今天喝过的所有咖啡，同时在表盘上显示当前咖啡因水平的复杂功能。对于我们的目的来说，这是一个很好的例子，因为虽然它是个小型 App，但它展示了我们需要考虑的各种不同内容，包括并发如何与 SwiftUI 协同工作、watch SDK 的委托回调、一些 I/O 操作，以及与 Apple SDK 中异步 API 的交互。现在让我们快速浏览一下这个 App。它大致分为三层。首先是 UI 层。这主要是 SwiftUI 视图，但在这里我们也可以将复杂功能数据源等视为 UI 层的一部分。接下来是模型层，它包含几个表示咖啡因饮品的简单值类型，以及一个名为 "Coffee model" 的模型类型。现在，这可以说是 UI 模型。也就是说，它是为 UI 层提供显示数据的地方。它是一个为 SwiftUI 视图提供数据的可观察对象，所有对它的更新都需要在主线程（main thread）上进行。我把它称为 UI 模型，因为它可能不是你整个应用程序数据的完整模型。它可能只是你数据模型的一个投影或子集；只是当前需要在 UI 上显示的内容。最后，我们有可以看作是后端层的数据处理：这些处理可能发生在后台，用于填充你的模型或与 App 外部的世界通信。在我们的例子中，它由 `HealthKitController` 类型表示，负责管理与 `HealthKit` 的通信，以保存和加载用户的咖啡因摄入量。现在，在我们看代码之前，先讨论一下 App 中是如何管理并发的。这个架构看起来相当清晰，但是当我们再加上并发处理方式时，情况就变得混乱多了。这个 App 基本上被分成了三个可以执行代码的并发队列（concurrent queues）。UI 和模型上的工作在主队列（main queue）上完成。App 还有一个用于后台工作的派发队列（dispatch queue）。最后，某些完成处理程序（completion handler）的回调——比如那些从 `HealthKit` 返回结果的——是在任意队列（arbitrary queues）上执行的。这是一种相当常见的情况。看似简单的应用程序架构，实际上忽略了它在处理并发时隐藏的许多复杂性。现在，快速剧透一下。在采用 Swift 并发之后，我们将从这种临时的并发架构转变为类似于这样的架构。我们将把 UI 视图和模型放在所谓的主要 Actor（main actor）上。我们将创建新的 Actor（actor）在后台运行，这些类型将使用 async/await 特性在彼此之间传递线程安全的值。完成后，并发架构应该和类型架构一样清晰易描述。现在我们使用了一些你可能不熟悉的术语，比如 "async/await" 和 "Actor"，我们将在代码中使用它们时做简要解释。但关于这些特性的更深入解释，还有其他几个演讲提供了更多细节。好了，现在我们已经看到了整体架构，让我们深入代码。

这里是不同的文件。首先是几个 SwiftUI 视图。然后是手表复杂功能控制器的扩展委托。我们有表示咖啡因饮品的简单模型类型，以及一个持有这些饮品数组的 `CoffeeData` UI 模型。最后，我们还有 `HealthKitController`。我将从这个层面开始，将一些 Swift 的新并发特性引入我们的 App。`HealthKitController` 包含几个调用 `HealthKit` SDK 并接受完成处理程序的方法。让我们先看看这个控制器的保存操作。我按 Control-6，调出这个文件中的函数列表，然后我们找到保存操作。现在，在我们进入新并发特性之前，先来谈谈 Swift 目前的线程安全。这段代码访问了一些变量：`isAvailable` 和 `store`。看起来我们在这个函数中只是读取这些变量。这样安全吗？不，不安全，如果其他代码同时向它们写入的话。要判断这段代码是否线程安全，我需要的信息比只看这个函数要更多。它里面没有使用派发队列或锁，所以无论是什么让这段代码线程安全——假设它是安全的——那一定在别处。也许是调用方通过一个队列序列化了所有对 `save` 的调用。或者 App 的构建方式使得这样做没问题。但我不能仅通过看这个函数就知道这一点。能够做到——只看这个函数就知道某些事情，而不必去查看程序的其他部分——我们称之为局部推理（local reasoning），这是 Swift 的一个非常重要的目标。例如，Swift 强调值类型就是为了局部推理。与引用类型不同，你不用担心你收到的值类型会在程序的其他地方被改变。Swift 5.5 为并发引入的许多语言特性，都是为了让你有更多机会对你的代码进行局部推理。恰巧，这个函数完全是线程安全的，但这是我自己弄清楚的；编译器并没有帮助发现这些问题。所以在下面，我们对 `HealthKit` SDK 发起了一个调用，来将一个 `caffeineSample` 保存到用户的健康数据中。这个调用接受一个完成处理程序，该处理程序接受两个值：`success` 或 `error`。如果操作成功，没有错误；`error` 将为 `nil`。这意味着我们需要记得检查状态，然后在适当的时候解包下面的可选 `error`。这通常不是我们在 Swift 中处理错误的方式。这最好是一个在失败时可以抛出的方法。但那种方式不适用于完成处理程序。现在，有了 `async` 方法，我们可以有能够抛出的异步函数。

这个 `HealthKit` 的 `save` 方法现在有一个 `async` 等效方法正是这么做的，所以我们转而使用它。为此，首先我们移除完成处理程序，然后在方法调用前写上 "await"。

这提醒我们这是一个异步函数调用，代码将在这一点挂起（suspend），并允许其他代码运行。稍后我们再来讨论为什么这很重要。如果我们编译，现在我们已经做了这个改动，我们会看到编译器告诉我们还需要一个 "try"。这是异步函数的一大好处：它们可以抛出。不再需要记得检查一个可选的错误。

所以我们可以在方法调用前添加一个 "try"，并且我们要立即处理这个错误。所以我们将这个调用包裹在一个 `do` 代码块中……然后 `catch` 这个错误。我们可以移除这个 `guard`。现在我们在捕捉这个错误，它不再是可选的，所以我们可以移除解包操作。这也意味着我们可以重新组织代码，将成功路径放在顶部，这样我们可以把成功日志行移到紧挨着保存操作的下方，然后在 `catch` 块中处理错误日志。

注意 `save` 不再返回值。返回成功/失败实际上与错误是重复的，所以我们的新函数要么抛出，要么成功。

现在我们添加了 `try-catch`，编译器又报了一个错误。我们在调用一个异步函数，但是我们是从一个同步函数中调用的它。这是行不通的。异步函数拥有同步函数所没有的能力：在 `await` 时放弃对当前线程的控制。为此，它们有一种处理其栈帧（stack frame）的单独方式，这与同步函数不兼容。所以一个选择是将这个函数改为 `async`。我们只需在函数定义后添加 `async` 关键字。现在，这个文件可以编译了。

但是整个项目还不能编译。将 `makeSave` 函数改为 `async` 将问题推到了调用它的上一层。

在我的数据模型中，现在我得到了同样的编译器错误，因为这个函数不是 `async` 的。我本可以继续向上传递，但现在，让我们看看另一种保持改动局部化的技巧。为了调用我的 async 函数，我将生成一个新的异步任务（task），这个任务被允许调用 async 函数。这个异步任务与在全局派发队列上调用 `async` 非常相似。你不能从中向外部函数返回值，因为闭包是并发执行的。所以你在分离的闭包中做的一切都需要是自包含的。在这个例子中，我们只是调用 `save`，它不返回值，所以没问题。你还需要小心不要触及可能被其他线程同时修改的全局状态。这就是之前 `save` 完全线程安全之所以重要的原因，否则我们可能会通过添加这个新任务意外引入新的竞态条件（race condition）。

现在我们已经把它放在了异步任务内部，我们的 `await` 函数编译通过，我们完成了在这个 App 中 async/await 的第一次使用，我们现在就可以运行它。

让我们再做一次这样的重构，这次看看迁移到 async 时的一些其他技巧。让我们看看对访问用户健康数据的 `requestAuthorization` 的调用。它类似地调用带有完成处理程序的 `HealthKit`。但与之前不同，这个函数本身接受一个完成处理程序。我打算做的是创建这个函数的第二个版本，使其变为 async，同时保留接受完成处理程序的版本。这样我们代码中其他使用完成处理程序调用它的部分可以在我们重构时继续工作。我可以轻松地使用 "Create Async Alternative" 重构操作来完成。这可以在代码操作菜单中找到——我可以通过 Command-Shift-A 调出——然后选择添加 async 替代方法的选项。所以这会为原始调用添加一个 async 版本。

它会用创建新异步任务的代码替换原始的完成处理程序代码……

……然后 `await` 这个 `async` 版本。注意 async 重构为原始方法添加了一个已废弃警告。这些警告将引导我去寻找代码中接下来可以从重构成调用这个新的 async 版本中受益的部分。我们先撤销，回到原始的完成处理程序版本。在这个 `requestAuthorization` 回调内部，这个回调可能发生在任意线程上。所以你需要知道里面的代码是线程安全的。但我不认为它是线程安全的。这里的赋值可能与其他线程上读取这个值的代码同时发生。这是这段代码缺乏局部推理的另一个例子。在那个赋值之后，这个完成处理程序被调用，我完全不知道那个完成处理程序内部的代码是否线程安全。我必须查看这个函数的所有调用点，看看它们的完成处理程序是如何编写的，才能知道这是否没问题。现在，让我们重新做一遍，看看重构后的版本。请记住，异步任务也运行在任意线程上，类似于派发回调。所以这个转发版本与我们之前使用的完成处理程序版本有类似的问题。我们还没有使代码更安全。我们很快就会通过将 Actor 引入代码来解决这个问题。但现在，我们应该注意，仅仅因为我们将这个函数转换成了 async，并不意味着我们就不会有竞态条件了。事实上，你应该意识到，如果你只进行引入 async 函数的重构，就有可能在你的代码中引入新的竞态条件。现在让我们看看这个新的 async 函数。重构操作已经将这里使用完成处理程序的调用转换成了调用这个 SDK API 的新 async 版本。

但将这个函数转换为 async 突显了一些有趣的事情。这里，当我们使用完成处理程序技术时，我们有一个没有调用完成处理程序的 `return`。这可能是一个 bug。调用方会被晾在那里。但是对于 async 函数，你必须返回一个值，所以现在我们得到一个编译错误，我们可以通过返回 `false` 表示失败来解决。

就像之前一样，这个新的 `requestAuthorization` async 版本实际上并不返回一个值，它要么成功，要么抛出。所以我们只需删除这个返回值。而在失败路径上，我们需要返回 `false`。如果我尝试现在编译，项目能通过，因为别处的旧代码仍然可以继续调用完成处理程序版本，而我们在这样做时会看到这些已废弃警告，这可以引导我们到下一个可能需要重构的地方。好了，让我们再做一次 async 转换。找到从 HealthKit 加载数据的函数。和之前一样，我们从创建一个旧代码可以调用的桩（stub）开始。然后转向 async 版本，顺便提一下，这个函数接受一个可选的完成处理程序，对应的 async 方法是让这个函数有一个可丢弃的结果。接下来，我们开始向下移动，用 `return` 替换任何对完成处理程序的使用。例如，我们可以删除这个完成处理程序，直接返回 `false`。但是再往下移动一点，我们就遇到了一个障碍，这与 HealthKit 查询 API 的构造方式有关。这里有一个完成处理程序，但它是在这个 `query` 对象上的；而实际上，我想 `await` 的是在函数底部执行这个查询。顺便说一句，在函数中上下跳转是 async/await 擅长解决的另一个问题。所以我想要做的是创建一个单一的 async 函数，它既创建查询又执行查询。我们现在将使用一种叫做 continuation 的技术来做到这一点。所以我回到这个函数的顶部，创建一个名为 `queryHealthKit` 的辅助函数。我本可以把所有工作都放在现有函数内部，但这可能会变得有点乱，所以我喜欢把它单独放在一个辅助函数中。这个函数将是 async 的，所以我们可以 `await` 它，并且它会抛出，因为查询操作可能失败。这个函数将返回当前被传递给查询完成处理程序的有用值。所以我将执行查询的逻辑剪切下来，移到辅助函数中。我也会移动查询的执行。现在，我需要以某种方式反转这段代码，使其能够 `await` 完成处理程序，并将这些传入完成处理程序的值从我的新异步函数中返回。这就是我使用 continuation 的地方。所以在这个函数中，我们将返回尝试 `await` 调用 `withCheckedThrowingContinuation` 函数的结果。这个函数接受一个接受 continuation 的闭包。我们将移动这段代码到那个闭包内部，然后在闭包中，我们将使用 continuation 将数据传递回这个函数，要么通过使用 continuation 在此处恢复抛出错误……要么……恢复返回我们在完成处理程序中收到的值。

现在我们有了这个可 `await` 的函数，我们可以在原始代码中使用它。

所以我们从调用函数中赋值结果。我们需要处理可能抛出的错误。实际上，我打算向上到这里，取这部分日志记录，在处理程序中处理它。

然后我们只需将所有成功代码移到成功路径中。最后，我们需要处理这个闭包。

在这里，我们使用 `dispatch async` 回到主线程。但是我们已经丢弃了完成处理程序，所以没有办法使用它将此信息传回主线程。我们需要一种不同的方式。为了解决这个问题，我们将首次使用 Actor。在 Swift 的并发模型中，有一个全局 Actor 叫做主要 Actor（main actor），它协调其所有操作在主线程上进行。我们可以将对 `dispatch main.async` 的调用替换为对主要 Actor 的 `run` 函数的调用。这个函数接受一个要在主要 Actor 上运行的代码块。`run` 是一个 async 函数，所以我们需要 `await` 它。需要 `await` 是因为这个函数可能需要在主线程准备好处理此操作之前挂起。但由于我们 `await` 它，我们可以移除完成处理程序，转而返回一个值。好的，最后，编译器现在给我一个关于捕获变量的错误。

这是一个只在异步函数内部出现的新错误。因为 Swift 中的闭包通过引用捕获变量，当你捕获一个可变变量时——在这个例子中是我们的 `newDrinks` 数组——你就创造了共享可变状态的可能性，这可能是竞态条件的来源。所以，在做这件事时，你需要确保你制作了这个值的一个副本。一种方法是像这样将 `newDrinks` 添加到闭包的捕获列表（capture list）中。但通常更好的做法是首先不拥有可变变量来避免这个问题。在这里，我们可以通过修改上面的代码来实现。它之所以这样写，是因为 `samples` 是可选的。但我们可以做的是将 `newDrinks` 改为不可变值，并在 `if` 分支中设置其值，或者添加一个 `else` 将其设置为空数组。如果我们愿意，也可以使用 nil 合并运算符。由于这个值现在是用 `let` 而不是 `var` 声明的，它是不可变的，这就解决了这个问题，而不需要额外进行捕获。

现在让我们继续讨论主要 Actor，看一下这个需要在主线程上被调用的函数。

在这个函数的顶部，有一个非常好的做法：有一个断言（assert）来确保函数正确地运行在主线程上。如果你曾经犯过错误，在没有用 `dispatch async` 包装到主线程的情况下调用这个函数，你在调试构建中会得到一个错误，你应该在你的一些现有代码中绝对采纳这种做法。但是这种做法有些局限性。你可能忘记在每个需要的地方放置断言，并且你不能对存储属性的访问进行断言，或者至少需要大量的模板代码。如果编译器能为你强制执行其中一些规则，那就好多了，这样你根本不会犯这样的错误。这就是我们使用主要 Actor 的方式。我可以使用 `@MainActor` 注解函数。这将要求调用方在运行此函数之前切换到主要 Actor。

既然我已经这样做了，我可以移除断言，因为编译器不允许这个函数在主线程之外的任何地方被调用。我们可以通过回到调用方，并将这个调用移出 `MainActor.run` 块来证明这是有效的。你会看到编译器告诉我们，不，我们不能从这里调用它，因为我们不在主要 Actor 上。这里有一种思考这个特性的方式：它很像可选值。我们过去有过像指针这样的值，必须记得检查是否为 nil，但这很容易忘记，让编译器确保这个检查始终发生，再加上一些语言语法糖使它更容易，就好多了。在这里，我们做的是类似的事情，只不过它不是在强制执行 nil 检查，而是在强制执行你在哪个 Actor 上运行。

既然我们已经把这个函数放在了主要 Actor 上，严格来说就不再需要这个 `MainActor.run` 了。如果你在一个 Actor 外部，你总是可以通过 `await` 它们来在那个 Actor 上运行函数。事实上，编译器告诉我们的正是这一点。它说我们需要一个 `await` 关键字来切换到主要 Actor 以运行这个函数。所以如果我们添加它，那么即使这个调用不在 `run` 块内部，代码也能编译。在这里，我们在一个同步函数——`updateModel` 是同步的——上使用 `await`，但 `await` 表示我们所在的函数可能需要挂起以将自己置于主要 Actor 上。可以把这想象成类似于进行 `DispatchQueue.sync` 调用，只不过使用 `await`，你的函数会挂起而不是阻塞，然后在到主线程的调用完成后恢复执行。

所以，我们不再需要它了，但这种 `MainActor.run` 技术出于另一个原因仍然很重要。在每一个 `await` 点，你的函数可能会挂起，并且其他代码可能会运行。这就是 `await` 的意义所在：让其他代码运行而不是阻塞。在这种情况下，我们只有一个函数需要 `await`，所以这无关紧要，但有时你可能希望在主线程上进行多次调用。例如，如果你正在进行 UI 更新，比如更新表格视图（table view）中的条目，你可能不希望主运行循环在你执行的操作之间切换。在这种情况下，你会想要使用 `MainActor.run` 将多次对主要 Actor 的调用分组，以确保每次调用之间没有任何可能的挂起。

所以，我们现在使用主要 Actor 来保护需要在主线程上运行的代码。但是这个类中的其他代码呢？特别是那些修改局部变量的代码，比如我们之前看到赋值的查询锚点。

我们如何保证它们没有竞态条件？一种方法是将 `HealthKitController` 中的所有内容都放在主要 Actor 上。如果我转到 `HealthKitController` 定义，直接在类上写上 `@MainActor` 而不是在单个方法上，那将保护此类型上的所有方法，并且其上的所有存储属性将在主线程上进行协调。对于像这样一个简单的 App，这可能是一个可以接受的选择。但这似乎也有点不对。这个 `HealthKitController` 实际上是我们 App 的后端；把所有工作都放在主线程上似乎没有必要。我们希望把这个线程空出来做以 UI 为中心的活动。所以，我们可以将这个类本身改为一个 Actor。与全局 Actor 的主要 Actor 不同，这种 Actor 类型可以被多次实例化。在我的项目中，我仍然只会创建一个实例，但在很多其他 Actor 的使用场景中，你可能会实例化同一个 Actor 的多个副本。例如，你可以将聊天服务器中的每个房间设为其自己的 Actor。所以既然我们已经将这个类变成了 Actor，让我们看看编译器怎么说。好的。我们得到了一些编译错误。现在让我们暂停一下，讨论一下编译错误。这些错误会引导你找到在将代码迁移到新的并发模型时需要进行更新的地方。当你遇到这些错误时，请确保你理解它们在告诉你什么。当你不确定它如何或为什么能解决这个问题时，要抵制点击修正按钮的诱惑。需要注意的一点是避免陷入错误的级联。有时你会做一个更改——就像我们刚才做的将类转换为 Actor，或者将方法改为 async 一样——它会生成一些编译错误。然后你转到那些错误的地方，很容易做更多的更改来修复这些错误，比如将该方法设为 async 或将其放在主要 Actor 上。问题是这可能导致更多的错误，很快你就会感到不知所措。相反，使用我们在这个演示中使用的技巧，尝试将更改隔离起来，一步一步地完成，并在期间保持项目能够编译和运行。添加垫片（shim）来允许你的旧代码继续工作，即使你以后可能会删除它们。这样，你可以从一个点开始逐步迁移，一边整理代码。顺便提一下，我在这里所做的首先是转换 `HealthKitController` 的方法为 async，然后将其变为 Actor。我发现按这个顺序做最方便，而不是从 Actor 转换开始。好了，让我们跳转到这些错误看看，它们在我们放在主要 Actor 上的函数里。这说得通，因为在这个函数里，我们触及了我们的新 `HealthKitController` Actor 的一个存储属性——`model` 属性。Actor 保护其状态，不允许不在 Actor 上的函数——比如我们显式放在主要 Actor 上的这个函数——触及它的存储属性。查看这个函数，它看起来触及的 Actor 上唯一的状态就是 `model` 对象。其他所有内容都作为函数参数传入。对我来说，这提示这个函数应该属于模型；这里的 `model` 实际上应该是 `self`。所以让我们把它移到模型上。我们可以把这个函数剪切下来，转到我们的 `CoffeeData` UI 模型，然后粘贴进去。

它将是 `internal` 而非 `private`，以便可以从 `HealthKitController` 调用。我们只需要遍历并移除所有对 `model` 的引用，因为现在它就是 `self`。最后，我们需要转到它被调用的地方……并将这里的 `self` 替换为对 `model` 的调用。所以现在，这个 `HealthKitController` 文件编译通过了，我从其他文件中得到了一组新的错误。让我们看看这些错误。这里我们在调用那些我们之前创建的完成处理程序垫片，以便即使我们已经将这个函数重写为 async，也能继续传入完成处理程序。这些函数现在正受到 Actor 的保护，所以我不能直接调用它们。但是如果我们查看一下，它们并没有触及 Actor 状态的任何其他部分。它们所做的只是分离出一个任务，然后 `await` 对函数的 async 版本的调用。由于它们不触及 Actor 内部状态的任何部分，我可以将它们标记为所谓的 "nonisolated"。下面这个也一样。将某些内容标记为 `nonisolated` 告诉编译器你不会触及任何隔离状态，因此这个函数可以从任何地方调用。当我们 `await` 对函数的 async 版本的调用时，实际上是在自动切换到 Actor。注意，编译器会检查这个 `nonisolated` 声明是否成立。如果我想尝试访问 Actor 的某些状态——例如，打印出授权状态——编译器会阻止我。

所以，现在我完成了将 `HealthKitController` 转换为 Actor 的工作，它可以保护其内部状态免受竞态条件的影响。接下来，让我们沿着这些已废弃的线索找到下一个需要处理的文件，也就是我们的 `CoffeeData` 模型类型。这个类实现了 `ObservableObject`，并且有一个 `Published` 属性。任何对发布到 SwiftUI 视图的属性的更新都必须在主线程上完成，所以这个类可能是一个放在主要 Actor 上的好候选。

但是这里还有一个用于后台工作的 `DispatchQueue`。让我们看看它是如何使用的。

它只在两个函数中使用：`load` 和 `save`。这说得通；你可能不想在主线程上执行加载和保存操作。当你看到这样一种模式——使用一个队列来协调某些特定活动，但类的其余部分需要在主线程上——这表明你应该将那些后台代码分解到一个单独的 Actor 中。那么让我们开始做吧。让我们转到文件的顶部，创建一个新的私有 Actor……我们就叫它 `CoffeeDataStore`。让我们在另一个窗口中打开 `CoffeeData`，开始将代码转移到我们的新 Actor 中。我们可以给它自己的日志记录器。

让我们调整分类（category），这样我们就能知道这个 Actor 何时在使用。接下来，我们不再使用这个 `DispatchQueue`，而是实例化一个我们新 Actor 的副本。接下来，让我们转到保存操作，把它移过去。所以我们可以把这个函数……

……从这里剪切下来，移入 Actor。

让我们先编译一下，看看会出现什么问题。首先，这里有 `currentDrinks` 属性。在我们把这个方法从模型移出到它的 Actor 之前，这是模型类型的一个属性。那么我们现在如何访问它呢？Actor 传递信息的方式是在彼此之间传递值。所以我们应该让这个函数接受 `currentDrinks` 作为参数。`save` 的这个参数接收由模型类型传入的要保存的 `currentDrinks` 列表。这就解决了这个问题。

接下来是 `savedDrinks`。这是上次保存值的副本，以避免在没有任何变化时进行不必要的保存。这个值被 `save` 和 `load` 函数都修改过，所以它绝对需要由 Actor 保护。让我们在模型中找到它……然后移过去。

好的，接下来是什么？好吧，这个属性 `dataURL`，实际上只被 `load` 和 `save` 操作使用，所以我们可以直接把它移过去作为 Actor 上的一个私有辅助属性。

好的，最后一个要解决的问题。现在，这里我们遇到了错误，如果我们查看，似乎有一个闭包正在捕获 Actor 的某些状态，所以我们需要修复它。那么为什么这里会有一个闭包呢？如果你往下看，是因为同一段代码在两个地方被调用。结果编译器真的为我们标记了一些有趣的东西。这段代码的作用是检查手表扩展是否在后台运行。其想法是，如果它已经在后台运行，那么就不要进入后台队列；只需留在主线程上同步执行保存任务。但这看起来不对。你永远不应该阻塞主线程来执行像保存这样的 I/O 操作，即使你的 App 在后台运行。为什么 App 要这样做？我们可以追溯到保存操作被调用的地方。

它是在 `currentDrinks` 的 `didSet` 中被调用的。当属性被赋值时，这个 `didSet` 就会触发，保存新的值。现在，`didSet` 非常方便，但它们可能有点太诱人了。让我们看看 `currentDrinks` 属性的所有调用者。如果我们一路深入到这里……

……我们发现保存操作最终是同步的，因为它是以这种方式从调用 `WatchKit` 扩展的 `handle` 后台任务函数中调用的。这个 `handle` API 有一个约定。你应该完成所有工作，然后，当所有工作完成后，调用这个 `setTaskCompletedWithSnapshot` 方法。你必须保证调用这个时你的所有工作都已完成，因为你的手表 App 将被挂起。当你声明完成时，不能还有一些 I/O 操作（比如我们的保存操作）仍在运行。这是一个完美的例子，展示了异步性如何迫使你在整个代码中进行全局推理。让我们可视化一下这里发生的事情。我们从 `handle(backgroundTasks:)` 开始，它调用从 `HealthKit` 加载的函数。这个函数接受一个完成处理程序。然后我们切换到 `updateModel()`，它是同步执行的，因此同步地调用 `didSet`，而 `didSet` 又同步地保存。一旦完成，完成处理程序被调用，通知 `WatchKit` 一切都已完成。正是同步部分迫使我们在主线程上执行同步 I/O。我们如何修复这个问题？要用完成处理程序修复它，你必须更新当前每个同步方法，使其接受一个完成处理程序。但是你不能在 `didSet` 上这样做；它不接受参数，它只是在更新属性时自动触发。但好消息是，我们所有的 async 重构现在都将得到回报，因为将函数从同步更新为 async 要容易得多。所以首先，让我们转到已发布的属性 `currentDrinks`，将其改为 `private(set)`，这样我们就知道所有修改都只从这个文件发生。然后让我们把这个 `didSet` 操作，改为将其逻辑移动到一个新的函数……叫做 "drinksUpdated()"。我们将把它设为 async，因为它要调用我们的 Actor 上的保存操作。这需要对 `CoffeeDataStore` 进行一次 `await`……我们将把新的 `currentDrinks` 值传递给它。然后，我们需要转到更新 `currentDrinks` 的地方，并确保之后调用 `drinksUpdated`。在这个函数中，有一点需要注意。重要的是，这个操作——获取 `currentDrinks` 的副本，修改它，然后写回——必须是原子性的。这就是 `await` 关键字至关重要的原因；它表明在这一点上，这个操作可能会挂起，而其他函数——可能也会更新 `currentDrinks` 的函数——可能会运行。所以我们需要确保我们整个的修改和写回操作在任何 `await` 之前完成，否则，其他函数进来修改 `currentDrinks` 可能导致不一致的状态。

所以这个函数需要是 async 的。我们可以转到保存操作，消除这个不必要的后台和前台分支，每次都只在 Actor 上执行操作。

好的。最后，让我们看看加载操作。在这里，逻辑被分割成需要在后台运行的代码和需要在主线程上运行的代码。

所以让我们先取前半部分——后台部分——并将其移入 Actor。

这样做时，我们注意到了另一个可能的数据争用。

这里的 `savedValues` 是在主队列上被修改的，但如果你记得 `save` 操作，它是在后台队列中被读取和写入的。现在，事实上，鉴于 App 的构建方式，`load` 只会在启动时发生，所以这没问题。但同样，这是依赖全局推理，这种假设在将来做改动时可能会以微妙的方式失效。让 Actor 来确保程序始终正确要好得多。

所以我们现在就来修复它。首先，移除这个队列管理……

……重新缩进函数，移除另一个队列管理。就像 `save` 一样，我们需要一种方式来回传加载的值，我们只需从 Actor 上的这个 `load` 函数返回一个值即可。现在，让我们跳回原始的 `load`。

我们已经移除了这个逻辑，所以我们可以直接删除它……

并用一个对 `await` 的调用替换它……从 Actor 加载饮品。

现在，因为我们在 `await` 这个 Actor，这意味着这个函数需要是 async 的。我们在这里的同时，可以清理这些已废弃警告。最后，因为这个 `load` 现在是 async 的，我们需要在这里 `await` 它。而且因为我们在 `await` 它，我们需要创建一个任务。但此时，如果我们只是使用一个异步任务，我们可能会引入一个新的竞态条件。记住，在 Actor 外部，这个新任务只是在一个任意线程上运行。我们不应该从任意线程修改像 `currentDrinks` 这样的共享状态。

现在，解决这个问题的一种方法是将 `load` 函数放在主要 Actor 上，但更好的做法是将整个模型类型移动到主要 Actor 上。所以我们转到 `CoffeeData` 定义，将 `@MainActor` 添加到我们的模型类型。通过将模型放在主要 Actor 上，我们现在保证了对 `CoffeeData` 属性的所有访问都将在主线程上进行。这是好的，因为正如我们之前指出的，它是一个可观察对象，并且有一个已发布的属性。发布到 SwiftUI 的属性必须只更新在主线程上。这也意味着任何来自 Actor 的对 async 的调用也将在 Actor 上运行，所以我们可以移除其他任何 `@MainActor` 注解，比如我们之前添加的那个。所以现在你可能会注意到，当我们编译时，我们没有遇到任何编译错误，不像我们之前将其他东西移到 Actor 时那样。这是因为我们调用模型的地方是像 SwiftUI 视图这样的东西。

例如，让我们转到 `DrinkListView`。这个类型在屏幕上显示一个按钮列表。然后它调用 `addDrink`，这在我们模型类型上。但是这个 `DrinkListView` 本身也在主要 Actor 上。所以它的方法……

……可以调用 `CoffeeData` 模型而无需 `await`。是什么决定了这个 SwiftUI 视图在主要 Actor 上？嗯，这是从它使用 `EnvironmentObject` 推断出来的。任何访问共享状态（比如环境对象或可观察对象）的 SwiftUI 视图都将始终在主要 Actor 上。

在其他地方……

……我们还在从这个扩展委托调用中访问我们的模型。

由于这个扩展委托保证在主线程上被调用，`WatchKit` 已将其注解为在主要 Actor 上运行，所以它也可以直接调用我们的模型类型。

最后，既然我们已经到了这里，让我们重构这个方法，去掉这个已废弃的完成处理程序的使用。我们可以将这个部分包装在一个新的异步任务中。

记住，这个处理程序在主线程上运行，所以当我们创建一个任务时，该任务也将在主线程上运行。

在这个新任务内部，我们现在可以 `await`……我们调用从 `HealthKit` 加载新数据的方法。去掉完成处理程序的一个非常好的地方是，你现在可以组合函数。所以，如果你愿意，你可以直接将这个 `await` 移入 `if` 语句。

一旦这个函数调用返回，我们就知道所有工作都完成了，因为在它内部，我们将 `await` 保存操作。所以，我们现在可以自信地调用 `background.Task.setTaskCompleted`，因为我们知道完成了所有 I/O 操作。我们现在拥有了这种漂亮的、结构化的、自上而下的方法，在完成更多工作之前等待异步操作。顺便提一下，这种结构化的并发方法是 Swift 并发特性的另一个非常重要的部分。要了解更多，请观看相关的演讲，它涵盖了如何利用这个特性来构建更复杂的示例，比如在继续之前等待多个异步操作完成。

如果你在观看这个演讲时，想知道其中一些新特性究竟是如何工作的，请查看我们的底层技术揭秘演讲，它深入探讨了一些技术细节。那么让我们来总结一下。我们处理了一些代码，它们有合理的类型架构，但有复杂的并发架构，其中包含一些很难发现的隐藏竞态条件。借助新的并发特性，我们重新设计了架构，使得并发和类型架构很好地协调一致。并且编译器在这个过程中帮助我们发现了一些隐藏的潜在竞态条件。Swift 5.5 还有很多我们尚未涵盖的内容，比如带有任务组（task group）的结构化并发、异步序列（async sequences）以及 SDK 中一些很棒的新异步 API。在这个项目中还有一些我们没有做的重构，你可能想自己尝试一下。学习这些技术的最好方法是在你自己的 App 中尝试它们，所以尽情享受这些更清晰、更安全的编码方式吧。♪

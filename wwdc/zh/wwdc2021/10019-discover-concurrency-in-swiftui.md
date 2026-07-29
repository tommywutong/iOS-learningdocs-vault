---
title: 在 SwiftUI 中探索并发
session_id: 10019
collection: wwdc2021
year: 2021
duration: '22:54'
topics: [Swift, 'SwiftUI & UI Frameworks']
group: C · 并发、锁与线程
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2021/10019/'
content_hash: 'sha256:390e297f752e7bad'
translated: true
---

# 在 SwiftUI 中探索并发

<sub>WWDC2021 · 22:54 · Swift、SwiftUI & UI Frameworks</sub>

探索如何使用 Swift 的并发功能来构建更出色的 SwiftUI App。我们将向你展示并发工作流如何交互...

> [!note] 归档理由
> SwiftUI 并发早期版本

## 相关资源

- [AsyncImage](https://developer.apple.com/documentation/SwiftUI/AsyncImage)
- [HD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10019/6/97B7FCAB-AC78-4A0D-8F28-C5C7AE8C339C/downloads/wwdc2021-10019_hd.mp4?dl=1)
- [SD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10019/6/97B7FCAB-AC78-4A0D-8F28-C5C7AE8C339C/downloads/wwdc2021-10019_sd.mp4?dl=1)
- [效率在前：SwiftUI 中的后台任务](https://developer.apple.com/videos/play/wwdc2022/10142)
- [使用 Swift 并发消除数据争用](https://developer.apple.com/videos/play/wwdc2022/110351)
- [揭秘 SwiftUI](https://developer.apple.com/videos/play/wwdc2021/10022)
- [探索 Swift 中的结构化并发](https://developer.apple.com/videos/play/wwdc2021/10134)
- [认识 Swift 中的 async/await](https://developer.apple.com/videos/play/wwdc2021/10132)
- [认识面向 Swift 的 MusicKit](https://developer.apple.com/videos/play/wwdc2021/10294)
- [使用 Swift Actor 保护可变状态](https://developer.apple.com/videos/play/wwdc2021/10133)
- [SwiftUI 新变化](https://developer.apple.com/videos/play/wwdc2021/10018)
- [SwiftUI 中的数据基础](https://developer.apple.com/videos/play/wwdc2020/10040)
- [SpacePhoto](https://developer.apple.com/videos/play/wwdc2021/10019/?time=115)
- [Photos](https://developer.apple.com/videos/play/wwdc2021/10019/?time=159)
- [CatalogView](https://developer.apple.com/videos/play/wwdc2021/10019/?time=204)
- [让抓取发生](https://developer.apple.com/videos/play/wwdc2021/10019/?time=609)
- [CatalogView](https://developer.apple.com/videos/play/wwdc2021/10019/?time=847)
- [包含图片的 PhotoView](https://developer.apple.com/videos/play/wwdc2021/10019/?time=911)
- [SavePhotoButton](https://developer.apple.com/videos/play/wwdc2021/10019/?time=1086)
- [CatalogView](https://developer.apple.com/videos/play/wwdc2021/10019/?time=1228)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎来到“在 SwiftUI 中探索并发”。我是 Curt Clifton，SwiftUI 团队的一名工程师。稍后我的同事 Jessica 也会加入进来。Swift 5.5 引入了一系列用于管理 Swift 代码中并发的新工具。在这个演讲中，Jessica 和我会帮助大家理解这些改进如何与你的 SwiftUI App 交互。我将介绍这些新工具如何帮助你改进数据模型，并展示 SwiftUI 如何与新的主要 Actor 配合工作。然后，Jessica 将展示如何将你的并发数据模型连接到 SwiftUI 视图，并介绍一些利用 Swift 新并发工具的优秀新 API。

为了充分利用 Jessica 和我分享的信息，了解一些 Swift 新并发支持的相关背景知识非常重要。我们建议你在观看本视频的其余部分之前，先观看“认识 Swift 中的 async/await”和“探索 Swift 中的结构化并发”。小时候，我总是梦想成为一名宇航员。我有时确实在宇宙飞船上工作，但除此之外，那个童年的梦想并没有实现。不过，我对太空的热情从未消退。因此，我决定运用我作为 SwiftUI 工程师的实际技能，构建一个下载太空相关照片的 App。让我们来看看我规划的 App。

这个 App 显示一个随机太空照片列表。这些颜色真是美极了。当我看到一张非常喜欢的照片时，可以将其保存下来以便稍后查看。为了获取这些美丽的图片，我的 App 需要使用 REST API 与 Web 服务交互。这听起来正是 Swift 中引入的新并发功能的绝佳用例。让我们从数据模型开始。

我使用一个 `SpacePhoto` 结构体来保存单张图片的信息。这个结构体包含标题、照片描述、图片发布日期以及指向实际图片的 URL 等字段。我让我的类型遵循 `Codable` 协议，这样就可以轻松地从服务器响应中创建实例，或者将其保存到磁盘；同时遵循 `Identifiable` 协议，这样我就可以在 `ForEach` 和其他数据驱动的视图中使用它们。接下来，我想要显示这些条目的列表。为此，我需要一个能够获取并持有它们集合的模型。我使用 `Photos` 类来实现这一点。通过让 `Photos` 类遵循 `ObservableObject` 协议，我的 SwiftUI 视图会在数据更新时自动更新。我使用一个 `@Published` 属性来存储一个 `[SpacePhoto]` 数组。

为了从 REST 端点获取更新后的条目，我使用了一个 `updateItems` 方法。稍后我会更详细地介绍这个方法。但首先，我想先勾勒出基本用户界面。

这就是我想要构建的用户界面。目前，我只放置了标签视图和一个基本的 `PhotoView`。

我的 `PhotoView` 接受一个 `SpacePhoto` 并显示其标题。有了这些基础设置，我就能看到数据模型在运行时的效果了。接下来让我们看看 `Catalog` 视图。我的 `Catalog` 视图将显示照片列表。为此，我会添加一个 `@StateObject` 属性，并用我的 `Photos` 可观察对象来实例化它。在视图的 `body` 中，我会添加一个 `NavigationView`。在这里使用导航视图可以方便我稍后添加一个大标题。接着，在 `NavigationView` 内部，我会添加一个 `List`。在 `List` 内部，我会使用 `ForEach` 来遍历我的照片，并为每一张显示一个 `PhotoView`。

这样，我就能看到示例数据了。

目前做到这里就够了，不过让我们再加一点润色。

首先，这是之前提到的导航标题。现在，默认的内嵌列表样式看起来很棒，但为了充分展示我的太空照片，我想切换到朴素样式，这样照片就能在黑色背景下真正凸显出来。

我可以使用这里新的类似枚举的静态成员语法将列表样式设置为 `plain`。使用这种语法，SwiftUI 的样式修饰符写法更简洁，并且在 Xcode 13 中有更好的自动补全支持。最后，让我使用今年 SwiftUI 的另一个新功能：列表分隔符的控制。

在我的 `ForEach` 内部，我可以使用 `listRowSeparator` 修饰符来隐藏分隔符。

有时在用 SwiftUI 打磨用户界面时，我发现很难停下来。但 UI 的工作先做到这里。Jessica 计划在我完成数据模型后完成它。

不过，在深入研究数据模型之前，我想先谈谈 SwiftUI 如何与你的可观察对象交互，以及 Swift 5.5 新的并发功能如何让这种交互比以前更容易做到正确。在 2020 年 WWDC 的“SwiftUI 中的数据基础”演讲中，我的同事 Raj 谈到了 SwiftUI 的更新生命周期。我将驱动这个生命周期的代码称为“运行循环（run loop）”。在 Swift 5.5 中，运行循环在主要 Actor 上运行。有关 Actor 的更多细节，请观看“使用 Swift Actor 保护可变状态”这个演讲。在这个演讲中，我和 Jessica 将重点讨论主要 Actor。SwiftUI 的运行循环接收来自用户的事件，让你更新模型，然后将 SwiftUI 视图渲染到屏幕上。我喜欢把这些更新称为“运行循环的嘀嗒声”。让我们展开这个循环，以便连续查看多个嘀嗒。

在 SwiftUI 中，`ObservableObject` 可以通过一些有趣的方式与 SwiftUI 运行循环交互。让我们回到 `Photos` 这个 `ObservableObject`，看看 `updateItems` 方法。我将从我的 SwiftUI 视图中调用 `updateItems`，它会在主要 Actor 上运行。让我们用这个蓝色矩形来显示 `updateItems` 运行的时间。我想把注意力集中在这行代码上，在这里我将获取到的照片赋值给我的 `items` 属性。因为 `items` 是一个 `@Published` 属性，这个赋值会触发一个 `objectWillChange` 事件，紧接着将获取到的照片写入 `items` 的存储。当 SwiftUI 看到这个 `objectWillChange` 时，它会对我的 `items` 拍一张快照。在快照之后的下一个运行循环嘀嗒中，SwiftUI 会将快照与当前值进行比较。因为这些值不同，所以 SwiftUI 知道要更新依赖于 `Photos` 的视图。请注意，因为 `objectWillChange` 的触发、存储的更新以及运行循环的嘀嗒都发生在主要 Actor 上，所以它们的执行顺序是有保证的。在 2020 年的“数据基础”演讲中，Raj 描述了当视图在 `body` 中做了太多工作时可能导致的缓慢更新。

如果你的模型代码在主要 Actor 上做了太多工作，也可能导致更新缓慢。

例如，假设我的 `fetchPhotos` 函数在等待下载完成时阻塞，并且我连接的是慢速网络。因为我阻塞了主要 Actor，所以我错过了这一个运行循环的嘀嗒。这对我的用户来说就是可见的卡顿（hitch）。在过去，你可能会将工作派发到另一个队列，这样耗时的 `fetchPhotos` 就在主线程之外执行了。这看起来似乎没问题，但我遇到了一个棘手的难题。我在主要 Actor 之外更改了我的 `ObservableObject`。我的更改和运行循环的嘀嗒可能会交错进行。例如，当我赋值给 `items` 并且 SwiftUI 进行 `objectWillChange` 快照时，这有可能正好发生在运行循环嘀嗒之前。状态变化还未发生，所以 SwiftUI 将快照与未变化的值进行比较。而实际的状态变化发生在运行循环嘀嗒之后，但 SwiftUI 无法感知到这个变化，因此我的视图没有更新。为了正确更新，SwiftUI 需要这些事件按顺序发生：`objectWillChange` 触发、`ObservableObject` 的状态更新，然后运行循环到达下一个嘀嗒。如果我能确保这一切都发生在主要 Actor 上，我就能保证这个顺序。在 Swift 5.5 之前，我可能需要派发回主队列来更新状态，但现在简单多了。只需使用 `await`！通过使用 `await` 从主要 Actor 发起一个异步调用，我让异步工作发生时，主要 Actor 上可以继续其他工作。这被称为“让出（yielding）主要 Actor”。

在 `updateItems` 方法中，我可以在执行长时间运行的 I/O 操作时使用 `await` 将主要 Actor 让回给 SwiftUI，这样它就能保持运行循环的嘀嗒，避免任何 UI 卡顿。当异步工作完成时，Swift 会重新进入我在主要 Actor 上的 `updateItems` 方法，这样我就可以更新我的状态了。让我们看看这是如何工作的。

无需派发到另一个队列，我只需 `await` 长时间运行操作的结果。当我写下 `await` 时，`updateItems` 函数会交出主要 Actor 的控制权，这样运行循环就可以继续执行。当等待的抓取完成时，主要 Actor 会重新进入我的函数，这样我就可以安全地更新我的 `@Published` 属性，触发 `objectWillChange`，并将新值提供给 SwiftUI。

让我们跳转到 Xcode，看看我是否能让抓取发生。

这是我在幻灯片上展示的 `updateItems` 方法。为了实现 `fetchPhotos`，让我们先添加抓取单张照片的代码。我会让 `fetchPhoto` 方法接收来自 REST 端点的照片 URL，并返回一个 `SpacePhoto`。

接下来，我将使用 `URLSession` 上新的异步版本的 data 便捷方法来从 URL 抓取数据。为了先占位，我在这里使用了一个强制 try。稍后我会清理它。

啊，data 方法是异步的，所以我需要使用 `await`。

这意味着我需要让我的 `fetchPhoto` 方法也变成异步的。

好的，太好了。现在我有数据了，我会使用 `Decodable` 的初始化方法来实例化一个照片并返回它。接下来看一下 `fetchPhotos` 方法。我已经预先写了一些代码来获取随机选择的日期并在它们上面循环。我想构建一个数组，所以我把 `downloaded` 设为变量，并在循环中添加一个 date 变量。

在循环内部，我会调用一个已有的辅助方法来构建用于抓取特定日期的 REST 端点 URL。

然后，我会调用 `fetchPhoto` 方法并将结果追加到我的数组中。让我们构建一下。啊，因为 `fetchPhoto` 是异步的，所以我需要 `await` 结果。

这意味着 `fetchPhotos` 也需要是异步的。

为了简单起见，我是顺序调用这些 `fetchPhoto` 方法的。请查阅 Swift 5.5 的任务组（task groups）以了解更强大的选项。

现在，我只需要像幻灯片中展示的那样 `await fetchPhotos` 即可。

这样，我的更新逻辑就就位了。现在，也许你和我一样对这些强制 try 感到不安。让我们清理一下。目前，我会在下载失败时返回 `nil`。然后在 `fetchPhotos` 中，我只将非 `nil` 的值添加到数组中。

既然 `Photos` 使用了 `async-await`，只要它在主要 Actor 上运行，我就能确保它不会遇到我讨论过的那些棘手的 `objectWillChange` bug。但我如何确保这一点呢？幸运的是，Swift 编译器可以帮到我。通过给 `Photos` 添加新的 `@MainActor` 注解，编译器会保证 `Photos` 上的属性和方法只从主要 Actor 访问。做完这些，模型就就位了。接下来，Jessica 会将我们的视图连接到模型，并向你展示一些用于在你的 App 中利用并发的新 SwiftUI API。Jessica？谢谢你，Curt。让我们切换到 `CatalogView`，并使用 Curt 刚刚展示的 `updateItems` 方法。

我想在 `Catalog` 显示时调用 `updateItems`。在过去，你可能会使用 `onAppear` 来做这件事，但从今年开始，在 SwiftUI 中请使用 `task` 修饰符。`Task` 让你将一个异步任务与你的视图关联起来。这个任务在视图的生命周期开始时启动。`Task` 默认是异步的，所以在它的闭包内部，我可以调用 `myPhotos` 对象上的 `updateItems` 方法并 `await` 结果。

这是 `task` 的一个很好的用途，但这个新修饰符还有更多功能。任务的生存期与视图的生存期绑定，因此你可以做一些事情，比如等待一个异步序列并响应其值。而且当视图的生命周期结束时，任务会自动取消。有关视图生存期的更多信息，请务必观看“揭秘 SwiftUI”这个演讲。使用实时预览，我可以看到条目已经更新。但我们仍然缺少美丽的图片。我已经在更新 Curt 之前展示过的 `PhotoView` 了。我会在标题后面添加一些背景材质。现在，让我们添加图片。令人高兴的是，使用新的 `AsyncImage` API，从远程服务器加载图片比以往任何时候都更加容易。我需要做的就是从我们的条目中取出想要抓取的图片 URL，然后把它传给 `AsyncImage`。嗯，这个全尺寸的图片有点太大了，所以让我们使用 `AsyncImage` 的重载版本，让我可以调整图片并显示一个占位符，这样用户就知道图片正在加载中。接下来，我会让图片可调整大小，并将其宽高比设置为填充空间。最后，我添加一个最小宽度和高度，让我的图片更灵活。使用非零的最小高度还可以确保进度视图能在我的标题区域上方露出来。和 SwiftUI 的其他部分一样，`AsyncImage` 内置了智能的默认值，所以即使加载图片时出现错误，结果也将是继续显示占位符。你也可以选择自定义错误处理行为。要做到这一点，请查阅“使用 phase 参数的 `AsyncImage` 重载”。

如果用户能够收藏他们喜欢的图片以便稍后查看，那就更好了。让我们在标题区域添加一个按钮来实现这个功能。该按钮将触发一个异步操作，将图片条目保存到磁盘。已保存的条目会出现在我们 App 的“已保存”标签页中。我已经预先写了一个视图来实现这个功能。让我把它加到这里，然后我们可以看看它的代码。这是我预先写好的 Save 按钮版本。让我们添加一个保存照片的操作。SwiftUI 中的按钮操作是同步的，但我的 `save` 方法是异步的。为了调用这个方法，我会启动一个异步任务。

然后，在闭包内部，我会调用 `photo` 上的 `save` 方法。它是异步的，所以我只需使用 `await`。

我认为在保存过程中显示一个进度视图会很好。为此，我会添加一个 `@State` 属性。然后，我会在调用 `save` 的前后更新这个状态。接着，我会更新按钮上的标签，以便在保存发生时显示一个进度视图。我使用“opacity”来隐藏“Save”标签，并使用覆盖层来显示进度视图。这种组合确保了按钮保持相同的大小（基于“save”这个词的本地化版本）。最后，我会在保存过程中禁用按钮。

让我们看看这在实时预览中如何工作。

太棒了！让我们回到 `Catalog` 视图，把所有东西整合起来。

SwiftUI 今年有一个很棒的新修饰符，你可以用它来让用户能够手动刷新数据。通过向我的 `List` 添加 `refreshable` 修饰符，我告诉 SwiftUI 这个内容是可刷新的。我可以为 `refreshable` 提供一个异步闭包，并调用我们的 `updateItems` 方法来刷新列表。正如我之前在 `task` 中展示的那样，我会在这个异步方法上使用 `await`。

当我的异步工作完成时，刷新指示器会自动消失。现在，我可以下拉刷新图片，点击 Save 保存我喜欢的图片，然后切换到“已保存”标签页查看我保存的图片。

Swift 的新功能使得处理并发数据变得容易。SwiftUI 与 Swift 的并发功能很好地集成在一起，默认提供了最佳行为。在许多情况下，你只需要使用 `await` 来利用并发的力量。将你的 `ObservableObject` 标记为 `@MainActor`，以便对你的对象以与视图良好配合的方式进行更新做更健壮的检查。

利用 SwiftUI 新增的 API，用最少的精力编写安全且高效的并发 App。使用 `AsyncImage` 并发加载图片。在你的视图层级结构中添加 `refreshable` 修饰符，以允许用户手动刷新数据。就像我们在 Save 按钮中看到的那样，你可以在自己的自定义视图中使用 Swift 的新并发功能。

我们都知道，并发是比较棘手的。这是一个困难的问题，但有了这些新的语言特性和 SwiftUI API，你现在拥有了在你的 App 中管理这种复杂性的工具。我们希望你喜欢了解 Swift 5.5 和 SwiftUI 中出色的新并发工具，我们期待看到你们用它们来解决 App 中的棘手问题。[音乐]

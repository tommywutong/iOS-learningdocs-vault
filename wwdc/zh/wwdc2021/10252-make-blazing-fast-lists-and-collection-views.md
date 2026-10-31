---
title: 打造极速列表与集合视图
session_id: 10252
collection: wwdc2021
year: 2021
duration: '22:30'
topics: ['SwiftUI & UI Frameworks']
group: E · UIKit/SwiftUI 渲染与 UI 性能
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2021/10252/'
content_hash: 'sha256:b3e9991475b7c4a4'
translated: true
---

# 打造极速列表与集合视图

<sub>WWDC2021 · 22:30 · SwiftUI & UI Frameworks</sub>

构建始终平滑滚动的列表与集合视图：探索单元格的生命周期，并学习如何把这些知识应用到……

> [!note] 归档理由
> 列表/集合视图性能：预取、cell 复用、diffable

## 相关资源

- [Building high-performance lists and collection views](https://developer.apple.com/documentation/UIKit/building-high-performance-lists-and-collection-views)
- [UIKit](https://developer.apple.com/documentation/UIKit)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10252/5/B37B6913-C7C8-49EA-982E-9D10AC147454/downloads/wwdc2021-10252_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2021/10252/5/B37B6913-C7C8-49EA-982E-9D10AC147454/downloads/wwdc2021-10252_sd.mp4?dl=1)
- [What's new in UIKit](https://developer.apple.com/videos/play/wwdc2021/10059)
- [Advances in diffable data sources](https://developer.apple.com/videos/play/wwdc2020/10045)
- [Advances in UICollectionView](https://developer.apple.com/videos/play/wwdc2020/10097)
- [Explore UI animation hitches and the render loop](https://developer.apple.com/videos/play/tech-talks/10855)
- [Structuring data](https://developer.apple.com/videos/play/wwdc2021/10252/?time=85)
- [Setting up diffable data source](https://developer.apple.com/videos/play/wwdc2021/10252/?time=121)
- [Creating cell registrations](https://developer.apple.com/videos/play/wwdc2021/10252/?time=227)
- [Using cell registrations](https://developer.apple.com/videos/play/wwdc2021/10252/?time=243)
- [Existing cell registration](https://developer.apple.com/videos/play/wwdc2021/10252/?time=838)
- [Updating cells asynchronously (wrong)](https://developer.apple.com/videos/play/wwdc2021/10252/?time=857)
- [Reconfiguring items](https://developer.apple.com/videos/play/wwdc2021/10252/?time=915)
- [Updating cells asynchronously (correct)](https://developer.apple.com/videos/play/wwdc2021/10252/?time=923)
- [Data source prefetching](https://developer.apple.com/videos/play/wwdc2021/10252/?time=952)
- [Using prepareForDisplay](https://developer.apple.com/videos/play/wwdc2021/10252/?time=1123)
- [Asset downloading without image preparation](https://developer.apple.com/videos/play/wwdc2021/10252/?time=1191)
- [Asset downloading with image preparation](https://developer.apple.com/videos/play/wwdc2021/10252/?time=1198)
- [Using prepareThumbnail](https://developer.apple.com/videos/play/wwdc2021/10252/?time=1250)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ 大家好，我是 Aditya Krishnadevan，UIKit 团队的工程师。许多 App 的核心是列表或集合视图。拥有超级平滑的滚动是让这些 App 感觉很棒的重要部分。这段视频将帮助你在打造极速列表与集合视图时取得成功。我们将构建这个使用集合视图显示一些绝佳旅行目的地图片帖子的 App。乍看很简单，有一张目的地照片和几条文本标签。在整个视频中，我们将讨论它的搭建方式以及如何达到人们期望的性能。首先，我们将学习在使用 diffable data source 和 cell registration 等 API 时如何从坚实基础开始。我们将刷新对集合视图单元格生命周期的理解。然后讨论为什么你可能看不到完美平滑的滚动，以及可以帮助的预取新进展。最后 Patrick 将解释在内容异步到达时如何正确更新单元格，以及如何使用新的 UIImage API 在所有设备上获得绝对最佳的滚动性能。好吧，让我们先讨论 App 如何组织数据。示例 App 检索帖子列表以供显示，每个帖子由这个 DestinationPost 结构体表示。DestinationPost 遵循 identifiable，意味着它有存储其标识符的 ID 属性。这是每个 DestinationPost 的唯一标识符，即使其他属性改变也保持稳定。Diffable data source 被设计为存储你模型中项目的标识符，而非模型对象本身。因此在示例 App 中，diffable data source 使用这里的 ID 属性填充，而不是 DestinationPost 本身。这里是 App 中使用的 diffable data source。就像我们刚讨论的，它对 item identifiers 使用 DestinationPost.ID 类型。这里的 Section 是一个只有一个 case 的枚举，因为 App 只有一个 section。要填充……

集合视图查询单元格的首选布局属性并相应调整单元格大小。此时单元格已完全准备就绪，进入第二阶段：显示。委托上调用 willDisplayCell，单元格在 UICollectionView 内部变为可见。单元格现在在屏幕上。在可见期间其生命周期不会改变。当它滚动出屏幕时，对单元格调用 didEndDisplaying，它就回到复用池。从复用池中，单元格可以再次被 dequeue，重复这个过程。现在让我们看看这些基础就绪时 App 的感觉。App 展示秘鲁的库斯科和加勒比的圣卢西亚。滚动浏览 App 查看其他目的地，但注意它滚动并不平滑。

滚动期间的这些中断称为"卡顿（hitch）"。要理解什么导致卡顿，先了解 App 如何更新显示。每帧，触摸等事件被传递给 App。作为响应，它更新视图和图层的属性。例如，滚动视图的 contentOffset 在平移手势期间会改变，改变它包含的所有视图的屏幕位置。由于这些变化，App 的视图和图层执行布局。这个过程称为"commit"。然后图层树被发送到渲染服务器。每帧都有 commit 截止时间。这是该帧所有 commit 需要完成的时间。App 每帧可用于 commit 的时间取决于显示的刷新率。例如在以更高刷新率 120 Hz 运行的 iPad Pro 上，App 每帧完成工作的时间比以 60 Hz 运行的 iPhone 更少。这里是滚动集合或表格视图中单元格列表的典型例子。当新单元格变为可见时，有更长的 commit，期间新单元格被配置并执行布局。然后有几帧只是把现有单元格在屏幕上移动。这些帧的 commit 很快，因为不需要新单元格。最终滚动位置变化足够大，导致新单元格变为可见，这个模式重复。那么像前面演示那样导致卡顿的原因是什么？当某帧的 commit 耗时过长并错过截止时间，这些更新不会被纳入预期帧。显示保持前一帧在屏幕上，直到 commit 完成，这个延迟帧才能渲染。这是 commit 卡顿，感知为滚动时的瞬间中断。

要了解更多关于这个和其他类型卡顿的信息，请观看"探索 UI 动画卡顿与渲染循环"视频。为帮助避免这些卡顿，UICollectionView 和 UITableView 在 iOS 15 中都有全新的单元格预取机制。

我们回到昂贵单元格在滚动期间导致卡顿的示例。关键要点是你通常并不需要每帧一个单元格。我们有几帧 commit 很短，做最少的工作。iOS 15 的单元格预取利用这个空闲时间，在完成短 commit 后立即准备下一个单元格。

然后，当最终需要该单元格时，只需让它变为可见。这就是为什么预取单元格变为可见的帧的 commit 非常快，因为所有工作都已提前完成。预取单元格所花的时间与它导致卡顿时相同。但因为我们能抢跑，就能避免卡顿。让我们通过逐步检查每个 commit 来理解为什么这有效。在预取发生之前，我们执行了该帧的 commit。因为不需要单元格，是快速 commit，且在截止时间前还有大量时间。在 iOS 15 中，系统识别这种情况，利用空闲时间开始预取下一个单元格，而不是只是等到下一帧。现在，下一帧变得有趣。因为被预取的单元格是昂贵的，它实际上导致该帧的 commit 比正常更晚开始。然而即使该 commit 开始得晚，它仍然在截止时间前完成，因为它很快。与我们之前看到的没有预取的图示比较。注意不再有 commit 错过截止时间，因此单元格预取时不再有卡顿。这意味着你的 App 获得多达两倍的时间来准备每个单元格，而不会导致任何卡顿。更重要的是，获得这个出色的新增功能你只需用 iOS 15 SDK 构建 App。上一次运行演示时，App 是用 iOS 14 SDK 构建的。让我们看看用 iOS 15 SDK 构建的 App 滚动情况。

太棒了！预取正好按我们期望工作。滚动现在完全平滑，而且我们一行代码都没改。

记住，你只需用 iOS 15 SDK 构建 App。对于 UICollectionView，这个新预取扩展了 iOS 10 引入的功能。单元格预取现在支持列表以及所有其他组合式布局。这个出色的新预取现在甚至在 UITableView 中启用。预取可以通过消除卡顿改善滚动性能，还会降低功耗、延长电池寿命。如果你的单元格准备很快，系统可以用额外时间以更节能的状态运行并仍然避免卡顿。因此即使你没注意到任何卡顿，使你的单元格配置和布局实现尽可能高效仍然非常重要。现在讨论预取如何影响单元格生命周期。这是前面讨论的没有预取的生命周期，有两个不同阶段。当单元格被预取时，准备阶段在单元格需要在屏幕上之前执行。要充分利用预取，单元格必须在这个阶段被完全配置。不要等到单元格可见才执行重活。当单元格回到集合视图时，它被调整大小以获取首选布局属性，也作为预取的一部分。预取后，现在有这个中间状态，单元格等待被显示。鉴于这个新阶段，App 有两个重要考虑。准备好的单元格可能永远不被显示，这可能发生在用户突然改变滚动方向时。然后一旦单元格被显示，它可以在滚动出屏幕后直接回到等待状态。同一单元格可以为同一索引路径显示多次。单元格结束显示时不再立即加入复用池。预取帮助我们实现平滑滚动，但只是因为它给了我们更多时间。在其他更高帧率的设备上，仍然……

iOS 15 引入了 reconfigureItems 快照方法。在已准备的单元格上调用 reconfigureItems 会重新运行其 registration 的配置处理程序。用这个替代 reloadItems，因为它复用项目的现有单元格，而不是 dequeue 并配置新单元格。在示例 App 中，我们将声明 setPostNeedsUpdate 方法，对传入的 ID 调用 reconfigureItems。

现在回到 registration 的配置处理程序，当图像为占位符时，我们将下载全尺寸资源并调用新方法。reconfigureItems 随后会再次调用这个处理程序，但此时 fetchByID 返回全尺寸资源而非占位符。这让我们可以把所有视图更新代码放在一处，并在获得数据时异步更新单元格。为最大化准备时间，我们还可以在 prefetchingDataSource 中使用 downloadAsset 方法。数据源预取是启动集合视图项目网络下载的好地方。它给下载资源、在单元格可见前就绪更多时间，减少用户看到占位符内容的时间。

让我们看看这在 App 中的样子。看起来还行，但滚动时有可见卡顿。它们似乎也与新图像显示时重合。当新单元格被准备时，没有卡顿。只有当图像用全分辨率图像更新时才会卡顿。那是因为所有图像显示前都需要解码时间，有些图像（如更大的非占位符资源）太大，无法及时解码显示。当单元格 registration 的配置处理程序第一次被调用且资源为占位符时，代码开始异步请求全尺寸图像并完成配置。当资源最终在后面被下载时，单元格配置处理程序用最终图像重新运行。当图像视图尝试 commit 新图像时，它必须先在主线程准备图像显示。这可能耗时很久，当 App 错过 commit 截止时间时就会卡顿。图像准备是所有图像显示前必须经历的强制过程。

渲染服务器只能显示位图，也就是原始像素数据。图像有多种格式，如 PNG、HEIC 和 JPEG，它们被压缩，必须处理和解包才能显示。图像视图在 commit 新图像时做这个处理，发生在主线程。理想情况下，我们能提前准备图像，只在最终完成时更新 UI。这样我们永远不阻塞主线程，也不会卡顿。iOS 15 引入图像准备 API，让你控制图像准备在哪里、何时发生。这些 API 产生新的 UIImage，只包含渲染器需要的像素数据。一旦设到图像视图上，不需要额外工作。它有两种形式：同步的，可在任何线程运行；以及异步的，运行在内部 UIKit 串行队列上。

要使用它，我们取一个已创建的 UIImage 并在图像视图上设置占位符图像。然后调用新 API 在后台对更大的图像开始准备。完成时，我们只需把它设到图像视图上。准备好的图像解决了任何图像密集型 App 的大问题，但也带来一些考虑。准备好的图像包含原始图像的原始像素数据。只要它在内存中被保留，就可以在图像视图中自由显示。但这也意味着它占用大量内存，应谨慎缓存。最后，因为其格式，它们不适合磁盘存储。改为把原始资源保存到磁盘。最后一个考虑是图像准备如何利用预取。预取给图像下载和准备更多时间。给过程更多时间意味着用户不会长时间看到占位符，甚至可能根本看不到。在示例 App 中，我们已经有了异步的资源检索路径。下载完成后，我们可以在调用完成处理程序之前准备资源。这些资源很大，但也很有价值，因此一旦图像被准备，我们想缓存它。我们的图像缓存使用图像的大小来估算准备后图像的内存使用。现在，当单元格请求资源时，我们先检查缓存再从服务器获取。如果我们有更小的图像，就能缓存更多。图像可能很大，iOS 15 引入了类似的 API 来准备图像的缩略图。

这些可以缩放并把图像准备到更小的尺寸。它确保图像以目的地尺寸为考量被读取和处理，节省大量 CPU 时间和内存。

你像使用图像准备 API 一样使用它。首先取一个 UIImage 并在图像视图上设置占位符图像。然后用视图大小作为缩略图的目标大小调用新缩放 API。

准备完成后，只需用新缩略图更新图像视图。结合图像准备 API，iOS 15 让加速图像、避免任何 App 中的卡顿变得容易得多。处理图像时，聚焦于拥有异步 API，可在图像就绪时更新 UI。同时使用占位符图像，它小到或便宜到可以同步显示。结合预取和 reconfigureItems，在集合和列表视图中显示异步内容从未如此简单或高性能。

要开始使用快速集合与表格视图，首先用 iOS 15 SDK 构建 App 以解锁许多新优化。特别是确保用新的预取验证集合与表格视图的行为。这里演示的所有新 API 都可以在本讲的示例代码中找到。查看它并确保在整个 App 中采用图像准备和缩放 API。这将确保你的集合与表格视图极速运行。感谢观看。[欢快音乐]

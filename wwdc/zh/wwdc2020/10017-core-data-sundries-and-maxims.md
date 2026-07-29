---
title: 'Core Data：细节与格言'
session_id: 10017
collection: wwdc2020
year: 2020
duration: '17:27'
topics: [Developer Tools, 'SwiftUI & UI Frameworks', System Services]
group: H · 持久化与文件系统
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2020/10017/'
content_hash: 'sha256:e3e466547cda5d71'
translated: true
---

# Core Data：细节与格言

<sub>WWDC2020 · 17:27 · Developer Tools、SwiftUI & UI Frameworks、System Services</sub>

Core Data 是持久化存储你的 App 信息的主要方式——我们将向你展示如何优化这一点……

> [!note] 归档理由
> Core Data 细节与陷阱集合

## 相关资源

- [Loading and displaying a large data feed](https://developer.apple.com/documentation/SwiftUI/loading-and-displaying-a-large-data-feed)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10017/5/F2FB4653-3146-4087-A264-6EFCE0C197D5/wwdc2020_10017_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10017/5/F2FB4653-3146-4087-A264-6EFCE0C197D5/wwdc2020_10017_sd.mp4?dl=1)
- [Making Apps with Core Data](https://developer.apple.com/videos/play/wwdc2019/230)
- [Batch Operations - Enable Persistent History](https://developer.apple.com/videos/play/wwdc2020/10017/?time=108)
- [NSBatchInsertRequest.h](https://developer.apple.com/videos/play/wwdc2020/10017/?time=152)
- [Earthquakes Sample - Regular Save](https://developer.apple.com/videos/play/wwdc2020/10017/?time=181)
- [Earthquakes Sample - Batch Insert with Array of Dictionaries](https://developer.apple.com/videos/play/wwdc2020/10017/?time=196)
- [Earthquakes Sample - Batch Insert with a block](https://developer.apple.com/videos/play/wwdc2020/10017/?time=208)
- [NSBatchInsertRequest - UPSERT](https://developer.apple.com/videos/play/wwdc2020/10017/?time=342)
- [Batch Update Example](https://developer.apple.com/videos/play/wwdc2020/10017/?time=390)
- [Batch Delete without and with a Fetch Limit](https://developer.apple.com/videos/play/wwdc2020/10017/?time=453)
- [Fetch average magnitude of each place](https://developer.apple.com/videos/play/wwdc2020/10017/?time=738)
- [NSManagedObjectContext.h - Modernized Notifications](https://developer.apple.com/videos/play/wwdc2020/10017/?time=816)
- [NSManagedObjectContext.h - Modernized Keys](https://developer.apple.com/videos/play/wwdc2020/10017/?time=834)
- [Enable Remote Change Notifications with Persistent History](https://developer.apple.com/videos/play/wwdc2020/10017/?time=848)
- [History Pointers](https://developer.apple.com/videos/play/wwdc2020/10017/?time=979)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎来到 WWDC。

大家好。我是 Core Data 团队的 Rishi Verma。本场讲座我们将向你展示如何利用 Core Data 来最好地满足应用的需求。首先，我们将研究如何通过批量操作（batch operations）快速高效地填充和维护你的持久化存储（persistent store）。

然后我们将介绍如何定制获取请求（fetch request）以匹配应用的需求。

最后，分享一些关于应用如何响应持久化存储变化的技巧和窍门。

让我们先从我们的示例 Earthquakes 开始。它是一个 Swift 应用，拥有一个用于驱动 UI 的视图上下文（view context）和一个用于摄取美国地质调查局提供的数据的后台上下文（background context）。我们的示例为应用提供了一个本地容器（container），并收集来自 USGS JSON feed 的地震数据。

在这里，我们将 JSON feed 发送给 JSON 解析器，解析器再将数据发送到我们的后台上下文，将其转换为地震托管对象（managed object）并保存到本地存储。

然后，我们的视图上下文合并更改，神奇地更新了 UI。

现在，我们的后台上下文可能需要处理大量被创建或获取后，在保存后立即丢弃的托管对象。而这正是批量操作大显身手的地方。

批量操作允许开发者轻松地进行插入、更新和删除，同时尽可能保持最小化。由于其最小化的特性，存在一些注意事项。

不会发布保存通知，因为，显然我们没有在这里执行保存。

而且因为我们没有实例化托管对象，所以不会收到任何关于我们更改的回调或访问器逻辑。但是等等。你可以通过持久化历史记录（persistent history）来绕过这两个注意事项。

启用持久化历史记录，你的批量操作就会被捕获，以便轻松获取通知，这样我们就绕过了批量操作的第一个注意事项。至于回调和访问器逻辑，我们可以通过解析持久化历史记录中与应用当前视图相关的更改来适应。我们来深入了解一下批量操作？我们的应用通常做的第一件事是将数据加载到持久化存储中，进而驱动 UI。当我们引入 NSBatchInsertRequest 时，它为数据摄取提供了批量操作的能力。它简化了摄取大量数据的能力，现在我们扩展了 NSBatchInsertRequest 的能力。

最初，我们允许开发者传递一个字典（dictionary）数组进行批量插入。字典数组代表要创建的对象，键（key）作为特性（attribute）名称，对应的值作为其赋值。

我们还有一项新增内容：一个初始化方法，允许开发者提供一个 block 来填充给定的字典或托管对象。这大大降低了摄取的峰值内存（peak memory），同时进一步减少了对象分配的数量。

我们来看一个例子？在这段代码片段中，我们正在为地震创建托管对象……

并用 USGS 提供的地震数据值填充它们。

然后我们保存。让我们看看如果采用 NSBatchInsertRequest，这段代码会是什么样子。

首先，我们收集所有地震数据的字典并将其添加到我们的数组中。

我们创建一个批量插入请求并执行。

很简单。现在让我们看看批量插入请求的这种 block 变体。我们使用一个 block 创建批量插入请求，该 block 将值赋给给定的字典。

然后我们执行请求，这个 block 会被重复调用，直到它返回"true"作为停止并保存的指示。但这三种不同方式的性能如何呢？让我们看看当我们摄取大量地震数据时，应用的性能表现。当我们使用托管对象保存上下文时，我们看到耗时超过一分钟，空闲内存大约为 30 兆。

初始峰值是 JSON 数据，而第一分钟的大部分时间实际上并不是摄取，而是合并更改通知，因为我们执行了大量的事务。但批量插入没有这个问题。当我们使用字典数组的 NSBatchInsert 时，我们在空闲内存 25 兆的情况下完成了相同的操作，并且能够在仅 13 秒内保存相同数量的对象，只是传统保存所需时间的一小部分。

但我们还能做得更好。让我们使用新的 block 摄取方式，我们能在 11 秒内摄取所有对象。现在我们已经优化了数据填充，让我们来了解一个关于批量插入的巧妙技巧。这里，我们有来自 Earthquakes 示例的托管对象模型，并且我选择了 quake 实体（entity）。右侧是 quake 实体的数据模型检查器。让我们仔细看看。我们可以看到特性"code"是一个唯一约束。这意味着在持久化存储中，只有一个对象可以拥有"code"的特定值。其他地震不能有相同的"code"值。这对 Earthquakes 示例有何影响？嗯，我们的 JSON feed 提供了过去 30 天的所有地震数据，每次用户点击重新加载按钮，我们都会摄取 JSON feed 中的所有数据，这些数据除了最近发生的几次地震和过去地震的更新数据外，大多是相同的数据。这里我们有一个 code 为 42 的地震从我们的 JSON feed 进入解析器。

然后它被传递到我们的后台上下文，后台上下文将地震 42 保存到存储中。

第一次摄取时，我们在存储中创建了一个新行。但是，在后续尝试插入相同地震时，我们不想删除旧地震并插入新地震。我们更希望更新任何已更改的数据，在 SQL 中这被称为 UPSERT。

如果你同时看到 SQL 语句，UPSERT 这个 SQL 术语会更容易理解。所以，这里是我们插入地震对象的操作，在插入时，如果在 code 上发生冲突，则更新这些属性而不是插入。如何获得这种行为？只需在上下文中设置 mergePolicy，将执行批量插入请求的策略设置为 NSMergeByPropertyObjectTrumpMergePolicy。

但是有一种更简单的方法来执行更新，没有比批量更新更简单的了。

使用 NSBatchUpdateRequest，无需先执行获取请求来更新托管对象再保存。NSBatchUpdateRequest 可以快速高效地更新那些满足获取请求中定义的搜索条件的对象的属性。

让我们看一个快速的例子。

使用我们的 Earthquakes 示例 App，如果我们能够通过另一个来源确认所有地震，我们就可以将它们标记为已验证。那么，假设我们的来源只验证震级大于 2.5 的地震。

我们可以为此构建一个批量更新。这段代码为"Quake"创建了一个批量更新请求，然后设置 propertiesToUpdate："validated"等于"true"，并设置我们的谓词（predicate），震级大于 2.5。

然后我们执行批量更新，就完成了。就是这么简单。我们已经介绍了插入和更新。接下来让我们做批量删除。

批量删除非常强大，可以轻松删除对象图中的大部分内容。关系规则会被遵守，因此删除会级联（cascade），关系会被置空（nullify）。我们看到的常见用例是来自过期代码，该代码确定对象的生存时间（time to live），并清理那些已达到过期时间的对象。

这是此 API 的一个很好的用途。然而，看似简单的操作可能会产生复杂的后果。来个例子怎么样？这里，我们有一个示例，其中地震数据在 30 天后过期。

由于这是一个清理任务，我们使用后台优先级异步调度它。我们的 block 在托管对象上下文上启动，并确定过期日期。然后我们构建获取请求并设置过期谓词……

使用新的获取请求创建一个批量删除请求，并执行。

嗯。但是，如果有大量对象与我们的批量删除搜索条件匹配呢？该请求将对我们的存储获取写入锁（write lock），呃，可能会占用一段不确定的时间。

但是等等。我们可以解决这个问题。

让我们设置一个获取限制（fetch limit）。这样我们的任务就不会无限制地执行，从而为我们的用户避免了很多挫败感。

现在我们已经避免了这种陷阱，让我们看看如何改进数据获取的方式。现在我们有了这个丰富的对象图，我们需要调查并显示我们存储中的内容。获取数据时，我们得到的数据可以驱动许多视图和计算。但我们总是需要那么多数据吗？我们又如何在不需要整个对象图的情况下执行这些复杂的计算呢？首先，managedObjectResultType 提供了最充分遍历对象图的最简单方法。

当我们将结果用于批量获取结果控制器（fetchResultsController）时，这非常有用。随着我们的托管对象被更新，fetchResultsController 会神奇地做出响应并应用差异。让我们看看实际效果。这是没有数据的 Earthquakes 示例，然后我们进行获取。

当对象被获取时，我们的 fetchResultsController 正在添加行。

当我们更新这些对象时，我们的视图也会更新。但如果你注意到，我们的视图只显示了大约 15 个地震。我们获取的数量远不止这些。我们还有一些改进空间。通过在获取请求上设置 batch size，结果中将只有第一批指定数量的对象被完全填充数据。当用户滚动时，剩余的对象将被填充，但只填充到用户需要的程度。

批量数组是特殊的，其行为与传统数组不同。让我展示给你看。

这里，我们有一个常规的结果数组。我们所有的托管对象都已填充，当我们遍历它们时，一切都符合预期。

现在我们有一个批量数组。注意，我们没有托管对象，而是有 ObjectID，它们会在遍历数组时变成托管对象。当我继续遍历时，批次被释放，只有 ObjectID 保留在结果中。

让我们看看实际效果。这是 Earthquakes 示例在获取数据，它显示空闲内存大约为 17 兆。

那么，如果我们开启批量获取（batch fetch）呢？当我们设置 batch size 时，我们只用了大约 12 兆的内存来完成相同的任务，我们节省了近 5 兆，几乎是我们应用内存使用的三分之一。

我们还能如何改进获取呢？我们可以缩减获取操作获取的数据量。如果我们知道结果将需要某些特性或关系，我们可以根据这些需求定制获取。

对于将要访问的已知特性，我们可以设置 propertiesToFetch。当我们使用托管对象时，默认行为是将关系设置为"false"，并且首次遍历关系将触发相关对象的获取。如果遍历的关系很少，或者根本没有遍历，这很好。但是，如果已知某个关系极有可能被遍历，我们建议预取（prefetch）该键路径（key path），从而避免稍后获取数据，因为每次遍历时都会加载惰值（faults），效率低下。

这是我们的基准获取，空闲内存为 17.6 兆。

但是，如果我们只将 propertiesToFetch 设置为 UI 中可见的那些特性，我们可以将空闲内存减少到 16.4 兆。

现在让我们谈谈 ObjectID。

托管对象很大且数据丰富，但这些不适合在线程（thread）之间传递，因此 ObjectIDResultType 就派上了用场。当我们想要完成工作并识别满足特定条件的对象时，这些简单的标识符可以传递给其他线程进行进一步处理，避免了在处理线程上的查找开销。但是，如果我们需要介于完整托管对象和 ObjectID 之间的东西呢？比如字典结果，它们非常方便，因为它们提供了轻量级、只读的数据集，可以传递给其他线程。

字典结果也可以定制以执行复杂的数据聚合，这有助于减少通常需要拉取相关对象图才能完成的大量计算……

例如对实体及其属性使用 groupBy 与聚合函数。让我们看一个例子。

按地点分组的平均震级。首先，我们确定震级的键路径表达式，然后确定用于获取平均值的函数表达式。

然后我们创建一个平均震级的表达式描述。

最后，我们为地震设置获取请求，包含 properties to fetch、我们的表达式描述和地点，按地点分组，并将结果类型设置为"dictionary"。这导致了这些结果，向我们显示了指定地点地震的平均震级。

我们要介绍的最后一个结果类型是 countResultType。它简单、优雅且经过优化。

还需要我多说吗？我们已经优化了摄取和获取。现在让我们看看如何改进应用对持久化存储中变化的响应。Core Data 提供了丰富的通知，让你了解何时添加或删除了存储，或者何时保存或更改了对象。但我们想重点关注两个特别有用的通知。今年，我们引入了 ObjectID 通知，除了传统的保存通知之外，它们也可用。ObjectID 通知是你已经熟悉的托管对象保存通知的轻量级对应物，这个便捷的通知来自持久化历史记录事务。让我们看看 Swift 中的这些新增内容。托管对象上下文现在具有针对 Swift 改良的通知。我们更新了一些原有的好东西，使其在 Swift 中更友好，并添加了这两个新通知，允许你使用 ObjectID 而不是托管对象来驱动应用。但这还不是我们改良的全部。作为我们改良工作的一部分，我们还添加了通知键，使得在 Swift 中处理通知更加容易。

我们还为 ObjectID 通知添加了一些新的键。我们要讨论的另一个通知是远程更改通知（remote change notification）。

远程更改通知信息量很大，因为它们是为所有 Core Data 客户端在进程内和进程外完成的所有操作发布的。

这允许你的应用避免轮询更改，并能够使用通知驱动相同的逻辑。

当持久化历史记录启用时，远程更改通知的 userInfo 包含一个持久化历史记录 token，可用于获取 ObjectID 通知。让我们看看实际效果。

这里我们有我们的容器和应用，以及一个显示到目前为止已捕获的持久化历史记录的表。

来自 USGS 的 JSON feed 上线，后台上下文将 JSON 数据摄取到持久化存储中。

持久化历史记录以非常详细的方式捕获了操作，比我们这里能展示的要多得多。

不过，以前我们的应用需要轮询存储以获取新更改。但有了远程更改通知就不用了。相反，我们会收到更改已发生的通知，并且远程更改通知的 userInfo 负载（payload）包含一个历史记录 token，因此我可以在持久化历史记录中看到确切的操作。让我们看看随着应用的演变，这是如何工作的。

我们的应用有一些新增内容：一个共享扩展（share extension）、第二个利用相同数据的应用，以及一个方便的 Photos 扩展。当这些新增内容之一对持久化存储进行更改时，该操作会记录在持久化历史记录中。

然而，当一个应用进入前台时，它需要轮询历史记录，这非常昂贵。

但是，如果我们启用了远程更改通知，当我们的应用被带到前台时，我们会收到通知……

以及随后由我们的 Photos 扩展所做的更改……

还有我们的第二个应用……

以及我们的共享扩展。

当我们的应用重新启动时，它会收到通知，并且可以轻松地查看持久化历史记录中发生了哪些更改。

这两个特性使得了解持久化存储的谁、什么、何时、何地以及如何更改变得非常容易。最后，一个关于持久化历史记录的快速提示。

一个关于持久化历史记录的非常方便的技巧与我们之前告诉你的关于获取请求的技巧相同。确保根据应用的需求定制请求。

这里，我们有一个如何定制更改请求的示例，以便我们可以查找在给定日期之后对特定 ObjectID 所做的所有更改。

首先，我们从获取持久化历史记录更改对象的实体描述开始……

这样我们就可以用它来构建我们的获取请求并设置实体。

然后我们在这里设置谓词，查找对特定 ObjectID 的更改，然后我们创建历史记录请求，并设置获取请求。

瞧，执行。我们的结果将只是给定 ObjectID 在指定日期之后发生的那些更改。这就是本场讲座的全部内容。快速回顾：尽可能使用批量操作，根据预期用途定制获取，并利用通知和持久化历史记录的力量。感谢大家，也感谢 Core Data 团队。很荣幸。

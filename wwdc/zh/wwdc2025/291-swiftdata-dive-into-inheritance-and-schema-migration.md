---
title: 'SwiftData：深入了解继承与 Schema 迁移'
session_id: 291
collection: wwdc2025
year: 2025
duration: '19:08'
topics: [App Services, Swift]
group: H · 持久化与文件系统
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2025/291/'
content_hash: 'sha256:5494421373d2ad51'
translated: true
---

# SwiftData：深入了解继承与 Schema 迁移

<sub>WWDC2025 · 19:08 · App Services、Swift</sub>

探索如何使用类继承来对数据进行建模。学习如何优化查询，以及如何无缝迁移 App 的数据，以便使用...

> [!note] 归档理由
> 继承与 schema 迁移

## 章节

- [简介](/videos/play/wwdc2025/291/?time=0)
- [利用类继承](/videos/play/wwdc2025/291/?time=131)
- [通过迁移演进数据](/videos/play/wwdc2025/291/?time=459)
- [定制获取到的数据](/videos/play/wwdc2025/291/?time=687)
- [观察数据的变更](/videos/play/wwdc2025/291/?time=834)
- [后续步骤](/videos/play/wwdc2025/291/?time=1108)

## 相关资源

- [简介](https://developer.apple.com/videos/play/wwdc2025/291/?time=0)
- [利用类继承](https://developer.apple.com/videos/play/wwdc2025/291/?time=131)
- [通过迁移演进数据](https://developer.apple.com/videos/play/wwdc2025/291/?time=459)
- [定制获取到的数据](https://developer.apple.com/videos/play/wwdc2025/291/?time=687)
- [观察数据的变更](https://developer.apple.com/videos/play/wwdc2025/291/?time=834)
- [后续步骤](https://developer.apple.com/videos/play/wwdc2025/291/?time=1108)
- [构建丰富的 SwiftUI 文本体验](https://developer.apple.com/documentation/SwiftUI/building-rich-swiftui-text-experiences)
- [SwiftData](https://developer.apple.com/documentation/SwiftData)
- [为 Core Data App 采用 SwiftData](https://developer.apple.com/documentation/CoreData/adopting-swiftdata-for-a-core-data-app)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2025/291/4/446be11b-b8d3-42dd-b981-a22010ddbbe9/downloads/wwdc2025-291_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2025/291/4/446be11b-b8d3-42dd-b981-a22010ddbbe9/downloads/wwdc2025-291_sd.mp4?dl=1)
- [SwiftUI 新功能](https://developer.apple.com/videos/play/wwdc2025/256)
- [通过 SwiftData 历史记录追踪模型变更](https://developer.apple.com/videos/play/wwdc2024/10075)
- [导入 SwiftData 并添加 @Model](https://developer.apple.com/videos/play/wwdc2025/291/?time=67)
- [添加 modelContainer 修饰器](https://developer.apple.com/videos/play/wwdc2025/291/?time=78)
- [采用 @Query](https://developer.apple.com/videos/play/wwdc2025/291/?time=90)
- [为 Trip 添加子类](https://developer.apple.com/videos/play/wwdc2025/291/?time=208)
- [更新 modelContainer 修饰器](https://developer.apple.com/videos/play/wwdc2025/291/?time=243)
- [添加分段控件来驱动谓词以按类型过滤](https://developer.apple.com/videos/play/wwdc2025/291/?time=426)
- [SampleTrips 版本化 Schema 2.0](https://developer.apple.com/videos/play/wwdc2025/291/?time=506)
- [SampleTrips 从版本 1.0 到 2.0 的自定义迁移阶段](https://developer.apple.com/videos/play/wwdc2025/291/?time=521)
- [SampleTrips 版本化 Schema 3.0](https://developer.apple.com/videos/play/wwdc2025/291/?time=549)
- [SampleTrips 从版本 2.0 到 3.0 的自定义迁移阶段](https://developer.apple.com/videos/play/wwdc2025/291/?time=573)
- [SampleTrips 版本化 Schema 4.0](https://developer.apple.com/videos/play/wwdc2025/291/?time=590)
- [SampleTrips 从版本 3.0 到 4.0 的轻量级迁移阶段](https://developer.apple.com/videos/play/wwdc2025/291/?time=603)
- [SampleTrips Schema 迁移计划](https://developer.apple.com/videos/play/wwdc2025/291/?time=624)
- [将 Schema 迁移计划与 ModelContainer 配合使用](https://developer.apple.com/videos/play/wwdc2025/291/?time=651)
- [为 Query 添加搜索谓词](https://developer.apple.com/videos/play/wwdc2025/291/?time=708)
- [在自定义迁移阶段定制 SwiftData 获取](https://developer.apple.com/videos/play/wwdc2025/291/?time=751)
- [在自定义迁移阶段添加 relationshipsToPrefetch](https://developer.apple.com/videos/play/wwdc2025/291/?time=791)
- [更新小组件以利用 fetchLimit](https://developer.apple.com/videos/play/wwdc2025/291/?time=808)
- [高效获取最后一笔事务](https://developer.apple.com/videos/play/wwdc2025/291/?time=984)
- [在给定 token 之后获取历史记录，并仅针对关注的实体](https://developer.apple.com/videos/play/wwdc2025/291/?time=1049)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，我是 Rishi Verma，我是 SwiftData 团队的一名工程师。欢迎观看“SwiftData：深入了解继承与 Schema 迁移”。SwiftData 在 iOS 17 中引入，它让你能够使用 Swift 在 Apple 的所有平台上对 App 的数据进行建模和持久化。它通过利用现代 Swift 语言特性，让你编写出快速、高效且安全的代码。

本视频将继续这一主题，介绍如何利用类继承，以及何时选择继承是正确的做法。随着继承的采用和 Schema 的演进，我们将讨论用于保留数据的迁移策略，之后我们将探索几种定制 SwiftData 获取和查询以实现最佳性能的方法。最后，还会介绍如何观察本地和远程对模型所做的更改。在过去几个版本中，我们一直在使用一个熟悉的 App——SampleTrips。这是一个用 SwiftUI 编写的 App，用于跟踪我计划的所有不同行程。

要在该 App 中将 SwiftData 与模型一起使用，我只需导入框架并使用 Model 宏装饰每个模型。

在 App 的定义中，我们在 WindowGroup 上添加 modelContainer 修饰器，使整个视图层级结构知晓模型 Trip。

连接好 modelContainer 后，我现在可以更新我的视图以利用 Query 宏。让我们移除这些静态数据，而是使用 Query 宏来填充视图，该宏将生成从模型容器中获取行程的代码。

就是这样。该 App 现在可以持久化我创建的所有行程，并且完美地适配我的 SwiftUI 视图。

SwiftData 不仅轻松提供了持久化功能，还提供了 Schema 的建模和迁移、图管理、与 CloudKit 同步等功能。SwiftData 的最新新功能是类继承。iOS 26 中新增了构建利用继承的模型图的能力。

类继承是一个强大的工具。让我们了解它何时是适合这项工作的工具。

当你的模型自然形成层次结构并共享特性时，继承非常适用。Trip 模型具有 destination、startDate 和 endDate 属性，这些是每次旅行都需要知道的属性，以便我们了解何时何地去。

因此，Trip 的任何新子类都已经拥有这些属性以及 Trip 中定义的任何其他共享行为。

Trip 模型也是一个广泛的领域。我们生活中旅行的类型有很多。Trip 的新子类应该是 Trip 这个更广泛领域内的一个自然子领域。

在我们的 SampleTrips App 中，许多行程分为两个自然的子领域：个人旅行和商务旅行。有了这两个表达旅行自然子领域的新模型，我想添加特定于这些子类的属性和行为。

对于个人旅行，我将添加一个枚举来捕捉我进行该特定旅行的原因。对于我的商务旅行，我想添加一个属性来记录我的每日津贴，这样我就知道下一次出差应该花多少钱。让我们在 SampleTrips App 中实现这一点，并创建更丰富的体验。

这是我们想要与子类共享属性的 Trip 类。让我们为 Trips App 添加两个新的子类，一个用于我的商务旅行，一个用于我的个人旅行。我还需要用 `@available(iOS 26, *)` 修饰它们，以便与 SwiftData 的继承支持保持一致。现在让我们将子领域特定的属性添加到我们的子类中。我可以为 BusinessTrip 添加一个 perdiem 并设置初始值。对于我们的 PersonalTrip，我们添加一个 Reason 枚举来捕获我们进行个人旅行的原因。

等等，我们还有最后一件事要做，那就是更新我们的 schema 以包含新的子类。让我们将 BusinessTrip 和 PersonalTrip 添加到 modelContainer 修饰器中，然后就可以开始了。

SampleTrips App 现在可以利用新的个人旅行（蓝色）和商务旅行（绿色）了，无需其他特殊代码。

虽然类继承是一个强大的工具，但它并不适用于所有问题。让我们讨论一下何时应该使用继承。

有一些场景下继承是正确的选择。如果你的模型自然表达了层次关系，并且具有你想扩展的共同特征，那么继承可能是正确的选择，因为你的类型形成了“is-a”关系。

当我们使用继承的模型时，我们知道一个个人行程是一种 Trip（IS-A Trip），这意味着每当我处理 Trip 类型（例如在视图中的 Query 中获取行程）时，我可以找到所有类型的行程，包括个人旅行和商务旅行，以及父类 Trip 的实例。在这里，我们看到我们的行程被表示为与我们 UI 颜色相同的飞机，从模型容器飞向支持查询的模型上下文。

然而，继承不应用于仅仅为了共享模型之间的共同特征。例如，如果我们对所有具有 name 属性的模型进行子类化，我们的类层次结构将包含许多仅共享一个用于共同目的的属性的子领域，而所有其他特征都孤立在它们各自的子领域中。

而且由于这些子领域不形成自然层次结构，它们更适合表示为协议一致性（protocol conformance）。

协议一致性允许不同的领域共享行为，但不共享其他不相关的特征。使用继承的另一个原因取决于你如何查询或获取模型。

有几种查询数据的方法，我们目前使用 Query 宏从模型容器中获取所有行程以驱动我们的视图。这是一个深度搜索（deep search）的示例。

如果我们只使用深度搜索，这意味着我们总是获取所有行程并且只使用 Trip 类型，那么我们应该考虑将 PersonalTrip 或 BusinessTrip 作为 Trip 上的属性而不是子类。

然而，如果你的查询或获取只获取叶子类类型，这称为浅层搜索（shallow search）。在这种情况下，我们会考虑扁平化我们的模型，因为 Trip 从未被作为类型查询或使用。但如果你同时使用深度搜索和浅层搜索，继承会有所帮助，因为你经常需要搜索所有行程，或特定的子类型（如 PersonalTrip）来驱动针对该类型定制的视图。让我们花点时间看看如何更新我们的 Trips App，使其只显示个人或商务行程。

让我们使用一个分段控件（segmented control），这样我们就可以显示所有的行程，然后显示特定的子类。

选定的分段可以用来驱动一个谓词（predicate），该谓词通过 `is` 关键字确定该类是否属于特定类型。例如，这里我正在检查它是否是 PersonalTrip。然后我们提供谓词并按行程的 startDate 排序，以初始化我们的 Query。让我们在 App 中看看效果。它从行程视图开始，这样我可以看到我所有的行程。然后我可以将视图缩小到特定的子类。太棒了！这就是我们在 iOS 26 中利用类继承的方式。但是，我还没做完。我们刚刚对 schema 做了一些重大更改，我们应该考虑这对我们现有 App 意味着什么，以及如何迁移我们的数据。

在过去的几个版本中，SampleTrips App 经历了几次演进。让我们花点时间将这些都记录在版本化 Schema（versioned Schemas）和一个 Schema 迁移计划（schema migration plan）中，这样我们的 App 在升级到最新的 SampleTrips App 时将会保留用户的数据。

这一切始于我们的第一个视频，我们在 iOS 17 中介绍了 SwiftData，并使用 Trip 来指导采用。

通过这些介绍性视频，我们学会了如何使行程的名称唯一，以及如何更改属性的原始名称以在迁移时保留数据。

对于 iOS 17，我们使用新的版本标识符 2.0 构建了版本化 Schema，并显示了更改后的模型 Trip，它具有唯一的名称和重命名的 startDate 和 endDate。

接下来，我们添加了一个自定义迁移阶段，以便对现有的行程进行去重。

在这里，我们利用了 ModelContext 的 fetch 函数，以便获取所有行程以对其进行去重。

在 iOS 18 中，我们利用 index 和 unique 宏，同时标记了我们希望在删除时保留哪些属性。

这使我们能够在从数据存储中删除后识别我们的模型。

在我们的 iOS 18 版本化 Schema 中，我们将其标记为版本 3，并捕获了对 Trip 模型的更改。新的 unique 和 index 宏的用法确保我们的数据被去重，并且获取和查询性能良好。我们还使用 preserved value on deletion 装饰了相同的属性，这样当我们在消费持久化历史记录时，可以识别已删除的行程。

我们还添加了另一个自定义迁移阶段，以便在从版本 2 迁移到版本 3 时再次对行程进行去重。现在，在 iOS 26 中，我们将添加版本 4，其中包含子类和一个轻量级迁移阶段。

对于我们当前的版本 Schema，我们将其标记为版本 4，并列出我们 Schema 中所有模型以及新的子类。

因为我们的子类是用 `@available(iOS 26, *)` 装饰的，所以我们的版本 Schema 也是如此。

我们需要添加一个从版本 3 到版本 4 的轻量级迁移阶段，并具有与之前相同的可用性要求。

在构建了最终的版本 Schema 和迁移阶段后，我们可以将所有内容封装到一个 Schema 迁移计划中，以便我们提供版本 Schema 和要运行的迁移阶段的顺序。

Schema 迁移计划由一个按发布顺序排列的 Schema 数组组成。当 iOS 26 可用时，我们添加包含子类的最新 Schema，然后是一个迁移阶段数组，以便我们可以从一个版本迁移到下一个版本。这就是我们构建 Schema 迁移计划的方式。现在我们已经构建了版本 Schema 及其对应的 Schema 迁移计划，下一步是在为 SampleTrips 创建 model container 时利用它们。

让我们回到 modelContainer 修饰器，并将其更新为使用带有 Schema 迁移计划的 model container。

我们首先为 App 添加一个新的 container 属性，在其中我们将使用版本 4 构建版本化 Schema，并将 Schema 迁移计划提供给 ModelContainer 初始化方法。

现在，我们更新 modelContainer 修饰器以使用新的可迁移容器。

一切就绪后，我们确保了 SampleTrips 利用继承的更新可以轻松地通过我们之前发布的各种迭代进行迁移，同时保留用户的数据。既然我们已经处理了迁移，现在是时候考虑如何改进我们用来驱动视图和迁移阶段的查询和获取了。

我们上次用选定的分段通过谓词更新了查询。

但是在过去的视频中，我们还有一个搜索栏。让我们把它加回来，直接开始处理用户输入的搜索文本。

我们首先用提供的 searchText 构建一个谓词。首先，检查文本是否为空。如果不为空，我们构建一个复合谓词，看看行程的 name 或 destination 是否包含给定的文本。

接下来，我们构建一个包含搜索谓词和类谓词的复合谓词。最后，我们更新 Query 初始化方法以接受新的复合谓词。

通过这次更新，我可以点击搜索栏，输入一些文本来过滤行程，甚至可以使用分段控件进一步缩小范围。

过滤和排序只是定制查询和获取的几种方式。

让我们探索一些其他定制 SwiftData 获取的方式。

这是我们从版本 1 到版本 2 的自定义迁移阶段。我们将使用 `willMigrate` block 来获取所有的行程。然而，在我的去重逻辑中，我只访问了单个属性 name，因为这是版本 2 中的唯一属性，我使用它来确保没有重复。由于 name 是我唯一访问的属性，我可以更新 `fetchDescriptor` 以使用 `propertiesToFetch` 并指定 name，这样我们的 Trip 模型在迁移期间只打包我们需要的数据。

此外，如果我们知道我们可能会遍历某个特定的关系（在这种情况下，我知道如果发现重复项，我会重新分配住宿关系），我们可以通过使用 `relationshipsToPrefetch` 进行同样的优化。让我们在这里添加 livingAccommodation 关系。

现在我们已经采用了预取属性，我们还可以更新 SampleTrips 中现有的小组件代码，使其性能更好。

在 SampleTrips 小组件中，我们有一个查询用于获取最近的行程。但是，它可以改进，以便我们只获取单个值。目前，小组件代码只利用了获取的第一个结果。但我们可以通过设置 `fetchLimit` 来提高效率。

通过设置 `fetchLimit`，小组件将获得匹配谓词的第一个行程，并且无需担心未来我计划了太多假期的情况。在改进了查询和获取之后，让我们探索如何知道你的模型何时发生了变化。

所有持久化模型都是 Observable 的，因此我们可以利用 `withObservationTracking` 来响应模型中我们感兴趣的属性的更改。

如果我们想观察行程的 startDate 和 endDate 的更改，我们可以添加这个函数 `datesChangedAlert`，这样如果用户更改了日期，我们就发布一个提醒。

我们可以通过这种方式观察对 PersistentModel 进行的许多本地更改，并且这对于本地更改非常有用。有关 Observable 的最新详细信息，请查看“Swift 新功能”。但是，并非所有更改都是 Observable 的，只有那些在进程中对你的模型所做的更改才是，而来自另一个进程（例如小组件或扩展，甚至是你 App 中的另一个 model container）对你的数据存储所做的更改则不是。你 App 中的本地或内部更改是指你有多个模型上下文使用同一个 model container 的情况。这些其他模型上下文可以看到彼此的更改，在 Query 的情况下，这些更改会自动应用。

但是，如果你正在使用模型上下文的 fetch API，则在触发重新获取之前，将看不到在另一个模型上下文中进行的更改。

此外，外部操作也可以更改你的数据，例如小组件保存或另一个 App 写入共享的 App Group 容器。这些更改会自动更新由 Query 支持的视图。但是，使用 fetch 的地方将需要重新获取。

重新获取可能代价高昂，特别是如果对我们的模型处理感兴趣的内容没有发生变化。

对我们来说幸运的是，SwiftData 有持久化的历史记录。我们可以知道哪些模型发生了变化、何时发生变化、谁更改了模型，甚至哪些属性被更新了。我们还对 Trip 的几个属性使用了 `preservedValueOnDeletion`，因此当行程被删除时，历史记录将有一个墓碑（tombstone），我们可以解析它来识别被删除的行程。有关历史记录的更多信息，请参阅 WWDC24 的“通过 SwiftData 历史记录追踪模型变更”。

让我们利用持久化历史记录来知道是否需要重新获取。我们想做的第一件事是从容器中获取最新的历史 token。

这样我们就可以使用这个 token 作为我们上次从数据库读取位置的标记。就像我们最喜欢的书中的书签一样，标记我们上次读到的地方。

我们使用 `historyDescriptor` 为默认历史事务设置一个历史获取。但是，如果我们有很多持久化历史记录，我们可能会获取大量数据，只是为了获取最后一个作为我们的 token。幸运的是，iOS 26 中新增了使用 `sortBy` 获取历史记录的功能。我们可以指定任何事务属性，例如 `author` 或 `transactionIdentifier`，作为键路径来对历史结果进行排序。让我们采用新的排序方式，将其设置为 `transactionIdentifier`，但使用 reverse，这样最新的事务排在前面。然后，我们只关心最新的事务，也就是第一个事务，所以让我们将结果限制为 1。这就是我们高效获取最新历史 token 并存储它所需的全部操作。让我们保存这个 token 以供以后使用，并在未来的历史记录获取中使用它。

现在，当新的更改发生时（例如小组件更新了一个行程），一个新的条目会被添加到我们的历史记录中，我们的 App 可以获取历史记录，看看自上次 token 以来是否有任何感兴趣的更改。现在我们有了一个存储的历史 token，我们可以构建一个谓词，只获取该 token 之后的历史记录。为了只找到我们关心的更改，我们构建我们想知道已更改的实体列表。这里，我们只想知道一个行程是否发生了变化，或者它的 livingAccommodation 是否发生了变化，以防小组件确认了我们住在哪里。

并在 changes 谓词中使用实体名称来过滤历史记录更改，以找到我们想要的类型。最后，使用我们的 token 谓词和 changes 谓词，我们构建复合谓词。

有了这些更改，当我们获取历史记录时，我们只得到我们 token 之后的、并且是针对我们当前关心处理的实体的历史记录。

通过更好的历史记录获取，如果没有感兴趣的更改，我们可以避免重新获取。值得庆幸的是，SwiftData 历史记录使这变得容易。至此，我们知道了如何观察本地和远程对模型和数据的更改。

希望您觉得本视频内容充实，并利用 SwiftData 满足您的持久化需求。在构建模型图时，请考虑继承是否合适，以及随着模型图的演进，迁移会带来什么影响。在获取数据方面，构建更丰富、性能更高的获取和查询。了解数据何时发生了变化可能非常有价值。观察和持久化历史记录可以满足您的需求。我就讲到这里。

祝您旅途愉快。

---
title: 将你的 App 迁移到 Swift 6
session_id: 10169
collection: wwdc2024
year: 2024
duration: '41:48'
topics: [Developer Tools, Swift]
group: C · 并发、锁与线程
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2024/10169/'
content_hash: 'sha256:6c49d5e634e94983'
translated: true
---

# 将你的 App 迁移到 Swift 6

<sub>WWDC2024 · 41:48 · Developer Tools、Swift</sub>

体验 Swift 6 迁移的实际过程，我们更新一个现有的示例 App。了解如何按模块逐步迁移，以及如何……

> [!note] 归档理由
> Swift 6 严格并发迁移路径与隔离模型

## 章节

- [简介](/videos/play/wwdc2024/10169/?time=0)
- [Coffee Tracker App](/videos/play/wwdc2024/10169/?time=33)
- [回顾 WWDC21 的重构](/videos/play/wwdc2024/10169/?time=45)
- [Swift 6 与数据争用安全](/videos/play/wwdc2024/10169/?time=200)
- [实践中的 Swift 6 迁移](/videos/play/wwdc2024/10169/?time=280)
- [策略](/videos/play/wwdc2024/10169/?time=446)
- [采用并发特性](/videos/play/wwdc2024/10169/?time=533)
- [在 watch 扩展中启用完整检查](/videos/play/wwdc2024/10169/?time=665)
- [全局变量中的共享可变状态](/videos/play/wwdc2024/10169/?time=785)
- [全局实例与函数中的共享可变状态](/videos/play/wwdc2024/10169/?time=1024)
- [委托回调与并发](/videos/play/wwdc2024/10169/?time=1169)
- [保证你不维护的代码的数据争用安全](/videos/play/wwdc2024/10169/?time=1420)
- [在 watch 扩展中启用 Swift 6 语言模式](/videos/play/wwdc2024/10169/?time=1551)
- [继续处理 CoffeeKit](/videos/play/wwdc2024/10169/?time=1595)
- [在 CoffeeKit 中启用完整检查](/videos/play/wwdc2024/10169/?time=1644)
- [常见模式与增量策略](/videos/play/wwdc2024/10169/?time=1667)
- [CoffeeKit 中的全局变量](/videos/play/wwdc2024/10169/?time=1795)
- [在 Actor 之间发送数组](/videos/play/wwdc2024/10169/?time=1865)
- [如果无法将某物标记为 Sendable？](/videos/play/wwdc2024/10169/?time=2033)
- [在 CoffeeKit 中启用 Swift 6 语言模式](/videos/play/wwdc2024/10169/?time=2123)
- [添加一个具有数据争用安全保证的新功能](/videos/play/wwdc2024/10169/?time=2159)
- [总结与 Swift 6 迁移指南](/videos/play/wwdc2024/10169/?time=2443)

## 相关资源

- [简介](https://developer.apple.com/videos/play/wwdc2024/10169/?time=0)
- [Coffee Tracker App](https://developer.apple.com/videos/play/wwdc2024/10169/?time=33)
- [回顾 WWDC21 的重构](https://developer.apple.com/videos/play/wwdc2024/10169/?time=45)
- [Swift 6 与数据争用安全](https://developer.apple.com/videos/play/wwdc2024/10169/?time=200)
- [实践中的 Swift 6 迁移](https://developer.apple.com/videos/play/wwdc2024/10169/?time=280)
- [策略](https://developer.apple.com/videos/play/wwdc2024/10169/?time=446)
- [采用并发特性](https://developer.apple.com/videos/play/wwdc2024/10169/?time=533)
- [在 watch 扩展中启用完整检查](https://developer.apple.com/videos/play/wwdc2024/10169/?time=665)
- [全局变量中的共享可变状态](https://developer.apple.com/videos/play/wwdc2024/10169/?time=785)
- [全局实例与函数中的共享可变状态](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1024)
- [委托回调与并发](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1169)
- [保证你不维护的代码的数据争用安全](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1420)
- [在 watch 扩展中启用 Swift 6 语言模式](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1551)
- [继续处理 CoffeeKit](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1595)
- [在 CoffeeKit 中启用完整检查](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1644)
- [常见模式与增量策略](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1667)
- [CoffeeKit 中的全局变量](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1795)
- [在 Actor 之间发送数组](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1865)
- [如果无法将某物标记为 Sendable？](https://developer.apple.com/videos/play/wwdc2024/10169/?time=2033)
- [在 CoffeeKit 中启用 Swift 6 语言模式](https://developer.apple.com/videos/play/wwdc2024/10169/?time=2123)
- [添加一个具有数据争用安全保证的新功能](https://developer.apple.com/videos/play/wwdc2024/10169/?time=2159)
- [总结与 Swift 6 迁移指南](https://developer.apple.com/videos/play/wwdc2024/10169/?time=2443)
- [Swift 迁移指南](https://www.swift.org/migration/documentation/migrationguide/)
- [将 App 更新为使用严格并发](https://developer.apple.com/documentation/Swift/updating-an-app-to-use-strict-concurrency)
- [论坛：编程语言](https://developer.apple.com/forums/topics/programming-languages-topic?cid=vf-a-0010)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10169/6/4E4B2CB2-ABE3-49B7-AA2B-D97C6BF13B49/downloads/wwdc2024-10169_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10169/6/4E4B2CB2-ABE3-49B7-AA2B-D97C6BF13B49/downloads/wwdc2024-10169_sd.mp4?dl=1)
- [Swift 并发：更新示例 App](https://developer.apple.com/videos/play/wwdc2021/10194)
- [Recaffeinater 与 CaffeineThresholdDelegate](https://developer.apple.com/videos/play/wwdc2024/10169/?time=548)
- [添加 @MainActor 以隔离 Recaffeinator](https://developer.apple.com/videos/play/wwdc2024/10169/?time=566)
- [协议实现中的警告](https://developer.apple.com/videos/play/wwdc2024/10169/?time=578)
- [理解警告存在的原因](https://developer.apple.com/videos/play/wwdc2024/10169/?time=599)
- [logger 变量上的警告](https://developer.apple.com/videos/play/wwdc2024/10169/?time=779)
- [选项 1：将 'logger' 转为 'let' 常量](https://developer.apple.com/videos/play/wwdc2024/10169/?time=818)
- [选项 2：将 'logger' 隔离到主要 Actor](https://developer.apple.com/videos/play/wwdc2024/10169/?time=860)
- [选项 3：将其标记为 nonisolated(unsafe)](https://developer.apple.com/videos/play/wwdc2024/10169/?time=898)
- [正确答案](https://developer.apple.com/videos/play/wwdc2024/10169/?time=943)
- [scheduleBackgroundRefreshTasks() 有两个警告](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1023)
- [用 @MainActor 标注函数](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1077)
- [重新审视 Recaffeinater](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1335)
- [选项 1：将函数标记为 nonisolated](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1346)
- [选项 1b：将功能封装在 Task 中](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1387)
- [选项 1c：探索更新协议的方案](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1414)
- [选项 1d：不封装在 Task 中，改用 `MainActor.assumeisolated`](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1455)
- [`@preconcurrency` 作为 assumeIsolated 的简写](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1521)
- [在 CoffeeKit 中为委托协议添加 `@MainActor`](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1602)
- [新的警告](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1610)
- [移除 @preconcurrency](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1629)
- [CoffeeKit 中的全局变量被标记为 `var`](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1796)
- [将所有全局变量改为 `let`](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1819)
- [警告 1：在 `drinksUpdated()` 中发送数组](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1838)
- [查看 Drink 结构体](https://developer.apple.com/videos/play/wwdc2024/10169/?time=1924)
- [将 `Drink` 结构体标记为 Sendable](https://developer.apple.com/videos/play/wwdc2024/10169/?time=2009)
- [另一个不是 Sendable 的类型](https://developer.apple.com/videos/play/wwdc2024/10169/?time=2015)
- [使用 nonisolated(unsafe)](https://developer.apple.com/videos/play/wwdc2024/10169/?time=2068)
- [撤销该更改](https://developer.apple.com/videos/play/wwdc2024/10169/?time=2085)
- [将 DrinkType 改为 Sendable](https://developer.apple.com/videos/play/wwdc2024/10169/?time=2104)
- [使用 AsyncSequence 的 CoreLocation](https://developer.apple.com/videos/play/wwdc2024/10169/?time=2195)
- [创建 CoffeeLocationDelegate](https://developer.apple.com/videos/play/wwdc2024/10169/?time=2290)
- [将 CoffeeLocationDelegate 放在主要 Actor 上](https://developer.apple.com/videos/play/wwdc2024/10169/?time=2372)
- [更新 locationManager 函数](https://developer.apple.com/videos/play/wwdc2024/10169/?time=2406)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，我是 Swift 团队的 Ben，在这个视频中，我将带你了解如何在现有 App 中启用 Swift 6 语言模式。我们将看到 Swift 6 如何帮助你防范可能的数据争用，并了解一些逐步将这一变更引入 App 的技巧，以及如何处理与尚未了解 Swift 并发保证的框架的交互。我将使用一个简单的 App，它跟踪一天中的咖啡消耗量，以及一个在表盘上显示当前咖啡因水平的复杂功能。当我们在 WWDC 2021 首次介绍 Swift 并发时，我曾带你了解如何在该 App 中采用 Swift 的新并发模型。在那次演讲中，你会看到看似整洁的 App 架构有时隐藏着并发的隐性复杂性。如果你查看视图和模型，一切组织得井井有条。但深入研究并发的管理方式时，却呈现出不同的画面。原始 App 有 3 个并发队列，代码可能在其上执行。UI 和模型的工作在主队列上完成。App 还有一个用于后台工作的 dispatch 队列。最后，某些回调到完成处理程序的调用，比如 HealthKit 返回结果的那些，是在任意队列上完成的。因此，虽然类型组织得整整齐齐，但 App 中并发的组织方式却不是那么清晰的故事。

代码在哪个队列上执行，以及为什么，以一种在多处都不清晰的方式贯穿于类型之中。

通过采用 Swift 并发，我们从这种临时并发架构。变成了这样。UI 视图和模型被设置为运行在所谓的主要 Actor 上，而后台操作在专门的 Actor 上执行。Actor 之间使用线程安全的值类型通过 Swift 的 async/await 特性进行通信。完成后，并发架构就像类型架构一样清晰且易于描述。但有一个小问题。在进行这次重构以改进架构时，避免数据争用的大量责任仍然落在我这个程序员身上。我遵循了所有指南，并使用值类型在 Actor 之间通信，但我不必这样做。我可以拿一个引用类型，比如一个类，把它从一个 Actor 传到另一个 Actor。引用类型允许共享可变状态被传递，当你这样做时，你可能破坏 Actor 提供的互斥，允许它们同时访问共享状态。所以，如果我把一个类的实例从一个 Actor 发送到另一个 Actor，仍然可能产生数据争用，可能导致程序崩溃，或者更糟，损坏用户数据。这引出了 Swift 6 的好处。

Swift 6 语言模式引入了数据隔离的全面执行。编译器将阻止这种 Actor 和任务之间状态的意外共享，允许你在不担心引入新并发错误的情况下进行重构，或给 App 添加新功能。

Swift 6 语言模式对现有项目和新项目都是可选的。采用它可以显著提高 App 质量，通过在编译时捕获并发代码中的错误。如果你正在经历难以复现的崩溃，并希望系统地消除数据争用风险，它会特别有用。如果你正在积极集成更多并发以提高响应性和性能，采用 Swift 6 模式可以确保这些更改不会带来引入新数据争用的风险。

如果你维护一个公共 Swift 包，我们鼓励你尽快采用 Swift 6，以帮助也想迁移代码库的用户。他们将受益于构建在同样采用 Swift 6 的依赖之上。大家可以在 swiftpackageindex.com 上关注流行包对 Swift 6 的采用情况。今天，我们将看到这在实践中如何工作。我们将拿我们的 CoffeeTracker App，启用 Swift 的数据隔离。我们将逐步进行，并查看编译器给出的关于需要修改哪些地方的指导，以便让 Swift 保证 CoffeeTracker 不含任何数据争用。现在，我不认为我的 App 今天实际上包含任何数据争用。你的代码大概率也是如此。你可能已经通过多年的改进、错误报告、使用主线程检查器、线程净化器等，把现有代码中的大多数数据争用都排查掉了。数据争用安全的真正价值在于防范你编写的新代码中的错误，无论是添加新功能，还是为了更好地利用并发而重构现有代码。数据争用安全允许你在 App 中利用并发，而不必担心引入新的数据争用，这些数据争用你之后不得不去追踪，或因为无法复现崩溃而只能 speculative 地修复。自从我们上次看到它以来，我们的咖啡追踪 App 真正火了起来，我们扩展了团队开始添加新功能。

作为其中的一部分，我们把 App 的一部分拆分到了一个新框架 CoffeeKit 中，现在有些代码 resides there。团队热衷于给 App 添加新功能，但在做这件事之前，我们要把它更新到 Swift 6，以便我们知道添加新功能时不会引入新的并发错误。现在，我刚刚下载了 Xcode 16 并打开它。这意味着我拥有新的 Swift 6 编译器和 watchOS 11 的最新 SDK，让我们试着构建这个 App。

它构建得很好。无需任何更新。但这并不是因为我们的 App 没有任何可能的数据争用。只是我们还没有启用 Swift 6 语言模式。就像之前的版本一样，Swift 6 有源代码兼容性保证。除了很小的更改之外，你的 App 应该始终能用新编译器构建。

既然我们知道 App 能用最新的 Xcode 构建，我们想要采取下一步，启用 Swift 6 模式，它带来数据隔离的全面执行。现在，在为此做准备时，你可以遍历并尝试在启用任何编译器诊断之前进行 MainActor 和 Sendable 审计。但这样就错过了新 Swift 编译器给你带来的好处。编译器诊断会引导你走向需要修复的地方。把它想象成一个指出代码中潜在错误的结对程序员。这为迁移过程添加了一些结构。我们将遵循一个逐步的过程，迁移代码中的每个目标。对于每个目标，我们将遵循以下步骤：首先，我们将启用完整并发检查。这是一个按模块的设置，让项目保持在 Swift 5 模式，但对所有会因 Swift 6 的强制数据隔离而失败的代码启用警告。我们将逐步解决该目标的所有这些警告。

一旦完成，我们就启用 Swift 6 模式。这锁定了我们所有的更改，并防止任何未来的重构退回到不安全状态。然后我们进入下一个目标并重复这个过程。最后，一旦启用，我们可能想回去做一些整个 App 的重构，也许是通过改变架构来撤销一些不安全的 opt out，或者进行你发现的能让代码更漂亮的重构。关于重构的一条建议：尽量抵制把重大重构和启用数据争用安全混在一起的诱惑。尽量一次做一件事。如果你试图同时做这两件事，你可能会发现一次改动太多，不得不回退。

在这次演讲中，我们将只专注于在我们已经先前重构为使用 Swift 并发的 App 中启用 Swift 6 这一步。所以我们从启用完整检查开始。完整检查启用什么？如果你已经在 App 中使用 Swift 并发，你可能已经看到 Swift 编译器关于并发问题的警告或错误，这些在你采用 Swift 的并发特性时出现。例如，这里我们正在添加一个新的委托，它将接收我们为 CoffeeKit 添加的回调，告诉我咖啡因水平低得令人担忧。这个委托将把一个值发布回我的 SwiftUI 视图，所以我希望它被隔离到主要 Actor。所以我可以在顶部添加 @MainActor，要求其所有方法和属性访问在主线程上进行。但当我这样做时，我在代码下方的协议实现上得到了一个错误。

它告诉我「主要 Actor 隔离的实例方法 'caffeineLevel(at:)' 不能用于满足非隔离的协议要求」。这个 CaffeineThresholdDelegate 协议现在不对它将如何被调用做任何保证。它在 CoffeeKit 内部，那还没有更新到 Swift 6。但这里我正在让我的 Recaffeinater 类型符合它，并且我刚刚把它约束到了主要 Actor。它的方法将在主要 Actor 上运行，所以它们不能只是符合一个不总是保证在主要 Actor 上调用的协议。我们会稍后回到这个问题并解决它。但这是 Swift 编译器因为把类型加入到检查它是否在主要 Actor 上被调用而生成的错误的一个例子。如果你看过之前的演讲，采用 Swift 并发在 Coffee Tracker，你会看到这些在 App 不同地方采用并发时出现的问题。

在目标的构建设置中启用严格检查，会把你的整个模块加入到检查可能的数据争用中。让我们现在启用它，看看会发生什么。Swift 中的数据隔离是按目标启用的，在我的 App 中，我有两个关键目标，watch 扩展，我的 UI 层 resides there，以及 CoffeeKit，一个进行咖啡因追踪和保存到 HealthKit 的业务逻辑的框架。

我将从在 watch 扩展上启用完整检查开始。有两个原因。第一，它通常是启用并发检查的更简单地方。UI 层的大部分将在主线程上运行，并将使用本身保证在主线程上执行操作的 API，比如 SwiftUI 或 UIKit。另一个原因是，启用严格并发时，你通常会与尚未更新为 Swift 并发的其他模块一起工作。也许你正在使用一个永远不会更新的 C 库。或者它是一个框架或包模块，将被更新到 Swift 6，只是还没有。当然，这包括我们自己的 CoffeeKit 框架。一旦我们开始，你就会看到为什么这样自上而下地做有帮助。所以，作为第一步，让我们进入扩展，打开它的设置。我们将搜索 Swift 并发检查设置，并将其设置为完整检查。

一旦我们这样做，编译器将开始发出关于它无法确认并发安全的代码的警告。这些只是警告，我们的项目仍然会构建和运行。所以让我们试着构建。

我们看到，除了我们早先引入的那个之外，还有更多警告。让我们来看看它们。

现在，我们能看到的第一个问题是处理 Swift 6 中最常见的问题之一，指这个 "logger" 变量。

我们看到一个 logger 实例被声明为全局变量。全局变量是共享可变状态的来源，无论代码在哪个线程上运行，程序中的每一部分代码都能读写这个相同的变量。所以这可能是数据争用的真正容易的来源，我们需要让它安全。我们有几种选择如何做。实际上如果我们展开这个问题，会看到编译器正在推荐一些。

第一个选项是最简单的，我们只是让它只读。Logger 是一个 Sendable 类型，这意味着如果它被声明为 let 变量，它在多线程使用时不会导致数据争用。所以把这个 var 改成 let。然后重新构建。

让那个问题消失。现在，这是正确的修复，但这里还有其他选项。

假设我不想让它不可变，比如我想稍后更新这个值。所以我希望保持它是 var 而不是 let。

另一个选项是把这个全局变量绑定到一个全局 Actor。这里，我在 UI 层，所以也许我所有的日志都将在主要 Actor 上发生。所以我可以用 @MainActor 标注这个全局变量，是的，我所有的日志使用都在主要 Actor 上，这也消除了警告。

最后，有时我有某种其他外部机制保护这个变量，编译器无法强制执行。也许我使用一个 dispatch 队列保护所有访问。在这种情况下，我可以使用 nonisolated(unsafe) 关键字。

像 Swift 中其他使用 "unsafe" 这个词的情况一样，这把确保这个变量安全的责任交给你。这应该是最后的手段，最好使用 Swift 的编译时保证。但编译器不可能知道一切，所以在这些情况下，nonisolated(unsafe) 作为选项提供给你。这可能是我想稍后回来重构这个代码的例子，也许把这个变量移动到一个 Actor 中，以便编译器可以验证它被安全使用。但就现在，我可以把它标记为 nonisolated(unsafe) 并继续下一个警告。这不是这些情况之一，所以我将回到把这个变量声明为 let，那是最佳选项。现在你可能想知道这个初始化器，它初始化这个全局。那什么时候运行？知道这一点对理解线程安全很重要吗？Swift 中的全局变量是惰性初始化的。值在首次使用时初始化，第一次 CoffeeTracker 记录日志时。与 C 和 Objective-C 相比，这是很重要的区别。在那些语言中，全局变量在启动时初始化。这可能对启动时间真的很糟糕。Swift 的惰性初始化避免了这些问题，允许你的 App 更快地到达可用状态。但惰性初始化也可能引入竞争：如果两个线程同时试图首次使用这个全局变量来记录日志，怎么办？它们会创建两个 logger 吗？别担心——在 Swift 中，全局变量保证会被原子地创建。如果两个线程试图同时首次访问 Logger，只有一个会初始化它，而另一个会阻塞等待。好了，解决了这个问题，让我们看看下一个。

这里我们有一些代码访问 WKApplication 的共享实例。这个全局实例方法是绑定到主要 Actor 的一个例子。

这里的第一条注释指出，对 Actor 隔离状态的调用是隐式异步的，也就是说，如果这是一个 async 函数，你可以使用 await 在主要 Actor 上访问这个全局变量。这个函数不是异步的，所以我们必须把它标记为 async，或者启动一个新任务。但编译器给我们提供了另一个修复，我们只需把这个函数放在主要 Actor 上。

因为这是一个自由函数，不是我们视图上的方法，它不会默认在主要 Actor 上。让我们应用 fixit，现在这个方法被隔离到主要 Actor，如果我们试着构建，它成功了。

为了看看为什么这奏效，让我们快速看看调用者。

我们看到它被调用了两次，都在我知道在主要 Actor 上的方法中。如果这个函数在主要 Actor 之外的任何地方被调用，我会得到一个编译器错误告诉我，我可以去查看那个调用者，看看它从什么上下文调用。一个是 SwiftUI 视图。另一个在 WKApplicationDelegate 的实现中。让我们去看看。

如果我们 option-click WKApplicationDelegate，可以看到它是一个绑定到主要 Actor 的协议。这是它只会在主要 Actor 上被调用的保证，无论由 WatchKit 框架，还是一旦启用 Swift 6 模式，由你的代码。

许多设计为只在主要 Actor 上操作的委托和其他协议，比如 SwiftUI 视图，都像这样被标注了，尤其是在 Xcode 16 附带的最新 SDK 中。最重要的是，这包括 SwiftUI View 协议。你可能会发现，如果你之前启用了严格并发检查，你必须比新 SDK 中必要时添加更多的主要 Actor 标注，并且你可能能够移除其中的一些标注。现在，让我们谈一谈委托回调与并发。你可能已经知道，无论何时你从委托或完成处理程序接收回调，你总是必须首先理解该回调的并发保证。有些回调有保证，它们可能在文档中说所有回调总是会在主线程上。很多 UI 框架给出这个保证，这就是为什么我们在 watch 扩展的这个视图层上把东西标记为主要 Actor 时，没有得到那么多警告的原因之一。另一方面，有些委托做相反的事，它们对如何被回调不做任何保证，说它将在某个任意线程或队列上。这对更可能进入 App 后端的回调很有意义。CoffeeTracker 从 HealthKit 接收的回调更像这样。在这些情况下，用户需要重新派发到正确的队列或 Actor，或者以线程安全的方式做他们的工作。这种每个委托都有自己的规则且只在文档中捕获的方法的问题在于，这把大量责任放在你这个用户身上，去做正确的事。你需要思考被回调时你在哪里，以及你需要在哪里做逻辑的下一部分。如果你忘了检查，或忘了重新派发到正确的地方，你很容易得到数据争用。更糟糕的是，假设一个回调已经就位并工作……

Swift 并发通过使这些保证，或缺乏保证，显式化来解决这个问题。如果一个回调不指定如何被回调，它被视为非隔离的，不能访问需要特定隔离的数据。另一方面，如果一个回调确实提供了隔离保证，比如说它总是会在主要 Actor 上被回调，那么它可以标注委托协议或回调总是会在主要 Actor 上，并且回调的接收者可以依赖该保证。有了这个，让我们回到我们看到的第一个警告，我们主要 Actor 上的委托类型无法符合非隔离的协议。我们有几个选项，编译器正在提供。第一个是把方法声明为 nonisolated。这意味着尽管这是主要 Actor 隔离类型上的方法，这个特定方法不会被隔离到主要 Actor。这是针对有意不对回调位置做任何承诺的回调的路径。当然，这是视图，我可能立即想转而做主要 Actor 上的工作。如果我不这样做，编译这个代码时会得到新错误，因为我正在访问视图上受主要 Actor 保护的属性。

我可以启动一个主要 Actor 上的任务来修复这个。

在这种情况下，我知道这个回调应该在主要 Actor 上，我知道它来自 CoffeeKit 内部本身运行在主要 Actor 上的模型类型。

一个选项，如果我维护整个代码库，就是现在就去修复它。我可以跳转到定义，这里我看到 CoffeeKit 内部的协议。我可以在这里用 @MainActor 标注它，以保证它会在主要 Actor 上被调用。但有时你并不像这样维护整个代码库。也许另一个团队维护 CoffeeKit，或者它是一个你依赖的由别人维护的包或框架。让我们假设这里就是这种情况，回到我们的委托实现。

现在，我知道这个方法在主要 Actor 上被调用，我刚检查了代码，或者也许我在该委托的某些文档中读到了。

当你确定调用将在特定 Actor 上时，有一个你可以用来告诉编译器这一点的方法，它叫做 assumeIsolated。所以，不是代码启动一个任务，我可以写 MainActor.assumeIsolated。这不会启动一个新任务来 async 到主要 Actor。它只是告诉 Swift 这段代码已经在主要 Actor 上运行。

注意，某些代码部分仍然完全可能从非主要 Actor 调用这个函数。这与今天假设它们从主线程被调用的 Swift 函数相同。保护这一点的一个好方法是，在函数内部添加一个断言，你确实在主要 Actor 上，这就是 assumeIsolated 做的。如果这个函数从主要 Actor 之外被调用，它会 trap，你的程序将停止运行。Trapping 不是你想要的，但它比可能导致损坏用户数据的数据争用要好。

现在，这种符合假设在主要 Actor 上被调用的委托协议的模式足够常见，以至于有一个简写。所以让我撤销这里的更改，改为，在协议一致性上，我写 @preconcurrency。

这做了我手动写出的一切，它假设它被调用在该视图被隔离到的 Actor 上，如果不是，它会 trap。

现在我们已经消除了所有并发警告，我们准备好在这个目标中启用 Swift 6。所以我们进入设置。这次搜索 Swift Language Mode。

并将其设置为 Swift 6。

编译，它没有任何错误和警告地构建了。我现在已经在扩展中锁定了完整的数据隔离检查，我在这里做的任何未来更改都会有编译器的完整数据隔离检查，确保我不小心引入数据争用。好了，现在扩展处于 Swift 6 模式，让我们把注意力转向 CoffeeKit 目标。现在我们正在处理这个目标，让我们给委托协议添加那个 @MainActor 标注。所以让我们找到它。添加主要 Actor 标注，重新构建，我们得到一个新警告。

警告回到扩展中，它在我们刚添加的 @preconcurrency 属性上。

现在编译器可以看到这个协议保证在主要 Actor 上，编译器警告说那个 pre concurrency 属性不再需要了。所以我们可以移除它。

好了。解决了这个问题后，我们可以遵循与之前相同的例程，启用完整并发检查。我们进入项目设置，并为 CoffeeKit 目标启用它。

然后构建。

这次我们看到更多警告——11 个。对于一个相当简单的项目来说，那是相当多的警告。

这将是常见体验。你在项目中启用完整并发检查，项目生成数百甚至数千个警告。当那发生时，你可能担心你签了什么。此时不要惊慌。大量警告通常都 stemming from 几个问题。并且这些问题中的许多通常很快就能修复。

所以，当首次清理并发警告时，一系列简单的更改，把一个方法放到主要 Actor 上，或把一个全局改为不可变，可以非常快速地削减这些警告。首次打开严格检查时，一个好的策略是去寻找这些快速胜利并采取行动，先用最简单的修复减少警告。也值得留意那些处于大量问题根源的问题。有时单行更改可以解决数百个连锁问题。如果你用之前版本的 Xcode 尝试过完整检查模式，也值得用最新的 Xcode beta 再试一次。更新的 SDK 包含更多帮助迁移的标注。例如，所有 SwiftUI 视图现在都绑定到主要 Actor，这意味着你不再需要自己给视图类型添加 MainActor 标注。事实上，你可能会发现可以移除其中的一些标注，因为它们已经被推断了。

一旦完成，你可能会发现自己剩下更少的警告，但更难处理。另一件要记住的是，你不必在一个 sitting 中解决所有这些问题。如果你必须发布一个版本，或者去处理更紧迫的更改，你可以回到设置并把严格检查关掉。你所做的所有减少这些警告的更改都将是代码库的有效改进，即使你随后回到最小检查一段时间，也可以保留和 check in。你可以在准备好时稍后返回那个设置，然后处理它们。在我们的例子中，一旦我们开始查看警告，我们看到了我们之前见过的模式。这些全局变量中有几个被标记为 var，但我认为这些都是常量，或不需要可变，就像我们之前看到的 logger 一样。我们可以相当快速地解决所有这些。顺便说一句，这是练习多行编辑技能的好时机。

所以我只需高亮 var，然后 cmd-option-E 选择所有，把它们改为 lets。

构建。

消除了这些警告。

现在，我不想给你留下我把这件事说得比实际容易的印象。这只是一个示例项目，在真实项目中会有更多警告。但我们的经验，把真实全规模项目放进去是，这是一个常见体验，很多容易的胜利，然后还有一些更难的问题要处理。让我们看看最后的错误。它们是由我们在不同 Actor 之间传递 drinks 数组引起的。例如，第一个说把 self.currentDrinks 发送到这个 save 方法可能引起数据争用。注意 save 是另一个 Actor 上的方法。CoffeeData 在主要 Actor 上，它必须这样，因为它是 SwiftUI ObservableObject。

但 save 在另一个 Actor 上，它在这个 CoffeeDataStore Actor 上，该 Actor 在后台做保存和从磁盘加载。如果我们回到警告，你可以看到我们发送给 save 的是与作为主要 Actor 隔离的模型保持相同的 drinks 数组。

如果 Drink 是一个引用类型，我们将设置潜在的数据争用，主要 Actor 和存储 Actor 都可能同时访问共享可变状态。为了解决这个，让我们看看 Drink。如果我们转到定义，可以看到它是一个结构体，有几个不可变属性，全部是值类型。基于这个，它显然可以被做成 Sendable，然后在不同 Actor 中存储 drinks 并把同一个数组发送到另一个 Actor 就完全没问题了。

现在，如果这是一个内部类型，Swift 只会自动为你考虑这个类型是 Sendable。但这是一个公共类型，我们与 CoffeTracker 扩展共享它。

Swift 不会自动为你推断公共类型的 sendability。它不这样做，因为标记一个类型为 sendable 是对客户端的保证。这个类型今天不包含可变状态，但也许我将来想改变，我不想过早锁定 sendability。因此，Swift 要求你在公共类型上显式添加 Sendable 一致性。

现在在这种情况下，我很乐意这样做。顺便说一句，这是我可以做的一个单行更改，可以一次消除多个警告的例子：三个不同的地方需要 Drink 类型为 Sendable。在大型项目中，可能不是三个，可能是多个项目中的数十个警告。所以，让我们继续把这个类型标记为 Sendable。

我们可以重新编译。

我们看到这里还有另一个类型不是 sendable。

现在，碰巧这只是一个枚举，所以我可以去把它标记为 sendable。但如果不是，如果它是一个 Objective-C 类型，也许一个永远不能是 sendable 的，因为它在引用类型中存储可变状态。此时你可能需要做出一些关于安全性的选择。一个选项是推理那个类型，并决定，即使它是一个可变引用类型，它是安全的，因为它是一个新副本，也许由 NSCopying 生成。你可能决定，即使它不是 sendable，你可以保护那个类，也许让变量 private 说，并 anyway 把它存储在你的 sendable 类型中。为此，你可以再次使用 nonisolated(unsafe) 关键字。

如果你这样做，那么 Drink 类型现在编译时带有 Sendable 标注。现在，我知道那是不必要的，所以相反，我将撤销那个，转而到 DrinkType，也把它标记为 Sendable。

现在我们已经在 CoffeeKit 中消除了所有并发警告，我们准备好在这个目标中启用 Swift 6 模式。所以再次进入设置。

这次搜索 Swift Language Mode。

并将其设置为 Swift 6。

编译。

它构建了。此时，我们的整个 CoffeeTracker App 都受到 Swift 并发的保护。

最后，既然我们已经受到保护，让我们看看给 CoffeeTracker 添加一个新功能。我们的用户想在喝咖啡时开始追踪他们的位置，以便他们可以挖掘数据以获得关于咖啡因习惯的关键洞察。所以让我们看看把 CoreLocation 加入我们的 App。所以，让我们转到 CoffeeKit 中的 addDrink 方法。就在我们添加 drink 之前，我们将使用 CoreLocation 获取用户当前位置。CoreLocation 有一个流式传输当前位置的 async sequence，与 Swift 并发配合得很好，我们可以在这里用它来循环遍历位置结果，直到我们得到正确的准确度级别，此时我们可以把位置分配给我们的 caffeine sample。你可能想给这段代码添加一个超时，你可以用 Swift 的结构化并发和取消来做到。这里只有一个问题。

我们将不得不提高 CoffeeTracker 的最低部署目标。我们还没准备好那样做，我们还有一些用户不想更新到 watchOS 10，但确实想追踪他们在哪里喝咖啡。所以，我们反而需要使用基于委托回调的旧 CoreLocation API。这些早于 Swift 并发，所以使用它们会更棘手。这种方法真正好的一点是，这段代码看起来像常规的同步代码。我们请求位置，循环遍历传入的位置更新流，直到我们得到一个足够准确的，全部在这个我们正在把新 drink 添加到数组的函数中。基于委托的 API，相比之下，将要求我们保存一些状态，等待委托方法触发，然后从那里继续用位置保存我们的 drink 值。所以值得尝试提高你的部署目标以利用这些新 API。

但假设我们不想那样做。所以，让我们移除这个新代码，转到这个文件的底部，创建一个 CoreLocation 委托对象。

所以这里我有一个委托类的基本实现，它可以接收来自 CoreLocation 的位置更新。这部分 CoreLocation 早于 Swift 并发。所以我必须做更多工作来确保我坚持规则。与我们在这次演讲中看到的所有其他回调不同，这个 CLLocation 委托有点不同。它没有关于将在哪个线程上调用它的静态保证。

到目前为止，我们讨论了总是在主线程上调用的委托，或在任意线程上调用的委托。如果你查看 CoreLocationManager 的文档，你会看到它给出的保证是，这个委托被调用的线程由你创建 CLManager 的线程决定。这是 Swift 无法在没有帮助的情况下自动为你强制执行的动态属性。

在我们的例子中，我们从主要 Actor 上的模型类型中使用这个信息。所以，最简单的路径是确保这个委托也在主线程上。要重新进入 Swift 将帮助我们强制执行该模式，把这种类型完全放在主要 Actor 上是简单的。

这意味着位置管理器将在初始化器中在主线程上被创建。因此委托也将在主要 Actor 上进来。

当然，一旦我们这样做，我们得到编译器熟悉的错误，告诉我们这个委托回调不被隔离到主要 Actor。我们已经看到处理这个的模式。

我们把委托标记为 nonisolated。

然后把必须在主要 Actor 上运行的代码封装在 MainActor.assumeIsolated 调用中。

我的构建成功了。我们现在在 App 中 sourcing 当前位置，仍然在 Swift 6 中构建。这是迁移 App 到 Swift 6 语言模式的一些技巧的快速巡览。今天有很多场景我们没有覆盖，但我们有更多资源供你使用。你可以从观看上一个演讲开始，它看了使用 Swift 的并发特性来现代化现有 App。把这段代码迁移到 Swift 6 的路径因那次演讲涵盖的一些重构而变得更简单。基于之前迁移的经验教训，Swift 6 语言模式被设计为跨越 Swift 生态系统的增量迁移。所以数据争用可以一次一个代码更改地消除。我们只是触及了在作为社区承担这一过渡时，桥接静态和动态数据争用安全的技巧的表面。你可以在 Swift.org/migration 找到包含所有这些策略和更多内容的指南。我们希望这些资源在你处理自己的代码时有用。感谢观看！

---
title: 演进你的 Core Data 架构
session_id: 10120
collection: wwdc2022
year: 2022
duration: '19:51'
topics: [System Services]
group: H · 持久化与文件系统
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2022/10120/'
content_hash: 'sha256:06c17400806eafde'
translated: true
---

# 演进你的 Core Data 架构

<sub>WWDC2022 · 19:51 · System Services</sub>

了解如何在更新 App 后干净利落地迁移 Core Data 架构，并轻松应对数据模型的变更。我们将向你演示如何...

> [!note] 归档理由
> 模型迁移机制（轻量/重量迁移）

## 相关资源

- [自动迁移你的数据模型](https://developer.apple.com/documentation/CoreData/migrating-your-data-model-automatically)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/10120/5/7685DE64-40AC-4C35-9865-8CDA798501E4/downloads/wwdc2022-10120_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/10120/5/7685DE64-40AC-4C35-9865-8CDA798501E4/downloads/wwdc2022-10120_sd.mp4?dl=1)
- [Core Data 新变化](https://developer.apple.com/videos/play/wwdc2023/10186)
- [认识演讲者：演进你的 Core Data 架构](https://developer.apple.com/videos/play/wwdc2022/110928)
- [优化 Core Data 和 CloudKit 的使用](https://developer.apple.com/videos/play/wwdc2022/10119)
- [问答：Core Data](https://developer.apple.com/videos/play/wwdc2022/110836)
- [问答：Core Data](https://developer.apple.com/videos/play/wwdc2022/110838)
- [迁移你的 Core Data 架构](https://developer.apple.com/videos/play/wwdc2022/10120/?time=376)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ David Stites：大家好，欢迎来到“演进你的 Core Data 架构”。我是 David Stites，Core Data 团队的一名工程师。在这次演讲中，我很兴奋能与大家讨论如何更新和迁移 App 中的 Core Data 架构。本次演讲的日程安排是：了解什么是架构迁移，以及为什么 App 在更新数据模型后必须执行它；如何迁移现有架构；以及 CloudKit 和架构迁移如何交互。首先，什么是架构迁移，以及为什么在更新数据模型时 App 必须进行迁移。

随着你的应用程序演化，可能有必要更改你的数据模型。更新数据模型要求这些更改在底层存储架构中得以实现。考虑这个数据模型。它有一个 Aircraft 实体，带有两个特性：type 和 number of engines。这些特性会反映到底层存储中。如果我添加一个 number of passengers 特性，就需要添加相应的存储。迁移之后，更改会完全反映在底层存储中。如果不迁移底层存储中的更改，Core Data 会拒绝打开你的持久化存储，因为新更改的模型与用于存储的模型不匹配。尝试打开不兼容的存储会导致错误，错误码为 `NSPersistentStoreIncompatibleVersionHashError`。如果你收到这个错误，它应该表明你需要进行迁移。现在我已经解释了什么是架构迁移以及为什么它对演进你的 App 至关重要，让我告诉你迁移是如何完成的。Core Data 内置了数据迁移工具，有助于保持 App 的数据存储与当前数据模型保持一致。这些工具统称为“轻量迁移”。轻量迁移是首选的迁移方法。轻量迁移会自动分析并从源托管对象模型和目标托管对象模型之间的差异推断出迁移。在运行时，Core Data 会在由 `NSBundle` 类的 `.allBundles` 和 `.allFrameworks` 方法返回的 bundle 中查找模型。然后，轻量迁移会生成一个映射模型，将你在 App 中所做的更改在你的数据库架构中实现。

使用轻量迁移要求对数据模型的更改符合明显的迁移模式。

涉及特性的轻量操作包括：添加特性、删除特性、将非可选特性变为可选、将可选特性变为非可选并定义默认值，以及重命名特性。如果你想重命名特性，请在目标模型中设置重命名标识符为源模型中对应特性的名称。

重命名标识符可以在 Xcode 数据模型编辑器的属性检查器（Property Inspector）中找到。例如，你可以将 Aircraft 实体的 color 特性重命名为 paintColor。重命名标识符会创建一个规范名称，因此需将重命名标识符设置为源模型中该特性的名称，除非该特性已有重命名标识符。这意味着你可以在模型版本 2 中重命名一个特性，然后在版本 3 中再次重命名它。从版本 2 到版本 3，或从版本 1 到版本 3，重命名都能正常工作。

轻量迁移也可以轻松处理关系到关系的更改。你可以添加新关系或删除现有关系。你也可以像对待特性一样，通过使用重命名标识符来重命名关系。此外，你可以更改关系的基数，例如，从对一迁移到对多，或从无序对多迁移到有序对多，反之亦然。

如果你猜想实体也适用于轻量迁移，那么你是对的。你可以添加新实体、删除现有实体以及重命名实体。你还可以创建新的父实体或子实体，并在实体层次结构中上下移动特性。你可以将实体移入或移出层次结构。但是，你不能合并实体层次结构。如果两个现有实体在源中没有共同的父级，它们在目标中也不能有共同的父级。轻量迁移由两个选项键控制：`NSMigratePersistentStoresAutomaticallyOption` 和 `NSInferMappingModelAutomaticallyOption`。当将存储添加到持久化协调器时，如果这两个键存在并设置为真值，且 Core Data 检测到持久化存储不再与当前模型匹配，它将自动执行轻量迁移。如果你使用 `NSPersistentContainer` 或 `NSPersistentStoreDescription`，这些选项会自动为你设置，你不需要做任何事。如果你使用替代 API，例如 `NSPersistentStoreCoordinator.addPersistentStore(type:configuration:at:options:)`，可以通过设置并传入一个选项字典，其中包含 `NSMigratePersistentStoresAutomaticallyOption` 和 `NSInferMappingModelAutomaticallyOption` 键并设置为 `YES` 来请求轻量迁移。如果 Core Data 检测到持久化存储不再与当前模型匹配，它将自动执行轻量迁移。

以下是在代码中如何实现。首先，我会导入 CoreData 并创建一个托管对象模型。然后，我会使用刚创建的模型创建一个持久化存储协调器。注意我创建的选项字典，以及在我将存储添加到持久化协调器时传递该字典。最后，我将存储添加到协调器，必要时迁移将在此自动发生。无论你使用什么 API，对数据模型的更改可以直接在与应用程序一起发布的同一模型中进行。无需为了进行更改而创建新版本的模型。如果你想事先确定 Core Data 是否能在不实际执行迁移工作的情况下推断源模型和目标模型之间的映射模型，你可以使用 `NSMappingModel.inferredMappingModel` 方法。如果 Core Data 能够创建推断模型，该方法会返回它；否则返回 nil。

有时，对架构的组合更改可能超出轻量迁移的能力。我将描述如何解决这个问题并仍然使用轻量迁移。

回到我们之前的示例模型，假设我们之前添加了一个名为“flightData”的特性，它使用外部存储来存放二进制数据，由存储在 `FLIGHT_DATA` 中的文件路径指示。进一步假设，需要更改该特性以在内部存储数据并移除外部存储。检查这个迁移是否符合轻量迁移的任何能力，发现并不符合。表面上看来，我们似乎陷入了困境，无法进行此更改。然而，别担心！轻量迁移仍然可以用于执行更复杂、不合规的迁移，尽管需要多个步骤。

目标是将不符合轻量迁移条件的迁移任务分解为一系列符合轻量迁移条件的最小迁移。通常，如果原始模型是 A，目标模型是 B，但模型 B 包含不符合轻量迁移条件的更改，可以通过引入一个或多个模型版本来创建桥梁，从而分解这些更改。

引入的每个模型都将包含一个或多个操作，这些操作在构成不合规更改的能力范围内。这将导致一系列迁移，其中每个模型现在都是轻量可迁移的，但等同于不合规的迁移。回到我那个不符合轻量迁移条件的例子，我们的原始模型是模型 A。我将通过引入一个新模型版本 A-prime 开始分解任务，并添加一个名为“tmpStorage”的新特性，用于临时存储从外部文件导入的数据。

接下来，我将数据从外部文件导入到我们的新特性中。导入此数据的代码与 Core Data 提供的功能是分开的。此导入的执行被插入到迁移之间。

一旦数据被安全导入，我将从 A-prime 创建另一个新版本的模型 A-double-prime。在 A-double-prime 中，我将删除旧的外部存储特性，同时重命名新特性。所描述的每个步骤都在轻量迁移的能力范围内。

直观来说，可以构建一个事件循环，使用设置了轻量迁移选项的方式打开持久化存储，并按顺序迭代处理每个未处理的模型，Core Data 将迁移该存储。如果你在迁移期间执行特定于 App 的逻辑，例如我在先前例子中从外部文件导入数据的方式，那么该逻辑必须是在迁移因进程终止而中断的情况下“可重新启动的”。

如果你的 App 使用 Core Data 和 CloudKit，在设计 Core Data 数据模型时需要记住一些要点。为了在 Core Data 存储和 CloudKit 数据库之间传递记录，它们需要对数据模型有共同的理解。你在 Core Data 模型编辑器中定义此模型。该模型随后用于生成 CloudKit 架构。生成的架构最初在 Development 环境中创建，然后提升到 Production 环境。你应该知道，CloudKit 不支持 Core Data 模型的所有功能。在设计模型时，请注意以下限制并创建一个兼容的数据模型。例如，实体上的唯一约束不受支持。Undefined 和 objectID 特性类型不支持作为特性类型。关系必须是可选值，并且需要有反向关系。此外，CloudKit 不支持 deny 删除规则。在你开发 App 时，你将使用 Development 环境。在此环境中，可以自由修改 CloudKit 架构。但是，在将架构提升到 Production 环境后，记录类型及其字段是不可变的。虽然轻量迁移处理了许多不同的场景，但 CloudKit 在其支持的内容上受到更多限制。我之前描述的许多轻量操作都不被支持。具体来说，CloudKit 支持的是向现有记录类型添加新字段以及添加新记录类型。你不能修改或删除现有的记录类型或字段。在修改模型架构时请考虑这些限制。

当需要更新数据模型时，请记住轻量迁移仅在本地存储文件中实现架构更改。无论特定存储是否与 CloudKit 一起使用，迁移只会更改磁盘上的存储，而不会对 CloudKit 架构进行更改。你仍然需要通过运行架构初始化器（schema initializer）在 Development 数据库中实现这些更改，然后使用 CloudKit 控制台将这些更改从 Development 提升到 Production。请记住，你的 App 的用户将同时使用旧版本和新版本。最新版本的 App 当然会了解架构的任何新添加。旧版本的 App 则不会知道新字段或记录类型。

由于 CloudKit 架构本质上是增量的，因此要考虑架构迁移对运行旧版本 App 的设备的影响。例如，一个常见的陷阱是忘记更新旧版本 App 使用而新版本不使用的旧字段。以下是一些迁移 CloudKit 架构的策略。第一个选项是逐步向现有记录类型添加新字段。如果采用此方法，旧版本的 App 将能够访问用户创建的每条记录，但无法访问所有字段。

第二个选项是通过包含一个版本特性来对你的实体进行版本控制，然后使用获取请求来仅选择与当前版本 App 兼容的记录。

如果采用此方法，旧版本的 App 将不会获取用户使用更新版本创建的记录，从而有效地将它们隐藏在那台设备上。最后一个策略是创建一个全新的容器，使用 `NSPersistentCloudKitContainerOptions` 将新存储与新容器关联。请注意，如果用户有大量数据集，将该数据集上传到 iCloud 可能需要较长时间。无论使用哪种方法，都要仔细设计数据模型。务必考虑跨版本兼容性问题，并一起测试不同版本的数据模型。现在我们深入讨论了数据模型、迁移和 CloudKit，我将演示实际操作。你可能已经猜到，我是一名飞行员。我创建了一个小 App 来记录我的飞行时长。以下是该 App 的数据模型。我有一个名为“LogEntry”的实体，并添加了许多特性，例如 aircraft type、flight duration、origin、destination 和 tail number，以便我记录所需的经验信息。当我第一次运行此应用程序时，Core Data 会创建存储并在该存储中实现架构。在运行应用程序之前，我将打开 `com.apple.CoreData.SQLDebug` 和 `com.apple.CoreData.MigrationDebug` 环境变量。这将导致 Core Data 记录其采取的步骤。设置好这些参数后，我将运行 App。

当 App 启动时，Core Data 会记录其采取的步骤：创建文件、创建存储元数据以及实现架构。SQLite 创建了包含我们架构的表 ZLOGENTRY。这也可以通过使用 sqlite3 命令行工具查看存储文件来确认。这里，我有 LogEntry 表，它包含与我数据模型中创建的特性相对应的列。现在我要进行一些轻量更改。

我添加了一些新实体：Aircraft、Pilot 和 Airport。这将有助于规范化架构。我将更改 LogEntry 实体中的一些特性为关系。例如，destination 和 origin 从字符串特性变为对 Airport 的对一关系。Airport 实体也有两个新特性：icaoIdentifier 和 faaIdentifier。type 特性被提升到一个新实体；我正添加两个新特性：tailNumber 和 registrationNumber。在 LogEntry 上，我创建了一个从 LogEntry 到 Aircraft 的对一关系。

最后，我添加了一个 Pilot 实体，它包含 name 和 certificate ID。

每个日志条目都将关联到一个 Pilot 实体。现在我已经完成了对数据模型的更改，我将再次运行 App。

哎呀！我运行 App 时遇到了一个错误。检查代码，它是 `NSPersistentStoreIncompatibleVersionHashError`。该错误意味着我当前的模型不再匹配存储中模型的架构。我需要迁移存储架构。我可以通过三种方式之一来做到这一点。使用第一种方法，我可以将代码转换为使用 `NSPersistentContainer`，因为轻量迁移选项会自动为我设置。使用第二种方法，我可以使用 `NSPersistentStoreDescription`，同样，轻量迁移选项会自动为我设置。最后，使用第三种方法，我可以手动在选项字典上设置轻量迁移选项，并在打开存储时将该字典传递给协调器。

我想我会选择第一个选项，使用 `NSPersistentContainer`。现在我已将代码转换为使用 `NSPersistentContainer`，我将启动 App 并再次观察 Core Data 正在迁移存储文件中的架构。

同样，这可以使用 sqlite3 命令行工具来确认。注意，新的架构是由 Core Data 使用轻量迁移自动实现的。还有什么比这更简单的呢？在结束演示之前，我想展示选项 3。回想一下，在此选项中，我手动在选项字典上设置轻量迁移选项，然后在打开存储时将该字典传递给协调器。最终结果是一样的，即存储被迁移到新架构。当你更改数据模型时，请使用轻量迁移来帮助你。对于绝大多数数据模型更改，轻量迁移非常灵活且易于使用。如果你有更复杂的数据模型，将它分解为由轻量更改组成的模型。最后，如果你将 CloudKit 与你的 App 一起使用，请仔细考虑数据模型更改的影响。彻底测试任何数据模型更改。我希望你觉得这些信息有用，并会考虑更新项目中的模型来构建一些很棒的新功能。感谢你与我一同飞行，祝你 WWDC 愉快。

---
title: Core Data 新变化
session_id: 10186
collection: wwdc2023
year: 2023
duration: '23:23'
topics: [System Services]
group: H · 持久化与文件系统
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2023/10186/'
content_hash: 'sha256:df748a8119d50774'
translated: true
---

# Core Data 新变化

<sub>WWDC2023 · 23:23 · System Services</sub>

利用 Core Data 的改进，提升 App 的数据持久化能力。了解如何使用复合特性（composite attributes）创建更直观的...

> [!note] 归档理由
> Core Data 年度更新

## 章节

- [简介](/videos/play/wwdc2023/10186/?time=0)
- [复合特性](/videos/play/wwdc2023/10186/?time=56)
- [分阶段迁移](/videos/play/wwdc2023/10186/?time=391)
- [延迟迁移](/videos/play/wwdc2023/10186/?time=1103)
- [总结](/videos/play/wwdc2023/10186/?time=1353)

## 相关资源

- [简介](https://developer.apple.com/videos/play/wwdc2023/10186/?time=0)
- [复合特性](https://developer.apple.com/videos/play/wwdc2023/10186/?time=56)
- [分阶段迁移](https://developer.apple.com/videos/play/wwdc2023/10186/?time=391)
- [延迟迁移](https://developer.apple.com/videos/play/wwdc2023/10186/?time=1103)
- [总结](https://developer.apple.com/videos/play/wwdc2023/10186/?time=1353)
- [自动迁移数据模型](https://developer.apple.com/documentation/CoreData/migrating-your-data-model-automatically)
- [Core Data](https://developer.apple.com/documentation/CoreData)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10186/4/169A3CA9-FA4A-40D0-A3A5-3635916BBCCE/downloads/wwdc2023-10186_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10186/4/169A3CA9-FA4A-40D0-A3A5-3635916BBCCE/downloads/wwdc2023-10186_sd.mp4?dl=1)
- [认识演讲者：Core Data 新变化](https://developer.apple.com/videos/play/wwdc2023/10330)
- [问答：Core Data](https://developer.apple.com/videos/play/wwdc2023/111450)
- [演化你的 Core Data 模式](https://developer.apple.com/videos/play/wwdc2022/10120)
- [添加复合特性](https://developer.apple.com/videos/play/wwdc2023/10186/?time=339)
- [设置复合特性](https://developer.apple.com/videos/play/wwdc2023/10186/?time=353)
- [获取复合特性](https://developer.apple.com/videos/play/wwdc2023/10186/?time=371)
- [为分阶段迁移创建托管对象模型引用](https://developer.apple.com/videos/play/wwdc2023/10186/?time=960)
- [为分阶段迁移创建迁移阶段](https://developer.apple.com/videos/play/wwdc2023/10186/?time=979)
- [NSCustomMigrationStage 的 willMigrationHandler 和 didMigrationHandler](https://developer.apple.com/videos/play/wwdc2023/10186/?time=1014)
- [使用 NSStagedMigrationManager 加载持久化存储](https://developer.apple.com/videos/play/wwdc2023/10186/?time=1061)
- [使用 NSPersistentStoreDeferredLightweightMigrationOptionKey 选项添加持久化存储](https://developer.apple.com/videos/play/wwdc2023/10186/?time=1261)
- [执行延迟迁移](https://developer.apple.com/videos/play/wwdc2023/10186/?time=1277)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ David：大家好，欢迎观看“Core Data 新变化”。我是 David Stites，Core Data 团队的一名工程师。在本 session 中，你将了解 Core Data 中的新技术，这些技术将帮助你更快速、更轻松地设计、查询、更新和迁移 App 中的 Core Data 数据模型。

我将首先介绍复合特性，这是一种在你的 App 模型中组织结构化数据的新方式，然后介绍如何“分阶段（stage）”进行最复杂的模型迁移，以便你可以使用轻量级迁移（lightweight migration），最后我将介绍如何延迟模型迁移以保持 App 的响应性。复合特性是一种新类型的特性。

复合特性允许在单个特性中封装复杂和自定义的数据类型。每个复合特性由你已经熟悉的内置 Core Data 类型的特性组成，例如 String、Float、Int 和 Data。

复合特性可以相互嵌套，因此顶层的复合特性可以包含额外的复合特性。

Xcode 的 Core Data 模型编辑器已经过更新，可以轻松定义和管理模型的复合特性。

复合特性是使用可转换类型特性（transformable type attribute）创建持久化自定义数据类型的一个很有吸引力的替代方案。无需编写用于转换特性值的代码。与可转换特性不同，复合特性允许 NSFetchRequest 与 NSPredicate 结合使用，这些 NSPredicate 通过复合特性的命名空间键路径进行配置。

复合特性可用于封装大量扁平化的特性，从而使代码更易于维护和阅读。

复合特性可用于提升 App 的性能。如果你的数据模型结构使得获取某个实体几乎总是需要访问另一个实体的关系，那么你可以将该关系重构为使用复合特性。在第一个实体中嵌入复合特性的效果是，它防止了跨关系产生惰值（faulting）对象。

复合特性类是 NSCompositeAttributeDescription。NSCompositeAttributeDescription 的特性类型是 NSCompositeAttributeType。

NSCompositeAttributeDescription 类包含一个数组 elements，该数组由 NSAttributeDescription 或其他嵌套的 NSCompositeAttributeDescription 组成。

elements 数组不能包含其他类型的属性描述，例如 NSRelationshipDescription。尝试设置无效的 elements 将导致 NSInvalidArgumentException。

我将通过一个演示向你介绍如何采用复合特性。

考虑这个包含 Aircraft 实体的基本数据模型。它有许多特性，包括一个 colors 特性，它是一个可转换类型。该类型的转换器存储并解析一个格式化的字符串，该字符串描述了 Aircraft 的主色、副色和第三色。

我将通过用复合特性 colorScheme 替换 colors 特性来改进这个实体，以存储 Aircraft 的涂装颜色。

colorScheme 是一个复合特性，包含 elements：primary、secondary 和 tertiary，每个 element 都是一个 String 特性。

在 Xcode 中，我将打开一个项目，这是一个我用来追踪飞行时间的 App。

该 App 的数据模型配置了刚才提到的 Aircraft 实体，以及另外几个实体。

要开始转换，在 Core Data 模型编辑器中，我将添加一个名为 colorScheme 的新复合特性。

在该复合特性中，我将添加三个字符串特性：primary、secondary 和 tertiary。

在 Aircraft 实体中，我将添加复合特性，并将该特性的类型设置为 colorScheme。

模型中的工作现已完成，是时候更新代码了。

在我的 Aircraft 实现中，我正在添加一个新属性 `@NSManaged var colorScheme`，其类型是键为 String、值为 Any 对象的 Dictionary。当我在代码中使用这个复合特性时，我使用字典表示法访问值，以特性名称作为键。在这里，我使用 String 键 primary、secondary 和 tertiary 设置 Aircraft 的 colorScheme 特性。

类似地，当我使用 NSPredicate 配置 NSFetchRequest 时，复合特性的 elements 通过命名键路径访问。这里，colorScheme.primary 用于对该特性进行过滤。

随着 App 的演化，可能需要更改数据模型。

更新数据模型需要将这些更改在底层存储模式中物化。

如果向模型添加了 numPassengers 特性，则必须更新相应的存储。

执行模式更改的过程称为迁移。

迁移后，更改将完全反映在底层存储中。

Core Data 有一个内置的迁移工具集，可帮助保持 App 的数据存储与当前数据模型同步。这些工具统称为“轻量级迁移”。要了解有关轻量级迁移的更多信息，请观看 WWDC2022 的“演化你的 Core Data 模式”。

有时，对数据模型进行的组合更改超出了轻量级迁移的能力。这个问题的解决方案是分阶段迁移（staged migration）。

分阶段迁移 API 的设计考虑了几个目标：帮助你迁移具有非合规轻量级模式更改的复杂数据模型；通过可能移除数千行与迁移和迁移基础设施相关的代码来简化你的 App；以及为你的 App 提供在迁移过程中获取执行控制以执行各种任务的机会。

要使用此 API，你需要执行以下几个步骤：确定模型的哪些更改不符合轻量级迁移支持的操作；将不符合的模型更改分解为一系列轻量级迁移支持的符合的模型更改；使用新的分阶段迁移 API 向 Core Data 描述 NSManagedObjectModel 的总顺序；然后让 Core Data 执行一个事件循环，该循环按串行顺序迭代处理每个未处理的模型并迁移存储。在迁移过程中的某些时刻，执行控制将交给你的 App，以执行与该迁移相关的任何必要任务。

要确定你的模型何时具有非合规的轻量级更改，你有几个选项。第一个选项是手动检查模式更改，并确保每个更改都符合轻量级迁移的条件。

第二个选项是尝试使用新模型和轻量级迁移选项打开持久化存储，将 NSMigratePersistentStores AutomaticallyOption 和 NSInferMappingModelAutomaticallyOption 设置为 true。如果更改不符合轻量级迁移条件，你将收到 NSPersistentStore IncompatibleVersionHashError。

最后一个选项是使用 NSMappingModel.inferredMappingModel (forSourceModel:destinationModel:)。如果 Core Data 能够创建推断的映射模型，此方法会返回该模型。否则，它返回 nil。

再次考虑 Aircraft 模型，它有一个新特性 flightData，以二进制格式存储数据。

假设需要反规范化此模型，并将所有飞行数据分离到其自己的实体类型中，同时保留任何现有数据以及它与生成它的 Aircraft 之间的关系。这是一个非常复杂的模型更改，本身不符合轻量级迁移的条件。这些更改需要分解后才能使用分阶段迁移。在分解非轻量级更改时，目标是将不符合轻量级迁移条件的迁移任务转换为一系列符合轻量级迁移条件的最小迁移。

引入的每个模型将包含一个或多个在轻量级迁移能力范围内的操作，这些操作共同构成了不符合的更改。结果是一系列迁移，其中每个模型都是可轻量级迁移的，但等价于不符合条件的迁移。

回到这个例子，我将原始模型标记为 ModelV1。此模型迁移将通过引入两个新模型版本 ModelV2 和 ModelV3 来进行分解。在 ModelV2 中，Aircraft 实体获得了一个名为 flightParameters 的关系，该关系是新建的 FlightData 实体的一个集合。FlightData 实体有一个二进制类型特性 data 和一个指向 Aircraft 的关系。为了保留现有数据，迁移阶段会将数据从 Aircraft 实体复制到新的 FlightData 实体中，并将它们关联到 Aircraft。

我们的最终模型是 ModelV3，由 ModelV2 创建。在 ModelV3 中，旧的 flightData 特性从 Aircraft 实体中删除，模型成功反规范化，并且所有现有数据都被保留下来。所描述的每个步骤都在轻量级迁移的能力范围内。

为了描述模型的总顺序，Core Data 框架级别的支持包括以下类：NSStagedMigrationManager、NSCustomMigrationStage、NSLightweightMigrationStage 和 NSManagedObjectModelReference。

NSStagedMigrationManager 类封装了你所描述的 NSCustomMigrationStage 和补充的 NSLightweightMigrationStage 的总顺序。分阶段迁移管理器还管理迁移事件循环，并通过 NSPersistentContainer 提供对正在迁移的存储的访问。该管理器使用键 NSPersistentStoreStagedMigrationManager OptionKey 添加到存储选项中。

迁移阶段构成了在模型版本之间进行迁移的基础。

当你采用分阶段迁移时，你将使用 NSCustomMigrationStage 或 NSLightweightMigrationStage 向 Core Data 描述每个模型版本。NSLightweightMigrationStage 类描述了一系列不需要分解且符合轻量级迁移条件的模型。这可能占你模型的大部分。这些轻量级迁移阶段用于补充向 Core Data 描述的模型总顺序。所有轻量级模型版本必须在一个或多个 NSLightweightMigrationStage 中表示。

你创建的每个分解的模型版本都将使用 NSCustomMigrationStage 表示，并包含一个源模型引用和一个目标模型引用。

NSCustomMigrationStage 提供了可选的处理器（handler），这些处理器会在迁移阶段之前和之后立即运行。这些处理器使你能够在迁移过程中运行自定义代码。

分阶段迁移使用了 NSManagedObjectModelReference 类。这个类代表了对 NSManagedObjectModel 的一种承诺。在迁移过程中，Core Data 会兑现这个承诺。NSManagedObjectModelReference 非常灵活，可以通过多种不同的方式创建。

每个 NSManagedObjectModelReference 都需要使用版本校验和（version checksum）进行初始化。这是为了验证模型没有被无意中更改。可以使用 NSManagedObjectModel.versionChecksum 方法获取校验和。

或者，你也可以从 Xcode 构建日志中“Compile data model”下检索版本校验和。搜索字符串“version checksum”。对于有版本控制的模型，校验和也可以在 NSManagedObjectModel bundle 的 VersionInfo.plist 中找到。

回到例子，要开始使用分阶段迁移，我将首先为三个模型分别创建模型引用。我使用的是接受模型名称和 bundle 引用的初始化器，但还有其他选项。

下一步是描述所需的迁移阶段。由于第一阶段只添加了 flightData 特性，这可以在一个轻量级阶段中表示，因为添加特性是一种轻量级更改。

然而，下一个阶段将是自定义阶段，因为模型更改被分解为两个模型版本，我们需要运行自定义代码来保留现有数据。自定义迁移阶段使用 ModelV2 和 ModelV3 进行初始化。

在 willMigrateHandler 中，代码会获取 flightData 不为 nil 的实体行。这里使用通用的 NSManagedObject 和 NSFetchRequestResult 类型，而不是 Aircraft 托管对象子类，因为 Aircraft 类在迁移过程中可能不会按预期存在。

对于每个获取到的 Aircraft 实体，数据会被复制到 FlightData 的一个新实例中，然后这两个实体被关联并持久化。在此迁移阶段执行结束时，存储模式会更新到最新模型，并且现有数据已被保留。

要完成分阶段迁移，我使用轻量级迁移阶段和自定义迁移阶段创建一个 NSStagedMigrationManager。

使用键 NSPersistentStore StagedMigrationManagerOptionKey 将 NSStagedMigrationManager 添加到 NSPersistentStoreDescription 选项中。

然后加载持久化存储以启动迁移过程并影响存储模式。就是这样。Core Data 将自动应用所需的阶段并迁移存储模式。

一些轻量级迁移需要额外的运行时，而你的 App 可能无法在前台提供这些运行时。

在轻量级迁移期间转换用户数据的过程并非瞬间完成。例如，如果迁移涉及将数据从一个列复制到另一个列，或从一个表复制到另一个表，则可能需要一些时间。这会导致糟糕的用户体验，尤其是在启动时进行迁移。

延迟迁移（Deferred migration）可以帮助你解决这个问题。此 API 允许你推迟轻量级迁移中的部分工作，并能够在以后完成这些被推迟的工作。在轻量级迁移期间，如果某个实体的迁移转换需要清理工作，例如在执行表复制后更新索引或删除列，则可以将此表转换延迟到你认为有资源可用于执行表转换时。轻量级迁移仍然是同步的，并且会正常进行。只有模式的清理工作被推迟了。你的 App 将像往常一样使用最新的模式。要选择使用延迟迁移，请将存储选项中的 NSPersistentStore DeferredLightweightMigrationOptionKey 设置为 true。

延迟迁移 API 具有运行时兼容性，可一直回溯到 macOS Big Sur 和 iOS 14。

延迟迁移仅适用于 SQLite 存储类型。

延迟迁移可能有用的示例包括：从实体中移除特性或关系；更改关系，其中实体层次结构不再存在；以及将关系从有序更改为无序。

要完成延迟迁移任务，请检查持久化存储的元数据。如果它包含键 NSPersistentStore DeferredLightweightMigrationOptionKey，这对你来说是一个信号，表明存在需要完成的延迟迁移工作。可以通过调用 NSPersistentStoreCoordinator.finishDeferredLightweightMigration 来处理延迟的迁移。

要在你的 App 中推迟任何轻量级迁移，请在将持久化存储添加到协调器时，将存储选项中的 NSPersistentStoreDeferred LightweightMigrationOptionKey 设置为 true。当是完成延迟迁移的好时机时，你可以通过检查存储的元数据来查看是否有待处理的延迟工作。如果 NSPersistentStoreDeferredLightweight MigrationOptionKey 设置为 true，则调用 finishDeferredLightweightMigration()。

要安排你的延迟迁移任务，请考虑使用后台任务 API。BGProcessingTask 适用于耗时操作，例如长时间的数据更新和 App 维护。系统将确定运行任务的最佳时间。然而，处理任务通常只在设备空闲时运行，并且会在用户开始使用设备时终止任何后台处理任务。

延迟迁移和分阶段迁移可以结合使用。如果你有一组可能需要一段时间的复杂迁移，请考虑设计能够利用这两个 API 功能的阶段。回到示例模型，在 ModelV3 中，我们移除了特性 flightData，这可能是一个很好的延迟迁移候选。

Core Data 中有三项出色的新技术。使用复合特性以可嵌套、结构化的方式封装你的自定义数据类型；通过分解模型更改，使用分阶段迁移执行复杂的模型迁移；并通过使用延迟迁移推迟部分迁移工作来提升 App 的性能。这三项技术协同工作，以改进你的 App。

我们的团队很期待听到你如何使用这些新技术。感谢观看，祝 WWDC 愉快。♪ ♪

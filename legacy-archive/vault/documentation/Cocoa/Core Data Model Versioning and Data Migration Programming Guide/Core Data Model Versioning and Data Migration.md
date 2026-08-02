---
title: Core Data 模型版本管理与数据迁移编程指南
apple_id: TP40004399
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/Introduction.html
archived_at: '2026-07-15T07:14:28.997432Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[下一页](Understanding%20Versions.md)

# Core Data 模型版本管理与数据迁移

Core Data 支持在应用程序不断演进的过程中管理托管对象模型的变更。

你只能使用创建某个 Core Data 存储时所用的托管对象模型来打开该存储。因此，更改模型会使其与之前创建的存储不兼容（从而无法打开这些存储）。如果你更改了模型，就需要将现有存储中的数据转换为新版本——这种转换存储格式的过程被称为 _迁移（migration）_。

要迁移一个存储，你需要同时拥有创建该存储时所用的模型版本，以及你想要迁移到的当前模型版本。你可以创建一个 _带版本的模型（versioned model）_，其中包含托管对象模型的多个版本。在带版本的模型中，你需要将其中一个版本标记为当前版本。这样 Core Data 就可以使用这个模型来打开使用任意一个模型版本创建的持久化存储，并将这些存储迁移到当前版本。不过，为了帮助 Core Data 完成迁移，你可能需要提供有关如何从一个模型版本映射到另一个版本的信息。这些信息既可以以带版本模型内部提示的形式存在，也可以放在你自己创建的独立映射模型文件中。

通常，随着应用程序从一个版本演进到另一个版本，许多方面都会随之改变：你实现的类、用户界面、文件格式等等。你需要了解并掌控所有这些方面；目前没有哪个 API 能一次性解决所有这些问题——例如，Cocoa 并不提供在你为托管对象模型中的实体添加新属性时自动更新用户界面的机制。Core Data 并不能解决你在发布应用程序更新过程中遇到的所有问题，但它确实为你在应用演进过程中必须完成的一小部分——但很重要且并不简单——的任务提供了支持。

- 模型版本管理让你能够指定并区分你的模式（schema）的不同配置。

  版本管理存在两种截然不同的视角：作为开发者的你的视角，以及 Core Data 的视角。这两种视角未必总是一致的。这些差异在 [理解版本](Understanding%20Versions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqmrnknltc) 中有所讨论。

  带版本的托管对象模型的格式，以及如何为模型添加版本，将在 [模型文件格式与版本](Model%20File%20Format%20and%20Versions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqmznknltc) 中讨论。
- Core Data 需要知道如何将源模型中的实体和属性映射到目标模型中的实体和属性。

  在许多情况下，Core Data 可以从托管对象模型的现有版本中推断出映射关系。这一点在 [轻量级迁移](Lightweight%20Migration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqnbnknltc) 中有所描述。

  如果你对模型所做的更改超出了 Core Data 能够推断出源到目标映射的范围，你就需要创建一个映射模型。映射模型与托管对象模型相对应，用于指定如何将源对象转换为适合目标的实例。

  如何创建映射模型将在 [映射概述](Mapping%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqnjnknltc) 中讨论。
- 数据迁移允许你使用映射，将数据从一个模型（模式）转换为另一个模型。

  迁移过程本身将在 [迁移过程](The%20Migration%20Process.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqnrnknltc) 中讨论。

  如何执行迁移将在 [启动迁移过程](Initiating%20the%20Migration%20Process.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqnznknltc) 中讨论。

  你还可以自定义迁移过程——也就是说，你可以通过编程方式判断是否需要迁移；如何找到正确的源模型、目标模型以及初始化迁移管理器所需的映射模型；以及如何执行迁移。

  只有当你想自行发起迁移时，才需要自定义迁移过程。例如，你可能出于以下目的这样做：在应用程序主 Bundle 之外的其他位置查找模型，或者通过使用不同的映射模型分多次迁移来处理大规模数据集。

  如何自定义该过程在 [自定义迁移过程](Customizing%20the%20Migration%20Process.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqobnknltc) 中有所描述。
- 如果你正在使用 iCloud，那么可执行的迁移方式会受到一些限制。

  如果你正在使用 iCloud，就必须使用轻量级迁移。其他需要注意的因素在 [迁移与 iCloud](Migration%20and%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqojnknltc) 中有所描述。

尽管 Core Data 让版本管理和迁移比通常情况下更容易实现，但这些过程实际上仍然并不简单。你仍然需要仔细考虑发布和支持应用程序不同版本所带来的影响。

本文档假设你已经熟悉 Core Data 的架构以及使用 Core Data 的基础知识。你应当能够识别 Core Data 技术栈的各个组成部分，并理解模型、托管对象上下文以及持久化存储协调器各自所扮演的角色。你还需要知道如何创建托管对象模型，以及如何以编程方式创建和操作 Core Data 技术栈中的各个部分。

如果你尚不满足这些前提条件，建议你先阅读 _[Core Data 编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_ 及相关资料。我们也强烈建议你学习 _[Core Data 实用工具教程](../Core%20Data%20Utility%20Tutorial/Introduction%20to%20Core%20Data%20Utility%20Tutorial.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbq)_。

[下一页](Understanding%20Versions.md)


---
title: Core Data 编程指南
apple_id: TP40001075
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html
archived_at: '2026-07-15T07:14:28.466481Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)



## 什么是 Core Data？

Core Data 是一个框架，你可以用它来管理应用中模型层的对象。它为对象生命周期和对象图管理（包括持久化）中常见的任务提供了通用化、自动化的解决方案。

Core Data 通常能将支持模型层所需编写的代码量减少 50% 到 70%。这主要归功于以下内置特性，你无需自己实现、测试或优化它们：

- 变更跟踪，以及在基本文本编辑之外对撤销和重做的内置管理。
- 变更传播的维护，包括维护对象之间关系的一致性。
- 对象的延迟加载、部分实体化的“未来对象”（故障，faulting），以及写时复制的数据共享，以降低开销。
- 属性值的自动验证。托管对象扩展了标准的键值编码验证方法，以确保各个值都落在可接受的范围内，从而使值的组合是合理的。
- 简化模式变更、支持高效原地模式迁移的模式迁移工具。
- 可选地与应用的控制器层集成，以支持用户界面同步。
- 在内存和用户界面中对数据进行分组、过滤和组织。
- 自动支持将对象存储到外部数据仓库中。
- 复杂的查询编译。你不必编写 SQL，而是可以通过将 NSPredicate 对象与获取请求相关联来创建复杂查询。
- 版本跟踪与乐观锁，以支持自动的多写入者冲突解决。
- 与 macOS 和 iOS 工具链的有效集成。

> [!NOTE]
> 

[Creating a Managed Object Model](KeyConcepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmzqfvjvomi)

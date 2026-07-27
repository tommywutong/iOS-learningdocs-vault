---
title: 进行更改以减少内存使用
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/making-changes-to-reduce-memory-use
source_url: 'https://developer.apple.com/documentation/xcode/making-changes-to-reduce-memory-use'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/making-changes-to-reduce-memory-use.json'
content_hash: 'sha256:33d4e48188cb7ecb'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Performance and metrics](performance-and-metrics.md) · [Reducing your app’s memory use](reducing-your-app-s-memory-use.md)

# 进行更改以减少内存使用

<sub>文章</sub>

处理内存使用过量的常见原因，以减少 App 的内存使用。

## 概述

将 App 内存使用量的增长定位到某项具体功能或操作后，你就可以进行更改以减少内存使用。下面介绍内存使用过量的常见原因，以及可以采取哪些措施来降低其影响。

### 优化图像资源

大型图像会占用大量内存，高色深图像尤其如此。请根据 App 显示图像的尺寸来优化随 App 捆绑的资源。对于从其他来源（例如网络服务或用户的照片图库）加载的图像，请将其转换为合适的缩放比例和色深。使用 [Image I/O](../imageio.md) 进行这些转换，以尽量降低对内存的影响。WWDC 2018 Session 416 [iOS Memory Deep Dive](https://developer.apple.com/videos/play/wwdc2018/416) 提供了有关选择合适 Image I/O 转换的建议。

### 减小 Core Data 事务的规模

[Core Data](../coredata.md) 会将对 [NSManagedObject](../coredata/nsmanagedobject.md) 实例（instance）的更改保存在内存中，直到保存与这些实例关联的 [NSManagedObjectContext](../coredata/nsmanagedobjectcontext.md)。保存时，它会将更改写入父 `NSManagedObjectContext` 或持久化存储（persistent store）。在更改写入持久化存储之前，它们会常驻内存，因此 App 两次保存之间的间隔越长，Core Data 的工作集（working set）就可能增长得越大。相反，App 保存得越频繁，对设备固态硬盘的写入次数就越多，这会影响性能并增加硬盘磨损。请设计 App 的持久化模型，在这两项资源约束之间取得平衡。

### 丢弃未使用的视图对象

用户锁定屏幕或 App 处于后台时，不会查看 App 的视图。在这些时候，无需将图像、视频、SceneKit 场景和其他与视图相关的对象保留在内存中。当 App 进入后台时释放与视图相关的内容，并在 App 重新进入前台时再次准备视图。有关如何让 App 为后台使用做好准备的信息，请参阅[管理 App 的生命周期](../uikit/managing-your-app-s-life-cycle.md)。

### 消除内存泄漏

当已分配的内存变得无法访问，而 App 无法释放它时，就会发生内存泄漏（memory leak）。让指向已分配内存的指针在未释放内存的情况下超出作用域，可能导致内存泄漏。App 对象图中的保留周期（retain cycle）也可能导致内存泄漏。当 App 移除对保留周期中任一对象的引用时，周期内部仍然存在强引用，对象不会被释放。

使用 [Leaks 分析模板](https://help.apple.com/instruments/mac/10.0/#/dev022f987b)检测内存泄漏。Instruments 会定期扫描 App 正在使用的内存，并报告已分配但无法访问的内存区域。Leaks instrument 会显示泄漏内存的地址和大小，并提供栈回溯，指出负责分配该内存的代码。

### 移除对未使用对象的引用

App 可能会不断积累由它分配并且可以访问、但并未使用的内存。这些未使用的内存会增加 App 的内存使用量，却不会为 App 的功能作出贡献，也不会出现在 Leaks instrument 等泄漏检测工具中。

例如，一个社交媒体 App 可能会从服务加载消息列表，并按消息标识符将消息存储在字典中。当用户滚动时间线时，App 会将更多消息加载到字典中，以便用户点按某条消息时能快速显示更多信息。如果没有从该字典清除较早消息的策略，随着用户继续滚动列表，字典可能会无限增长。

确保 App 只保留对当前用户所使用功能所必需对象的引用。丢弃旧内容，或将其写入磁盘供日后检索。例如，当用户滚动离开某些消息时，社交媒体 App 可以从字典中丢弃这些消息。

## 另请参阅

### 任务

- [收集内存使用信息](gathering-information-about-memory-use.md) — 通过测量和分析你的 App，识别内存使用效率低下的问题。
- [防止内存使用衰退](preventing-memory-use-regressions.md) — 测量 App 功能所使用的内存，并使用 XCTest 性能测试检测内存使用量的增加。
- [响应低内存警告](responding-to-low-memory-warnings.md) — 检测 App 何时使用了过多内存，并使内存使用恢复到可控范围。

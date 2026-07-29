---
title: 减小 Metal App 的内存占用空间
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/reducing-the-memory-footprint-of-metal-apps
source_url: 'https://developer.apple.com/documentation/metal/reducing-the-memory-footprint-of-metal-apps'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/reducing-the-memory-footprint-of-metal-apps.json'
content_hash: 'sha256:1b0ef459cb43e525'
translated: true
---

> 导航： [技术](../technologies.md) · [Metal](../metal.md) · [资源基础](resource-fundamentals.md)

# 减小 Metal App 的内存占用空间

<sub>文章</sub>

了解在 iOS 和 tvOS 中高效使用内存的最佳实践。

## 概述

对于 iOS 和 tvOS 中资源密集型的 Metal App 而言，高效的内存使用是一个关键考量因素。设计 App 时应使其尽可能少用内存，从而为其他 App 和系统服务释放更多可用内存。

iOS 和 tvOS 会在运行时监控你的 App 的总内存用量，如果用量超过预定的限制，系统会终止你的 App。此限制因设备型号而异，因此你应在所有支持的设备上测试你的 App。

### 优化 Metal App 中的内存使用

以下是一些了解你的 Metal App 如何使用内存的建议，以及减少内存使用的最佳实践。

**使用 Xcode 11 及更高版本测量内存消耗。** 使用 iOS 或 tvOS SDK 构建你的 App，然后使用 Xcode 内存报告在执行期间观察你的 App 的总内存占用空间（memory footprint）。有关 Xcode 内存报告的更多信息，请参阅[收集有关内存使用的信息](../xcode/gathering-information-about-memory-use.md)。

**使用这些工具来更深入地了解你的 App 的内存占用空间。**

- 获取 [Instruments](https://help.apple.com/instruments/mac/current/#//apple_ref/doc/uid/TP40004652-CH19-SW13) 跟踪记录并查看 Metal Resource Allocations Instrument，它是 Metal System Trace 模板的一部分。有关使用 Metal Resource Allocations Instrument 的更多信息，请参阅[交付优化的 Metal App 和游戏](https://developer.apple.com/videos/play/wwdc2019/606/?time=1726)。
- 使用 [Metal 调试器](../xcode/metal-debugger.md)捕获 GPU 跟踪记录，并通过内存视图查看某一帧的全部 GPU 资源的可视化表示以及每个资源的属性表格。有关内存视图的详细信息，请参阅[交付优化的 Metal App 和游戏](https://developer.apple.com/videos/play/wwdc2019/606/?time=1665)。
- 观察并对 GPU 跟踪记录摘要的内存洞察部分中高亮显示的建议采取行动。有关内存洞察的更多信息，请参阅[使用 Xcode 12 深入了解你的 Metal App](https://developer.apple.com/videos/play/wwdc2020-10605/?time=620)。
- 使用内存图工具来帮助识别泄漏和废弃内存。有关详细信息，请参阅[内存图调试](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/debugging_with_xcode/chapters/special_debugging_workflows.html#//apple_ref/doc/uid/TP40015022-CH9-DontLinkElementID_1)。
- 使用 [os_proc_available_memory](../os/os_proc_available_memory.md) API 在运行时查询你的 App 的可用内存量，以帮助你识别内存峰值。

**尽可能减小资源的尺寸。** 避免在较小的资源可用时加载大型资源。使用压缩纹理格式。在内存受限的设备上运行时加载低分辨率纹理。考虑降低 3D 模型的保真度并压缩逐顶点数据。

**简化内存密集型特效。** 某些特效（如阴影或运动模糊）需要大型离屏缓冲区（offscreen buffers）来存储临时图像数据。考虑在内存受限的设备上运行时降低这些图像缓冲区的分辨率，或减少应用的特效数量。

**避免加载未使用的资源。** Xcode 可以帮助你识别未使用的 Metal 对象。使用 Metal 调试器获取 GPU 跟踪记录。然后导航到内存视图，并选择「未使用」过滤器。

**尽可能将资源标记为易失（volatile）。** 使用 [MTLPurgeableStateVolatile](mtlpurgeablestate/volatile.md) 和 [- setPurgeableState:](<mtlresource/setpurgeablestate(__).md>) 来标记那些操作系统在低内存条件下可以安全丢弃、并且之后可由你的 App 按需重新创建或重新加载的纹理和缓冲区。这种设计意味着你的 App 在内存中会保留闲置资源的缓存，但这些资源不计入内存限制。

**对临时渲染目标使用无内存（memoryless）纹理存储。** [MTLStorageModeMemoryless](mtlstoragemode/memoryless.md) 避免了分配常规系统内存，允许 App 直接在 GPU 的 tile 内存（tile memory）中存储临时渲染目标的内容。

**使用 Metal 资源堆（MTLHeap）。** 通过使用 [MTLHeap](mtlheap.md)，你的 App 可以让多个 Metal 资源由同一内存分配支持。例如，当每帧产生和消耗的临时资源并非全部同时使用时，可以使用资源堆。那些不同时使用的资源共享同一内存，由堆支持。

### 其他资源

WWDC 视频 [使用 Xcode 12 深入了解你的 Metal App](https://developer.apple.com/videos/play/wwdc2020/10605/) 提供了有关最新内存调试工具和最佳实践的更多信息，帮助你优化 Metal App 和游戏的内存占用空间。

## 另请参阅

### 资源管理

- [设置资源存储模式](setting-resource-storage-modes.md) — 设置定义资源内存位置和访问权限的存储模式。
- [为 Apple GPU 选择资源存储模式](choosing-a-resource-storage-mode-for-apple-gpus.md) — 在 Apple GPU 上为你的纹理和缓冲区选择适当的存储模式。
- [为 Intel 和 AMD GPU 选择资源存储模式](choosing-a-resource-storage-mode-for-intel-and-amd-gpus.md) — 在 AMD 和 Intel GPU 上为你的纹理和缓冲区选择适当的存储模式。
- [将数据拷贝到私有资源](copying-data-to-a-private-resource.md) — 使用 blit 命令编码器将缓冲区或纹理数据拷贝到私有资源。
- [在 macOS 中同步托管资源](synchronizing-a-managed-resource-in-macos.md) — 在 App 中手动同步 Metal 资源的内存。
- [在连接的 GPU 之间传输数据](transferring-data-between-connected-gpus.md) — 利用 GPU 之间的高速连接快速传输数据。

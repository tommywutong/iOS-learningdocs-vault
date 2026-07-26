---
title: 减少你的 App 的电量使用
framework: xcode
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/reducing-your-app-s-battery-use
source_url: 'https://developer.apple.com/documentation/xcode/reducing-your-app-s-battery-use'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/reducing-your-app-s-battery-use.json'
content_hash: 'sha256:118144147357248c'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Performance and metrics](performance-and-metrics.md)

# 减少你的 App 的电量使用

采用设计原则和推荐的 API 来降低耗电量。

## 概述

当你的 App 执行密集计算、或使用定位和网络等设备功能时，会导致设备使用更多能量。大量的能量消耗既会降低你的 App 的性能，也会影响设备的整体使用体验。更多信息请参阅[分析你的 App 的电量使用](analyzing-your-app-s-battery-use.md)。

使用以下三阶段流程来减少你的 App 的能耗：

1. 减少工作量。
2. 提高工作效率。
3. 避免误用 API。

以下各节介绍每个阶段应采取的方法。

### 减少总体计算量

考虑你的 App 能否降低状态更新的频率。寻找彻底移除某些活动的机会，让你的 App 避免使用其实并不需要的设备子系统来消耗能量。

如果你的 App 持续执行高耗能操作（例如请求设备的位置信息），请改为仅在有人主动请求时才执行此操作。将 App 对定位服务的使用限制在有人明确请求的时刻，也能让人们更容易理解你的 App 的隐私影响，因为他们可以理解自己的意图与 App 使用其数据方式之间的关系。更多信息请参阅《人机界面指南》中的[基础 \> 隐私](https://developer.apple.com/design/human-interface-guidelines/privacy)。

### 提高 App 中任务的能效

优先使用针对硬件高效利用做过优化的高层级框架，而不是直接、难以高效使用的底层硬件访问方式。遵循具体框架文档中的指导，以高效方式使用它们。

### 高效使用 API

遵循最佳实践建议，以节能的方式使用 API。以下文章针对特定技术，提供了降低能耗的指导。

## 主题

### 基础

- [高效地调度 CPU 工作](scheduling-cpu-work-efficiently.md) — 使用并发编程并调整后台活动的优先级，以提升 App 的性能。
- [响应电源通知](responding-to-power-notifications.md) — 采用更节能的策略，延长设备的电池续航时间。

### 图形和声音

- [提升你的 App 的渲染效率](improving-your-app-s-rendering-efficiency.md) — 通过尽量减少不必要的重绘并使用高效的更新策略来优化视图更新。
- [降低采集媒体时的功耗](reducing-power-usage-when-capturing-media.md) — 通过在不需要时停止会话并选择合适的视频格式来优化设备摄像头的功耗。

### 网络和定位

- [降低网络和蓝牙功耗](reducing-networking-and-bluetooth-power-usage.md) — 有策略地调度请求，并尽量减少后台网络活动，以降低 App 的能耗。
- [高效访问设备的位置信息](accessing-the-device-s-location-efficiently.md) — 使用 Core Location 功能来管理能耗、接收更新，并尽量降低位置更新的频率。

### 存储

- [减少磁盘写入](reducing-disk-writes.md) — 通过优化 App 向永久性存储写入数据的方式，提升 App 的响应速度。

## 另请参阅

### 电源

- [分析你的 App 的电量使用](analyzing-your-app-s-battery-use.md) — 通过降低你的 App 的功耗，增加 App 在单次电池充电下的可用时长。
- [使用 Power Profiler 测量你的 App 的功耗](measuring-your-app-s-power-use-with-power-profiler.md) — 无论设备是否连接到 Xcode，都能分析你的 App 对功耗的影响。

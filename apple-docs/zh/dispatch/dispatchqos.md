---
title: DispatchQoS
framework: Dispatch
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqos
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqos'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqos.json'
content_hash: 'sha256:5b840256a0818af6'
translated: true
---

> 导航：[技术](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchQoS

<sub>结构体</sub>

要应用于任务的服务质量，也就是执行优先级。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DispatchQoS
```

## 概述

服务质量（QoS）类别将对 [DispatchQueue](dispatchqueue.md) 上执行的工作进行分类。通过指定任务的服务质量，你可以表明该任务在你的 App 中的重要性。在调度任务时，系统会优先处理服务类别更高的那些任务。

由于优先级更高的工作执行速度更快、占用的资源也更多，因此它通常比优先级更低的工作消耗更多能量。为你 App 执行的工作精确指定合适的 QoS 类别，可以确保你的 App 既响应迅速又节能高效。

## 关系

- **遵循**：[Equatable](../swift/equatable.md)、[Sendable](../swift/sendable.md)、[SendableMetatype](../swift/sendablemetatype.md)

## 主题

### 获取预定义的 QoS 对象

- [userInteractive](dispatchqos/userinteractive.md) — 用于用户交互任务的服务质量类别，例如动画、事件处理或 App 用户界面的更新。
- [userInitiated](dispatchqos/userinitiated.md) — 用于阻止用户主动使用你的 App 的任务的服务质量类别。
- [default](dispatchqos/default.md) — 默认的服务质量类别。
- [utility](dispatchqos/utility.md) — 用于用户不主动跟踪的任务的服务质量类别。
- [background](dispatchqos/background.md) — 用于你创建的维护或清理任务的服务质量类别。
- [unspecified](dispatchqos/unspecified.md) — 未指定服务质量类别。

### 创建 QoS 结构体

- [init(qosClass:relativePriority:)](<dispatchqos/init(qosclass_relativepriority_).md>) — 使用指定的 QoS 类别和相对优先级创建一个新的 `DispatchQoS` 对象。
- [QoSClass](dispatchqos/qosclass-swift.enum.md) — 服务质量类别，用于指定执行任务的优先级。

### 获取 QoS 特性

- [qosClass](dispatchqos/qosclass-swift.property.md) — 服务质量类别。
- [relativePriority](dispatchqos/relativepriority.md) — 某个服务质量相对于同类别中其他服务质量的优先级。

---
title: OSSignpostType
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/os/ossignposttype
source_url: 'https://developer.apple.com/documentation/os/ossignposttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposttype.json'
content_hash: 'sha256:bea2f5e3458a98bf'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OSSignpostType

<sub>结构体</sub>

signpost 的各种类型。

> [!warning] 已废弃
> 请改用 [OSSignposter](ossignposter.md)。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct OSSignpostType
```

## 关系

- **遵循**： [BitwiseCopyable](../swift/bitwisecopyable.md)、[Equatable](../swift/equatable.md)、[Hashable](../swift/hashable.md)、[RawRepresentable](../swift/rawrepresentable.md)、[Sendable](../swift/sendable.md)

## 主题

### 指定 Signpost 类型

- [begin](ossignposttype/begin.md) — 标记代码中感兴趣的时间区间起点的 signpost。
- [end](ossignposttype/end.md) — 标记代码中感兴趣的时间区间终点的 signpost。
- [event](ossignposttype/event.md) — 标记代码中某个事件的 signpost。

### 创建 Signpost 类型

- [init(rawValue:)](<ossignposttype/init(rawvalue_).md>) — 根据原始整数值创建 signpost。
- [init(_:)](<ossignposttype/init(__).md>) — 根据原始整数值创建 signpost。

### 检查 Signpost 类型

- [rawValue](ossignposttype/rawvalue.md) — 表示 signpost 角色的整数值。

## 另请参阅

### 测量事件

- [Recording Performance Data](recording-performance-data.md) — 添加 signpost 来记录感兴趣的、基于时间的事件。
- [OSSignposter](ossignposter.md) — 用于借助统一日志系统测量任务性能的对象。
- [Legacy Signpost Symbols](legacy-signpost-symbols.md) — 把你的代码从这些遗留符号迁移出来。
- [os_signpost_id_t](os_signpost_id_t.md) — 用于区分名称和目标日志相同的多个 signpost 的标识符。

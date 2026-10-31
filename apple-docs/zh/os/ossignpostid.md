---
title: OSSignpostID
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/ossignpostid
source_url: 'https://developer.apple.com/documentation/os/ossignpostid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostid.json'
content_hash: 'sha256:f00bee167b4e9bf3'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OSSignpostID

<sub>结构体</sub>

用于区分带 signpost 标记的时间区间的标识符。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct OSSignpostID
```

## 概述

名称、子系统和分类均匹配，且处于同一作用域的多个时间区间可以同时进行。为了匹配一对时间区间调用，你需要用唯一的 signpost 标识符来标识每个时间区间。请采用下列策略中第一条符合你用例的做法：

- 如果相同的时间区间绝不会重叠，请使用 [exclusive](ossignpostid/exclusive.md) signpost ID。
- 如果你有可唯一标识所测量任务每个实例的数据，请使用 [init(_:)](<ossignpostid/init(__).md>) 方法创建 signpost ID。你提供的值不得与任一系统定义的 signpost ID 相同。
- 如果你有可唯一标识一对时间区间调用的对象（例如你正在测量的对象），请使用 [makeSignpostID(from:)](<ossignposter/makesignpostid(from_).md>) 方法创建 signpost ID。不要将此方法用于跨越进程边界的 signpost。
- 否则，请使用 [makeSignpostID()](<ossignposter/makesignpostid().md>) 方法创建 signpost ID。

## 关系

- **遵循**： [Comparable](../swift/comparable.md)、[Equatable](../swift/equatable.md)、[Sendable](../swift/sendable.md)、[SendableMetatype](../swift/sendablemetatype.md)

## 主题

### 获取 Signpost 标识符

- [exclusive](ossignpostid/exclusive.md) — 一个表示不同 signpost 时间区间互不重叠的 signpost 标识符。
- [invalid](ossignpostid/invalid.md) — 表示出错的 signpost 标识符。
- [null](ossignpostid/null.md) — 表示已禁用 signpost 的 signpost 标识符。

### 创建 Signpost 标识符

- [init(_:)](<ossignpostid/init(__).md>) — 用任意 64 位整数值创建 signpost ID。
- [init(log:)](<ossignpostid/init(log_).md>) — 为指定日志创建 signpost ID。 _(已废弃)_
- [init(log:object:)](<ossignpostid/init(log_object_).md>) — 创建一个 signpost ID，并将其与指定对象关联。 _(已废弃)_

### 获取标识符的原始值

- [rawValue](ossignpostid/rawvalue.md) — 该 signpost ID 的原始值。

## 另请参阅

### 生成 Signpost ID

- [makeSignpostID()](<ossignposter/makesignpostid().md>) — 返回在该 signposter 作用域内唯一的标识符。
- [makeSignpostID(from:)](<ossignposter/makesignpostid(from_).md>) — 返回由该 signposter 从指定对象派生的标识符。

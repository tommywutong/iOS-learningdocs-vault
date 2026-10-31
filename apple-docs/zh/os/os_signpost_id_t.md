---
title: os_signpost_id_t
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_signpost_id_t
source_url: 'https://developer.apple.com/documentation/os/os_signpost_id_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_signpost_id_t.json'
content_hash: 'sha256:acd6cb9dafd5d452'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_signpost_id_t

<sub>类型别名</sub>

用于区分名称和目标日志相同的多个 signpost 的标识符。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias os_signpost_id_t = UInt64
```

## 讨论

日志对象和区间名称均匹配的多个区间可以同时进行。为了让数据处理工具正确匹配区间的开始与结束，你需要用唯一的 signpost 标识符来标识每个区间。请采用下列策略中第一条符合你用例的做法：

- 如果你能保证具有相同日志和名称的区间在时间上绝不会重叠，请将 [OS_SIGNPOST_ID_EXCLUSIVE](os_signpost_id_exclusive.md) 指定为 signpost ID。
- 如果你已经有可唯一标识所测量任务每个实例的整数数据，请将该数据从 [uint64_t](../kernel/uint64_t.md) 值直接转换为 `os_signpost_id_t`。该值不得与任一预定义的 signpost 值相同。
- 如果你有可唯一标识 begin/end 配对的指针（例如指向被测量代码所用数据对象的指针），请调用 [os_signpost_id_make_with_pointer](os_signpost_id_make_with_pointer.md)。不要将此函数用于跨越进程边界的 signpost。
- 否则，请在每次创建新的一对 signpost 时调用 [os_signpost_id_generate](os_signpost_id_generate.md)，为该配对生成唯一值。

## 另请参阅

### 测量事件

- [Recording Performance Data](recording-performance-data.md) — 添加 signpost 来记录感兴趣的、基于时间的事件。
- [OSSignposter](ossignposter.md) — 用于借助统一日志系统测量任务性能的对象。
- [Legacy Signpost Symbols](legacy-signpost-symbols.md) — 把你的代码从这些遗留符号迁移出来。
- [OSSignpostType](ossignposttype.md) — signpost 的各种类型。 _(已废弃)_

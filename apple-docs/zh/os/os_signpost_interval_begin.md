---
title: os_signpost_interval_begin
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_signpost_interval_begin
source_url: 'https://developer.apple.com/documentation/os/os_signpost_interval_begin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_signpost_interval_begin.json'
content_hash: 'sha256:9efba5c46ab0d87c'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_signpost_interval_begin

<sub>宏</sub>

使用 signpost 标记代码中某个时间区间的开始。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_signpost_interval_begin(log, interval_id, name, ...)
```

## 参数

- `log` — 用于将 signpost 记录到其中的日志对象。

- `interval_id` — 用于区分同名 signpost 的 signpost 标识符。

- `name` — signpost 的名称。

- `…` — 可选。若指定，请提供格式字符串，后跟字符串中按出现顺序排列的相应数量的参数。

## 讨论

调用此函数等价于以类型 [OS_SIGNPOST_INTERVAL_BEGIN](os_signpost_type_t/os_signpost_interval_begin.md) 调用 [os_signpost_emit_with_type](os_signpost_emit_with_type.md)。

## 另请参阅

### 测量事件

- [Recording Performance Data](recording-performance-data.md) — 添加 signpost 来记录感兴趣的、基于时间的事件。
- [Legacy Signpost Symbols](legacy-signpost-symbols.md) — 把你的代码从这些遗留符号迁移出来。
- [os_signpost_emit_with_type](os_signpost_emit_with_type.md) — 把代码中的某个关注点记录为一个时间区间，或者记录为一个用于在 Instruments 中调试性能的事件。
- [OSSignpostType](ossignposttype.md) — signpost 的各种类型。 _(已废弃)_
- [os_signpost_interval_end](os_signpost_interval_end.md) — 使用 signpost 标记代码中某个时间区间的结束。
- [os_signpost_event_emit](os_signpost_event_emit.md) — 标记时间上的一个关注点。
- [os_signpost_id_t](os_signpost_id_t.md) — 用于区分名称和目标日志相同的多个 signpost 的标识符。

---
title: os_signpost_event_emit
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_signpost_event_emit
source_url: 'https://developer.apple.com/documentation/os/os_signpost_event_emit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_signpost_event_emit.json'
content_hash: 'sha256:9481baad0327352a'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_signpost_event_emit

<sub>宏</sub>

标记时间上的某个关注点。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_signpost_event_emit(log, event_id, name, ...)
```

## 参数

- `log` — 提供要使用的子系统和分类的日志。更多信息参见 [os_log_create](os_log_create.md)。

- `event_id` — 事件的标识符。

- `name` — 事件的名称。

- `…` — 可选的格式字符串。若提供该字符串，必须在其后按字符串中出现的顺序跟上所有必需的参数。

## 讨论

此函数等效于调用 [os_signpost_emit_with_type](os_signpost_emit_with_type.md)，并将类型指定为 [OS_SIGNPOST_EVENT](os_signpost_type_t/os_signpost_event.md)。

## 另请参阅

### 测量事件

- [Recording Performance Data](recording-performance-data.md) — 添加 signpost 来记录感兴趣的、基于时间的事件。
- [Legacy Signpost Symbols](legacy-signpost-symbols.md) — 把你的代码从这些遗留符号迁移出来。
- [os_signpost_emit_with_type](os_signpost_emit_with_type.md) — 把代码中的某个关注点记录为一个时间区间，或者记录为一个用于在 Instruments 中调试性能的事件。
- [OSSignpostType](ossignposttype.md) — signpost 的各种类型。 _(已废弃)_
- [os_signpost_interval_begin](os_signpost_interval_begin.md) — 使用 signpost 标记代码中某个时间区间的开始。
- [os_signpost_interval_end](os_signpost_interval_end.md) — 使用 signpost 标记代码中某个时间区间的结束。
- [os_signpost_id_t](os_signpost_id_t.md) — 用于区分名称和目标日志相同的多个 signpost 的标识符。

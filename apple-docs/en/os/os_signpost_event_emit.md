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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_signpost_event_emit

<sub>Macro</sub>

Marks a point of interest in time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_signpost_event_emit(log, event_id, name, ...)
```

## Parameters

- `log` — The log that provides the subsystem and category to use. For more information, see [os_log_create](os_log_create.md).

- `event_id` — The event’s identifier.

- `name` — The event’s name.

- `…` — An optional format string. If you provide the string, you must follow it with any required arguments in the order that they appear in the string.

## Discussion

This function is equivalent to calling [os_signpost_emit_with_type](os_signpost_emit_with_type.md) with a type of [OS_SIGNPOST_EVENT](os_signpost_type_t/os_signpost_event.md).

## See Also

### Measure Events

- [Recording Performance Data](recording-performance-data.md) — Add signposts to record interesting time-based events.
- [Legacy Signpost Symbols](legacy-signpost-symbols.md) — Migrate your code away from using these legacy symbols.
- [os_signpost_emit_with_type](os_signpost_emit_with_type.md) — Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments.
- [OSSignpostType](ossignposttype.md) — The different kinds of signpost. _(deprecated)_
- [os_signpost_interval_begin](os_signpost_interval_begin.md) — Marks the start of a time interval in your code using a signpost.
- [os_signpost_interval_end](os_signpost_interval_end.md) — Marks the end of a time interval in your code using a signpost.
- [os_signpost_id_t](os_signpost_id_t.md) — An identifier you use to distinguish between signposts that have the same name and destination log.

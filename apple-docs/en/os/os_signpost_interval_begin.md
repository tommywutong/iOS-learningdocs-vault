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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_signpost_interval_begin

<sub>Macro</sub>

Marks the start of a time interval in your code using a signpost.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_signpost_interval_begin(log, interval_id, name, ...)
```

## Parameters

- `log` — A log object to log the signpost to.

- `interval_id` — A signpost identifier used to disambiguate between signposts with the same name.

- `name` — The name of the signpost.

- `…` — Optional. If specified, provide a format string, followed by the expected number of arguments in the order that they appear in the string.

## Discussion

Calling this function is equivalent to calling [os_signpost_emit_with_type](os_signpost_emit_with_type.md) with a type of [OS_SIGNPOST_INTERVAL_BEGIN](os_signpost_type_t/os_signpost_interval_begin.md).

## See Also

### Measure Events

- [Recording Performance Data](recording-performance-data.md) — Add signposts to record interesting time-based events.
- [Legacy Signpost Symbols](legacy-signpost-symbols.md) — Migrate your code away from using these legacy symbols.
- [os_signpost_emit_with_type](os_signpost_emit_with_type.md) — Logs a point of interest in your code as a time interval or as an event for debugging performance in Instruments.
- [OSSignpostType](ossignposttype.md) — The different kinds of signpost. _(deprecated)_
- [os_signpost_interval_end](os_signpost_interval_end.md) — Marks the end of a time interval in your code using a signpost.
- [os_signpost_event_emit](os_signpost_event_emit.md) — Marks a point of interest in time.
- [os_signpost_id_t](os_signpost_id_t.md) — An identifier you use to distinguish between signposts that have the same name and destination log.

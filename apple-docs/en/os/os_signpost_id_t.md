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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_signpost_id_t

<sub>Type Alias</sub>

An identifier you use to distinguish between signposts that have the same name and destination log.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias os_signpost_id_t = UInt64
```

## Discussion

Multiple intervals with matching log objects and interval names can be in-flight simultaneously. In order for data-processing tools to correctly match the beginning and end of an interval, you need to identify each interval with a unique signpost identifier. Use the first strategy in the list below that matches your use case:

- If you can guarantee that intervals with the same log and name can never overlap in time, specify [OS_SIGNPOST_ID_EXCLUSIVE](os_signpost_id_exclusive.md) as the signpost ID.
- If you already have your own integer data that can uniquely identify each instance of the task being measured, cast the data from a [uint64_t](../kernel/uint64_t.md) value directly to a `os_signpost_id_t`. The value must not match one of the predefined signpost values.
- If you have a pointer that can uniquely identify begin/end pairs (such as a pointer to a data object used by the code being measured), call [os_signpost_id_make_with_pointer](os_signpost_id_make_with_pointer.md). Don’t use this function for signposts that span process boundaries.
- Otherwise, call [os_signpost_id_generate](os_signpost_id_generate.md) each time you create a new pair of signposts to generate a unique value for that pair.

## See Also

### Measure Events

- [Recording Performance Data](recording-performance-data.md) — Add signposts to record interesting time-based events.
- [OSSignposter](ossignposter.md) — An object for measuring task performance using the unified logging system.
- [Legacy Signpost Symbols](legacy-signpost-symbols.md) — Migrate your code away from using these legacy symbols.
- [OSSignpostType](ossignposttype.md) — The different kinds of signpost. _(deprecated)_

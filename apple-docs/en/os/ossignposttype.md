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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# OSSignpostType

<sub>Structure</sub>

The different kinds of signpost.

> [!warning] Deprecated
> Use [OSSignposter](ossignposter.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct OSSignpostType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md)

## Topics

### Specifying Signpost Types

- [begin](ossignposttype/begin.md) — A signpost that marks the start of a time interval of interest in your code.
- [end](ossignposttype/end.md) — A signpost that marks the end of a time interval of interest in your code.
- [event](ossignposttype/event.md) — A signpost that marks an event in your code.

### Creating Signpost Types

- [init(rawValue:)](<ossignposttype/init(rawvalue_).md>) — Creates a signpost from a raw integer value.
- [init(_:)](<ossignposttype/init(__).md>) — Creates a signpost from a raw integer value.

### Inspecting Signpost Types

- [rawValue](ossignposttype/rawvalue.md) — An integer value that represents the role of a signpost.

## See Also

### Measure Events

- [Recording Performance Data](recording-performance-data.md) — Add signposts to record interesting time-based events.
- [OSSignposter](ossignposter.md) — An object for measuring task performance using the unified logging system.
- [Legacy Signpost Symbols](legacy-signpost-symbols.md) — Migrate your code away from using these legacy symbols.
- [os_signpost_id_t](os_signpost_id_t.md) — An identifier you use to distinguish between signposts that have the same name and destination log.

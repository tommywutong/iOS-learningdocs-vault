---
title: DispatchSource.MemoryPressureEvent
framework: Dispatch
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsource/memorypressureevent
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/memorypressureevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/memorypressureevent.json'
content_hash: 'sha256:4a821b2b6ea7f824'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSource](../dispatchsource.md)

# DispatchSource.MemoryPressureEvent

<sub>Structure</sub>

Memory pressure events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MemoryPressureEvent
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Memory Pressure Event Flags

- [all](memorypressureevent/all.md) — All memory pressure events.
- [normal](memorypressureevent/normal.md) — An event indicating that the system memory pressure condition changed to normal.
- [warning](memorypressureevent/warning.md) — An event indicating that the system memory pressure condition changed to warning.
- [critical](memorypressureevent/critical.md) — An event indicating that the system memory pressure condition changed to critical.

## See Also

### Creating a Memory Pressure Source

- [makeMemoryPressureSource(eventMask:queue:)](<makememorypressuresource(eventmask_queue_).md>) — Creates a new dispatch source object that monitors the system for changes in the memory pressure condition.
- [DispatchSourceMemoryPressure](../dispatchsourcememorypressure.md) — A dispatch source that monitors the system for changes in the memory pressure condition.

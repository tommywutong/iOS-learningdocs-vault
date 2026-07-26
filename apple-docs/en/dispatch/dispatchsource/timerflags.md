---
title: DispatchSource.TimerFlags
framework: Dispatch
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsource/timerflags
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsource/timerflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsource/timerflags.json'
content_hash: 'sha256:d7493147e4e698b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSource](../dispatchsource.md)

# DispatchSource.TimerFlags

<sub>Structure</sub>

Flags to use when configuring a timer dispatch source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TimerFlags
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Timer Flags

- [strict](timerflags/strict.md) — The system makes its best effort to observe the timer’s specified leeway value, even if the value is smaller than the default leeway.

## See Also

### Creating a Timer Source

- [makeTimerSource(flags:queue:)](<maketimersource(flags_queue_).md>) — Creates a new dispatch source object for monitoring timer events.
- [DispatchSourceTimer](../dispatchsourcetimer.md) — A dispatch source that submits the event handler block based on a timer.

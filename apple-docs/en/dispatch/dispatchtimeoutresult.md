---
title: DispatchTimeoutResult
framework: Dispatch
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchtimeoutresult
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchtimeoutresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchtimeoutresult.json'
content_hash: 'sha256:4a0f813020375906'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchTimeoutResult

<sub>Enumeration</sub>

A result value indicating whether a dispatch operation finished before a specified time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum DispatchTimeoutResult
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [DispatchTimeoutResult.success](dispatchtimeoutresult/success.md) — Indicates that a dispatch operation successfully finished before the specified time elapsed.
- [DispatchTimeoutResult.timedOut](dispatchtimeoutresult/timedout.md) — Indicates that a dispatch operation failed to finish before the specified time elapsed.

## See Also

### Time Constructs

- [DispatchTime](dispatchtime.md) — A point in time relative to the default clock, with nanosecond precision.
- [DispatchWallTime](dispatchwalltime.md) — An absolute point in time according to the wall clock, with microsecond precision.
- [DispatchTimeInterval](dispatchtimeinterval.md) — A number of seconds, millisconds, microseconds, or nanoseconds.
- [dispatch_time_t](dispatch_time_t.md) — An abstract representation of time.
- [DISPATCH_WALLTIME_NOW](dispatch_walltime_now.md) — The current time.
- [Wall Time Constants](2963138-wall-time-constants.md) — Constants for wall time values.

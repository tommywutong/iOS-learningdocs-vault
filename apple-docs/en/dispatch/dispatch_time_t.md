---
title: dispatch_time_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_time_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_time_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_time_t.json'
content_hash: 'sha256:97b5c240391189e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_time_t

<sub>Type Alias</sub>

An abstract representation of time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias dispatch_time_t = UInt64
```

## Topics

### Well-Defined Times

- [DISPATCH_TIME_NOW](dispatch_time_now.md)
- [DISPATCH_TIME_FOREVER](dispatch_time_forever.md)

### Time Multiplier Constants

- [USEC_PER_SEC](usec_per_sec.md)
- [NSEC_PER_SEC](nsec_per_sec.md)
- [NSEC_PER_MSEC](nsec_per_msec.md)
- [NSEC_PER_USEC](nsec_per_usec.md)

## See Also

### Time Constructs

- [DispatchTime](dispatchtime.md) — A point in time relative to the default clock, with nanosecond precision.
- [DispatchWallTime](dispatchwalltime.md) — An absolute point in time according to the wall clock, with microsecond precision.
- [DispatchTimeInterval](dispatchtimeinterval.md) — A number of seconds, millisconds, microseconds, or nanoseconds.
- [DispatchTimeoutResult](dispatchtimeoutresult.md) — A result value indicating whether a dispatch operation finished before a specified time.
- [DISPATCH_WALLTIME_NOW](dispatch_walltime_now.md) — The current time.
- [Wall Time Constants](2963138-wall-time-constants.md) — Constants for wall time values.

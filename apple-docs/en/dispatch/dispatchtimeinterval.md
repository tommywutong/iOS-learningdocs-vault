---
title: DispatchTimeInterval
framework: Dispatch
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchtimeinterval
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchtimeinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchtimeinterval.json'
content_hash: 'sha256:1209d5f50e626985'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchTimeInterval

<sub>Enumeration</sub>

A number of seconds, millisconds, microseconds, or nanoseconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum DispatchTimeInterval
```

## Overview

Use [DispatchTimeInterval](dispatchtimeinterval.md) values to specify the interval at which a [DispatchSourceTimer](dispatchsourcetimer.md) fires or I/O handlers are invoked for a [DispatchIO](dispatchio.md) channel, as well as to increment and decrement [DispatchTime](dispatchtime.md) values.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [DispatchTimeInterval.seconds(_:)](<dispatchtimeinterval/seconds(__).md>) — A number of seconds.
- [DispatchTimeInterval.milliseconds(_:)](<dispatchtimeinterval/milliseconds(__).md>) — A number of milliseconds.
- [DispatchTimeInterval.microseconds(_:)](<dispatchtimeinterval/microseconds(__).md>) — A number of microseconds.
- [DispatchTimeInterval.nanoseconds(_:)](<dispatchtimeinterval/nanoseconds(__).md>) — A number of nanoseconds.
- [DispatchTimeInterval.never](dispatchtimeinterval/never.md) — No interval.

## See Also

### Time Constructs

- [DispatchTime](dispatchtime.md) — A point in time relative to the default clock, with nanosecond precision.
- [DispatchWallTime](dispatchwalltime.md) — An absolute point in time according to the wall clock, with microsecond precision.
- [DispatchTimeoutResult](dispatchtimeoutresult.md) — A result value indicating whether a dispatch operation finished before a specified time.
- [dispatch_time_t](dispatch_time_t.md) — An abstract representation of time.
- [DISPATCH_WALLTIME_NOW](dispatch_walltime_now.md) — The current time.
- [Wall Time Constants](2963138-wall-time-constants.md) — Constants for wall time values.

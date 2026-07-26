---
title: DispatchTime
framework: Dispatch
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchtime
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchtime.json'
content_hash: 'sha256:f28b9d2a44d9d16f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchTime

<sub>Structure</sub>

A point in time relative to the default clock, with nanosecond precision.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DispatchTime
```

## Overview

On Apple platforms, the default clock is based on the Mach absolute time unit.

## Relationships

- **Conforms To**: [Comparable](../swift/comparable.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting Well-Known Times

- [now()](<dispatchtime/now().md>) — Returns the current time.
- [distantFuture](dispatchtime/distantfuture.md) — A time in the distant future.

### Creating a Dispatch Time Object

- [init(uptimeNanoseconds:)](<dispatchtime/init(uptimenanoseconds_).md>) — Creates a time relative to the amount of time the system has been running.

### Getting the Time

- [rawValue](dispatchtime/rawvalue.md) — Returns the underlying time value.
- [uptimeNanoseconds](dispatchtime/uptimenanoseconds.md) — Returns the number of nanoseconds since boot, excluding any time the system spent asleep.

### Modifying the Value

- [advanced(by:)](<dispatchtime/advanced(by_).md>)
- [distance(to:)](<dispatchtime/distance(to_).md>)

### Operator Functions

- [+(_:_:)](<+(____)-6fmcc.md>)
- [+(_:_:)](<+(____)-2dcrq.md>)
- [-(_:_:)](<-(____)-5l4yh.md>)
- [-(_:_:)](<-(____)-8usj3.md>)

## See Also

### Time Constructs

- [DispatchWallTime](dispatchwalltime.md) — An absolute point in time according to the wall clock, with microsecond precision.
- [DispatchTimeInterval](dispatchtimeinterval.md) — A number of seconds, millisconds, microseconds, or nanoseconds.
- [DispatchTimeoutResult](dispatchtimeoutresult.md) — A result value indicating whether a dispatch operation finished before a specified time.
- [dispatch_time_t](dispatch_time_t.md) — An abstract representation of time.
- [DISPATCH_WALLTIME_NOW](dispatch_walltime_now.md) — The current time.
- [Wall Time Constants](2963138-wall-time-constants.md) — Constants for wall time values.

---
title: DispatchWallTime
framework: Dispatch
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchwalltime
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchwalltime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchwalltime.json'
content_hash: 'sha256:0225472d5dc48cb9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchWallTime

<sub>Structure</sub>

An absolute point in time according to the wall clock, with microsecond precision.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DispatchWallTime
```

## Relationships

- **Conforms To**: [Comparable](../swift/comparable.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting Well-Known Times

- [now()](<dispatchwalltime/now().md>) — Returns the current time.
- [distantFuture](dispatchwalltime/distantfuture.md) — A time in the distant future.

### Creating a Dispatch Wall Time Object

- [init(timespec:)](<dispatchwalltime/init(timespec_).md>) — Creates an absolute time for a specified value.

### Getting the Time

- [rawValue](dispatchwalltime/rawvalue.md) — The underlying time value.

### Operator Functions

- [+(_:_:)](<+(____)-8ylhk.md>)
- [+(_:_:)](<+(____)-8pe6k.md>)
- [-(_:_:)](<-(____)-6jk71.md>)
- [-(_:_:)](<-(____)-50bxr.md>)

## See Also

### Time Constructs

- [DispatchTime](dispatchtime.md) — A point in time relative to the default clock, with nanosecond precision.
- [DispatchTimeInterval](dispatchtimeinterval.md) — A number of seconds, millisconds, microseconds, or nanoseconds.
- [DispatchTimeoutResult](dispatchtimeoutresult.md) — A result value indicating whether a dispatch operation finished before a specified time.
- [dispatch_time_t](dispatch_time_t.md) — An abstract representation of time.
- [DISPATCH_WALLTIME_NOW](dispatch_walltime_now.md) — The current time.
- [Wall Time Constants](2963138-wall-time-constants.md) — Constants for wall time values.

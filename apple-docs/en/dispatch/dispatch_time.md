---
title: dispatch_time
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_time
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_time'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_time.json'
content_hash: 'sha256:8a6d42604a1249b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_time

<sub>Function</sub>

Creates a `dispatch_time_t` relative to the default clock or modifies an existing `dispatch_time_t`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern dispatch_time_t dispatch_time(dispatch_time_t when, int64_t delta);
```

## Parameters

- `when` — The [dispatch_function_t](dispatch_function_t.md) value to use as the basis for a new value. Pass [DISPATCH_TIME_NOW](dispatch_time_now.md) to create a new time value relative to now.

- `delta` — The number of nanoseconds to add to the time in the `when` parameter.

## Return Value

A new [dispatch_time_t](dispatch_time_t.md).

## Discussion

The default clock is based on [mach_absolute_time](../kernel/1462446-mach_absolute_time.md).

## See Also

### Time Constructs

- [dispatch_walltime](dispatch_walltime.md) — Creates a `dispatch_time_t` using an absolute time according to the wall clock.
- [dispatch_time_t](dispatch_time_t.md) — An abstract representation of time.
- [DISPATCH_WALLTIME_NOW](dispatch_walltime_now.md) — The current time.
- [Wall Time Constants](2963138-wall-time-constants.md) — Constants for wall time values.

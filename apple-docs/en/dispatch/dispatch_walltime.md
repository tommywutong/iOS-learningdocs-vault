---
title: dispatch_walltime
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_walltime
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_walltime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_walltime.json'
content_hash: 'sha256:7c26ea791ed37d42'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_walltime

<sub>Function</sub>

Creates a `dispatch_time_t` using an absolute time according to the wall clock.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern dispatch_time_t dispatch_walltime(const struct timespec *when, int64_t delta);
```

## Parameters

- `when` — A `struct timespec` to add time to. If `NULL` is passed, then this function uses the result of `gettimeofday`.

- `delta` — Nanoseconds to add.

## Return Value

A new [dispatch_time_t](dispatch_time_t.md).

## Discussion

The wall clock is based on `gettimeofday(_:_:)`.

## See Also

### Time Constructs

- [dispatch_time](dispatch_time.md) — Creates a `dispatch_time_t` relative to the default clock or modifies an existing `dispatch_time_t`.
- [dispatch_time_t](dispatch_time_t.md) — An abstract representation of time.
- [DISPATCH_WALLTIME_NOW](dispatch_walltime_now.md) — The current time.
- [Wall Time Constants](2963138-wall-time-constants.md) — Constants for wall time values.

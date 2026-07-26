---
title: dispatch_source_timer_flags_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_source_timer_flags_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_source_timer_flags_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_source_timer_flags_t.json'
content_hash: 'sha256:93b83e030f267248'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_source_timer_flags_t

<sub>Type Alias</sub>

Flags to use when configuring a timer dispatch source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef unsigned long dispatch_source_timer_flags_t;
```

## Topics

### Timer Flags

- [DISPATCH_TIMER_STRICT](dispatch_timer_strict.md) — The system makes its best effort to observe the timer’s specified leeway value, even if the value is smaller than the default leeway.

## See Also

### Managing Timer Parameters

- [dispatch_source_set_timer](dispatch_source_set_timer.md) — Sets a start time, interval, and leeway value for a timer source.

---
title: 'init(uptimeNanoseconds:)'
framework: Dispatch
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchtime/init(uptimenanoseconds:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchtime/init(uptimenanoseconds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchtime/init%28uptimenanoseconds%3A%29.json'
content_hash: 'sha256:4bf169b13bcdb954'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchTime](../dispatchtime.md)

# init(uptimeNanoseconds:)

<sub>Initializer</sub>

Creates a time relative to the amount of time the system has been running.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(uptimeNanoseconds: UInt64)
```

## Parameters

- `uptimeNanoseconds` — The number of nanoseconds since boot, excluding any time the system spent asleep.

## Discussion

On Apple platforms, this clock is the same as the value returned by [mach_absolute_time](../../kernel/1462446-mach_absolute_time.md) when converted into nanoseconds.

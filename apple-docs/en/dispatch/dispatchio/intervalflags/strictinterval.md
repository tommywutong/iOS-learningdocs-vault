---
title: strictInterval
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchio/intervalflags/strictinterval
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchio/intervalflags/strictinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchio/intervalflags/strictinterval.json'
content_hash: 'sha256:3f0fb5eb78fa0c90'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchIO](../../dispatchio.md) · [IntervalFlags](../intervalflags.md)

# strictInterval

<sub>Type Property</sub>

Enqueue handlers for a channel at strict intervals regardless of how much data has been read or written.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let strictInterval: DispatchIO.IntervalFlags
```

## Discussion

Setting this flag can lead to the handler being called even if the amount of data does not exceed the channel’s low-water mark.

## See Also

### Interval Flags

- [DISPATCH_IO_STRICT_INTERVAL](../../dispatch_io_strict_interval.md) — Enqueue handlers for a channel at strict intervals regardless of how much data has been read or written.

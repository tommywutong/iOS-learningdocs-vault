---
title: DISPATCH_IO_STRICT_INTERVAL
framework: Dispatch
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_io_strict_interval
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_io_strict_interval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_io_strict_interval.json'
content_hash: 'sha256:ad2591d8f643a3dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DISPATCH_IO_STRICT_INTERVAL

<sub>Global Variable</sub>

Enqueue handlers for a channel at strict intervals regardless of how much data has been read or written.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var DISPATCH_IO_STRICT_INTERVAL: Int32 { get }
```

## Discussion

Setting this flag can lead to the handler being called even if the amount of data does not exceed the channel’s low-water mark.

## See Also

### Interval Flags

- [strictInterval](dispatchio/intervalflags/strictinterval.md) — Enqueue handlers for a channel at strict intervals regardless of how much data has been read or written.

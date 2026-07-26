---
title: handle
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsourceprotocol/handle
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/handle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceprotocol/handle.json'
content_hash: 'sha256:7a67e1de629c920b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSourceProtocol](../dispatchsourceprotocol.md)

# handle

<sub>Instance Property</sub>

Returns the underlying system handle associated with the specified dispatch source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var handle: UInt { get }
```

## See Also

### Getting the Dispatch Source Attributes

- [data](data.md) — Returns pending data for the dispatch source.
- [mask](mask.md) — Returns the mask of events monitored by the dispatch source.

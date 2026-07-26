---
title: deallocateReceiveRight
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmachport/options/deallocatereceiveright
source_url: 'https://developer.apple.com/documentation/foundation/nsmachport/options/deallocatereceiveright'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachport/options/deallocatereceiveright.json'
content_hash: 'sha256:1568a40b4db60975'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSMachPort](../../nsmachport.md) · [Options](../options.md)

# deallocateReceiveRight

<sub>Type Property</sub>

Remove a receive right when the `NSMachPort` object is invalidated or destroyed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var deallocateReceiveRight: NSMachPort.Options { get }
```

## See Also

### Constants

- [NSMachPortDeallocateSendRight](deallocatesendright.md) — Deallocate a send right when the `NSMachPort` object is invalidated or destroyed.

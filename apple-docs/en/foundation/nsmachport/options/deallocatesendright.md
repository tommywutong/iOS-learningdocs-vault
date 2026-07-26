---
title: deallocateSendRight
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmachport/options/deallocatesendright
source_url: 'https://developer.apple.com/documentation/foundation/nsmachport/options/deallocatesendright'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachport/options/deallocatesendright.json'
content_hash: 'sha256:7118dcd8f21dd390'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSMachPort](../../nsmachport.md) · [Options](../options.md)

# deallocateSendRight

<sub>Type Property</sub>

Deallocate a send right when the `NSMachPort` object is invalidated or destroyed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var deallocateSendRight: NSMachPort.Options { get }
```

## See Also

### Constants

- [NSMachPortDeallocateReceiveRight](deallocatereceiveright.md) — Remove a receive right when the `NSMachPort` object is invalidated or destroyed.

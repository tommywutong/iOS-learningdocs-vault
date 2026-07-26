---
title: machPort
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmachport/machport
source_url: 'https://developer.apple.com/documentation/foundation/nsmachport/machport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachport/machport.json'
content_hash: 'sha256:3a8e60d2eba32c55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMachPort](../nsmachport.md)

# machPort

<sub>Instance Property</sub>

The Mach port used by the receiver, represented as an integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var machPort: UInt32 { get }
```

## Discussion

The Mach port used by the receiver. Cast this value to a mach_port_t when using it with Mach system calls.

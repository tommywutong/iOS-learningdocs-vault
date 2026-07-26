---
title: dispatchType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepassdescriptor/dispatchtype
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepassdescriptor/dispatchtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepassdescriptor/dispatchtype.json'
content_hash: 'sha256:fb90e6a4c1739ff7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePassDescriptor](../mtlcomputepassdescriptor.md)

# dispatchType

<sub>Instance Property</sub>

The strategy for dispatching any compute commands encoded in the compute pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var dispatchType: MTLDispatchType { get set }
```

## Discussion

The default dispatch type is [MTLDispatchTypeSerial](../mtldispatchtype/serial.md).

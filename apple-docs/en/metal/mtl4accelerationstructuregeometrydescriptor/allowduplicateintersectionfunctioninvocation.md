---
title: allowDuplicateIntersectionFunctionInvocation
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4accelerationstructuregeometrydescriptor/allowduplicateintersectionfunctioninvocation
source_url: 'https://developer.apple.com/documentation/metal/mtl4accelerationstructuregeometrydescriptor/allowduplicateintersectionfunctioninvocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4accelerationstructuregeometrydescriptor/allowduplicateintersectionfunctioninvocation.json'
content_hash: 'sha256:dacb3ac96f0a9db2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4AccelerationStructureGeometryDescriptor](../mtl4accelerationstructuregeometrydescriptor.md)

# allowDuplicateIntersectionFunctionInvocation

<sub>Instance Property</sub>

A boolean value that indicates whether the ray-tracing system in Metal allows the invocation of intersection functions more than once per ray-primitive intersection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var allowDuplicateIntersectionFunctionInvocation: Bool { get set }
```

## Discussion

The property’s default value is [true](../../swift/true.md).

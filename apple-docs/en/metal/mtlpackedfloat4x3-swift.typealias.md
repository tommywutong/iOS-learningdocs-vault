---
title: MTLPackedFloat4x3
framework: Metal
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpackedfloat4x3-swift.typealias
source_url: 'https://developer.apple.com/documentation/metal/mtlpackedfloat4x3-swift.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpackedfloat4x3-swift.typealias.json'
content_hash: 'sha256:15e14fc3f3e7ac4a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLPackedFloat4x3

<sub>Type Alias</sub>

A structure that contains the top three rows of a 4x4 matrix of 32-bit floating-point values, in column-major order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias MTLPackedFloat4x3 = _MTLPackedFloat4x3
```

## Discussion

Metal uses the values `[0,0,0,1]` as the bottom row of the `4x4` matrix.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md)

## Topics

### Instance Properties

- [columns](mtlpackedfloat4x3-swift.typealias/columns.md)

## See Also

### Supporting types

- [MTLAxisAlignedBoundingBox](mtlaxisalignedboundingbox-swift.typealias.md) — The bounds for an axis-aligned bounding box.
- [MTLPackedFloat3](mtlpackedfloat3-swift.typealias.md) — }
- [MTLPackedFloat3Make](<mtlpackedfloat3make(______).md>) — Returns a new packed vector with three floating-point values.
- [MTL4BufferRange](mtl4bufferrange.md)
- [MTL4BufferRangeMake](<mtl4bufferrangemake(____).md>)

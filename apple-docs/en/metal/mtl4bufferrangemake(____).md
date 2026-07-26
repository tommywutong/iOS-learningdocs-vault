---
title: 'MTL4BufferRangeMake(_:_:)'
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4bufferrangemake(_:_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4bufferrangemake(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4bufferrangemake%28_%3A_%3A%29.json'
content_hash: 'sha256:5b89188aa8bad1fc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4BufferRangeMake(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTL4BufferRangeMake(_ bufferAddress: MTLGPUAddress, _ length: UInt64) -> MTL4BufferRange
```

## Discussion

Create a buffer range from a buffer’s GPU address (given by the gpuAddress property) and length. A length of (uint64_t)-1 represents the the range from the given address to the end of the buffer.

## See Also

### Supporting types

- [MTLAxisAlignedBoundingBox](mtlaxisalignedboundingbox-swift.typealias.md) — The bounds for an axis-aligned bounding box.
- [MTLPackedFloat3](mtlpackedfloat3-swift.typealias.md) — }
- [MTLPackedFloat4x3](mtlpackedfloat4x3-swift.typealias.md) — A structure that contains the top three rows of a 4x4 matrix of 32-bit floating-point values, in column-major order.
- [MTLPackedFloat3Make](<mtlpackedfloat3make(______).md>) — Returns a new packed vector with three floating-point values.
- [MTL4BufferRange](mtl4bufferrange.md)

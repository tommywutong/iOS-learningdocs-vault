---
title: MTL4BufferRange
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4bufferrange
source_url: 'https://developer.apple.com/documentation/metal/mtl4bufferrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4bufferrange.json'
content_hash: 'sha256:4dd197f2b7834470'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4BufferRange

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTL4BufferRange
```

## Overview

A struct representing a range of a Metal buffer. The offset into the buffer is included in the address. The length is generally optional, which a value of (uint64_t)-1 representing the range from the given address to the end of the buffer. However, providing the length can enable more accurate API validation, especially when sub-allocating ranges of a buffer.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<mtl4bufferrange/init().md>)
- [init(bufferAddress:length:)](<mtl4bufferrange/init(bufferaddress_length_).md>)

### Instance Properties

- [bufferAddress](mtl4bufferrange/bufferaddress.md)
- [length](mtl4bufferrange/length.md)

## See Also

### Supporting types

- [MTLAxisAlignedBoundingBox](mtlaxisalignedboundingbox-swift.typealias.md) — The bounds for an axis-aligned bounding box.
- [MTLPackedFloat3](mtlpackedfloat3-swift.typealias.md) — }
- [MTLPackedFloat4x3](mtlpackedfloat4x3-swift.typealias.md) — A structure that contains the top three rows of a 4x4 matrix of 32-bit floating-point values, in column-major order.
- [MTLPackedFloat3Make](<mtlpackedfloat3make(______).md>) — Returns a new packed vector with three floating-point values.
- [MTL4BufferRangeMake](<mtl4bufferrangemake(____).md>)

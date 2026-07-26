---
title: MTLPackedFloat4x3
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpackedfloat4x3-c.struct
source_url: 'https://developer.apple.com/documentation/metal/mtlpackedfloat4x3-c.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpackedfloat4x3-c.struct.json'
content_hash: 'sha256:a7d8bdda4df7f223'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLPackedFloat4x3

<sub>Structure</sub>

A structure that contains the top three rows of a 4x4 matrix of 32-bit floating-point values, in column-major order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
typedef struct _MTLPackedFloat4x3 { ... } MTLPackedFloat4x3;
```

## Overview

Metal uses the values `[0,0,0,1]` as the bottom row of the `4x4` matrix.

## Topics

### Instance Properties

- [columns](mtlpackedfloat4x3-c.struct/columns.md)

## See Also

### Supporting types

- [MTLAxisAlignedBoundingBox](mtlaxisalignedboundingbox-c.struct.md) — The bounds for an axis-aligned bounding box.
- [MTLPackedFloat3](mtlpackedfloat3-c.struct.md) — A structure that contains three 32-bit floating-point values with no additional padding.
- [MTLPackedFloat3Make](<mtlpackedfloat3make(______).md>) — Returns a new packed vector with three floating-point values.
- [MTL4BufferRange](mtl4bufferrange.md)
- [MTL4BufferRangeMake](<mtl4bufferrangemake(____).md>)

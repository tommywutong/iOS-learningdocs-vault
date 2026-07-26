---
title: refitScratchBufferSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuresizes/refitscratchbuffersize
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuresizes/refitscratchbuffersize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuresizes/refitscratchbuffersize.json'
content_hash: 'sha256:32b173ccb7461418'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureSizes](../mtlaccelerationstructuresizes.md)

# refitScratchBufferSize

<sub>Instance Property</sub>

The amount of scratch memory, in bytes, the GPU device needs to refit the acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var refitScratchBufferSize: Int
```

## Discussion

This value can be zero, which indicates that refitting the acceleration structure doesn’t require a scratch buffer.

## See Also

### Retrieving the sizes

- [accelerationStructureSize](accelerationstructuresize.md) — The size of the acceleration structure, in bytes.
- [buildScratchBufferSize](buildscratchbuffersize.md) — The amount of scratch memory, in bytes, the GPU devices needs to build the acceleration structure.

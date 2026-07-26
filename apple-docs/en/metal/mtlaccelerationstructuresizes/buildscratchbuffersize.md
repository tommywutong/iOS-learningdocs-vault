---
title: buildScratchBufferSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuresizes/buildscratchbuffersize
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuresizes/buildscratchbuffersize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuresizes/buildscratchbuffersize.json'
content_hash: 'sha256:511671b1e1989805'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureSizes](../mtlaccelerationstructuresizes.md)

# buildScratchBufferSize

<sub>Instance Property</sub>

The amount of scratch memory, in bytes, the GPU devices needs to build the acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var buildScratchBufferSize: Int
```

## See Also

### Retrieving the sizes

- [accelerationStructureSize](accelerationstructuresize.md) — The size of the acceleration structure, in bytes.
- [refitScratchBufferSize](refitscratchbuffersize.md) — The amount of scratch memory, in bytes, the GPU device needs to refit the acceleration structure.

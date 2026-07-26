---
title: 'init(accelerationStructureSize:buildScratchBufferSize:refitScratchBufferSize:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlaccelerationstructuresizes/init(accelerationstructuresize:buildscratchbuffersize:refitscratchbuffersize:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuresizes/init(accelerationstructuresize:buildscratchbuffersize:refitscratchbuffersize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuresizes/init%28accelerationstructuresize%3Abuildscratchbuffersize%3Arefitscratchbuffersize%3A%29.json'
content_hash: 'sha256:9bdd29e42b2944e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureSizes](../mtlaccelerationstructuresizes.md)

# init(accelerationStructureSize:buildScratchBufferSize:refitScratchBufferSize:)

<sub>Initializer</sub>

Creates an acceleration sizes instance with specific values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(accelerationStructureSize: Int, buildScratchBufferSize: Int, refitScratchBufferSize: Int)
```

## Parameters

- `accelerationStructureSize` — The size of the acceleration structure, in bytes.

- `buildScratchBufferSize` — The amount of scratch memory, in bytes, the GPU devices needs to build the acceleration structure.

- `refitScratchBufferSize` — The amount of scratch memory, in bytes, the GPU device needs to refit the acceleration structure.

## See Also

### Creating an acceleration size structure

- [init()](<init().md>) — Creates an acceleration sizes instance with default values.

---
title: MTLAccelerationStructureSizes
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructuresizes
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructuresizes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructuresizes.json'
content_hash: 'sha256:9dbd21606bdcbc37'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLAccelerationStructureSizes

<sub>Structure</sub>

The expected sizes for a ray-tracing acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLAccelerationStructureSizes
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Retrieving the sizes

- [accelerationStructureSize](mtlaccelerationstructuresizes/accelerationstructuresize.md) — The size of the acceleration structure, in bytes.
- [buildScratchBufferSize](mtlaccelerationstructuresizes/buildscratchbuffersize.md) — The amount of scratch memory, in bytes, the GPU devices needs to build the acceleration structure.
- [refitScratchBufferSize](mtlaccelerationstructuresizes/refitscratchbuffersize.md) — The amount of scratch memory, in bytes, the GPU device needs to refit the acceleration structure.

### Creating an acceleration size structure

- [init()](<mtlaccelerationstructuresizes/init().md>) — Creates an acceleration sizes instance with default values.
- [init(accelerationStructureSize:buildScratchBufferSize:refitScratchBufferSize:)](<mtlaccelerationstructuresizes/init(accelerationstructuresize_buildscratchbuffersize_refitscratchbuffersize_).md>) — Creates an acceleration sizes instance with specific values.

## See Also

### Creating acceleration structures for ray tracing

- [- newAccelerationStructureWithDescriptor:](<mtldevice/makeaccelerationstructure(descriptor_).md>) — Creates a new ray-tracing acceleration structure from a descriptor.
- [- newAccelerationStructureWithSize:](<mtldevice/makeaccelerationstructure(size_).md>) — Creates a new acceleration structure with a specific size.
- [- accelerationStructureSizesWithDescriptor:](<mtldevice/accelerationstructuresizes(descriptor_).md>) — Returns the buffer sizes the GPU device needs to build, refit, and store an acceleration structure.

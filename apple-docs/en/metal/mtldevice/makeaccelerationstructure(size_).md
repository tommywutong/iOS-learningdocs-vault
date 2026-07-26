---
title: 'makeAccelerationStructure(size:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makeaccelerationstructure(size:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makeaccelerationstructure(size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makeaccelerationstructure%28size%3A%29.json'
content_hash: 'sha256:e56fdcd0a4040b82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeAccelerationStructure(size:)

<sub>Instance Method</sub>

Creates a new acceleration structure with a specific size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeAccelerationStructure(size: Int) -> (any MTLAccelerationStructure)?
```

## Parameters

- `size` — The size of the new acceleration structure, in bytes.

## Return Value

A new [MTLAccelerationStructure](../mtlaccelerationstructure.md) instance if the method completed successfully; otherwise `nil`.

## See Also

### Creating acceleration structures for ray tracing

- [- newAccelerationStructureWithDescriptor:](<makeaccelerationstructure(descriptor_).md>) — Creates a new ray-tracing acceleration structure from a descriptor.
- [- accelerationStructureSizesWithDescriptor:](<accelerationstructuresizes(descriptor_).md>) — Returns the buffer sizes the GPU device needs to build, refit, and store an acceleration structure.
- [MTLAccelerationStructureSizes](../mtlaccelerationstructuresizes.md) — The expected sizes for a ray-tracing acceleration structure.

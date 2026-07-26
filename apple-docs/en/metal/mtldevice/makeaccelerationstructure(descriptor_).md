---
title: 'makeAccelerationStructure(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makeaccelerationstructure(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makeaccelerationstructure(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makeaccelerationstructure%28descriptor%3A%29.json'
content_hash: 'sha256:39d2598d89724922'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeAccelerationStructure(descriptor:)

<sub>Instance Method</sub>

Creates a new ray-tracing acceleration structure from a descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeAccelerationStructure(descriptor: MTLAccelerationStructureDescriptor) -> (any MTLAccelerationStructure)?
```

## Parameters

- `descriptor` — An [MTLAccelerationStructureDescriptor](../mtlaccelerationstructuredescriptor.md) instance.

## Return Value

A new [MTLAccelerationStructure](../mtlaccelerationstructure.md) instance if the method completed successfully; otherwise `nil`.

## See Also

### Creating acceleration structures for ray tracing

- [- newAccelerationStructureWithSize:](<makeaccelerationstructure(size_).md>) — Creates a new acceleration structure with a specific size.
- [- accelerationStructureSizesWithDescriptor:](<accelerationstructuresizes(descriptor_).md>) — Returns the buffer sizes the GPU device needs to build, refit, and store an acceleration structure.
- [MTLAccelerationStructureSizes](../mtlaccelerationstructuresizes.md) — The expected sizes for a ray-tracing acceleration structure.

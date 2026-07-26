---
title: 'accelerationStructureSizes(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/accelerationstructuresizes(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/accelerationstructuresizes(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/accelerationstructuresizes%28descriptor%3A%29.json'
content_hash: 'sha256:d321d7f5e2b83bf2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# accelerationStructureSizes(descriptor:)

<sub>Instance Method</sub>

Returns the buffer sizes the GPU device needs to build, refit, and store an acceleration structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func accelerationStructureSizes(descriptor: MTLAccelerationStructureDescriptor) -> MTLAccelerationStructureSizes
```

## Parameters

- `descriptor` — An [MTLAccelerationStructureDescriptor](../mtlaccelerationstructuredescriptor.md) instance.

## Return Value

A new [MTLAccelerationStructureSizes](../mtlaccelerationstructuresizes.md) instance.

## See Also

### Creating acceleration structures for ray tracing

- [- newAccelerationStructureWithDescriptor:](<makeaccelerationstructure(descriptor_).md>) — Creates a new ray-tracing acceleration structure from a descriptor.
- [- newAccelerationStructureWithSize:](<makeaccelerationstructure(size_).md>) — Creates a new acceleration structure with a specific size.
- [MTLAccelerationStructureSizes](../mtlaccelerationstructuresizes.md) — The expected sizes for a ray-tracing acceleration structure.

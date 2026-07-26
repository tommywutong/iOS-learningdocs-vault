---
title: 'heapAccelerationStructureSizeAndAlign(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/heapaccelerationstructuresizeandalign(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/heapaccelerationstructuresizeandalign(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/heapaccelerationstructuresizeandalign%28descriptor%3A%29.json'
content_hash: 'sha256:6d942f7185e4e5d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# heapAccelerationStructureSizeAndAlign(descriptor:)

<sub>Instance Method</sub>

Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap with a descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func heapAccelerationStructureSizeAndAlign(descriptor: MTLAccelerationStructureDescriptor) -> MTLSizeAndAlign
```

## Parameters

- `descriptor` — An [MTLAccelerationStructureDescriptor](../mtlaccelerationstructuredescriptor.md) instance.

## Return Value

An [MTLSizeAndAlign](../mtlsizeandalign.md) instance.

## Discussion

Use this method to help estimate an appropriate size for a new heap before you create it.

## See Also

### Working with resource heaps

- [- newHeapWithDescriptor:](<makeheap(descriptor_).md>) — Creates a new GPU heap instance.
- [- heapBufferSizeAndAlignWithLength:options:](<heapbuffersizeandalign(length_options_).md>) — Returns the size and alignment, in bytes, of a buffer if you create it from a heap.
- [- heapTextureSizeAndAlignWithDescriptor:](<heaptexturesizeandalign(descriptor_).md>) — Returns the size and alignment, in bytes, of a texture if you create it from a heap.
- [- heapAccelerationStructureSizeAndAlignWithSize:](<heapaccelerationstructuresizeandalign(size_).md>) — Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap.
- [MTLSizeAndAlign](../mtlsizeandalign.md) — The size and alignment of a resource, in bytes.

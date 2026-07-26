---
title: 'makeHeap(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makeheap(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makeheap(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makeheap%28descriptor%3A%29.json'
content_hash: 'sha256:eddfdc12fca8a49e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeHeap(descriptor:)

<sub>Instance Method</sub>

Creates a new GPU heap instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeHeap(descriptor: MTLHeapDescriptor) -> (any MTLHeap)?
```

## Parameters

- `descriptor` — An [MTLHeapDescriptor](../mtlheapdescriptor.md) instance.

## Return Value

A new [MTLHeap](../mtlheap.md) instance if the method completed successfully; otherwise nil.

## Discussion

For more information about using heaps, see [Memory heaps](../memory-heaps.md).

## See Also

### Working with resource heaps

- [- heapBufferSizeAndAlignWithLength:options:](<heapbuffersizeandalign(length_options_).md>) — Returns the size and alignment, in bytes, of a buffer if you create it from a heap.
- [- heapTextureSizeAndAlignWithDescriptor:](<heaptexturesizeandalign(descriptor_).md>) — Returns the size and alignment, in bytes, of a texture if you create it from a heap.
- [- heapAccelerationStructureSizeAndAlignWithSize:](<heapaccelerationstructuresizeandalign(size_).md>) — Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap.
- [- heapAccelerationStructureSizeAndAlignWithDescriptor:](<heapaccelerationstructuresizeandalign(descriptor_).md>) — Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap with a descriptor.
- [MTLSizeAndAlign](../mtlsizeandalign.md) — The size and alignment of a resource, in bytes.

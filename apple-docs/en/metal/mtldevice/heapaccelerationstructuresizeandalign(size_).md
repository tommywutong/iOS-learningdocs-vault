---
title: 'heapAccelerationStructureSizeAndAlign(size:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/heapaccelerationstructuresizeandalign(size:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/heapaccelerationstructuresizeandalign(size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/heapaccelerationstructuresizeandalign%28size%3A%29.json'
content_hash: 'sha256:f07c1a96ec17d939'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# heapAccelerationStructureSizeAndAlign(size:)

<sub>Instance Method</sub>

Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func heapAccelerationStructureSizeAndAlign(size: Int) -> MTLSizeAndAlign
```

## Parameters

- `size` — The size of an acceleration structure, in bytes.

## Return Value

An [MTLSizeAndAlign](../mtlsizeandalign.md) instance

## Discussion

Use this method to help estimate an appropriate size for a new heap before you create it.

## See Also

### Working with resource heaps

- [- newHeapWithDescriptor:](<makeheap(descriptor_).md>) — Creates a new GPU heap instance.
- [- heapBufferSizeAndAlignWithLength:options:](<heapbuffersizeandalign(length_options_).md>) — Returns the size and alignment, in bytes, of a buffer if you create it from a heap.
- [- heapTextureSizeAndAlignWithDescriptor:](<heaptexturesizeandalign(descriptor_).md>) — Returns the size and alignment, in bytes, of a texture if you create it from a heap.
- [- heapAccelerationStructureSizeAndAlignWithDescriptor:](<heapaccelerationstructuresizeandalign(descriptor_).md>) — Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap with a descriptor.
- [MTLSizeAndAlign](../mtlsizeandalign.md) — The size and alignment of a resource, in bytes.

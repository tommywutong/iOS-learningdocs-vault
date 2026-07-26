---
title: 'heapTextureSizeAndAlign(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/heaptexturesizeandalign(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/heaptexturesizeandalign(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/heaptexturesizeandalign%28descriptor%3A%29.json'
content_hash: 'sha256:ae655b9b3d34b73c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# heapTextureSizeAndAlign(descriptor:)

<sub>Instance Method</sub>

Returns the size and alignment, in bytes, of a texture if you create it from a heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func heapTextureSizeAndAlign(descriptor desc: MTLTextureDescriptor) -> MTLSizeAndAlign
```

## Parameters

- `desc` — An [MTLTextureDescriptor](../mtltexturedescriptor.md) instance.

## Return Value

An [MTLSizeAndAlign](../mtlsizeandalign.md) instance.

## Discussion

Use this method to help estimate an appropriate size for a new heap before you create it.

## See Also

### Working with resource heaps

- [- newHeapWithDescriptor:](<makeheap(descriptor_).md>) — Creates a new GPU heap instance.
- [- heapBufferSizeAndAlignWithLength:options:](<heapbuffersizeandalign(length_options_).md>) — Returns the size and alignment, in bytes, of a buffer if you create it from a heap.
- [- heapAccelerationStructureSizeAndAlignWithSize:](<heapaccelerationstructuresizeandalign(size_).md>) — Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap.
- [- heapAccelerationStructureSizeAndAlignWithDescriptor:](<heapaccelerationstructuresizeandalign(descriptor_).md>) — Returns the size and alignment, in bytes, of an acceleration structure if you create it from a heap with a descriptor.
- [MTLSizeAndAlign](../mtlsizeandalign.md) — The size and alignment of a resource, in bytes.

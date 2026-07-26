---
title: 'maxAvailableSize(alignment:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlheap/maxavailablesize(alignment:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlheap/maxavailablesize(alignment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheap/maxavailablesize%28alignment%3A%29.json'
content_hash: 'sha256:b73134b2610a6e40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeap](../mtlheap.md)

# maxAvailableSize(alignment:)

<sub>Instance Method</sub>

The maximum size of a resource, in bytes, that can be currently allocated from the heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func maxAvailableSize(alignment: Int) -> Int
```

## Parameters

- `alignment` — The alignment of the resource, in bytes. This value needs to be a power of two.

## Return Value

The maximum size for the resource, in bytes.

## Discussion

This method measures fragmentation within the heap. You can use the [- heapBufferSizeAndAlignWithLength:options:](<../mtldevice/heapbuffersizeandalign(length_options_).md>) and [- heapTextureSizeAndAlignWithDescriptor:](<../mtldevice/heaptexturesizeandalign(descriptor_).md>) methods to help you determine the correct alignment for the resource.

## See Also

### Checking a heap’s size information

- [size](size.md) — The total size of the heap, in bytes.
- [usedSize](usedsize.md) — The size of all resources currently in the heap, in bytes.
- [currentAllocatedSize](currentallocatedsize.md) — The size, in bytes, of the current heap allocation.

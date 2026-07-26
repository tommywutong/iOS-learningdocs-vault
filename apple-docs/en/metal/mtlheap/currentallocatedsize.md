---
title: currentAllocatedSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheap/currentallocatedsize
source_url: 'https://developer.apple.com/documentation/metal/mtlheap/currentallocatedsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheap/currentallocatedsize.json'
content_hash: 'sha256:1b54a078cf4e6a34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeap](../mtlheap.md)

# currentAllocatedSize

<sub>Instance Property</sub>

The size, in bytes, of the current heap allocation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var currentAllocatedSize: Int { get }
```

## See Also

### Checking a heap’s size information

- [- maxAvailableSizeWithAlignment:](<maxavailablesize(alignment_).md>) — The maximum size of a resource, in bytes, that can be currently allocated from the heap.
- [size](size.md) — The total size of the heap, in bytes.
- [usedSize](usedsize.md) — The size of all resources currently in the heap, in bytes.

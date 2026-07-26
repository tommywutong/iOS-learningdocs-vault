---
title: usedSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheap/usedsize
source_url: 'https://developer.apple.com/documentation/metal/mtlheap/usedsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheap/usedsize.json'
content_hash: 'sha256:7f8647bfc4c16e0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeap](../mtlheap.md)

# usedSize

<sub>Instance Property</sub>

The size of all resources currently in the heap, in bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var usedSize: Int { get }
```

## See Also

### Checking a heap’s size information

- [- maxAvailableSizeWithAlignment:](<maxavailablesize(alignment_).md>) — The maximum size of a resource, in bytes, that can be currently allocated from the heap.
- [size](size.md) — The total size of the heap, in bytes.
- [currentAllocatedSize](currentallocatedsize.md) — The size, in bytes, of the current heap allocation.

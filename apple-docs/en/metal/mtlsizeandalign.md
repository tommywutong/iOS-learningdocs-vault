---
title: MTLSizeAndAlign
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsizeandalign
source_url: 'https://developer.apple.com/documentation/metal/mtlsizeandalign'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsizeandalign.json'
content_hash: 'sha256:5e4762bcb398b4f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLSizeAndAlign

<sub>Structure</sub>

The size and alignment of a resource, in bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLSizeAndAlign
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Accessing the size and alignment

- [size](mtlsizeandalign/size.md) — The size of a resource, in bytes.
- [align](mtlsizeandalign/align.md) — The alignment of a resource, in bytes.

### Creating instances

- [init()](<mtlsizeandalign/init().md>) — Creates a default instance.
- [init(size:align:)](<mtlsizeandalign/init(size_align_).md>) — Creates a new instance initialized to the given values.

## See Also

### Resource memory allocation and management

- [Using argument buffers with resource heaps](using-argument-buffers-with-resource-heaps.md) — Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [Implementing a multistage image filter using heaps and events](implementing-a-multistage-image-filter-using-heaps-and-events.md) — Use events to synchronize access to resources allocated on a heap.
- [Implementing a multistage image filter using heaps and fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md) — Use fences to synchronize access to resources allocated on a heap.
- [MTLHeap](mtlheap.md) — A memory pool from which you can suballocate resources.
- [MTLHeapDescriptor](mtlheapdescriptor.md) — A configuration that customizes the behavior for a Metal memory heap.
- [MTLHeapType](mtlheaptype.md) — The options you use to choose the heap type.

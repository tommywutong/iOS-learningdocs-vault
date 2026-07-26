---
title: MTLHeapType
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheaptype
source_url: 'https://developer.apple.com/documentation/metal/mtlheaptype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheaptype.json'
content_hash: 'sha256:ba26c224bae843c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLHeapType

<sub>Enumeration</sub>

The options you use to choose the heap type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLHeapType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Specifying the heap type

- [MTLHeapTypeAutomatic](mtlheaptype/automatic.md) — A heap that automatically places new resource allocations.
- [MTLHeapTypePlacement](mtlheaptype/placement.md) — The app controls placement of resources on the heap.
- [MTLHeapTypeSparse](mtlheaptype/sparse.md) — The heap contains sparse texture tiles.

### Initializers

- [init(rawValue:)](<mtlheaptype/init(rawvalue_).md>)

## See Also

### Resource memory allocation and management

- [Using argument buffers with resource heaps](using-argument-buffers-with-resource-heaps.md) — Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [Implementing a multistage image filter using heaps and events](implementing-a-multistage-image-filter-using-heaps-and-events.md) — Use events to synchronize access to resources allocated on a heap.
- [Implementing a multistage image filter using heaps and fences](implementing-a-multistage-image-filter-using-heaps-and-fences.md) — Use fences to synchronize access to resources allocated on a heap.
- [MTLHeap](mtlheap.md) — A memory pool from which you can suballocate resources.
- [MTLHeapDescriptor](mtlheapdescriptor.md) — A configuration that customizes the behavior for a Metal memory heap.
- [MTLSizeAndAlign](mtlsizeandalign.md) — The size and alignment of a resource, in bytes.

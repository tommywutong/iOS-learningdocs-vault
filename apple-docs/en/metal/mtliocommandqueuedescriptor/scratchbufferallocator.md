---
title: scratchBufferAllocator
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandqueuedescriptor/scratchbufferallocator
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandqueuedescriptor/scratchbufferallocator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandqueuedescriptor/scratchbufferallocator.json'
content_hash: 'sha256:6e8aae6d87340ade'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandQueueDescriptor](../mtliocommandqueuedescriptor.md)

# scratchBufferAllocator

<sub>Instance Property</sub>

An optional memory allocator that you implement to manage the scratch memory that an input/output command queue requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var scratchBufferAllocator: (any MTLIOScratchBufferAllocator)? { get set }
```

## Discussion

Your app can manage an input/output command queue’s scratch memory by an implementing [MTLIOScratchBufferAllocator](../mtlioscratchbufferallocator.md) in one of your types, and assigning an instance of it to [scratchBufferAllocator](scratchbufferallocator.md). Otherwise, set to `nil` to instruct the input/output command queue to allocate and manage its own scratch buffers.

> [!note] Note
> An input/output command queue uses scratch buffers for memory-intensives tasks, including loading textures and decompressing asset files.

---
title: MTLResourceStatePassSampleBufferAttachmentDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptor.json'
content_hash: 'sha256:edf2dabcf8502c29'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLResourceStatePassSampleBufferAttachmentDescriptor

<sub>Class</sub>

A description of where to store GPU counter information at the start and end of a resource state pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLResourceStatePassSampleBufferAttachmentDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the sample buffer attachment

- [sampleBuffer](mtlresourcestatepasssamplebufferattachmentdescriptor/samplebuffer.md) — A specialized memory buffer that the GPU uses to store its counter data during the resource state pass.
- [startOfEncoderSampleIndex](mtlresourcestatepasssamplebufferattachmentdescriptor/startofencodersampleindex.md) — The index the Metal device object should use to store GPU counters when starting the resource state pass.
- [endOfEncoderSampleIndex](mtlresourcestatepasssamplebufferattachmentdescriptor/endofencodersampleindex.md) — The index the Metal device object should use to store GPU counters when ending the resource state pass.

## See Also

### Sparse textures

- [Managing sparse texture memory](managing-sparse-texture-memory.md) — Take direct control of memory allocation for texture data by using sparse textures.
- [Creating sparse heaps and sparse textures](creating-sparse-heaps-and-sparse-textures.md) — Allocate memory for sparse textures by creating a sparse heap.
- [Converting between pixel regions and sparse tile regions](converting-between-pixel-regions-and-sparse-tile-regions.md) — Learn how a sparse texture’s contents are organized in memory.
- [Assigning memory to sparse textures](assigning-memory-to-sparse-textures.md) — Use a resource state encoder to allocate and deallocate sparse tiles for a sparse texture.
- [Reading and writing to sparse textures](reading-and-writing-to-sparse-textures.md) — Decide how to handle access to unmapped texture regions.
- [Estimating how often a texture region is accessed](estimating-how-often-a-texture-region-is-accessed.md) — Use texture access patterns to determine when you need to map a texture region.
- [MTLResourceStatePassDescriptor](mtlresourcestatepassdescriptor.md) — A configuration for a resource state pass, used to create a resource state command encoder.
- [MTLResourceStatePassSampleBufferAttachmentDescriptorArray](mtlresourcestatepasssamplebufferattachmentdescriptorarray.md) — An array of sample buffer attachments for a resource state pass.
- [MTLResourceStateCommandEncoder](mtlresourcestatecommandencoder.md) — An encoder that encodes commands that modify resource configurations.
- [MTLMapIndirectArguments](mtlmapindirectarguments.md) — The data layout for mapping sparse texture regions when using indirect commands.

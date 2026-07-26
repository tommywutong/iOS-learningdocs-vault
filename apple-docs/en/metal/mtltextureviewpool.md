---
title: MTLTextureViewPool
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltextureviewpool
source_url: 'https://developer.apple.com/documentation/metal/mtltextureviewpool'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltextureviewpool.json'
content_hash: 'sha256:575cc7c4da96966c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTextureViewPool

<sub>Protocol</sub>

A pool of lightweight texture views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLTextureViewPool : MTLResourceViewPool
```

## Overview

Use texture view pools to create lightweight texture view objects of [MTLTexture](mtltexture.md) and [MTLBuffer](mtlbuffer.md) instances.

## Relationships

- **Inherits From**: [MTLResourceViewPool](mtlresourceviewpool.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Methods

- [- setTextureViewFromBuffer:descriptor:offset:bytesPerRow:atIndex:](<mtltextureviewpool/settextureview(buffer_descriptor_offset_bytesperrow_index_).md>) — Creates a new lightweight texture view of a buffer.
- [- setTextureView:descriptor:atIndex:](<mtltextureviewpool/settextureview(texture_descriptor_index_).md>) — Creates a new lightweight texture view.
- [- setTextureView:atIndex:](<mtltextureviewpool/settextureview(texture_index_).md>) — Copies a default texture view to a slot in this texture view pool at an index provided.

## See Also

### View pools

- [MTLResourceViewPool](mtlresourceviewpool.md) — Contains views over resources of a specific type, and allows you to manage those views.
- [MTLResourceViewPoolDescriptor](mtlresourceviewpooldescriptor.md) — Provides parameters for creating a resource view pool.
- [MTLTextureViewDescriptor](mtltextureviewdescriptor.md)

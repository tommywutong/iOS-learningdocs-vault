---
title: 'copyTextureMappingsFromTexture:toTexture:operations:count:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/copytexturemappingsfromtexture:totexture:operations:count:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/copytexturemappingsfromtexture:totexture:operations:count:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/copytexturemappingsfromtexture%3Atotexture%3Aoperations%3Acount%3A.json'
content_hash: 'sha256:a2e2f1d2d4b6987d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# copyTextureMappingsFromTexture:toTexture:operations:count:

<sub>Instance Method</sub>

Copies multiple regions within a source placement sparse texture to a destination placement sparse texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) copyTextureMappingsFromTexture:(id<MTLTexture>) sourceTexture toTexture:(id<MTLTexture>) destinationTexture operations:(const MTL4CopySparseTextureMappingOperation[]) operations count:(NSUInteger) count;
```

## Parameters

- `sourceTexture` — The source placement sparse [MTLTexture](../mtltexture.md).

- `destinationTexture` — The destination placement sparse [MTLTexture](../mtltexture.md).

- `operations` — An array of [MTL4CopySparseTextureMappingOperation](../mtl4copysparsetexturemappingoperation.md) instances to perform.

- `count` — Number of operations to perform.

## Discussion

You are responsible for ensuring the source and destination textures have the same [placementSparsePageSize](../mtltexturedescriptor/placementsparsepagesize.md).

Additionally, you are responsible for ensuring that the source and destination textures don’t use the same aliased tiles at the same time.

> [!note] Note
> If a sparse texture and a sparse buffer share the same backing tiles, these don’t provide you you with meaningful views of the other resource’s data.

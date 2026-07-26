---
title: 'copyMappings(sourceTexture:destinationTexture:operations:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandqueue/copymappings(sourcetexture:destinationtexture:operations:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandqueue/copymappings(sourcetexture:destinationtexture:operations:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandqueue/copymappings%28sourcetexture%3Adestinationtexture%3Aoperations%3A%29.json'
content_hash: 'sha256:b75749d1171ce328'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandQueue](../mtl4commandqueue.md)

# copyMappings(sourceTexture:destinationTexture:operations:)

<sub>Instance Method</sub>

Copies multiple regions within a source placement sparse texture to a destination placement sparse texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copyMappings(sourceTexture: any MTLTexture, destinationTexture: any MTLTexture, operations: [MTL4CopySparseTextureMappingOperation])
```

## Parameters

- `sourceTexture` — The source placement sparse [MTLTexture](../mtltexture.md).

- `destinationTexture` — The destination placement sparse [MTLTexture](../mtltexture.md).

- `operations` — An array of [MTL4CopySparseTextureMappingOperation](../mtl4copysparsetexturemappingoperation.md) instances to perform.

## Discussion

You are responsible for ensuring the source and destination textures have the same [placementSparsePageSize](../mtltexturedescriptor/placementsparsepagesize.md).

Additionally, you are responsible for ensuring that the source and destination textures don’t use the same aliased tiles at the same time.

> [!note] Note
> If a sparse texture and a sparse buffer share the same backing tiles, these don’t provide you you with meaningful views of the other resource’s data.

---
title: MTLVertexAmplificationViewMapping
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexamplificationviewmapping
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexamplificationviewmapping'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexamplificationviewmapping.json'
content_hash: 'sha256:c58f71bd2cd8a939'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLVertexAmplificationViewMapping

<sub>Structure</sub>

An offset applied to a render target index and viewport index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLVertexAmplificationViewMapping
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a view mapping

- [init()](<mtlvertexamplificationviewmapping/init().md>) — Initializes a default view mapping.
- [init(viewportArrayIndexOffset:renderTargetArrayIndexOffset:)](<mtlvertexamplificationviewmapping/init(viewportarrayindexoffset_rendertargetarrayindexoffset_).md>) — Initializes a new view mapping.

### Specifying mapping offsets

- [renderTargetArrayIndexOffset](mtlvertexamplificationviewmapping/rendertargetarrayindexoffset.md) — An offset into the list of render targets.
- [viewportArrayIndexOffset](mtlvertexamplificationviewmapping/viewportarrayindexoffset.md) — An offset into the list of viewports.

## See Also

### Dynamic render pipeline states

- [MTLViewport](mtlviewport.md) — A 3D rectangular region for the viewport clipping.
- [MTLScissorRect](mtlscissorrect.md) — A rectangle for the scissor fragment test.
- [MTLQuadTessellationFactorsHalf](mtlquadtessellationfactorshalf.md) — The per-patch tessellation factors for a quad patch.
- [MTLTriangleTessellationFactorsHalf](mtltriangletessellationfactorshalf.md) — The per-patch tessellation factors for a triangle patch.

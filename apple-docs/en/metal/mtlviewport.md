---
title: MTLViewport
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlviewport
source_url: 'https://developer.apple.com/documentation/metal/mtlviewport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlviewport.json'
content_hash: 'sha256:ccf6e8524528d79d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLViewport

<sub>Structure</sub>

A 3D rectangular region for the viewport clipping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLViewport
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a viewport

- [init()](<mtlviewport/init().md>) — Returns a new viewport.
- [init(originX:originY:width:height:znear:zfar:)](<mtlviewport/init(originx_originy_width_height_znear_zfar_).md>) — Returns a new viewport of a specified size at a specified origin.

### Specifying viewport boundaries

- [originX](mtlviewport/originx.md) — The x coordinate of the upper-left corner of the viewport.
- [originY](mtlviewport/originy.md) — The y coordinate of the upper-left corner of the viewport.
- [width](mtlviewport/width.md) — The width of the viewport, in pixels.
- [height](mtlviewport/height.md) — The height of the viewport, in pixels.
- [znear](mtlviewport/znear.md) — The z coordinate of the near clipping plane of the viewport.
- [zfar](mtlviewport/zfar.md) — The z coordinate of the far clipping plane of the viewport.

## See Also

### Dynamic render pipeline states

- [MTLScissorRect](mtlscissorrect.md) — A rectangle for the scissor fragment test.
- [MTLVertexAmplificationViewMapping](mtlvertexamplificationviewmapping.md) — An offset applied to a render target index and viewport index.
- [MTLQuadTessellationFactorsHalf](mtlquadtessellationfactorshalf.md) — The per-patch tessellation factors for a quad patch.
- [MTLTriangleTessellationFactorsHalf](mtltriangletessellationfactorshalf.md) — The per-patch tessellation factors for a triangle patch.

---
title: MTLScissorRect
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlscissorrect
source_url: 'https://developer.apple.com/documentation/metal/mtlscissorrect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlscissorrect.json'
content_hash: 'sha256:0fb2e1ab3dc0b7fc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLScissorRect

<sub>Structure</sub>

A rectangle for the scissor fragment test.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLScissorRect
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a scissor rectangle

- [init()](<mtlscissorrect/init().md>)
- [init(x:y:width:height:)](<mtlscissorrect/init(x_y_width_height_).md>)

### Specifying scissor boundaries

- [height](mtlscissorrect/height.md) — The height of the scissor rectangle, in pixels.
- [width](mtlscissorrect/width.md) — The width of the scissor rectangle, in pixels.
- [x](mtlscissorrect/x.md) — The x window coordinate of the upper-left corner of the scissor rectangle.
- [y](mtlscissorrect/y.md) — The y window coordinate of the upper-left corner of the scissor rectangle.

## See Also

### Dynamic render pipeline states

- [MTLViewport](mtlviewport.md) — A 3D rectangular region for the viewport clipping.
- [MTLVertexAmplificationViewMapping](mtlvertexamplificationviewmapping.md) — An offset applied to a render target index and viewport index.
- [MTLQuadTessellationFactorsHalf](mtlquadtessellationfactorshalf.md) — The per-patch tessellation factors for a quad patch.
- [MTLTriangleTessellationFactorsHalf](mtltriangletessellationfactorshalf.md) — The per-patch tessellation factors for a triangle patch.

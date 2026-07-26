---
title: MTLQuadTessellationFactorsHalf
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlquadtessellationfactorshalf
source_url: 'https://developer.apple.com/documentation/metal/mtlquadtessellationfactorshalf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlquadtessellationfactorshalf.json'
content_hash: 'sha256:a63567a34fc1b708'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLQuadTessellationFactorsHalf

<sub>Structure</sub>

The per-patch tessellation factors for a quad patch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLQuadTessellationFactorsHalf
```

## Overview

Refer to the [Tessellation](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Tessellation/Tessellation.html#//apple_ref/doc/uid/TP40014221-CH15) chapter of the [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221) for further information.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<mtlquadtessellationfactorshalf/init().md>) — Returns a new per-patch tessellation factors structure.
- [init(edgeTessellationFactor:insideTessellationFactor:)](<mtlquadtessellationfactorshalf/init(edgetessellationfactor_insidetessellationfactor_).md>) — Returns a new per-patch tessellation factors structure with the specified parameters.

### Instance Properties

- [edgeTessellationFactor](mtlquadtessellationfactorshalf/edgetessellationfactor.md) — The edge tessellation factors, with each index value providing the tessellation factor for a particular edge.
- [insideTessellationFactor](mtlquadtessellationfactorshalf/insidetessellationfactor.md) — The inside tessellation factors, with the value in index 0 providing the horizontal tessellation factor and the value in index 1 providing the vertical tessellation factor.

## See Also

### Dynamic render pipeline states

- [MTLViewport](mtlviewport.md) — A 3D rectangular region for the viewport clipping.
- [MTLScissorRect](mtlscissorrect.md) — A rectangle for the scissor fragment test.
- [MTLVertexAmplificationViewMapping](mtlvertexamplificationviewmapping.md) — An offset applied to a render target index and viewport index.
- [MTLTriangleTessellationFactorsHalf](mtltriangletessellationfactorshalf.md) — The per-patch tessellation factors for a triangle patch.

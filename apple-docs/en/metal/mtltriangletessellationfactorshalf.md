---
title: MTLTriangleTessellationFactorsHalf
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtltriangletessellationfactorshalf
source_url: 'https://developer.apple.com/documentation/metal/mtltriangletessellationfactorshalf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltriangletessellationfactorshalf.json'
content_hash: 'sha256:1066fb357ae597ea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLTriangleTessellationFactorsHalf

<sub>Structure</sub>

The per-patch tessellation factors for a triangle patch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLTriangleTessellationFactorsHalf
```

## Overview

Refer to the [Tessellation](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Tessellation/Tessellation.html#//apple_ref/doc/uid/TP40014221-CH15) chapter of the [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221) for further information.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<mtltriangletessellationfactorshalf/init().md>)
- [init(edgeTessellationFactor:insideTessellationFactor:)](<mtltriangletessellationfactorshalf/init(edgetessellationfactor_insidetessellationfactor_).md>)

### Instance Properties

- [edgeTessellationFactor](mtltriangletessellationfactorshalf/edgetessellationfactor.md) — The edge tessellation factors, with each index value providing the tessellation factor for a particular edge.
- [insideTessellationFactor](mtltriangletessellationfactorshalf/insidetessellationfactor.md) — The inside tessellation factor.

## See Also

### Dynamic render pipeline states

- [MTLViewport](mtlviewport.md) — A 3D rectangular region for the viewport clipping.
- [MTLScissorRect](mtlscissorrect.md) — A rectangle for the scissor fragment test.
- [MTLVertexAmplificationViewMapping](mtlvertexamplificationviewmapping.md) — An offset applied to a render target index and viewport index.
- [MTLQuadTessellationFactorsHalf](mtlquadtessellationfactorshalf.md) — The per-patch tessellation factors for a quad patch.

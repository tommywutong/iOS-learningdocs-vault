---
title: computeKernelInvocations
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcounterresultstatistic/computekernelinvocations
source_url: 'https://developer.apple.com/documentation/metal/mtlcounterresultstatistic/computekernelinvocations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounterresultstatistic/computekernelinvocations.json'
content_hash: 'sha256:6fc512e555f46e0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterResultStatistic](../mtlcounterresultstatistic.md)

# computeKernelInvocations

<sub>Instance Property</sub>

The number of times a pass calls any compute kernel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var computeKernelInvocations: UInt64
```

## See Also

### Statistics values

- [tessellationInputPatches](tessellationinputpatches.md) — The number of tessellation patches a render pass sends to the tessellation stage.
- [vertexInvocations](vertexinvocations.md) — The number of times a render pass calls any vertex shader.
- [postTessellationVertexInvocations](posttessellationvertexinvocations.md) — The number of vertices a render pass sends to a post-tessellation vertex shader.
- [clipperInvocations](clipperinvocations.md) — The number of primitives a render pass sends to the clip stage.
- [clipperPrimitivesOut](clipperprimitivesout.md) — The number of primitives the clip stage produces during a render pass.
- [fragmentInvocations](fragmentinvocations.md) — The number of times a render pass calls fragment shaders.
- [fragmentsPassed](fragmentspassed.md) — The number of fragments a render pass sends to the visibility and blend stages because they pass the scissor, depth, and stencil tests.

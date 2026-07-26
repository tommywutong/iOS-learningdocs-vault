---
title: 'init(tessellationInputPatches:vertexInvocations:postTessellationVertexInvocations:clipperInvocations:clipperPrimitivesOut:fragmentInvocations:fragmentsPassed:computeKernelInvocations:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcounterresultstatistic/init(tessellationinputpatches:vertexinvocations:posttessellationvertexinvocations:clipperinvocations:clipperprimitivesout:fragmentinvocations:fragmentspassed:computekernelinvocations:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcounterresultstatistic/init(tessellationinputpatches:vertexinvocations:posttessellationvertexinvocations:clipperinvocations:clipperprimitivesout:fragmentinvocations:fragmentspassed:computekernelinvocations:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounterresultstatistic/init%28tessellationinputpatches%3Avertexinvocations%3Aposttessellationvertexinvocations%3Aclipperinvocations%3Aclipperprimitivesout%3Afragmentinvocations%3Afragmentspassed%3Acomputekernelinvocations%3A%29.json'
content_hash: 'sha256:a3fc70fb8ae14f27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterResultStatistic](../mtlcounterresultstatistic.md)

# init(tessellationInputPatches:vertexInvocations:postTessellationVertexInvocations:clipperInvocations:clipperPrimitivesOut:fragmentInvocations:fragmentsPassed:computeKernelInvocations:)

<sub>Initializer</sub>

Creates a statistics result from statistic values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(tessellationInputPatches: UInt64, vertexInvocations: UInt64, postTessellationVertexInvocations: UInt64, clipperInvocations: UInt64, clipperPrimitivesOut: UInt64, fragmentInvocations: UInt64, fragmentsPassed: UInt64, computeKernelInvocations: UInt64)
```

## Parameters

- `tessellationInputPatches` — The number of tessellation patches the render pass sends to the tessellation stage.

- `vertexInvocations` — The number of times the render pass calls vertex shaders.

- `postTessellationVertexInvocations` — The number of vertices the tessellation stage creates.

- `clipperInvocations` — The number of primitives the clip stage consumes.

- `clipperPrimitivesOut` — The number of primitives the clip stage produces.

- `fragmentInvocations` — The number of times the render pass calls fragment shaders.

- `fragmentsPassed` — The number of fragments the render pass sends to the visibility and blend stages.

- `computeKernelInvocations` — The number of times the pass calls compute kernels.

## Discussion

Metal creates [MTLCounterResultStatistic](../mtlcounterresultstatistic.md) instances for you when you resolve the counter set’s data (see [Converting a GPU’s counter data into a readable format](../converting-a-gpus-counter-data-into-a-readable-format.md)). There’s no reason for you to manually create one in your app.

## See Also

### Swift support

- [init()](<init().md>) — Creates a default statistics result.

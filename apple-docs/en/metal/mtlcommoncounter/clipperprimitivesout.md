---
title: clipperPrimitivesOut
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommoncounter/clipperprimitivesout
source_url: 'https://developer.apple.com/documentation/metal/mtlcommoncounter/clipperprimitivesout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommoncounter/clipperprimitivesout.json'
content_hash: 'sha256:34218d32d5d0bee2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommonCounter](../mtlcommoncounter.md)

# clipperPrimitivesOut

<sub>Type Property</sub>

The common name for the counter that tracks the number of primitives the clip stage produces during a render pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let clipperPrimitivesOut: MTLCommonCounter
```

## See Also

### Common counter names

- [MTLCommonCounterTimestamp](timestamp.md) — The common name for the counter that tracks the current time.
- [MTLCommonCounterTessellationInputPatches](tessellationinputpatches.md) — The common name for the counter that tracks the number of tessellation patches a render pass sends to the tessellation stage.
- [MTLCommonCounterVertexInvocations](vertexinvocations.md) — The common name for the counter that tracks the number of times a render pass calls any vertex shader.
- [MTLCommonCounterPostTessellationVertexInvocations](posttessellationvertexinvocations.md) — The common name for the counter that tracks the number of vertices a render pass sends to a post-tessellation vertex shader.
- [MTLCommonCounterClipperInvocations](clipperinvocations.md) — The common name for the counter that tracks the number of primitives a render pass sends to the clip stage.
- [MTLCommonCounterFragmentInvocations](fragmentinvocations.md) — The common name for the counter that tracks the number of times a render pass calls fragment shaders.
- [MTLCommonCounterFragmentsPassed](fragmentspassed.md) — The common name for the counter that tracks the number of fragments a render pass sends to the visibility and blend stages.
- [MTLCommonCounterComputeKernelInvocations](computekernelinvocations.md) — The common name for the counter that tracks the number of times a pass invokes any compute kernel.
- [MTLCommonCounterTotalCycles](totalcycles.md) — The common name for the counter that tracks the total number of cycles the GPU uses to run a pass.
- [MTLCommonCounterVertexCycles](vertexcycles.md) — The common name for the counter that tracks the number of cycles the GPU uses to run vertex shaders during a pass.
- [MTLCommonCounterPostTessellationVertexCycles](posttessellationvertexcycles.md) — The common name for the counter that tracks the number of cycles the GPU uses to run post-tessellation vertex shaders during a pass.
- [MTLCommonCounterFragmentCycles](fragmentcycles.md) — The common name for the counter that tracks the number of cycles the GPU uses to run fragment shaders during a pass.
- [MTLCommonCounterTessellationCycles](tessellationcycles.md) — The common name for the counter that tracks the number of cycles the GPU uses to run the tessellation stage during a pass.
- [MTLCommonCounterRenderTargetWriteCycles](rendertargetwritecycles.md) — The common name for the counter that tracks the number of cycles the GPU uses to write data to render targets during a render pass.

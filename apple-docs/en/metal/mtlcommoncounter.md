---
title: MTLCommonCounter
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommoncounter
source_url: 'https://developer.apple.com/documentation/metal/mtlcommoncounter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommoncounter.json'
content_hash: 'sha256:454d82da8ade4af6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCommonCounter

<sub>Structure</sub>

The name of a specific counter that can appear in a GPU device’s counter sets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLCommonCounter
```

## Overview

This type defines the constants that let a GPU device declare which counters it supports within a counter set. For more information, see [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Common counter names

- [MTLCommonCounterTimestamp](mtlcommoncounter/timestamp.md) — The common name for the counter that tracks the current time.
- [MTLCommonCounterTessellationInputPatches](mtlcommoncounter/tessellationinputpatches.md) — The common name for the counter that tracks the number of tessellation patches a render pass sends to the tessellation stage.
- [MTLCommonCounterVertexInvocations](mtlcommoncounter/vertexinvocations.md) — The common name for the counter that tracks the number of times a render pass calls any vertex shader.
- [MTLCommonCounterPostTessellationVertexInvocations](mtlcommoncounter/posttessellationvertexinvocations.md) — The common name for the counter that tracks the number of vertices a render pass sends to a post-tessellation vertex shader.
- [MTLCommonCounterClipperInvocations](mtlcommoncounter/clipperinvocations.md) — The common name for the counter that tracks the number of primitives a render pass sends to the clip stage.
- [MTLCommonCounterClipperPrimitivesOut](mtlcommoncounter/clipperprimitivesout.md) — The common name for the counter that tracks the number of primitives the clip stage produces during a render pass.
- [MTLCommonCounterFragmentInvocations](mtlcommoncounter/fragmentinvocations.md) — The common name for the counter that tracks the number of times a render pass calls fragment shaders.
- [MTLCommonCounterFragmentsPassed](mtlcommoncounter/fragmentspassed.md) — The common name for the counter that tracks the number of fragments a render pass sends to the visibility and blend stages.
- [MTLCommonCounterComputeKernelInvocations](mtlcommoncounter/computekernelinvocations.md) — The common name for the counter that tracks the number of times a pass invokes any compute kernel.
- [MTLCommonCounterTotalCycles](mtlcommoncounter/totalcycles.md) — The common name for the counter that tracks the total number of cycles the GPU uses to run a pass.
- [MTLCommonCounterVertexCycles](mtlcommoncounter/vertexcycles.md) — The common name for the counter that tracks the number of cycles the GPU uses to run vertex shaders during a pass.
- [MTLCommonCounterPostTessellationVertexCycles](mtlcommoncounter/posttessellationvertexcycles.md) — The common name for the counter that tracks the number of cycles the GPU uses to run post-tessellation vertex shaders during a pass.
- [MTLCommonCounterFragmentCycles](mtlcommoncounter/fragmentcycles.md) — The common name for the counter that tracks the number of cycles the GPU uses to run fragment shaders during a pass.
- [MTLCommonCounterTessellationCycles](mtlcommoncounter/tessellationcycles.md) — The common name for the counter that tracks the number of cycles the GPU uses to run the tessellation stage during a pass.
- [MTLCommonCounterRenderTargetWriteCycles](mtlcommoncounter/rendertargetwritecycles.md) — The common name for the counter that tracks the number of cycles the GPU uses to write data to render targets during a render pass.

### Swift support

- [init(rawValue:)](<mtlcommoncounter/init(rawvalue_).md>) — Creates a common counter name from a raw value.

## See Also

### Counters and counter sets

- [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md) — Check whether a GPU produces the runtime performance data you want to sample.
- [MTLCounterSet](mtlcounterset.md) — A collection of individual counters a GPU device supports for a counter set.
- [MTLCommonCounterSet](mtlcommoncounterset.md) — The name of a specific counter set that a GPU device can support.
- [MTLCounter](mtlcounter.md) — An individual counter a GPU device lists within one of its counter sets.

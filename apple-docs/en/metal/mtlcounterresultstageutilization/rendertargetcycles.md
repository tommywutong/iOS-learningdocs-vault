---
title: renderTargetCycles
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcounterresultstageutilization/rendertargetcycles
source_url: 'https://developer.apple.com/documentation/metal/mtlcounterresultstageutilization/rendertargetcycles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounterresultstageutilization/rendertargetcycles.json'
content_hash: 'sha256:971ee75e47b0bb8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterResultStageUtilization](../mtlcounterresultstageutilization.md)

# renderTargetCycles

<sub>Instance Property</sub>

The number of cycles the GPU uses to write data to render targets during a render pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var renderTargetCycles: UInt64
```

## See Also

### Stage utilization values

- [totalCycles](totalcycles.md) — The total number of cycles the GPU uses to run a pass.
- [vertexCycles](vertexcycles.md) — The number of cycles the GPU uses to run vertex shaders during a pass.
- [tessellationCycles](tessellationcycles.md) — The number of cycles the GPU uses to run the tessellation stage during a pass.
- [postTessellationVertexCycles](posttessellationvertexcycles.md) — The number of cycles the GPU uses to run post-tessellation vertex shaders during a pass.
- [fragmentCycles](fragmentcycles.md) — The number of cycles the GPU uses to run fragment shaders during a pass.

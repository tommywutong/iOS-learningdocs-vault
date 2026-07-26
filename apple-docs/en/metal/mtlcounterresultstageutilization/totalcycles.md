---
title: totalCycles
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcounterresultstageutilization/totalcycles
source_url: 'https://developer.apple.com/documentation/metal/mtlcounterresultstageutilization/totalcycles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounterresultstageutilization/totalcycles.json'
content_hash: 'sha256:d914aaf30af516b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterResultStageUtilization](../mtlcounterresultstageutilization.md)

# totalCycles

<sub>Instance Property</sub>

The total number of cycles the GPU uses to run a pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var totalCycles: UInt64
```

## See Also

### Stage utilization values

- [vertexCycles](vertexcycles.md) — The number of cycles the GPU uses to run vertex shaders during a pass.
- [tessellationCycles](tessellationcycles.md) — The number of cycles the GPU uses to run the tessellation stage during a pass.
- [postTessellationVertexCycles](posttessellationvertexcycles.md) — The number of cycles the GPU uses to run post-tessellation vertex shaders during a pass.
- [fragmentCycles](fragmentcycles.md) — The number of cycles the GPU uses to run fragment shaders during a pass.
- [renderTargetCycles](rendertargetcycles.md) — The number of cycles the GPU uses to write data to render targets during a render pass.

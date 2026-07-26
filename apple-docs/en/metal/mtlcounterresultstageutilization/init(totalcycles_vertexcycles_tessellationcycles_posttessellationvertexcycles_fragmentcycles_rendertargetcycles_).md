---
title: 'init(totalCycles:vertexCycles:tessellationCycles:postTessellationVertexCycles:fragmentCycles:renderTargetCycles:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcounterresultstageutilization/init(totalcycles:vertexcycles:tessellationcycles:posttessellationvertexcycles:fragmentcycles:rendertargetcycles:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcounterresultstageutilization/init(totalcycles:vertexcycles:tessellationcycles:posttessellationvertexcycles:fragmentcycles:rendertargetcycles:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounterresultstageutilization/init%28totalcycles%3Avertexcycles%3Atessellationcycles%3Aposttessellationvertexcycles%3Afragmentcycles%3Arendertargetcycles%3A%29.json'
content_hash: 'sha256:7f65d40628535654'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterResultStageUtilization](../mtlcounterresultstageutilization.md)

# init(totalCycles:vertexCycles:tessellationCycles:postTessellationVertexCycles:fragmentCycles:renderTargetCycles:)

<sub>Initializer</sub>

Creates a stage-utilization result from utilization values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(totalCycles: UInt64, vertexCycles: UInt64, tessellationCycles: UInt64, postTessellationVertexCycles: UInt64, fragmentCycles: UInt64, renderTargetCycles: UInt64)
```

## Parameters

- `totalCycles` — The number of GPU cycles the entire render pass takes to run.

- `vertexCycles` — The number of GPU cycles the vertex shaders take to run.

- `tessellationCycles` — The number of GPU cycles the tessellating patches take to run.

- `postTessellationVertexCycles` — The number of GPU cycles the post-tessellation vertex shaders take to run.

- `fragmentCycles` — The number of GPU cycles the fragment shaders take to run.

- `renderTargetCycles` — The number of GPU cycles the pass takes writing data to render targets.

## Discussion

Metal creates [MTLCounterResultStageUtilization](../mtlcounterresultstageutilization.md) instances for you when you resolve the counter set’s data (see [Converting a GPU’s counter data into a readable format](../converting-a-gpus-counter-data-into-a-readable-format.md)). There’s no reason for you to manually create one in your app.

## See Also

### Swift support

- [init()](<init().md>) — Creates a default stage-utilization result.

---
title: init()
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcounterresultstageutilization/init()
source_url: 'https://developer.apple.com/documentation/metal/mtlcounterresultstageutilization/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounterresultstageutilization/init%28%29.json'
content_hash: 'sha256:b67c2f05c2b790d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterResultStageUtilization](../mtlcounterresultstageutilization.md)

# init()

<sub>Initializer</sub>

Creates a default stage-utilization result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init()
```

## Discussion

Metal creates [MTLCounterResultStageUtilization](../mtlcounterresultstageutilization.md) instances for you when you resolve the counter set’s data (see [Converting a GPU’s counter data into a readable format](../converting-a-gpus-counter-data-into-a-readable-format.md)). There’s no reason for you to manually create one in your app.

## See Also

### Swift support

- [init(totalCycles:vertexCycles:tessellationCycles:postTessellationVertexCycles:fragmentCycles:renderTargetCycles:)](<init(totalcycles_vertexcycles_tessellationcycles_posttessellationvertexcycles_fragmentcycles_rendertargetcycles_).md>) — Creates a stage-utilization result from utilization values.

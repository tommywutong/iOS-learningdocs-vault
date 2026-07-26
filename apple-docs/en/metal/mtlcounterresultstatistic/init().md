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
doc_path: /documentation/metal/mtlcounterresultstatistic/init()
source_url: 'https://developer.apple.com/documentation/metal/mtlcounterresultstatistic/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounterresultstatistic/init%28%29.json'
content_hash: 'sha256:1e090563387487f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterResultStatistic](../mtlcounterresultstatistic.md)

# init()

<sub>Initializer</sub>

Creates a default statistics result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init()
```

## Discussion

Metal creates [MTLCounterResultStatistic](../mtlcounterresultstatistic.md) instances for you when you resolve the counter set’s data (see [Converting a GPU’s counter data into a readable format](../converting-a-gpus-counter-data-into-a-readable-format.md)). There’s no reason for you to manually create one in your app.

## See Also

### Swift support

- [init(tessellationInputPatches:vertexInvocations:postTessellationVertexInvocations:clipperInvocations:clipperPrimitivesOut:fragmentInvocations:fragmentsPassed:computeKernelInvocations:)](<init(tessellationinputpatches_vertexinvocations_posttessellationvertexinvocations_clipperinvocations_clipperprimitivesout_fragmentinvocations_fragmentspassed_co-3af97d296b.md>) — Creates a statistics result from statistic values.

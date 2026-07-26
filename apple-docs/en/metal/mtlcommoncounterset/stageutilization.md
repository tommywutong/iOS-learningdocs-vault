---
title: stageUtilization
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommoncounterset/stageutilization
source_url: 'https://developer.apple.com/documentation/metal/mtlcommoncounterset/stageutilization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommoncounterset/stageutilization.json'
content_hash: 'sha256:1938e44f752d8cb0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommonCounterSet](../mtlcommoncounterset.md)

# stageUtilization

<sub>Type Property</sub>

The common name for the counter set that contains hardware utilization measurements from various render stages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let stageUtilization: MTLCommonCounterSet
```

## Discussion

The stage utilization counter set contains the following counters:

- [MTLCommonCounterTotalCycles](../mtlcommoncounter/totalcycles.md)
- [MTLCommonCounterVertexCycles](../mtlcommoncounter/vertexcycles.md)
- [MTLCommonCounterFragmentCycles](../mtlcommoncounter/fragmentcycles.md)
- [MTLCommonCounterTessellationCycles](../mtlcommoncounter/tessellationcycles.md)
- [MTLCommonCounterPostTessellationVertexCycles](../mtlcommoncounter/posttessellationvertexcycles.md)
- [MTLCommonCounterRenderTargetWriteCycles](../mtlcommoncounter/rendertargetwritecycles.md)

Use this name to check whether a GPU device supports the corresponding counter set (see [Confirming which counters and counter sets a GPU supports](../confirming-which-counters-and-counter-sets-a-gpu-supports.md)).

## See Also

### Common counter set names

- [MTLCommonCounterSetTimestamp](timestamp.md) — The common name for the counter set that contains the timestamp counter.
- [MTLCommonCounterSetStatistic](statistic.md) — The common name for the counter set that contains GPU workload statistics.

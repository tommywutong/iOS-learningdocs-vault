---
title: statistic
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommoncounterset/statistic
source_url: 'https://developer.apple.com/documentation/metal/mtlcommoncounterset/statistic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommoncounterset/statistic.json'
content_hash: 'sha256:4cef0f3117160d22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommonCounterSet](../mtlcommoncounterset.md)

# statistic

<sub>Type Property</sub>

The common name for the counter set that contains GPU workload statistics.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let statistic: MTLCommonCounterSet
```

## Discussion

The statistics counter set contains the following counters:

- [MTLCommonCounterComputeKernelInvocations](../mtlcommoncounter/computekernelinvocations.md)
- [MTLCommonCounterVertexInvocations](../mtlcommoncounter/vertexinvocations.md)
- [MTLCommonCounterFragmentInvocations](../mtlcommoncounter/fragmentinvocations.md)
- [MTLCommonCounterFragmentsPassed](../mtlcommoncounter/fragmentspassed.md)
- [MTLCommonCounterTessellationInputPatches](../mtlcommoncounter/tessellationinputpatches.md)
- [MTLCommonCounterPostTessellationVertexInvocations](../mtlcommoncounter/posttessellationvertexinvocations.md)
- [MTLCommonCounterClipperInvocations](../mtlcommoncounter/clipperinvocations.md)
- [MTLCommonCounterClipperPrimitivesOut](../mtlcommoncounter/clipperprimitivesout.md)

Use this name to check whether a GPU device supports the corresponding counter set (see [Confirming which counters and counter sets a GPU supports](../confirming-which-counters-and-counter-sets-a-gpu-supports.md)).

## See Also

### Common counter set names

- [MTLCommonCounterSetTimestamp](timestamp.md) — The common name for the counter set that contains the timestamp counter.
- [MTLCommonCounterSetStageUtilization](stageutilization.md) — The common name for the counter set that contains hardware utilization measurements from various render stages.

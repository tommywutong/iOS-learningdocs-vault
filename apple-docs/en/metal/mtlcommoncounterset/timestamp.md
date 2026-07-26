---
title: timestamp
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommoncounterset/timestamp
source_url: 'https://developer.apple.com/documentation/metal/mtlcommoncounterset/timestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommoncounterset/timestamp.json'
content_hash: 'sha256:7cba9b90d3c7403c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommonCounterSet](../mtlcommoncounterset.md)

# timestamp

<sub>Type Property</sub>

The common name for the counter set that contains the timestamp counter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let timestamp: MTLCommonCounterSet
```

## Discussion

The [MTLCommonCounterSetTimestamp](timestamp.md) counter set contains the [MTLCommonCounterTimestamp](../mtlcommoncounter/timestamp.md) counter. Use this name to check whether a GPU device supports the corresponding counter set (see [Confirming which counters and counter sets a GPU supports](../confirming-which-counters-and-counter-sets-a-gpu-supports.md)).

## See Also

### Common counter set names

- [MTLCommonCounterSetStageUtilization](stageutilization.md) — The common name for the counter set that contains hardware utilization measurements from various render stages.
- [MTLCommonCounterSetStatistic](statistic.md) — The common name for the counter set that contains GPU workload statistics.

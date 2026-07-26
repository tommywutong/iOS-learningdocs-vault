---
title: MTLCommonCounterSet
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommoncounterset
source_url: 'https://developer.apple.com/documentation/metal/mtlcommoncounterset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommoncounterset.json'
content_hash: 'sha256:8ce8501b188bce55'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCommonCounterSet

<sub>Structure</sub>

The name of a specific counter set that a GPU device can support.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLCommonCounterSet
```

## Overview

This type defines the constants that let a GPU device declare which counter sets it supports.

> [!important] Important
> Some GPUs may only support some of the counters within a counter set.

For more information, see [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Common counter set names

- [MTLCommonCounterSetTimestamp](mtlcommoncounterset/timestamp.md) — The common name for the counter set that contains the timestamp counter.
- [MTLCommonCounterSetStageUtilization](mtlcommoncounterset/stageutilization.md) — The common name for the counter set that contains hardware utilization measurements from various render stages.
- [MTLCommonCounterSetStatistic](mtlcommoncounterset/statistic.md) — The common name for the counter set that contains GPU workload statistics.

### Swift support

- [init(rawValue:)](<mtlcommoncounterset/init(rawvalue_).md>) — Creates a common counter set name from a raw value.

## See Also

### Counters and counter sets

- [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md) — Check whether a GPU produces the runtime performance data you want to sample.
- [MTLCounterSet](mtlcounterset.md) — A collection of individual counters a GPU device supports for a counter set.
- [MTLCounter](mtlcounter.md) — An individual counter a GPU device lists within one of its counter sets.
- [MTLCommonCounter](mtlcommoncounter.md) — The name of a specific counter that can appear in a GPU device’s counter sets.

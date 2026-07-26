---
title: MTLCounterErrorValue
framework: Metal
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcountererrorvalue
source_url: 'https://developer.apple.com/documentation/metal/mtlcountererrorvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountererrorvalue.json'
content_hash: 'sha256:830d1d9e8a39bb16'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCounterErrorValue

<sub>Global Variable</sub>

A sentinel value for an entry in a counter sample buffer that indicates the entry’s data is invalid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var MTLCounterErrorValue: UInt64 { get }
```

## Discussion

A GPU driver typically sets entries to this value when it encounters an error resolving a counter’s data. The driver also uses this value for counters it doesn’t support within a counter set (see [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md)).

## See Also

### Counter sample data output

- [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md) — Inspect and use the data within a GPU’s counter sample buffer by resolving it into a standard format.
- [MTLCounterResultTimestamp](mtlcounterresulttimestamp.md) — The data structure for storing the data you resolve from a timestamp counter set.
- [MTLCounterResultStatistic](mtlcounterresultstatistic.md) — The data structure for storing the data you resolve from a statistic counter set.
- [MTLCounterResultStageUtilization](mtlcounterresultstageutilization.md) — The data structure for storing the data you resolve from a stage-utilization counter set.

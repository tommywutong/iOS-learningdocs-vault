---
title: MTLCounterResultTimestamp
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcounterresulttimestamp
source_url: 'https://developer.apple.com/documentation/metal/mtlcounterresulttimestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounterresulttimestamp.json'
content_hash: 'sha256:ffe19865d272e7d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCounterResultTimestamp

<sub>Structure</sub>

The data structure for storing the data you resolve from a timestamp counter set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLCounterResultTimestamp
```

## Overview

For steps that explain how to resolve data from a counter set, such as [timestamp](mtlcounterresulttimestamp/timestamp.md), see [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Timestamp values

- [timestamp](mtlcounterresulttimestamp/timestamp.md) — A timestamp value from a GPU at a particular point in time during an operation, typically at the beginning or ending of a render stage.

### Swift support

- [init()](<mtlcounterresulttimestamp/init().md>) — Creates a default timestamp result.
- [init(timestamp:)](<mtlcounterresulttimestamp/init(timestamp_).md>) — Creates a timestamp result from a value.

## See Also

### Counter sample data output

- [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md) — Inspect and use the data within a GPU’s counter sample buffer by resolving it into a standard format.
- [MTLCounterResultStatistic](mtlcounterresultstatistic.md) — The data structure for storing the data you resolve from a statistic counter set.
- [MTLCounterResultStageUtilization](mtlcounterresultstageutilization.md) — The data structure for storing the data you resolve from a stage-utilization counter set.
- [MTLCounterErrorValue](mtlcountererrorvalue.md) — A sentinel value for an entry in a counter sample buffer that indicates the entry’s data is invalid.

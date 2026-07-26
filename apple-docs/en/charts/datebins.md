---
title: DateBins
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/datebins
source_url: 'https://developer.apple.com/documentation/charts/datebins'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/datebins.json'
content_hash: 'sha256:985fd73c506bd5fa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# DateBins

<sub>Structure</sub>

A collection of bins for a chart that plots data against dates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DateBins
```

## Relationships

- **Conforms To**: [Collection](../swift/collection.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Sequence](../swift/sequence.md)

## Topics

### Initializers

- [init(data:desiredCount:calendar:)](<datebins/init(data_desiredcount_calendar_).md>) — Automatically determine the bins from data.
- [init(range:desiredCount:calendar:)](<datebins/init(range_desiredcount_calendar_).md>) — Automatically determine the bins from a range of data.
- [init(thresholds:)](<datebins/init(thresholds_).md>) — Creates N-1 bins with the given N `thresholds`.
- [init(timeInterval:range:)](<datebins/init(timeinterval_range_).md>) — Creates uniform bins covering the given range. The first bin starts at the lower bound of the range.
- [init(unit:by:range:calendar:)](<datebins/init(unit_by_range_calendar_).md>) — Creates uniform bins covering the given range.

### Instance Properties

- [thresholds](datebins/thresholds.md) — Find the bin thresholds.

### Instance Methods

- [index(for:)](<datebins/index(for_).md>) — Returns the bin index for the given value.

## See Also

### Data bins

- [NumberBins](numberbins.md) — A collection of bins for a chart that plots data against numbers.
- [ChartBinRange](chartbinrange.md) — The range of data that a single bin of a chart represents.

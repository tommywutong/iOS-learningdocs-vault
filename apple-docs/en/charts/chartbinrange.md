---
title: ChartBinRange
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/chartbinrange
source_url: 'https://developer.apple.com/documentation/charts/chartbinrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartbinrange.json'
content_hash: 'sha256:4dbce693980c6378'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# ChartBinRange

<sub>Structure</sub>

The range of data that a single bin of a chart represents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ChartBinRange<Bound> where Bound : Comparable
```

## Overview

All bins except the last for a particular chart represent an open range, meaning that the range doesn’t include the upper bound. The last range of the last bin is closed, so that it does include the upper bound. The system keeps track of the open or closed state of a particular range.

## Relationships

- **Conforms To**: [RangeExpression](../swift/rangeexpression.md)

## Topics

### Instance Properties

- [lowerBound](chartbinrange/lowerbound.md)
- [upperBound](chartbinrange/upperbound.md)

## See Also

### Data bins

- [NumberBins](numberbins.md) — A collection of bins for a chart that plots data against numbers.
- [DateBins](datebins.md) — A collection of bins for a chart that plots data against dates.

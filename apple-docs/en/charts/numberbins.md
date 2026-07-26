---
title: NumberBins
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/numberbins
source_url: 'https://developer.apple.com/documentation/charts/numberbins'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/numberbins.json'
content_hash: 'sha256:dad0be7520a2591c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# NumberBins

<sub>Structure</sub>

A collection of bins for a chart that plots data against numbers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NumberBins<Value> where Value : Comparable, Value : Numeric
```

## Relationships

- **Conforms To**: [Collection](../swift/collection.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Sequence](../swift/sequence.md)

## Topics

### Initializers

- [init(data:desiredCount:minimumStride:)](<numberbins/init(data_desiredcount_minimumstride_)-3txi5.md>) — Automatically determine the bins from data.
- [init(data:desiredCount:minimumStride:)](<numberbins/init(data_desiredcount_minimumstride_)-8pvv7.md>) — Automatically determine the bins from data.
- [init(range:count:)](<numberbins/init(range_count_)-6hip8.md>) — Creates the given number of bins for the range. Expects that the range length is a multiple of `count` to allow uniform integer bins.
- [init(range:count:)](<numberbins/init(range_count_)-7975l.md>) — Creates the given number of bins for the range.
- [init(range:desiredCount:minimumStride:)](<numberbins/init(range_desiredcount_minimumstride_)-32ok2.md>) — Automatically determine the bins from a range of data.
- [init(range:desiredCount:minimumStride:)](<numberbins/init(range_desiredcount_minimumstride_)-4qxfa.md>) — Automatically determine the bins from a range of data.
- [init(size:range:)](<numberbins/init(size_range_)-3ach2.md>) — Creates uniform bins covering the given range.
- [init(size:range:)](<numberbins/init(size_range_)-5me6y.md>) — Creates uniform bins covering the given range.
- [init(thresholds:)](<numberbins/init(thresholds_).md>) — Creates N-1 bins with the given N `thresholds`.

### Instance Properties

- [thresholds](numberbins/thresholds.md) — Find the bin thresholds.

### Instance Methods

- [index(for:)](<numberbins/index(for_).md>) — Returns the bin index for the given value.

## See Also

### Data bins

- [DateBins](datebins.md) — A collection of bins for a chart that plots data against dates.
- [ChartBinRange](chartbinrange.md) — The range of data that a single bin of a chart represents.

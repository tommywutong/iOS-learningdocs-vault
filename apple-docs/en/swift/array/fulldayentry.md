---
title: fullDayEntry
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: /documentation/swift/array/fulldayentry
source_url: 'https://developer.apple.com/documentation/swift/array/fulldayentry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/fulldayentry.json'
content_hash: 'sha256:bc0028dcbd603579'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# fullDayEntry

<sub>Instance Property</sub>

The full day interval entry spanning the entire report collection period.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var fullDayEntry: MetricReport.IntervalEntry { get }
```

## Discussion

This entry contains metrics aggregated across the entire aggregation period while other interval entries represent breakdowns within that period.

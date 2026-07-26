---
title: 'init(unit:by:range:calendar:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/datebins/init(unit:by:range:calendar:)'
source_url: 'https://developer.apple.com/documentation/charts/datebins/init(unit:by:range:calendar:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/datebins/init%28unit%3Aby%3Arange%3Acalendar%3A%29.json'
content_hash: 'sha256:67cbda395e75b1a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [DateBins](../datebins.md)

# init(unit:by:range:calendar:)

<sub>Initializer</sub>

Creates uniform bins covering the given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(unit: Calendar.Component, by stride: Int = 1, range: ClosedRange<Date>, calendar: Calendar = .autoupdatingCurrent)
```

## Parameters

- `unit` — The size of the bins.

- `stride` — The number of components for each bin.

- `range` — The range of the data the bins cover.

- `calendar` — The calendar to use.

## Return Value

The bins.

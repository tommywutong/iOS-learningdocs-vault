---
title: 'init(range:desiredCount:calendar:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/datebins/init(range:desiredcount:calendar:)'
source_url: 'https://developer.apple.com/documentation/charts/datebins/init(range:desiredcount:calendar:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/datebins/init%28range%3Adesiredcount%3Acalendar%3A%29.json'
content_hash: 'sha256:a7774bc15af34316'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [DateBins](../datebins.md)

# init(range:desiredCount:calendar:)

<sub>Initializer</sub>

Automatically determine the bins from a range of data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(range: ClosedRange<Date>, desiredCount: Int = 10, calendar: Calendar = .autoupdatingCurrent)
```

## Parameters

- `range` — The range the bins should cover.

- `desiredCount` — The desired number of bins for the given data.

## Return Value

The inferred bins.

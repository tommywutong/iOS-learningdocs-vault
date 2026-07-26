---
title: 'init(data:desiredCount:calendar:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/datebins/init(data:desiredcount:calendar:)'
source_url: 'https://developer.apple.com/documentation/charts/datebins/init(data:desiredcount:calendar:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/datebins/init%28data%3Adesiredcount%3Acalendar%3A%29.json'
content_hash: 'sha256:47177a4da8f239a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [DateBins](../datebins.md)

# init(data:desiredCount:calendar:)

<sub>Initializer</sub>

Automatically determine the bins from data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(data: [Date], desiredCount: Int? = nil, calendar: Calendar = .autoupdatingCurrent)
```

## Parameters

- `data` — The given data values.

- `desiredCount` — The desired number of bins for the given data. If `nil`, infer the number of bins automatically from data using [Scott’s normal reference rule](https://doi.org/10.1093/biomet/66.3.605) capped at 200.

## Return Value

The inferred bins.

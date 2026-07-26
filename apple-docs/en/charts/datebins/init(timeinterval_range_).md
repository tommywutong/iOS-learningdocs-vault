---
title: 'init(timeInterval:range:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/datebins/init(timeinterval:range:)'
source_url: 'https://developer.apple.com/documentation/charts/datebins/init(timeinterval:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/datebins/init%28timeinterval%3Arange%3A%29.json'
content_hash: 'sha256:bdb35fdd7a55eb78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [DateBins](../datebins.md)

# init(timeInterval:range:)

<sub>Initializer</sub>

Creates uniform bins covering the given range. The first bin starts at the lower bound of the range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(timeInterval: TimeInterval, range: ClosedRange<Date>)
```

## Parameters

- `timeInterval` — The size of the bins.

- `range` — The range of the data the bins cover.

## Return Value

The bins.

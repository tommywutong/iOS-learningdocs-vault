---
title: 'init(size:range:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/numberbins/init(size:range:)-5me6y'
source_url: 'https://developer.apple.com/documentation/charts/numberbins/init(size:range:)-5me6y'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/numberbins/init%28size%3Arange%3A%29-5me6y.json'
content_hash: 'sha256:8d9672c48ad4a9e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [NumberBins](../numberbins.md)

# init(size:range:)

<sub>Initializer</sub>

Creates uniform bins covering the given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(size: Value, range: ClosedRange<Value>) where Value : BinaryInteger
```

## Parameters

- `size` — The size of the bins.

- `range` — The range of the data the bins cover.

## Return Value

The bins.

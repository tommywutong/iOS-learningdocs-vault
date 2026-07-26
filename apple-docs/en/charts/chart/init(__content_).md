---
title: 'init(_:content:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chart/init(_:content:)'
source_url: 'https://developer.apple.com/documentation/charts/chart/init(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chart/init%28_%3Acontent%3A%29.json'
content_hash: 'sha256:f558016328d9200c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [Chart](../chart.md)

# init(_:content:)

<sub>Initializer</sub>

Creates a chart composed of a series of identifiable marks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<Data, C>(_ data: Data, @ContentBuilder content: @escaping (Data.Element) -> C) where Content == ForEach<Data, Data.Element.ID, C>, Data : RandomAccessCollection, C : ChartContent, Data.Element : Identifiable
```

## Parameters

- `data` — A collection of data that conforms to the [Identifiable](../../swift/identifiable.md) protocol.

- `content` — The mark that the chart should draw for each element in the data collection.

## Discussion

This initializer wraps the data that you provide as input in an implicit [ForEach](../../swiftui/foreach.md) structure. If you need to represent more than one series in your chart, use [init(content:)](<init(content_).md>) instead.

## See Also

### Creating a chart

- [init(content:)](<init(content_).md>) — Creates a chart composed of any number of data series and individual marks.
- [init(_:id:content:)](<init(__id_content_).md>) — Creates a chart composed of a series of marks.

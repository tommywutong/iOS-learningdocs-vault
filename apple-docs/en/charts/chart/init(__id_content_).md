---
title: 'init(_:id:content:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chart/init(_:id:content:)'
source_url: 'https://developer.apple.com/documentation/charts/chart/init(_:id:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chart/init%28_%3Aid%3Acontent%3A%29.json'
content_hash: 'sha256:d0d94bcc27b8e84b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [Chart](../chart.md)

# init(_:id:content:)

<sub>Initializer</sub>

Creates a chart composed of a series of marks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<Data, ID, C>(_ data: Data, id: KeyPath<Data.Element, ID>, @ContentBuilder content: @escaping (Data.Element) -> C) where Content == ForEach<Data, ID, C>, Data : RandomAccessCollection, ID : Hashable, C : ChartContent
```

## Parameters

- `data` — A collection of data.

- `id` — A key path that represents a property of each data element that can act as a unique identifier for that element. Ensure that this property conforms to the [Hashable](../../swift/hashable.md) protocol.

- `content` — The mark that the chart should draw for each element in the data collection.

## Discussion

This initializer wraps the data that you provide as input in an implicit [ForEach](../../swiftui/foreach.md) structure. If you need to represent more than one series in your chart, use [init(content:)](<init(content_).md>) instead.

## See Also

### Creating a chart

- [init(content:)](<init(content_).md>) — Creates a chart composed of any number of data series and individual marks.
- [init(_:content:)](<init(__content_).md>) — Creates a chart composed of a series of identifiable marks.

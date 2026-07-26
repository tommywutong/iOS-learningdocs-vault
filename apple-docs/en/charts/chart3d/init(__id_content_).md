---
title: 'init(_:id:content:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chart3d/init(_:id:content:)'
source_url: 'https://developer.apple.com/documentation/charts/chart3d/init(_:id:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chart3d/init%28_%3Aid%3Acontent%3A%29.json'
content_hash: 'sha256:3ae15718a75f480d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [Chart3D](../chart3d.md)

# init(_:id:content:)

<sub>Initializer</sub>

Creates a 3D chart composed of a series of marks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init<Data, ID, C>(_ data: Data, id: KeyPath<Data.Element, ID>, @Chart3DContentBuilder content: @escaping (Data.Element) -> C) where Content == ForEach<Data, ID, C>, Data : RandomAccessCollection, ID : Hashable, C : Chart3DContent
```

## Parameters

- `data` — A collection of data.

- `id` — A key path that represents a property of each data element that can act as a unique identifier for that element. Ensure that this property conforms to the [Hashable](../../swift/hashable.md) protocol.

- `content` — The mark that the chart should draw for each element in the data collection.

## Discussion

This initializer wraps the data that you provide as input in an implicit [ForEach](../../swiftui/foreach.md) structure. If you need to represent more than one series in your chart, use [init(content:)](<init(content_).md>) instead.

## See Also

### Creating 3D charts

- [init(_:content:)](<init(__content_).md>) — Creates a 3D chart composed of a series of identifiable marks.
- [init(content:)](<init(content_).md>)

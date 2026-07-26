---
title: 'init(_:content:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chart3d/init(_:content:)'
source_url: 'https://developer.apple.com/documentation/charts/chart3d/init(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chart3d/init%28_%3Acontent%3A%29.json'
content_hash: 'sha256:0e890abb7627257e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [Chart3D](../chart3d.md)

# init(_:content:)

<sub>Initializer</sub>

Creates a 3D chart composed of a series of identifiable marks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init<Data, C>(_ data: Data, @Chart3DContentBuilder content: @escaping (Data.Element) -> C) where Content == ForEach<Data, Data.Element.ID, C>, Data : RandomAccessCollection, C : Chart3DContent, Data.Element : Identifiable
```

## Parameters

- `data` — A collection of data that conforms to the [Identifiable](../../swift/identifiable.md) protocol.

- `content` — The mark that the chart should draw for each element in the data collection.

## Discussion

This initializer wraps the data that you provide as input in an implicit [ForEach](../../swiftui/foreach.md) structure. If you need to represent more than one series in your chart, use [init(content:)](<init(content_).md>) instead.

## See Also

### Creating 3D charts

- [init(_:id:content:)](<init(__id_content_).md>) — Creates a 3D chart composed of a series of marks.
- [init(content:)](<init(content_).md>)

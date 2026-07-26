---
title: 'init(_:id:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/slidertickcontentforeach/init(_:id:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/slidertickcontentforeach/init(_:id:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/slidertickcontentforeach/init%28_%3Aid%3Acontent%3A%29.json'
content_hash: 'sha256:bfc8f192001b2b8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SliderTickContentForEach](../slidertickcontentforeach.md)

# init(_:id:content:)

<sub>Initializer</sub>

Creates an instance that uniquely identifies and creates slider ticks across updates based on the provided key path to the underlying data’s identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init<V>(_ data: Data, id: KeyPath<Data.Element, ID>, @SliderTickBuilder<V> content: @escaping (Data.Element) -> Content) where V == Data.Element, Data.Element == Content.Value
```

## Parameters

- `data` — The data that the [ForEach](../foreach.md) instance uses to create mark items dynamically.

- `id` — The key path to the provided data’s identifier.

- `content` — The builder that creates ticks dynamically.

## Discussion

It’s important that the `id` of a data element doesn’t change, unless SwiftUI considers the data element to have been replaced with a new data element that has a new identity. If the `id` of a data element changes, then the marks generated from that data element will lose any current state and animations.

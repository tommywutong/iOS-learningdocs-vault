---
title: 'init(_:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/slidertickcontentforeach/init(_:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/slidertickcontentforeach/init(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/slidertickcontentforeach/init%28_%3Acontent%3A%29.json'
content_hash: 'sha256:07346a6597c8c01d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SliderTickContentForEach](../slidertickcontentforeach.md)

# init(_:content:)

<sub>Initializer</sub>

Creates an instance that uniquely identifies and creates slider ticks across updates based on the identity of the underlying data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init<V>(_ data: Data, @SliderTickBuilder<V> content: @escaping (Data.Element) -> Content) where ID == V.ID, V : Identifiable, V == Data.Element, Data.Element == Content.Value
```

## Parameters

- `data` — The identified data that the [ForEach](../foreach.md) instance uses to create slider ticks dynamically.

- `content` — The builder that creates ticks dynamically for each element.

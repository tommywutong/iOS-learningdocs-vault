---
title: 'init(_:id:content:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/foreach/init(_:id:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/foreach/init(_:id:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/foreach/init%28_%3Aid%3Acontent%3A%29.json'
content_hash: 'sha256:f079ef862605e3ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ForEach](../foreach.md)

# init(_:id:content:)

<sub>Initializer</sub>

Creates an instance that uniquely identifies and creates map content across updates based on the provided key path to the underlying data’s identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor init(_ data: Data, id: KeyPath<Data.Element, ID>, @MapContentBuilder content: @escaping (Data.Element) -> Content)
```

## Parameters

- `data` — The data that the [ForEach](../foreach.md) instance uses to create map content dynamically.

- `id` — The key path to the provided data’s identifier.

- `content` — The map content builder that creates map content dynamically.

## Discussion

It’s important that the `id` of a data element doesn’t change, unless the data element has been replaced with a new data element that has a new identity. If the `id` of a data element changes, then the map content generated from that data element will lose any current state and animations.

## See Also

### Creating a collection

- [init(_:)](<init(__).md>) — Creates an instance that uniquely identifies and creates table rows across updates based on the identity of the underlying data.
- [init(_:content:)](<init(__content_).md>) — Creates an instance that uniquely identifies and creates map content across updates based on the identity of the underlying data.
- [init(sections:content:)](<init(sections_content_).md>) — Creates an instance that uniquely identifies and creates views across updates based on the sections of a given view.
- [init(subviews:content:)](<init(subviews_content_).md>) — Creates an instance that uniquely identifies and creates views across updates based on the subviews of a given view.

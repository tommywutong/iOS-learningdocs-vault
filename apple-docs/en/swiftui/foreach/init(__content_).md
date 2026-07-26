---
title: 'init(_:content:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/foreach/init(_:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/foreach/init(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/foreach/init%28_%3Acontent%3A%29.json'
content_hash: 'sha256:2d15297512590f16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ForEach](../foreach.md)

# init(_:content:)

<sub>Initializer</sub>

Creates an instance that uniquely identifies and creates map content across updates based on the identity of the underlying data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor init(_ data: Data, @MapContentBuilder content: @escaping (Data.Element) -> Content) where ID == Data.Element.ID, Data.Element : Identifiable
```

## Parameters

- `data` — The identified data that the [ForEach](../foreach.md) instance uses to create map content dynamically.

- `content` — The map content builder that creates map content dynamically.

## Discussion

It’s important that the `id` of a data element doesn’t change unless you replace the data element with a new data element that has a new identity. If the `id` of a data element changes, the content view generated from that data element loses any current state and animations.

## See Also

### Creating a collection

- [init(_:)](<init(__).md>) — Creates an instance that uniquely identifies and creates table rows across updates based on the identity of the underlying data.
- [init(_:id:content:)](<init(__id_content_).md>) — Creates an instance that uniquely identifies and creates map content across updates based on the provided key path to the underlying data’s identifier.
- [init(sections:content:)](<init(sections_content_).md>) — Creates an instance that uniquely identifies and creates views across updates based on the sections of a given view.
- [init(subviews:content:)](<init(subviews_content_).md>) — Creates an instance that uniquely identifies and creates views across updates based on the subviews of a given view.

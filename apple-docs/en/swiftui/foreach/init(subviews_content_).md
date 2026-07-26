---
title: 'init(subviews:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/foreach/init(subviews:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/foreach/init(subviews:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/foreach/init%28subviews%3Acontent%3A%29.json'
content_hash: 'sha256:702c9e23a6376a05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ForEach](../foreach.md)

# init(subviews:content:)

<sub>Initializer</sub>

Creates an instance that uniquely identifies and creates views across updates based on the subviews of a given view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<V>(subviews view: V, @ContentBuilder content: @escaping (Subview) -> Content) where Data == ForEachSubviewCollection<Content>, ID == Subview.ID, Content : View, V : View
```

## Parameters

- `view` — The view to extract the subviews of.

- `content` — The content builder that creates views from subviews.

## Discussion

Subviews are proxies to the resolved view they represent, meaning that modifiers applied to the original view will be applied before modifiers applied to the subview, and the view is resolved using the environment of its container, _not_ the environment of the its subview proxy. Additionally, because subviews must represent a single leaf view, or container, a subview may represent a view after the application of styles. As such, attempting to apply a style to it may have no effect.

## See Also

### Creating a collection

- [init(_:)](<init(__).md>) — Creates an instance that uniquely identifies and creates table rows across updates based on the identity of the underlying data.
- [init(_:content:)](<init(__content_).md>) — Creates an instance that uniquely identifies and creates map content across updates based on the identity of the underlying data.
- [init(_:id:content:)](<init(__id_content_).md>) — Creates an instance that uniquely identifies and creates map content across updates based on the provided key path to the underlying data’s identifier.
- [init(sections:content:)](<init(sections_content_).md>) — Creates an instance that uniquely identifies and creates views across updates based on the sections of a given view.

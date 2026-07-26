---
title: 'init(destination:isActive:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（16.0 起废弃）, iPadOS 13.0+（16.0 起废弃）, Mac Catalyst 13.0+（16.0 起废弃）, macOS 10.15+（13.0 起废弃）, tvOS 13.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 6.0+（9.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/navigationlink/init(destination:isactive:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationlink/init(destination:isactive:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationlink/init%28destination%3Aisactive%3Alabel%3A%29.json'
content_hash: 'sha256:f571361419a45cf2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationLink](../navigationlink.md)

# init(destination:isActive:label:)

<sub>Initializer</sub>

Creates a navigation link that presents the destination view when active.

> [!warning] Deprecated
> Use [init(value:label:)](<init(value_label_)-3qb8y.md>) instead. For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(destination: Destination, isActive: Binding<Bool>, @ContentBuilder label: () -> Label)
```

## Parameters

- `destination` — A view for the navigation link to present.

- `isActive` — A binding to a Boolean value that indicates whether `destination` is currently presented.

- `label` — A content builder to produce a label describing the `destination` to present.

## See Also

### Creating links with view arguments

- [init(_:destination:isActive:)](<init(__destination_isactive_).md>) — Creates a navigation link that presents a destination view when active, with a text label that the link generates from a localized string key. _(deprecated)_
- [init(_:destination:tag:selection:)](<init(__destination_tag_selection_).md>) — Creates a navigation link that presents a destination view when a bound selection variable matches a value you provide, using a text label that the link generates from a title string. _(deprecated)_
- [init(destination:tag:selection:label:)](<init(destination_tag_selection_label_).md>) — Creates a navigation link that presents the destination view when a bound selection variable equals a given tag value. _(deprecated)_

---
title: 'init(_:destination:isActive:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（16.0 起废弃）, iPadOS 13.0+（16.0 起废弃）, Mac Catalyst 13.0+（16.0 起废弃）, macOS 10.15+（13.0 起废弃）, tvOS 13.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 6.0+（9.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/navigationlink/init(_:destination:isactive:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationlink/init(_:destination:isactive:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationlink/init%28_%3Adestination%3Aisactive%3A%29.json'
content_hash: 'sha256:e3614c9c283986d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationLink](../navigationlink.md)

# init(_:destination:isActive:)

<sub>Initializer</sub>

Creates a navigation link that presents a destination view when active, with a text label that the link generates from a localized string key.

> [!warning] Deprecated
> Use [init(_:value:)](<init(__value_)-810b2.md>) instead. For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ titleKey: LocalizedStringKey, destination: Destination, isActive: Binding<Bool>)
```

## Parameters

- `titleKey` — A localized string key for creating a text label.

- `destination` — A view for the navigation link to present.

- `isActive` — A binding to a Boolean value that indicates whether `destination` is currently presented.

## See Also

### Creating links with view arguments

- [init(destination:isActive:label:)](<init(destination_isactive_label_).md>) — Creates a navigation link that presents the destination view when active. _(deprecated)_
- [init(_:destination:tag:selection:)](<init(__destination_tag_selection_).md>) — Creates a navigation link that presents a destination view when a bound selection variable matches a value you provide, using a text label that the link generates from a title string. _(deprecated)_
- [init(destination:tag:selection:label:)](<init(destination_tag_selection_label_).md>) — Creates a navigation link that presents the destination view when a bound selection variable equals a given tag value. _(deprecated)_

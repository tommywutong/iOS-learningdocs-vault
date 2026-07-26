---
title: 'init(_:tag:selection:destination:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（16.0 起废弃）, iPadOS 13.0+（16.0 起废弃）, Mac Catalyst 13.0+（16.0 起废弃）, macOS 10.15+（13.0 起废弃）, tvOS 13.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 6.0+（9.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/navigationlink/init(_:tag:selection:destination:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationlink/init(_:tag:selection:destination:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationlink/init%28_%3Atag%3Aselection%3Adestination%3A%29.json'
content_hash: 'sha256:533bad993009879a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationLink](../navigationlink.md)

# init(_:tag:selection:destination:)

<sub>Initializer</sub>

Creates a navigation link that presents a destination view when a bound selection variable matches a value you provide, using a text label that the link generates from a title string.

> [!warning] Deprecated
> Use [init(_:value:)](<init(__value_)-9ziux.md>) inside a [List](../list.md) within a [NavigationStack](../navigationstack.md) or [NavigationSplitView](../navigationsplitview.md). For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init<S, V>(_ title: S, tag: V, selection: Binding<V?>, @ContentBuilder destination: () -> Destination) where S : StringProtocol, V : Hashable
```

## Parameters

- `title` — A string for creating a text label.

- `tag` — The value of `selection` that causes the link to present `destination`.

- `selection` — A bound variable that causes the link to present `destination` when `selection` becomes equal to `tag`.

- `destination` — A view for the navigation link to present.

## See Also

### Creating links with content builders

- [init(_:isActive:destination:)](<init(__isactive_destination_).md>) — Creates a navigation link that presents a destination view when active, with a text label that the link generates from a localized string key. _(deprecated)_
- [init(isActive:destination:label:)](<init(isactive_destination_label_).md>) — Creates a navigation link that presents the destination view when active. _(deprecated)_
- [init(tag:selection:destination:label:)](<init(tag_selection_destination_label_).md>) — Creates a navigation link that presents the destination view when a bound selection variable equals a given tag value. _(deprecated)_

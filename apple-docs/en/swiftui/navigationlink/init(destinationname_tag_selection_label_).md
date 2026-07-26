---
title: 'init(destinationName:tag:selection:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/navigationlink/init(destinationname:tag:selection:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationlink/init(destinationname:tag:selection:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationlink/init%28destinationname%3Atag%3Aselection%3Alabel%3A%29.json'
content_hash: 'sha256:7cc8603d0af89b72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationLink](../navigationlink.md)

# init(destinationName:tag:selection:label:)

<sub>Initializer</sub>

Creates a navigation link that presents a view from a WatchKit storyboard when a bound selection variable matches a value you provide.

> [!warning] Deprecated
> Use [init(value:label:)](<init(value_label_)-3qb8y.md>) inside a [List](../list.md) within a [NavigationStack](../navigationstack.md) or [NavigationSplitView](../navigationsplitview.md). For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

<sub>watchOS</sub>

```swift
nonisolated init<V>(destinationName: String, tag: V, selection: Binding<V?>, @ContentBuilder label: () -> Label) where V : Hashable
```

## Parameters

- `destinationName` — The storyboard name of a view for the navigation link to present.

- `tag` — The value of `selection` that causes the link to present `destination`.

- `selection` — A bound variable that causes the link to present `destination` when `selection` becomes equal to `tag`.

- `label` — A content builder to produce a label describing the `destination` to present.

## See Also

### Creating links for WatchKit

- [init(destinationName:isActive:label:)](<init(destinationname_isactive_label_).md>) — Creates a navigation link that presents a view from a WatchKit storyboard when active. _(deprecated)_
- [init(destinationName:label:)](<init(destinationname_label_).md>) — Creates a navigation link that presents a view from a WatchKit storyboard. _(deprecated)_

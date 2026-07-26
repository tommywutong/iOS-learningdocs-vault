---
title: 'init(destinationName:isActive:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/navigationlink/init(destinationname:isactive:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationlink/init(destinationname:isactive:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationlink/init%28destinationname%3Aisactive%3Alabel%3A%29.json'
content_hash: 'sha256:cc7e0cd3ee16a185'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationLink](../navigationlink.md)

# init(destinationName:isActive:label:)

<sub>Initializer</sub>

Creates a navigation link that presents a view from a WatchKit storyboard when active.

> [!warning] Deprecated
> Use [init(value:label:)](<init(value_label_)-3qb8y.md>) instead. For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

<sub>watchOS</sub>

```swift
nonisolated init(destinationName: String, isActive: Binding<Bool>, @ContentBuilder label: () -> Label)
```

## Parameters

- `destinationName` — The storyboard name of a view for the navigation link to present.

- `isActive` — A binding to a Boolean value that indicates whether `destination` is currently presented.

- `label` — A content builder to produce a label describing the `destination` to present.

## See Also

### Creating links for WatchKit

- [init(destinationName:tag:selection:label:)](<init(destinationname_tag_selection_label_).md>) — Creates a navigation link that presents a view from a WatchKit storyboard when a bound selection variable matches a value you provide. _(deprecated)_
- [init(destinationName:label:)](<init(destinationname_label_).md>) — Creates a navigation link that presents a view from a WatchKit storyboard. _(deprecated)_

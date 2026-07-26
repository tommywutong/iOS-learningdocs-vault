---
title: 'init(destinationName:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/navigationlink/init(destinationname:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationlink/init(destinationname:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationlink/init%28destinationname%3Alabel%3A%29.json'
content_hash: 'sha256:7ee0ecc81f485fd6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationLink](../navigationlink.md)

# init(destinationName:label:)

<sub>Initializer</sub>

Creates a navigation link that presents a view from a WatchKit storyboard.

> [!warning] Deprecated
> Use [init(destination:label:)](<init(destination_label_)-27n7s.md>) instead.

<sub>watchOS</sub>

```swift
nonisolated init(destinationName: String, @ContentBuilder label: () -> Label)
```

## Parameters

- `destinationName` — The storyboard name of a view for the navigation link to present.

- `label` — A content builder to produce a label describing the `destination` to present.

## See Also

### Creating links for WatchKit

- [init(destinationName:isActive:label:)](<init(destinationname_isactive_label_).md>) — Creates a navigation link that presents a view from a WatchKit storyboard when active. _(deprecated)_
- [init(destinationName:tag:selection:label:)](<init(destinationname_tag_selection_label_).md>) — Creates a navigation link that presents a view from a WatchKit storyboard when a bound selection variable matches a value you provide. _(deprecated)_

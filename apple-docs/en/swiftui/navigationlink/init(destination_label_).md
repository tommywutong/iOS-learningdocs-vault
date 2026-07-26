---
title: 'init(destination:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/navigationlink/init(destination:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationlink/init(destination:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationlink/init%28destination%3Alabel%3A%29.json'
content_hash: 'sha256:b7f4c7583ca33c39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationLink](../navigationlink.md)

# init(destination:label:)

<sub>Initializer</sub>

Creates a navigation link that presents the destination view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(@ContentBuilder destination: () -> Destination, @ContentBuilder label: () -> Label)
```

## Parameters

- `destination` — A view for the navigation link to present.

- `label` — A content builder to produce a label describing the `destination` to present.

## See Also

### Presenting a destination view

- [init(_:destination:)](<init(__destination_).md>) — Creates a navigation link that presents a destination view, with a text label that the link generates from a localized string key.

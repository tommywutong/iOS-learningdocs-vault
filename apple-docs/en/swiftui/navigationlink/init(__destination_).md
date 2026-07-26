---
title: 'init(_:destination:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/navigationlink/init(_:destination:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationlink/init(_:destination:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationlink/init%28_%3Adestination%3A%29.json'
content_hash: 'sha256:7304356d3690b070'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationLink](../navigationlink.md)

# init(_:destination:)

<sub>Initializer</sub>

Creates a navigation link that presents a destination view, with a text label that the link generates from a localized string key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleKey: LocalizedStringKey, @ContentBuilder destination: () -> Destination)
```

## Parameters

- `titleKey` — A localized string key for creating a text label.

- `destination` — A view for the navigation link to present.

## See Also

### Presenting a destination view

- [init(destination:label:)](<init(destination_label_).md>) — Creates a navigation link that presents the destination view.

---
title: 'init(_:systemImage:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/label/init(_:systemimage:)'
source_url: 'https://developer.apple.com/documentation/swiftui/label/init(_:systemimage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/label/init%28_%3Asystemimage%3A%29.json'
content_hash: 'sha256:2f4631df470eb0e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Label](../label.md)

# init(_:systemImage:)

<sub>Initializer</sub>

Creates a label with a system icon image and a title generated from a localized string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, systemImage name: String)
```

## Parameters

- `titleResource` — A title generated from a localized string.

## See Also

### Creating a label

- [init(_:image:)](<init(__image_).md>) — Creates a label with an icon image and a title generated from a localized string.
- [init(title:icon:)](<init(title_icon_).md>) — Creates a label with a custom title and icon.
- [init(_:)](<init(__).md>) — Creates a label representing a family activity application.
- [init(_:image:)](<init(__image_).md>) — Creates a label with an icon image and a title generated from a localized string.

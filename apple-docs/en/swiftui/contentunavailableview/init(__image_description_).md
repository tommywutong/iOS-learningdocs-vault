---
title: 'init(_:image:description:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/contentunavailableview/init(_:image:description:)'
source_url: 'https://developer.apple.com/documentation/swiftui/contentunavailableview/init(_:image:description:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contentunavailableview/init%28_%3Aimage%3Adescription%3A%29.json'
content_hash: 'sha256:d81947ebc9d80223'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentUnavailableView](../contentunavailableview.md)

# init(_:image:description:)

<sub>Initializer</sub>

Creates an interface, consisting of a title generated from a localized string resource, an image and additional content, that you display when the content of your app is unavailable to users.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ title: LocalizedStringResource, image name: String, description: Text? = nil)
```

## Parameters

- `title` — A title generated from a localized string.

- `name` — The name of the image resource to lookup.

- `description` — The view that describes the interface.

## See Also

### Creating an unavailable view

- [init(label:description:actions:)](<init(label_description_actions_).md>) — Creates an interface, consisting of a label and additional content, that you display when the content of your app is unavailable to users.
- [init(_:systemImage:description:)](<init(__systemimage_description_).md>) — Creates an interface, consisting of a title generated from a localized string resource, a system icon image and additional content, that you display when the content of your app is unavailable to users.

---
title: 'init(label:description:actions:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/contentunavailableview/init(label:description:actions:)'
source_url: 'https://developer.apple.com/documentation/swiftui/contentunavailableview/init(label:description:actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contentunavailableview/init%28label%3Adescription%3Aactions%3A%29.json'
content_hash: 'sha256:848dfdaeca026f4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentUnavailableView](../contentunavailableview.md)

# init(label:description:actions:)

<sub>Initializer</sub>

Creates an interface, consisting of a label and additional content, that you display when the content of your app is unavailable to users.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(@ContentBuilder label: () -> Label, @ContentBuilder description: () -> Description = { EmptyView() }, @ContentBuilder actions: () -> Actions = { EmptyView() })
```

## Parameters

- `label` — The label that describes the view.

- `description` — The view that describes the interface.

- `actions` — The content of the interface actions.

## See Also

### Creating an unavailable view

- [init(_:image:description:)](<init(__image_description_).md>) — Creates an interface, consisting of a title generated from a localized string resource, an image and additional content, that you display when the content of your app is unavailable to users.
- [init(_:systemImage:description:)](<init(__systemimage_description_).md>) — Creates an interface, consisting of a title generated from a localized string resource, a system icon image and additional content, that you display when the content of your app is unavailable to users.

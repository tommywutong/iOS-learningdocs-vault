---
title: 'init(_:image:action:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/button/init(_:image:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/button/init(_:image:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/button/init%28_%3Aimage%3Aaction%3A%29.json'
content_hash: 'sha256:9c353912d6675aae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Button](../button.md)

# init(_:image:action:)

<sub>Initializer</sub>

Creates a button that generates its label from a localized string resource and image resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency @export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, action: @escaping @MainActor () -> Void)
```

## Parameters

- `titleResource` — Text resource for the button’s localized title, that describes the purpose of the button’s `action`.

- `image` — The image resource to lookup.

- `action` — The action to perform when the user triggers the button.

## Discussion

This initializer creates a [Label](../label.md) view on your behalf. See [Text](../text.md) for more information about localizing strings.

## See Also

### Creating a button

- [init(action:label:)](<init(action_label_).md>) — Creates a button that displays a custom label.
- [init(_:action:)](<init(__action_).md>) — Creates a button that generates its label from a localized string resource.
- [init(_:systemImage:action:)](<init(__systemimage_action_).md>) — Creates a button that generates its label from a localized string key and system image name.

---
title: 'init(_:action:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/button/init(_:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/button/init(_:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/button/init%28_%3Aaction%3A%29.json'
content_hash: 'sha256:392aad7fc15ac04a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Button](../button.md)

# init(_:action:)

<sub>Initializer</sub>

Creates a button that generates its label from a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency @export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, action: @escaping @MainActor () -> Void)
```

## Parameters

- `titleResource` — Text resource for the button’s localized title, that describes the purpose of the button’s `action`.

- `action` — The action to perform when the user triggers the button.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf. See [Text](../text.md) for more information about localizing strings.

## See Also

### Creating a button

- [init(action:label:)](<init(action_label_).md>) — Creates a button that displays a custom label.
- [init(_:image:action:)](<init(__image_action_).md>) — Creates a button that generates its label from a localized string resource and image resource.
- [init(_:systemImage:action:)](<init(__systemimage_action_).md>) — Creates a button that generates its label from a localized string key and system image name.

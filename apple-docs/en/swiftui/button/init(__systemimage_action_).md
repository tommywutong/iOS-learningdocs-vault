---
title: 'init(_:systemImage:action:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/button/init(_:systemimage:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/button/init(_:systemimage:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/button/init%28_%3Asystemimage%3Aaction%3A%29.json'
content_hash: 'sha256:4f525299849fb5d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Button](../button.md)

# init(_:systemImage:action:)

<sub>Initializer</sub>

Creates a button that generates its label from a localized string key and system image name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, action: @escaping @MainActor () -> Void)
```

## Parameters

- `titleKey` — The key for the button’s localized title, that describes the purpose of the button’s `action`.

- `systemImage` — The name of the image resource to lookup.

- `action` — The action to perform when the user triggers the button.

## Discussion

This initializer creates a [Label](../label.md) view on your behalf, and treats the localized key similar to [init(_:tableName:bundle:comment:)](<../text/init(__tablename_bundle_comment_).md>). See [Text](../text.md) for more information about localizing strings.

## See Also

### Creating a button

- [init(action:label:)](<init(action_label_).md>) — Creates a button that displays a custom label.
- [init(_:action:)](<init(__action_).md>) — Creates a button that generates its label from a localized string resource.
- [init(_:image:action:)](<init(__image_action_).md>) — Creates a button that generates its label from a localized string resource and image resource.

---
title: 'init(_:systemImage:role:action:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/button/init(_:systemimage:role:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/button/init(_:systemimage:role:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/button/init%28_%3Asystemimage%3Arole%3Aaction%3A%29.json'
content_hash: 'sha256:76948ceea88112cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Button](../button.md)

# init(_:systemImage:role:action:)

<sub>Initializer</sub>

Creates a button with a specified role that generates its label from a localized string key and a system image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, role: ButtonRole?, action: @escaping @MainActor () -> Void)
```

## Parameters

- `titleKey` — The key for the button’s localized title, that describes the purpose of the button’s `action`.

- `systemImage` — The name of the image resource to lookup.

- `role` — An optional semantic role describing the button. A value of `nil` means that the button doesn’t have an assigned role.

- `action` — The action to perform when the user triggers the button.

## Discussion

This initializer creates a [Label](../label.md) view on your behalf, and treats the localized key similar to [init(_:tableName:bundle:comment:)](<../text/init(__tablename_bundle_comment_).md>). See [Text](../text.md) for more information about localizing strings.

## See Also

### Creating a button with a role

- [init(role:action:label:)](<init(role_action_label_).md>) — Creates a button with a specified role that displays a custom label.
- [init(_:role:action:)](<init(__role_action_).md>) — Creates a button with a specified role that generates its label from a localized string resource.
- [init(_:image:role:action:)](<init(__image_role_action_).md>) — Creates a button with a specified role that generates its label from a localized string resource and an image resource.

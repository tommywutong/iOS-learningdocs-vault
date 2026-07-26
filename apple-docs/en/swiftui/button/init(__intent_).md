---
title: 'init(_:intent:)'
framework: AppIntents
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/button/init(_:intent:)'
source_url: 'https://developer.apple.com/documentation/swiftui/button/init(_:intent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/button/init%28_%3Aintent%3A%29.json'
content_hash: 'sha256:8d8783ce250b999f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Button](../button.md)

# init(_:intent:)

<sub>Initializer</sub>

Creates a button that performs an `AppIntent` and generates its label from a localized string key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ titleKey: LocalizedStringKey, intent: some AppIntent)
```

## Parameters

- `titleKey` — The key for the button’s localized title, that describes the purpose of the button’s `intent`.

- `intent` — The `AppIntent` to execute.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf, and treats the localized key similar to [init(_:tableName:bundle:comment:)](<../text/init(__tablename_bundle_comment_).md>). See [Text](../text.md) for more information about localizing strings.

To initialize a button with a string variable, use [init(_:intent:)](<init(__intent_).md>) instead.

## See Also

### Creating a button to perform an App Intent

- [init(intent:label:)](<init(intent_label_).md>) — Creates a button that performs an `AppIntent`.
- [init(_:role:intent:)](<init(__role_intent_).md>) — Creates a button with a specified role that performs an `AppIntent` and generates its label from a string.
- [init(role:intent:label:)](<init(role_intent_label_).md>) — Creates a button with a specified role that performs an `AppIntent`.
- [init(_:image:role:intent:)](<init(__image_role_intent_).md>) — Creates a button with a specified role that generates its label from a string and an image resource.
- [init(_:systemImage:role:intent:)](<init(__systemimage_role_intent_).md>) — Creates a button with a specified role that generates its label from a string and a system image.

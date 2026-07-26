---
title: 'init(_:role:intent:)'
framework: AppIntents
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/button/init(_:role:intent:)'
source_url: 'https://developer.apple.com/documentation/swiftui/button/init(_:role:intent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/button/init%28_%3Arole%3Aintent%3A%29.json'
content_hash: 'sha256:7ce16331ee56ae3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Button](../button.md)

# init(_:role:intent:)

<sub>Initializer</sub>

Creates a button with a specified role that performs an `AppIntent` and generates its label from a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ title: some StringProtocol, role: ButtonRole?, intent: some AppIntent)
```

## Parameters

- `title` — A string that describes the purpose of the button’s `intent`.

- `role` — An optional semantic role describing the button. A value of `nil` means that the button doesn’t have an assigned role.

- `intent` — The `AppIntent` to execute.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf, and treats the title similar to [init(_:)](<../text/init(__)-9d1g4.md>). See [Text](../text.md) for more information about localizing strings.

## See Also

### Creating a button to perform an App Intent

- [init(_:intent:)](<init(__intent_).md>) — Creates a button that performs an `AppIntent` and generates its label from a localized string key.
- [init(intent:label:)](<init(intent_label_).md>) — Creates a button that performs an `AppIntent`.
- [init(role:intent:label:)](<init(role_intent_label_).md>) — Creates a button with a specified role that performs an `AppIntent`.
- [init(_:image:role:intent:)](<init(__image_role_intent_).md>) — Creates a button with a specified role that generates its label from a string and an image resource.
- [init(_:systemImage:role:intent:)](<init(__systemimage_role_intent_).md>) — Creates a button with a specified role that generates its label from a string and a system image.

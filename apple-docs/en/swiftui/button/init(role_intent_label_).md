---
title: 'init(role:intent:label:)'
framework: AppIntents
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/button/init(role:intent:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/button/init(role:intent:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/button/init%28role%3Aintent%3Alabel%3A%29.json'
content_hash: 'sha256:34d93b8e0a04044f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Button](../button.md)

# init(role:intent:label:)

<sub>Initializer</sub>

Creates a button with a specified role that performs an `AppIntent`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(role: ButtonRole?, intent: some AppIntent, @ViewBuilder label: () -> Label)
```

## Parameters

- `role` — An optional semantic role describing the button. A value of `nil` means that the button doesn’t have an assigned role.

- `intent` — The `AppIntent` to execute.

- `label` — A view that describes the purpose of the button’s `action`.

## See Also

### Creating a button to perform an App Intent

- [init(_:intent:)](<init(__intent_).md>) — Creates a button that performs an `AppIntent` and generates its label from a localized string key.
- [init(intent:label:)](<init(intent_label_).md>) — Creates a button that performs an `AppIntent`.
- [init(_:role:intent:)](<init(__role_intent_).md>) — Creates a button with a specified role that performs an `AppIntent` and generates its label from a string.
- [init(_:image:role:intent:)](<init(__image_role_intent_).md>) — Creates a button with a specified role that generates its label from a string and an image resource.
- [init(_:systemImage:role:intent:)](<init(__systemimage_role_intent_).md>) — Creates a button with a specified role that generates its label from a string and a system image.

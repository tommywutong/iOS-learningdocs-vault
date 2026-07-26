---
title: 'init(intent:label:)'
framework: AppIntents
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/button/init(intent:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/button/init(intent:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/button/init%28intent%3Alabel%3A%29.json'
content_hash: 'sha256:a6efd44a5967900d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Button](../button.md)

# init(intent:label:)

<sub>Initializer</sub>

Creates a button that performs an `AppIntent`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<I>(intent: I, @ViewBuilder label: () -> Label) where I : AppIntent
```

## Parameters

- `intent` — The `AppIntent` to execute.

- `label` — A view that describes the purpose of the button’s `action`.

## See Also

### Creating a button to perform an App Intent

- [init(_:intent:)](<init(__intent_).md>) — Creates a button that performs an `AppIntent` and generates its label from a localized string key.
- [init(_:role:intent:)](<init(__role_intent_).md>) — Creates a button with a specified role that performs an `AppIntent` and generates its label from a string.
- [init(role:intent:label:)](<init(role_intent_label_).md>) — Creates a button with a specified role that performs an `AppIntent`.
- [init(_:image:role:intent:)](<init(__image_role_intent_).md>) — Creates a button with a specified role that generates its label from a string and an image resource.
- [init(_:systemImage:role:intent:)](<init(__systemimage_role_intent_).md>) — Creates a button with a specified role that generates its label from a string and a system image.

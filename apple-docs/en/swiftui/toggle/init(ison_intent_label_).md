---
title: 'init(isOn:intent:label:)'
framework: AppIntents
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/toggle/init(ison:intent:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toggle/init(ison:intent:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toggle/init%28ison%3Aintent%3Alabel%3A%29.json'
content_hash: 'sha256:63144e388938b854'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Toggle](../toggle.md)

# init(isOn:intent:label:)

<sub>Initializer</sub>

Creates a toggle performing an `AppIntent`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<I>(isOn: Bool, intent: I, @ViewBuilder label: () -> Label) where I : AppIntent
```

## Parameters

- `isOn` — Whether the toggle is on or off.

- `intent` — The `AppIntent` to be performed.

- `label` — A view that describes the purpose of the toggle.

## See Also

### Creating a toggle for an App Intent

- [init(_:isOn:intent:)](<init(__ison_intent_).md>) — Creates a toggle performing an `AppIntent` and generates its label from a localized string key.

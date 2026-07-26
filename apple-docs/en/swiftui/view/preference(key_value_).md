---
title: 'preference(key:value:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/preference(key:value:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/preference(key:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/preference%28key%3Avalue%3A%29.json'
content_hash: 'sha256:007bdbab4d2ad808'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# preference(key:value:)

<sub>Instance Method</sub>

Sets a value for the given preference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func preference<K>(key: K.Type = K.self, value: K.Value) -> some View where K : PreferenceKey

```

## See Also

### Setting preferences

- [transformPreference(_:_:)](<transformpreference(____).md>) — Applies a transformation to a preference value.

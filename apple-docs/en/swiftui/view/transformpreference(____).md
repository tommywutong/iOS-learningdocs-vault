---
title: 'transformPreference(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/transformpreference(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/transformpreference(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/transformpreference%28_%3A_%3A%29.json'
content_hash: 'sha256:5162db5dfa25e108'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# transformPreference(_:_:)

<sub>Instance Method</sub>

Applies a transformation to a preference value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func transformPreference<K>(_ key: K.Type = K.self, _ callback: @escaping (inout K.Value) -> Void) -> some View where K : PreferenceKey

```

## See Also

### Setting preferences

- [preference(key:value:)](<preference(key_value_).md>) — Sets a value for the given preference.

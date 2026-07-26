---
title: 'anchorPreference(key:value:transform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/anchorpreference(key:value:transform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/anchorpreference(key:value:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/anchorpreference%28key%3Avalue%3Atransform%3A%29.json'
content_hash: 'sha256:32feb719ab65a282'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# anchorPreference(key:value:transform:)

<sub>Instance Method</sub>

Sets a value for the specified preference key, the value is a function of a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func anchorPreference<A, K>(key _: K.Type = K.self, value: Anchor<A>.Source, transform: @escaping (Anchor<A>) -> K.Value) -> some View where K : PreferenceKey

```

## Parameters

- `key` — The preference key type.

- `value` — The geometry value in the current coordinate space.

- `transform` — The function to produce the preference value.

## Return Value

A new version of the view that writes the preference.

## See Also

### Setting preferences based on geometry

- [transformAnchorPreference(key:value:transform:)](<transformanchorpreference(key_value_transform_).md>) — Sets a value for the specified preference key, the value is a function of the key’s current value and a geometry value tied to the current coordinate space, allowing readers of the value to convert the geometry to their local coordinates.

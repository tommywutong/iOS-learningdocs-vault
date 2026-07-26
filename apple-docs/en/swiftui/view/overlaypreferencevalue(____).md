---
title: 'overlayPreferenceValue(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/overlaypreferencevalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/overlaypreferencevalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/overlaypreferencevalue%28_%3A_%3A%29.json'
content_hash: 'sha256:fe8695c74a442dbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# overlayPreferenceValue(_:_:)

<sub>Instance Method</sub>

Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func overlayPreferenceValue<Key, T>(_ key: Key.Type = Key.self, @ContentBuilder _ transform: @escaping (Key.Value) -> T) -> some View where Key : PreferenceKey, T : View

```

## Parameters

- `key` — The preference key type whose value is to be read.

- `transform` — A function that produces the overlay view from the preference value read from the original view.

## Return Value

A view that layers a second view in front of the view.

## See Also

### Generating backgrounds and overlays from preferences

- [backgroundPreferenceValue(_:_:)](<backgroundpreferencevalue(____).md>) — Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [backgroundPreferenceValue(_:alignment:_:)](<backgroundpreferencevalue(__alignment___).md>) — Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [overlayPreferenceValue(_:alignment:_:)](<overlaypreferencevalue(__alignment___).md>) — Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.

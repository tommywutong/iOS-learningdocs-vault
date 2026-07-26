---
title: 'overlayPreferenceValue(_:alignment:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/overlaypreferencevalue(_:alignment:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/overlaypreferencevalue(_:alignment:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/overlaypreferencevalue%28_%3Aalignment%3A_%3A%29.json'
content_hash: 'sha256:c99083201f3c04cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# overlayPreferenceValue(_:alignment:_:)

<sub>Instance Method</sub>

Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func overlayPreferenceValue<K, V>(_ key: K.Type, alignment: Alignment = .center, @ContentBuilder _ transform: @escaping (K.Value) -> V) -> some View where K : PreferenceKey, V : View

```

## Parameters

- `key` — The preference key type whose value is to be read.

- `alignment` — An optional alignment to use when positioning the overlay view relative to the original view.

- `transform` — A function that produces the overlay view from the preference value read from the original view.

## Return Value

A view that layers a second view in front of the view.

## Discussion

The values of the preference key from both views are combined and made visible to the parent view.

## See Also

### Generating backgrounds and overlays from preferences

- [backgroundPreferenceValue(_:_:)](<backgroundpreferencevalue(____).md>) — Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [backgroundPreferenceValue(_:alignment:_:)](<backgroundpreferencevalue(__alignment___).md>) — Reads the specified preference value from the view, using it to produce a second view that is applied as the background of the original view.
- [overlayPreferenceValue(_:_:)](<overlaypreferencevalue(____).md>) — Reads the specified preference value from the view, using it to produce a second view that is applied as an overlay to the original view.

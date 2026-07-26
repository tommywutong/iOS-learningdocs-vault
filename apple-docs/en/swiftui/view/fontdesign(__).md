---
title: 'fontDesign(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.1+, iPadOS 16.1+, Mac Catalyst 16.1+, macOS 13.0+, tvOS 16.1+, visionOS 1.0+, watchOS 9.1+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/fontdesign(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/fontdesign(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/fontdesign%28_%3A%29.json'
content_hash: 'sha256:853e953ec8dd12da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fontDesign(_:)

<sub>Instance Method</sub>

Sets the font design of the text in this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func fontDesign(_ design: Font.Design?) -> some View

```

## Parameters

- `design` — One of the available font designs. Providing `nil` removes the effect of any font design modifier applied higher in the view hierarchy.

## Return Value

A view that uses the font design you specify.

## See Also

### Setting a font

- [Applying custom fonts to text](../applying-custom-fonts-to-text.md) — Add and use a font in your app that scales with Dynamic Type.
- [font(_:)](<font(__).md>) — Sets the default font for text in this view.
- [fontWeight(_:)](<fontweight(__).md>) — Sets the font weight of the text in this view.
- [fontWidth(_:)](<fontwidth(__).md>) — Sets the font width of the text in this view.
- [font](../environmentvalues/font.md) — The default font of this environment.
- [Font](../font.md) — An environment-dependent font.

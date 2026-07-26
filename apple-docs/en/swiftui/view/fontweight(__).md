---
title: 'fontWeight(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/fontweight(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/fontweight(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/fontweight%28_%3A%29.json'
content_hash: 'sha256:73506e4ee19244ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fontWeight(_:)

<sub>Instance Method</sub>

Sets the font weight of the text in this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func fontWeight(_ weight: Font.Weight?) -> some View

```

## Parameters

- `weight` — One of the available font weights. Providing `nil` removes the effect of any font weight modifier applied higher in the view hierarchy.

## Return Value

A view that uses the font weight you specify.

## See Also

### Setting a font

- [Applying custom fonts to text](../applying-custom-fonts-to-text.md) — Add and use a font in your app that scales with Dynamic Type.
- [font(_:)](<font(__).md>) — Sets the default font for text in this view.
- [fontDesign(_:)](<fontdesign(__).md>) — Sets the font design of the text in this view.
- [fontWidth(_:)](<fontwidth(__).md>) — Sets the font width of the text in this view.
- [font](../environmentvalues/font.md) — The default font of this environment.
- [Font](../font.md) — An environment-dependent font.

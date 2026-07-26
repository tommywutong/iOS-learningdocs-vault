---
title: 'fontWidth(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/fontwidth(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/fontwidth(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/fontwidth%28_%3A%29.json'
content_hash: 'sha256:e638bffbde328f5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fontWidth(_:)

<sub>Instance Method</sub>

Sets the font width of the text in this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func fontWidth(_ width: Font.Width?) -> some View

```

## Parameters

- `width` — One of the available font widths. Providing `nil` removes the effect of any font width modifier applied higher in the view hierarchy.

## Return Value

A view that uses the font width you specify.

## See Also

### Setting a font

- [Applying custom fonts to text](../applying-custom-fonts-to-text.md) — Add and use a font in your app that scales with Dynamic Type.
- [font(_:)](<font(__).md>) — Sets the default font for text in this view.
- [fontDesign(_:)](<fontdesign(__).md>) — Sets the font design of the text in this view.
- [fontWeight(_:)](<fontweight(__).md>) — Sets the font weight of the text in this view.
- [font](../environmentvalues/font.md) — The default font of this environment.
- [Font](../font.md) — An environment-dependent font.

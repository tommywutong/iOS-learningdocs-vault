---
title: 'font(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/font(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/font(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/font%28_%3A%29.json'
content_hash: 'sha256:0c7031b138648b6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# font(_:)

<sub>Instance Method</sub>

Sets the default font for text in this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func font(_ font: Font?) -> some View

```

## Parameters

- `font` — The default font to use in this view.

## Return Value

A view with the default font set to the value you supply.

## Discussion

Use `font(_:)` to apply a specific font to all of the text in a view.

The example below shows the effects of applying fonts to individual views and to view hierarchies. Font information flows down the view hierarchy as part of the environment, and remains in effect unless overridden at the level of an individual view or view container.

Here, the outermost [VStack](../vstack.md) applies a 16-point system font as a default font to views contained in that [VStack](../vstack.md). Inside that stack, the example applies a [largeTitle](../font/largetitle.md) font to just the first text view; this explicitly overrides the default. The remaining stack and the views contained with it continue to use the 16-point system font set by their containing view:

```swift
VStack {
    Text("Font applied to a text view.")
        .font(.largeTitle)

    VStack {
        Text("These 2 text views have the same font")
        Text("applied to their parent hierarchy")
    }
}
.font(.system(size: 16, weight: .light, design: .default))
```

![A screenshot showing the application fonts to an individual text field](../../../../attachments/96bbeed6b182bf19c533efcca8a5fcaa/SwiftUI-view-font@2x.png)

## See Also

### Setting a font

- [Applying custom fonts to text](../applying-custom-fonts-to-text.md) — Add and use a font in your app that scales with Dynamic Type.
- [fontDesign(_:)](<fontdesign(__).md>) — Sets the font design of the text in this view.
- [fontWeight(_:)](<fontweight(__).md>) — Sets the font weight of the text in this view.
- [fontWidth(_:)](<fontwidth(__).md>) — Sets the font width of the text in this view.
- [font](../environmentvalues/font.md) — The default font of this environment.
- [Font](../font.md) — An environment-dependent font.

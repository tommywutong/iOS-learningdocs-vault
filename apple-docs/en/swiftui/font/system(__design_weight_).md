---
title: 'system(_:design:weight:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/font/system(_:design:weight:)'
source_url: 'https://developer.apple.com/documentation/swiftui/font/system(_:design:weight:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/system%28_%3Adesign%3Aweight%3A%29.json'
content_hash: 'sha256:e7160241bda37787'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# system(_:design:weight:)

<sub>Type Method</sub>

Gets a system font that uses the specified style, design, and weight.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func system(_ style: Font.TextStyle, design: Font.Design? = nil, weight: Font.Weight? = nil) -> Font
```

## Discussion

Use this method to create a system font that has the specified properties. The following example creates a system font with the [Font.TextStyle.body](textstyle/body.md) text style, a [Font.Design.serif](design/serif.md) design, and a [bold](weight/bold.md) weight, and applies the font to a [Text](../text.md) view using the [font(_:)](<../view/font(__).md>) view modifier:

```swift
Text("Hello").font(.system(.body, design: .serif, weight: .bold))
```

The `design` and `weight` parameters are both optional. If you omit either, the system uses a default value for that parameter. The default values are typically [Font.Design.default](design/default.md) and [regular](weight/regular.md), respectively, but might vary depending on the context.

## See Also

### Getting system fonts

- [system(size:weight:design:)](<system(size_weight_design_)-697b2.md>) — Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.
- [Design](design.md) — A design to use for fonts.
- [TextStyle](textstyle.md) — A dynamic text style to use for fonts.
- [Weight](weight.md) — A weight to use for fonts.

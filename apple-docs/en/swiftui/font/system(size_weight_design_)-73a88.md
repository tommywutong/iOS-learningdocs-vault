---
title: 'system(size:weight:design:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/font/system(size:weight:design:)-73a88'
source_url: 'https://developer.apple.com/documentation/swiftui/font/system(size:weight:design:)-73a88'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/system%28size%3Aweight%3Adesign%3A%29-73a88.json'
content_hash: 'sha256:72af063ce4282999'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# system(size:weight:design:)

<sub>Type Method</sub>

Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.

> [!warning] Deprecated
> Use [system(size:weight:design:)](<system(size_weight_design_)-697b2.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func system(size: CGFloat, weight: Font.Weight = .regular, design: Font.Design = .default) -> Font
```

## Discussion

Use this function to create a system font by specifying the size and weight, and a type design together. The following styles the system font as 17 point, [semibold](weight/semibold.md) text:

```swift
Text("Hello").font(.system(size: 17, weight: .semibold))
```

While the following styles the text as 17 point [bold](weight/bold.md), and applies a `serif` [Design](design.md) to the system font:

```swift
Text("Hello").font(.system(size: 17, weight: .bold, design: .serif))
```

If you want to use the default [Weight](weight.md) ([regular](weight/regular.md)), you don’t need to specify the `weight` in the method. The following example styles the text as 17 point [regular](weight/regular.md), and uses a [Font.Design.rounded](design/rounded.md) system font:

```swift
Text("Hello").font(.system(size: 17, design: .rounded))
```

## See Also

### Deprecated symbols

- [system(_:design:)](<system(__design_).md>) — Gets a system font with the given text style and design. _(deprecated)_

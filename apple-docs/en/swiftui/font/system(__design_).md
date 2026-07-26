---
title: 'system(_:design:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/font/system(_:design:)'
source_url: 'https://developer.apple.com/documentation/swiftui/font/system(_:design:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/system%28_%3Adesign%3A%29.json'
content_hash: 'sha256:6997c2caa91e03d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# system(_:design:)

<sub>Type Method</sub>

Gets a system font with the given text style and design.

> [!warning] Deprecated
> Use [system(_:design:weight:)](<system(__design_weight_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func system(_ style: Font.TextStyle, design: Font.Design = .default) -> Font
```

## See Also

### Deprecated symbols

- [system(size:weight:design:)](<system(size_weight_design_)-73a88.md>) — Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text. _(deprecated)_

---
title: 'system(size:weight:design:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/font/system(size:weight:design:)'
source_url: 'https://developer.apple.com/documentation/swiftui/font/system(size:weight:design:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/system%28size%3Aweight%3Adesign%3A%29.json'
content_hash: 'sha256:50c7b1d582938a5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# system(size:weight:design:)

<sub>Type Method</sub>

Specifies a system font to use, along with the style, weight, and any design parameters you want applied to the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func system(size: CGFloat, weight: Font.Weight? = nil, design: Font.Design? = nil) -> Font
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

Both `weight` and `design` can be optional. When you do not provide a `weight` or `design`, the system can pick one based on the current context, which may not be [regular](weight/regular.md) or [Font.Design.default](design/default.md) in certain context. The following example styles the text as 17 point system font using [Font.Design.rounded](design/rounded.md) design, while its weight can depend on the current context:

```swift
Text("Hello").font(.system(size: 17, design: .rounded))
```

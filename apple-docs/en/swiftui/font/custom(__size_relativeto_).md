---
title: 'custom(_:size:relativeTo:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/font/custom(_:size:relativeto:)'
source_url: 'https://developer.apple.com/documentation/swiftui/font/custom(_:size:relativeto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/custom%28_%3Asize%3Arelativeto%3A%29.json'
content_hash: 'sha256:f46f436734decfb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# custom(_:size:relativeTo:)

<sub>Type Method</sub>

Create a custom font with the given `name` and `size` that scales relative to the given `textStyle`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func custom(_ name: String, size: CGFloat, relativeTo textStyle: Font.TextStyle) -> Font
```

## See Also

### Creating custom fonts

- [custom(_:fixedSize:)](<custom(__fixedsize_).md>) — Create a custom font with the given `name` and a fixed `size` that does not scale with Dynamic Type.
- [custom(_:size:)](<custom(__size_).md>) — Create a custom font with the given `name` and `size` that scales with the body text style.

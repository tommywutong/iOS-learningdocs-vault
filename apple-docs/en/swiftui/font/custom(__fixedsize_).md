---
title: 'custom(_:fixedSize:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/font/custom(_:fixedsize:)'
source_url: 'https://developer.apple.com/documentation/swiftui/font/custom(_:fixedsize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/custom%28_%3Afixedsize%3A%29.json'
content_hash: 'sha256:fa017e1d28c9dc17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# custom(_:fixedSize:)

<sub>Type Method</sub>

Create a custom font with the given `name` and a fixed `size` that does not scale with Dynamic Type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func custom(_ name: String, fixedSize: CGFloat) -> Font
```

## See Also

### Creating custom fonts

- [custom(_:size:relativeTo:)](<custom(__size_relativeto_).md>) — Create a custom font with the given `name` and `size` that scales relative to the given `textStyle`.
- [custom(_:size:)](<custom(__size_).md>) — Create a custom font with the given `name` and `size` that scales with the body text style.

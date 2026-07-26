---
title: 'custom(_:size:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/font/custom(_:size:)'
source_url: 'https://developer.apple.com/documentation/swiftui/font/custom(_:size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/custom%28_%3Asize%3A%29.json'
content_hash: 'sha256:52c06825276dcecc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# custom(_:size:)

<sub>Type Method</sub>

Create a custom font with the given `name` and `size` that scales with the body text style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func custom(_ name: String, size: CGFloat) -> Font
```

## See Also

### Creating custom fonts

- [custom(_:fixedSize:)](<custom(__fixedsize_).md>) — Create a custom font with the given `name` and a fixed `size` that does not scale with Dynamic Type.
- [custom(_:size:relativeTo:)](<custom(__size_relativeto_).md>) — Create a custom font with the given `name` and `size` that scales relative to the given `textStyle`.

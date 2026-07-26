---
title: 'pointSize(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/font/pointsize(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/font/pointsize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/pointsize%28_%3A%29.json'
content_hash: 'sha256:6b102824b2fee982'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# pointSize(_:)

<sub>Instance Method</sub>

Sets the point size of the font explicitly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func pointSize(_ size: CGFloat) -> Font
```

## Discussion

Setting the point size explicitly will result in style based fonts no longer scaling with the device’s preferred text size. To scale a font’s size relative to its current size, see [scaled(by:)](<scaled(by_).md>).

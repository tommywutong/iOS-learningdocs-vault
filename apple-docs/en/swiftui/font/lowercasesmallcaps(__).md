---
title: 'lowercaseSmallCaps(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/font/lowercasesmallcaps(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/font/lowercasesmallcaps(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/lowercasesmallcaps%28_%3A%29.json'
content_hash: 'sha256:5b06acf059ffca41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# lowercaseSmallCaps(_:)

<sub>Instance Method</sub>

Adjusts the font to enable/disable lowercase small capitals.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func lowercaseSmallCaps(_ isActive: Bool) -> Font
```

## Discussion

This function controls turning lowercase characters into small capitals for the font. It is generally used for display lines set in large and small caps, such as titles. It may include forms related to small capitals, such as old-style figures.

---
title: 'uppercaseSmallCaps(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/font/uppercasesmallcaps(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/font/uppercasesmallcaps(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/uppercasesmallcaps%28_%3A%29.json'
content_hash: 'sha256:3abf12a1edf192a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# uppercaseSmallCaps(_:)

<sub>Instance Method</sub>

Adjusts the font to enable/disable uppercase small capitals.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func uppercaseSmallCaps(_ isActive: Bool) -> Font
```

## Discussion

This feature controls turning capital characters into small capitals. It is generally used for words which would otherwise be set in all caps, such as acronyms, but which are desired in small-cap form to avoid disrupting the flow of text.

---
title: 'scaled(by:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/font/scaled(by:)'
source_url: 'https://developer.apple.com/documentation/swiftui/font/scaled(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/font/scaled%28by%3A%29.json'
content_hash: 'sha256:d32f0ec3c823fdd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Font](../font.md)

# scaled(by:)

<sub>Instance Method</sub>

Scales the point size of the font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scaled(by factor: CGFloat) -> Font
```

## Discussion

Calls to scale are multiplicative, based on the size of the resolved font. For example,

```swift
Font.body
    .scaled(by: 2)
    .bold()
    .scaled(by: 3)
```

results in a bold body font 6x its usual size.

---
title: 'appendInterpolation(accessibilityName:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(accessibilityname:)'
source_url: 'https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(accessibilityname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation%28accessibilityname%3A%29.json'
content_hash: 'sha256:3a53987d1449dcb3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [LocalizedStringKey](../../localizedstringkey.md) · [StringInterpolation](../stringinterpolation.md)

# appendInterpolation(accessibilityName:)

<sub>Instance Method</sub>

Appends a localized description of a color for accessibility to a string interpolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(accessibilityName color: Color)
```

## Parameters

- `color` — The color being described.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

---
title: 'custom(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/presentationdetent/custom(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/presentationdetent/custom(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/presentationdetent/custom%28_%3A%29.json'
content_hash: 'sha256:d4309b1087f540ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PresentationDetent](../presentationdetent.md)

# custom(_:)

<sub>Type Method</sub>

A custom detent with a calculated height.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func custom<D>(_ type: D.Type) -> PresentationDetent where D : CustomPresentationDetent
```

## See Also

### Creating custom detents

- [fraction(_:)](<fraction(__).md>) — A custom detent with the specified fractional height.
- [height(_:)](<height(__).md>) — A custom detent with the specified height.
- [Context](context.md) — Information that you use to calculate the presentation’s height.

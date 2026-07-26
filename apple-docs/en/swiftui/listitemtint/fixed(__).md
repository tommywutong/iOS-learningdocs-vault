---
title: 'fixed(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/listitemtint/fixed(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/listitemtint/fixed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/listitemtint/fixed%28_%3A%29.json'
content_hash: 'sha256:83d42cf90ba44ba1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ListItemTint](../listitemtint.md)

# fixed(_:)

<sub>Type Method</sub>

An explicit tint color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func fixed(_ tint: Color) -> ListItemTint
```

## Parameters

- `tint` — The color to use to tint the content.

## Discussion

The system doesn’t override this tint effect.

## See Also

### Getting list item tint options

- [monochrome](monochrome.md) — A standard grayscale tint effect.
- [preferred(_:)](<preferred(__).md>) — An explicit tint color that the system can override.

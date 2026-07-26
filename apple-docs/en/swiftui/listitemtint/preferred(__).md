---
title: 'preferred(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/listitemtint/preferred(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/listitemtint/preferred(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/listitemtint/preferred%28_%3A%29.json'
content_hash: 'sha256:da5924cb627c6cb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ListItemTint](../listitemtint.md)

# preferred(_:)

<sub>Type Method</sub>

An explicit tint color that the system can override.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func preferred(_ tint: Color) -> ListItemTint
```

## Parameters

- `tint` — The color to use to tint the content.

## Discussion

On macOS, the system can override this tint with the person’s chosen accent color when one is set. Use [fixed(_:)](<fixed(__).md>) to prevent the system from overriding the tint.

## See Also

### Getting list item tint options

- [monochrome](monochrome.md) — A standard grayscale tint effect.
- [fixed(_:)](<fixed(__).md>) — An explicit tint color.

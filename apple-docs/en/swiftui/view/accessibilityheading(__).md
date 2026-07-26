---
title: 'accessibilityHeading(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilityheading(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilityheading(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilityheading%28_%3A%29.json'
content_hash: 'sha256:2abb64f83741134b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityHeading(_:)

<sub>Instance Method</sub>

Sets the accessibility level of this heading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityHeading(_ level: AccessibilityHeadingLevel) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Parameters

- `level` — The heading level to associate with this element from the available [AccessibilityHeadingLevel](../accessibilityheadinglevel.md) levels.

## Discussion

Use this modifier to set the level of this heading in relation to other headings. The system speaks the level number of levels [AccessibilityHeadingLevel.h1](../accessibilityheadinglevel/h1.md) through [AccessibilityHeadingLevel.h6](../accessibilityheadinglevel/h6.md) alongside the text.

The default heading level if you don’t use this modifier is [AccessibilityHeadingLevel.unspecified](../accessibilityheadinglevel/unspecified.md).

## See Also

### Describing content

- [accessibilityTextContentType(_:)](<accessibilitytextcontenttype(__).md>) — Sets an accessibility text content type.
- [AccessibilityHeadingLevel](../accessibilityheadinglevel.md) — The hierarchy of a heading in relation to other headings.
- [AccessibilityTextContentType](../accessibilitytextcontenttype.md) — Textual context that assistive technologies can use to improve the presentation of spoken text.

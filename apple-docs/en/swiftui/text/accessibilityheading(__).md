---
title: 'accessibilityHeading(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/accessibilityheading(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/accessibilityheading(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/accessibilityheading%28_%3A%29.json'
content_hash: 'sha256:5574e7be30f2a61d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# accessibilityHeading(_:)

<sub>Instance Method</sub>

Sets the accessibility level of this heading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityHeading(_ level: AccessibilityHeadingLevel) -> Text
```

## Parameters

- `level` — The heading level to associate with this element from the available [AccessibilityHeadingLevel](../accessibilityheadinglevel.md) levels.

## Discussion

Use this modifier to set the level of this heading in relation to other headings. The system speaks the level number of levels [AccessibilityHeadingLevel.h1](../accessibilityheadinglevel/h1.md) through [AccessibilityHeadingLevel.h6](../accessibilityheadinglevel/h6.md) alongside the text.

The default heading level if you don’t use this modifier is [AccessibilityHeadingLevel.unspecified](../accessibilityheadinglevel/unspecified.md).

## See Also

### Providing accessibility information

- [accessibilityLabel(_:)](<accessibilitylabel(__).md>) — Adds a label to the view that describes its contents.
- [accessibilityTextContentType(_:)](<accessibilitytextcontenttype(__).md>) — Sets an accessibility text content type.

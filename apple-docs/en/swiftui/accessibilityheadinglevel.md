---
title: AccessibilityHeadingLevel
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilityheadinglevel
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilityheadinglevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilityheadinglevel.json'
content_hash: 'sha256:31a6be34ab6ccd91'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AccessibilityHeadingLevel

<sub>Enumeration</sub>

The hierarchy of a heading in relation to other headings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum AccessibilityHeadingLevel
```

## Overview

Assistive technologies can use this to improve a user’s navigation through multiple headings. When users navigate through top level headings they expect the content for each heading to be unrelated.

For example, you can categorize a list of available products into sections, like Fruits and Vegetables. With only top level headings, this list requires no heading hierarchy, and you use the [AccessibilityHeadingLevel.unspecified](accessibilityheadinglevel/unspecified.md) heading level. On the other hand, if sections contain subsections, like if the Fruits section has subsections for varieties of Apples, Pears, and so on, you apply the [AccessibilityHeadingLevel.h1](accessibilityheadinglevel/h1.md) level to Fruits and Vegetables, and the [AccessibilityHeadingLevel.h2](accessibilityheadinglevel/h2.md) level to Apples and Pears.

Except for [AccessibilityHeadingLevel.h1](accessibilityheadinglevel/h1.md), be sure to precede all leveled headings by another heading with a level that’s one less.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the heading level

- [AccessibilityHeadingLevel.h1](accessibilityheadinglevel/h1.md) — Level 1 heading.
- [AccessibilityHeadingLevel.h2](accessibilityheadinglevel/h2.md) — Level 2 heading.
- [AccessibilityHeadingLevel.h3](accessibilityheadinglevel/h3.md) — Level 3 heading.
- [AccessibilityHeadingLevel.h4](accessibilityheadinglevel/h4.md) — Level 4 heading.
- [AccessibilityHeadingLevel.h5](accessibilityheadinglevel/h5.md) — Level 5 heading.
- [AccessibilityHeadingLevel.h6](accessibilityheadinglevel/h6.md) — Level 6 heading.
- [AccessibilityHeadingLevel.unspecified](accessibilityheadinglevel/unspecified.md) — A heading without a hierarchy.

## See Also

### Describing content

- [accessibilityTextContentType(_:)](<view/accessibilitytextcontenttype(__).md>) — Sets an accessibility text content type.
- [accessibilityHeading(_:)](<view/accessibilityheading(__).md>) — Sets the accessibility level of this heading.
- [AccessibilityTextContentType](accessibilitytextcontenttype.md) — Textual context that assistive technologies can use to improve the presentation of spoken text.

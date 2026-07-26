---
title: AttributeScopes.AccessibilityAttributes.HeadingLevelAttribute
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/accessibilityattributes/headinglevelattribute
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/headinglevelattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/accessibilityattributes/headinglevelattribute.json'
content_hash: 'sha256:7e2690bd7c0321b0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributeScopes](../../attributescopes.md) · [AccessibilityAttributes](../accessibilityattributes.md)

# AttributeScopes.AccessibilityAttributes.HeadingLevelAttribute

<sub>Enumeration</sub>

An attribute for the level of this heading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum HeadingLevelAttribute
```

## Overview

Assistive technologies can use this property to improve navigation and describe the level number of levels [AttributeScopes.AccessibilityAttributes.HeadingLevelAttribute.HeadingLevel.h1](headinglevelattribute/headinglevel/h1.md) through [AttributeScopes.AccessibilityAttributes.HeadingLevelAttribute.HeadingLevel.h6](headinglevelattribute/headinglevel/h6.md) alongside the text.

For example, you can rank sections within UI using a heading level. The most important section is marked with[AttributeScopes.AccessibilityAttributes.HeadingLevelAttribute.HeadingLevel.h1](headinglevelattribute/headinglevel/h1.md). Nested sections can use subsequent heading levels. For unranked headings, use [AttributeScopes.AccessibilityAttributes.HeadingLevelAttribute.HeadingLevel.unspecified](headinglevelattribute/headinglevel/unspecified.md).

## Relationships

- **Conforms To**: [AttributedStringKey](../../attributedstringkey.md), [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Copyable](../../../swift/copyable.md), [DecodableAttributedStringKey](../../decodableattributedstringkey.md), [EncodableAttributedStringKey](../../encodableattributedstringkey.md), [MarkdownDecodableAttributedStringKey](../../markdowndecodableattributedstringkey.md), [ObjectiveCConvertibleAttributedStringKey](../../objectivecconvertibleattributedstringkey.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Enumerations

- [HeadingLevel](headinglevelattribute/headinglevel.md) — The hierarchy of a heading in relation other headings.

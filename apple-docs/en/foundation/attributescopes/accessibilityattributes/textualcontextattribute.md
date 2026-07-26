---
title: AttributeScopes.AccessibilityAttributes.TextualContextAttribute
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/accessibilityattributes/textualcontextattribute
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/textualcontextattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/accessibilityattributes/textualcontextattribute.json'
content_hash: 'sha256:815256b6a4b1304e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributeScopes](../../attributescopes.md) · [AccessibilityAttributes](../accessibilityattributes.md)

# AttributeScopes.AccessibilityAttributes.TextualContextAttribute

<sub>Enumeration</sub>

An attribute for the textual context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum TextualContextAttribute
```

## Overview

Assistive technologies can use this property to choose an appropriate way to output the text. For example, when encountering a source coding context, VoiceOver could choose to speak all punctuation.

> [!note] Note
> This attribute is not used on macOS

## Relationships

- **Conforms To**: [AttributedStringKey](../../attributedstringkey.md), [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Copyable](../../../swift/copyable.md), [DecodableAttributedStringKey](../../decodableattributedstringkey.md), [EncodableAttributedStringKey](../../encodableattributedstringkey.md), [MarkdownDecodableAttributedStringKey](../../markdowndecodableattributedstringkey.md), [ObjectiveCConvertibleAttributedStringKey](../../objectivecconvertibleattributedstringkey.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Enumerations

- [TextualContext](textualcontextattribute/textualcontext.md) — Textual context that assistive technologies can use to improve the presentation of spoken text.

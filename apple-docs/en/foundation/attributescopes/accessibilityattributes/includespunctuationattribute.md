---
title: AttributeScopes.AccessibilityAttributes.IncludesPunctuationAttribute
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/accessibilityattributes/includespunctuationattribute
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/includespunctuationattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/accessibilityattributes/includespunctuationattribute.json'
content_hash: 'sha256:d744edf5001cfd98'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributeScopes](../../attributescopes.md) · [AccessibilityAttributes](../accessibilityattributes.md)

# AttributeScopes.AccessibilityAttributes.IncludesPunctuationAttribute

<sub>Enumeration</sub>

An attribute to define how punctuation should be spoken.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum IncludesPunctuationAttribute
```

## Overview

When `true`, all punctuation will be spoken. When `false`, no punctuation will be spoken. If this attribute is not present, the user’s settings will be used.

## Relationships

- **Conforms To**: [AttributedStringKey](../../attributedstringkey.md), [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Copyable](../../../swift/copyable.md), [DecodableAttributedStringKey](../../decodableattributedstringkey.md), [EncodableAttributedStringKey](../../encodableattributedstringkey.md), [MarkdownDecodableAttributedStringKey](../../markdowndecodableattributedstringkey.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

---
title: AttributeScopes.AccessibilityAttributes.AdjustedPitchAttribute
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributescopes/accessibilityattributes/adjustedpitchattribute
source_url: 'https://developer.apple.com/documentation/foundation/attributescopes/accessibilityattributes/adjustedpitchattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributescopes/accessibilityattributes/adjustedpitchattribute.json'
content_hash: 'sha256:6df653fe9b8587a5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributeScopes](../../attributescopes.md) · [AccessibilityAttributes](../accessibilityattributes.md)

# AttributeScopes.AccessibilityAttributes.AdjustedPitchAttribute

<sub>Enumeration</sub>

An attribute to adjust the pitch the spoken speech.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum AdjustedPitchAttribute
```

## Overview

Values between `-1` and `0` result in a lower pitch while values between `0` and `1` result in a higher pitch.

For example, you may want to lower the pitch when an object is deleted, or raise the pitch if an object is inserted.

## Relationships

- **Conforms To**: [AttributedStringKey](../../attributedstringkey.md), [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Copyable](../../../swift/copyable.md), [DecodableAttributedStringKey](../../decodableattributedstringkey.md), [EncodableAttributedStringKey](../../encodableattributedstringkey.md), [MarkdownDecodableAttributedStringKey](../../markdowndecodableattributedstringkey.md), [ObjectiveCConvertibleAttributedStringKey](../../objectivecconvertibleattributedstringkey.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

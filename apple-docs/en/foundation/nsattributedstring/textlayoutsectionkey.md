---
title: NSAttributedString.TextLayoutSectionKey
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/textlayoutsectionkey
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/textlayoutsectionkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/textlayoutsectionkey.json'
content_hash: 'sha256:1edab61a33a3e06f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# NSAttributedString.TextLayoutSectionKey

<sub>Structure</sub>

Constants for the text layout sections document attribute key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TextLayoutSectionKey
```

## Overview

Use these constants as values for the [textLayoutSections](documentattributekey/textlayoutsections.md) key in the document attributes dictionary.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting keys for text layouts

- [orientation](textlayoutsectionkey/orientation.md) — The orientation of the text.
- [range](textlayoutsectionkey/range.md) — The character range.

### Initializers

- [init(rawValue:)](<textlayoutsectionkey/init(rawvalue_).md>) — Creates a text layout section key with the specified raw value.

## See Also

### Getting document-wide attributes

- [DocumentAttributeKey](documentattributekey.md) — The attributes you apply to an entire document.
- [DocumentReadingOptionKey](documentreadingoptionkey.md) — Options for constructing an attributed string from data you read from disk.
- [HTML attributes](../html-attributes.md) — Documentwide attributes that provide control over the form of generated HTML.
- [DocumentType](documenttype.md) — Constants for the document type document attribute key.
- [NSTextScalingType](../../uikit/nstextscalingtype.md) — Constants that specify the text scaling.

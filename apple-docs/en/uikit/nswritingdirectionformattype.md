---
title: NSWritingDirectionFormatType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nswritingdirectionformattype
source_url: 'https://developer.apple.com/documentation/uikit/nswritingdirectionformattype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nswritingdirectionformattype.json'
content_hash: 'sha256:bd5f939f8ce1bf91'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSWritingDirectionFormatType

<sub>Enumeration</sub>

Constants for the writing direction attribute key.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
enum NSWritingDirectionFormatType
```

## Overview

Use these constants as the values for the [writingDirection](../foundation/nsattributedstring/key/writingdirection.md) key in Swift or the [NSWritingDirectionAttributeName](nswritingdirectionattributename.md) key in Objective-C.

You can use the logical OR operator to combine these constants with [NSWritingDirectionLeftToRight](nswritingdirection/lefttoright.md) or [NSWritingDirectionRightToLeft](nswritingdirection/righttoleft.md) when used with the [writingDirection](../foundation/nsattributedstring/key/writingdirection.md) key in Swift or the [NSWritingDirectionAttributeName](nswritingdirectionattributename.md) key in Objective-C to specify formatting controls defined by the Unicode Bidirectional Algorithm in [Unicode Standard Annex #9](http://unicode.org/reports/tr9/).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [NSWritingDirectionEmbedding](nswritingdirectionformattype/embedding.md) — Text is embedded in text with another writing direction. For example, an English quotation in the middle of an Arabic sentence could be marked as being embedded left-to-right text.
- [NSWritingDirectionOverride](nswritingdirectionformattype/override.md) — Enables character types with inherent directionality to be overridden when required for special cases, such as for part numbers made of mixed English, digits, and Hebrew letters to be written from right to left.

### Initializers

- [init(rawValue:)](<nswritingdirectionformattype/init(rawvalue_).md>)

## See Also

### Getting text content attributes

- [NSUnderlineStyle](nsunderlinestyle.md) — Constants for the underline style and strikethrough style attribute keys.

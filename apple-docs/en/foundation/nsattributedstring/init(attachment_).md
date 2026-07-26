---
title: 'init(attachment:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/init(attachment:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(attachment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28attachment%3A%29.json'
content_hash: 'sha256:3b6067c92fed0bbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(attachment:)

<sub>Initializer</sub>

Creates an attributed string with an attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(attachment: NSTextAttachment)
```

## Parameters

- `attachment` — The attrachment to place in the string.

## Return Value

An attributed string containing the attachment.

## Discussion

This is a convenience method for creating an attributed string containing an attachment using [character](../../appkit/nstextattachment/character.md) as the base character.

## See Also

### Creating a string with an attachment

- [+ attributedStringWithAttachment:attributes:](<init(attachment_attributes_).md>) — Creates an attributed string with an attachment and applies the specified attributes to it.
- [+ attributedStringWithAdaptiveImageGlyph:attributes:](<init(adaptiveimageglyph_attributes_).md>) — Creates an attributed string with an adaptive image glyph and applies the specified attributes to it.

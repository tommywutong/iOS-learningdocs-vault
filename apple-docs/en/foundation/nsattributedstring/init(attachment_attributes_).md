---
title: 'init(attachment:attributes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/init(attachment:attributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(attachment:attributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28attachment%3Aattributes%3A%29.json'
content_hash: 'sha256:3eadc21b65be2ee9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(attachment:attributes:)

<sub>Initializer</sub>

Creates an attributed string with an attachment and applies the specified attributes to it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(attachment: NSTextAttachment, attributes: [NSAttributedString.Key : Any] = [:])
```

## Parameters

- `attachment` — The attrachment to place in the string.

- `attributes` — The attributes to apply to the attachment. Specify an empty dictionary to create the string without any extra attributes.

## Return Value

An attributed string containing the attachment.

## See Also

### Creating a string with an attachment

- [+ attributedStringWithAttachment:](<init(attachment_).md>) — Creates an attributed string with an attachment.
- [+ attributedStringWithAdaptiveImageGlyph:attributes:](<init(adaptiveimageglyph_attributes_).md>) — Creates an attributed string with an adaptive image glyph and applies the specified attributes to it.

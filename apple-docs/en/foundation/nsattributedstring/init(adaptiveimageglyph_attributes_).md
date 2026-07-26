---
title: 'init(adaptiveImageGlyph:attributes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/init(adaptiveimageglyph:attributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(adaptiveimageglyph:attributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28adaptiveimageglyph%3Aattributes%3A%29.json'
content_hash: 'sha256:2c1ca310fad83296'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(adaptiveImageGlyph:attributes:)

<sub>Initializer</sub>

Creates an attributed string with an adaptive image glyph and applies the specified attributes to it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(adaptiveImageGlyph: NSAdaptiveImageGlyph, attributes: [NSAttributedString.Key : Any] = [:])
```

## Parameters

- `adaptiveImageGlyph` — The adaptive image glyph to place in the string. Typically, you get this type from the text input system.

- `attributes` — The attributes to apply to the adaptive image glyph. Specify an empty dictionary to create the string without any extra attributes.

## Return Value

An attributed string containing the adaptive image glyph.

## See Also

### Creating a string with an attachment

- [+ attributedStringWithAttachment:](<init(attachment_).md>) — Creates an attributed string with an attachment.
- [+ attributedStringWithAttachment:attributes:](<init(attachment_attributes_).md>) — Creates an attributed string with an attachment and applies the specified attributes to it.

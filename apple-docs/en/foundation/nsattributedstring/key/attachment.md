---
title: attachment
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/attachment
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/attachment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/attachment.json'
content_hash: 'sha256:fffcf9faa228b881'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# attachment

<sub>Type Property</sub>

The attachment for the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let attachment: NSAttributedString.Key
```

## Discussion

The value of this attribute is an [NSTextAttachment](../../../appkit/nstextattachment.md) object. The default value of this property is `nil`, indicating no attachment.

## See Also

### Getting attachment attribute keys

- [adaptiveImageGlyph](adaptiveimageglyph.md) — The adaptive image glyph for the text.

---
title: presentationIntentAttributeName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/presentationintentattributename
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/presentationintentattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/presentationintentattributename.json'
content_hash: 'sha256:2859c910c0583a2c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# presentationIntentAttributeName

<sub>Type Property</sub>

An attribute that provides details for a block-level Markdown element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let presentationIntentAttributeName: NSAttributedString.Key
```

## Discussion

The value of this key is an [NSPresentationIntent](../../nspresentationintent.md) object. Block-level elements include paragraphs, headers, lists, tables, and other structural elements of the Markdown content.

The system provides default visual treatments for ranges of text with this attribute. To replace the default visual treatment, remove this attribute and replace it with the formatting options you want.

## See Also

### Getting Markdown attribute keys

- [NSInlinePresentationIntentAttributeName](inlinepresentationintent.md) — An attribute that provides details for an inline Markdown element.
- [NSMarkdownSourcePositionAttributeName](markdownsourceposition.md) — The position in a Markdown source string corresponding to some attributed text.
- [NSAlternateDescriptionAttributeName](alternatedescription.md) — An alternate description for a URL or image.
- [NSImageURLAttributeName](imageurl.md) — The URL for an image in Markdown text.

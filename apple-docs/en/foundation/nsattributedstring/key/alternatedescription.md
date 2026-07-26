---
title: alternateDescription
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/alternatedescription
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/alternatedescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/alternatedescription.json'
content_hash: 'sha256:2d6bbcbfe7639b82'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# alternateDescription

<sub>Type Property</sub>

An alternate description for a URL or image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let alternateDescription: NSAttributedString.Key
```

## Discussion

The value of this key is an [NSString](../../nsstring.md) with the alternate description of the URL or image.

When a Markdown link contains a title string, the system adds this key to the link text and sets the value to the title. For example, in the Markdown tect `[Visit the Apple Store](https://store.apple.com “The Apple Store website”)`, the system sets the value of this key to `The Apple Store website`.

## See Also

### Getting Markdown attribute keys

- [NSInlinePresentationIntentAttributeName](inlinepresentationintent.md) — An attribute that provides details for an inline Markdown element.
- [NSPresentationIntentAttributeName](presentationintentattributename.md) — An attribute that provides details for a block-level Markdown element.
- [NSMarkdownSourcePositionAttributeName](markdownsourceposition.md) — The position in a Markdown source string corresponding to some attributed text.
- [NSImageURLAttributeName](imageurl.md) — The URL for an image in Markdown text.

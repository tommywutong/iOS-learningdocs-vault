---
title: markdownSourcePosition
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/markdownsourceposition
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/markdownsourceposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/markdownsourceposition.json'
content_hash: 'sha256:373886acd1376e2c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# markdownSourcePosition

<sub>Type Property</sub>

The position in a Markdown source string corresponding to some attributed text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let markdownSourcePosition: NSAttributedString.Key
```

## Discussion

This attribute indicates the position in the Markdown source where a run of attributed text begins and ends, omitting markup characters in the source. For example, after parsing the source string `“This is *emphasized*.”`, the text `emphasized` has a Markdown source position that starts at column `10`. This index is the `“e”` character, not the `“*”` formatting character.

An attributed string parsed from Markdown text includes this attribute only if the [appliesSourcePositionAttributes](../../nsattributedstringmarkdownparsingoptions/appliessourcepositionattributes.md) value in the directory of [DocumentReadingOptionKey](../documentreadingoptionkey.md) options provided to the [NSAttributedString](../../nsattributedstring.md) initializer is `YES`.

## See Also

### Getting Markdown attribute keys

- [NSInlinePresentationIntentAttributeName](inlinepresentationintent.md) — An attribute that provides details for an inline Markdown element.
- [NSPresentationIntentAttributeName](presentationintentattributename.md) — An attribute that provides details for a block-level Markdown element.
- [NSAlternateDescriptionAttributeName](alternatedescription.md) — An alternate description for a URL or image.
- [NSImageURLAttributeName](imageurl.md) — The URL for an image in Markdown text.

---
title: accessibilityTextHeadingLevel
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/accessibilitytextheadinglevel
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/accessibilitytextheadinglevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/accessibilitytextheadinglevel.json'
content_hash: 'sha256:7ffe3001c8e3053d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# accessibilityTextHeadingLevel

<sub>Type Property</sub>

A key for specifying the heading level of the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated static let accessibilityTextHeadingLevel: NSAttributedString.Key
```

## Discussion

The value of this key is an [NSNumber](../../nsnumber.md) object with a value that is a number in the range of `0` to `6`. Use `0` to indicate the absence of a specific heading level, and use other numbers to indicate the heading level.

## See Also

### Getting accessibility attribute keys

- [accessibilityAlignment](accessibilityalignment.md)
- [accessibilityAnnotationTextAttribute](accessibilityannotationtextattribute.md)
- [accessibilityAttachment](accessibilityattachment.md) — Text attachment (`id`). _(deprecated)_
- [accessibilityAutocorrected](accessibilityautocorrected.md) — Autocorrected text (`NSNumber` as a Boolean value).
- [accessibilityBackgroundColor](accessibilitybackgroundcolor.md) — Text background color (`CGColorRef`).
- [accessibilityCustomText](accessibilitycustomtext.md)
- [accessibilityFont](accessibilityfont.md) — Font keys (`NSDictionary`).
- [accessibilityFontBoldAttribute](accessibilityfontboldattribute.md)
- [accessibilityFontItalicAttribute](accessibilityfontitalicattribute.md)
- [accessibilityForegroundColor](accessibilityforegroundcolor.md) — Text foreground color (`CGColorRef`).
- [accessibilityLanguage](accessibilitylanguage.md)
- [accessibilityLink](accessibilitylink.md) — Text link (`id`).
- [accessibilityListItemIndex](accessibilitylistitemindex.md)
- [accessibilityListItemLevel](accessibilitylistitemlevel.md)
- [accessibilityListItemPrefix](accessibilitylistitemprefix.md)

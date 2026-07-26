---
title: accessibilitySpeechPunctuation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/accessibilityspeechpunctuation
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/accessibilityspeechpunctuation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/accessibilityspeechpunctuation.json'
content_hash: 'sha256:845b73f2e051a080'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# accessibilitySpeechPunctuation

<sub>Type Property</sub>

A key that indicates whether to speak punctuation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated static let accessibilitySpeechPunctuation: NSAttributedString.Key
```

## Discussion

The value of this key is an [NSNumber](../../nsnumber.md) object that the system interprets as a Boolean value. When the value is [true](../../../swift/true.md), the assistive app speaks all punctuation in the text. You might use this for code or other text where the punctuation is relevant.

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

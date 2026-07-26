---
title: accessibilityMisspelled
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/accessibilitymisspelled
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/accessibilitymisspelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/accessibilitymisspelled.json'
content_hash: 'sha256:7e2333cc8744be44'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# accessibilityMisspelled

<sub>Type Property</sub>

Misspelled text that isn’t necessarily visibly marked as misspelled ([NSNumber](../../nsnumber.md) as a Boolean value). Beginning in macOS 10.9, VoiceOver no longer checks for this attribute; instead, VoiceOver uses [accessibilityMarkedMisspelled](accessibilitymarkedmisspelled.md).

<sub>macOS</sub>

```swift
static let accessibilityMisspelled: NSAttributedString.Key
```

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

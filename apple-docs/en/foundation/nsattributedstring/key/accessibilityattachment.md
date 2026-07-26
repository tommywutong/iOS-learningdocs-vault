---
title: accessibilityAttachment
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsattributedstring/key/accessibilityattachment
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/accessibilityattachment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/accessibilityattachment.json'
content_hash: 'sha256:314a14cb1f0791e3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# accessibilityAttachment

<sub>Type Property</sub>

Text attachment (`id`).

> [!warning] Deprecated
> Use [NSAccessibilityProtocol](../../../appkit/nsaccessibilityprotocol.md) instead.

<sub>macOS</sub>

```swift
static let accessibilityAttachment: NSAttributedString.Key
```

## See Also

### Getting accessibility attribute keys

- [accessibilityAlignment](accessibilityalignment.md)
- [accessibilityAnnotationTextAttribute](accessibilityannotationtextattribute.md)
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
- [accessibilityMarkedMisspelled](accessibilitymarkedmisspelled.md) — Misspelled text that is visibly marked as misspelled (`NSNumber` as a Boolean value). If you’re implementing a custom text-editing app, use `NSAccessibilityMarkedMisspelledTextAttribute` to ensure that VoiceOver properly identifies misspelled text to users.

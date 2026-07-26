---
title: NSCharacterShapeAttributeName
framework: AppKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.0+（10.11 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nscharactershapeattributename
source_url: 'https://developer.apple.com/documentation/appkit/nscharactershapeattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nscharactershapeattributename.json'
content_hash: 'sha256:99708185a15b21d5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSCharacterShapeAttributeName

<sub>Global Variable</sub>

The character shape attribute.

<sub>macOS</sub>

```objc
extern NSAttributedStringKey NSCharacterShapeAttributeName;
```

## Discussion

An integer value. The value is interpreted as Apple Type Services `kCharacterShapeType selector + 1`.

The character shape feature type (`kCharacterShapeType`) is used when a single font contains different appearances for the same character shape, and these shapes are not traditionally treated as swashes. It is needed for languages such as Chinese that have both traditional and simplified character sets. The default value is `0` (disable). `1` is `kTraditionalCharactersSelector`, and so on. Refer to `<ATS/SFNTLayoutTypes.h>` and Font Features in ATSUI Programming Guide for additional information.

## See Also

### Deprecated keys

- [NSAccessibilityAttachmentTextAttribute](nsaccessibilityattachmenttextattribute.md) — Text attachment (`id`). _(deprecated)_
- [NSExpansionAttributeName](nsexpansionattributename.md) — The expansion factor of the text. _(deprecated)_
- [NSObliquenessAttributeName](nsobliquenessattributename.md) — The obliqueness of the text. _(deprecated)_
- [NSVerticalGlyphFormAttributeName](nsverticalglyphformattributename.md) — The vertical glyph form of the text. _(deprecated)_
- [NSUsesScreenFontsDocumentAttribute](nsusesscreenfontsdocumentattribute.md) — The screen fonts attribute. _(deprecated)_

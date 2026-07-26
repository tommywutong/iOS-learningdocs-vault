---
title: NSUsesScreenFontsDocumentAttribute
framework: AppKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.8+（10.11 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsusesscreenfontsdocumentattribute
source_url: 'https://developer.apple.com/documentation/appkit/nsusesscreenfontsdocumentattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsusesscreenfontsdocumentattribute.json'
content_hash: 'sha256:34257b9db95fffb6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSUsesScreenFontsDocumentAttribute

<sub>Global Variable</sub>

The screen fonts attribute.

<sub>macOS</sub>

```objc
extern NSAttributedStringKey NSUsesScreenFontsDocumentAttribute;
```

## Discussion

The value of this attribute is an [NSNumber](../foundation/nsnumber.md) object containing a Boolean; this attribute corresponds to the [usesScreenFonts](nslayoutmanager/usesscreenfonts.md) method of [NSLayoutManager](nslayoutmanager.md); if absent, follows the system default setting.

## See Also

### Deprecated keys

- [NSAccessibilityAttachmentTextAttribute](nsaccessibilityattachmenttextattribute.md) — Text attachment (`id`). _(deprecated)_
- [NSExpansionAttributeName](nsexpansionattributename.md) — The expansion factor of the text. _(deprecated)_
- [NSObliquenessAttributeName](nsobliquenessattributename.md) — The obliqueness of the text. _(deprecated)_
- [NSVerticalGlyphFormAttributeName](nsverticalglyphformattributename.md) — The vertical glyph form of the text. _(deprecated)_
- [NSCharacterShapeAttributeName](nscharactershapeattributename.md) — The character shape attribute. _(deprecated)_

---
title: NSAccessibilityAttachmentTextAttribute
framework: AppKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/appkit/nsaccessibilityattachmenttextattribute
source_url: 'https://developer.apple.com/documentation/appkit/nsaccessibilityattachmenttextattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsaccessibilityattachmenttextattribute.json'
content_hash: 'sha256:583745958902842f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSAccessibilityAttachmentTextAttribute

<sub>Global Variable</sub>

Text attachment (`id`).

> [!warning] Deprecated
> Use [NSAccessibility](nsaccessibility-swift.struct.md) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
extern NSAttributedStringKey const NSAccessibilityAttachmentTextAttribute;
```

## See Also

### Constants

- [NSAccessibilityAutocorrectedTextAttribute](nsaccessibilityautocorrectedtextattribute.md) — Autocorrected text (`NSNumber` as a Boolean value).
- [NSAccessibilityBackgroundColorTextAttribute](nsaccessibilitybackgroundcolortextattribute.md) — Text background color (`CGColorRef`).
- [NSAccessibilityForegroundColorTextAttribute](nsaccessibilityforegroundcolortextattribute.md) — Text foreground color (`CGColorRef`).
- [NSAccessibilityUnderlineColorTextAttribute](nsaccessibilityunderlinecolortextattribute.md) — Text underline color (`CGColorRef`).
- [NSAccessibilityStrikethroughColorTextAttribute](nsaccessibilitystrikethroughcolortextattribute.md) — Text strikethrough color (`CGColorRef`).
- [NSAccessibilityUnderlineTextAttribute](nsaccessibilityunderlinetextattribute.md) — Text underline style (`NSNumber`).
- [NSAccessibilitySuperscriptTextAttribute](nsaccessibilitysuperscripttextattribute.md) — Text superscript style (`NSNumber`). Values \> 0 are superscript; values \< 0 are subscript.
- [NSAccessibilityStrikethroughTextAttribute](nsaccessibilitystrikethroughtextattribute.md) — Text strikethrough (`NSNumber` as a Boolean value).
- [NSAccessibilityShadowTextAttribute](nsaccessibilityshadowtextattribute.md) — Text shadow (`NSNumber` as a Boolean value).
- [NSAccessibilityLinkTextAttribute](nsaccessibilitylinktextattribute.md) — Text link (`id`).
- [NSAccessibilityMarkedMisspelledTextAttribute](nsaccessibilitymarkedmisspelledtextattribute.md) — Misspelled text that is visibly marked as misspelled (`NSNumber` as a Boolean value). If you’re implementing a custom text-editing app, use `NSAccessibilityMarkedMisspelledTextAttribute` to ensure that VoiceOver properly identifies misspelled text to users.
- [NSAccessibilityMisspelledTextAttribute](nsaccessibilitymisspelledtextattribute.md) — Misspelled text that isn’t necessarily visibly marked as misspelled (`NSNumber` as a Boolean value).
- [NSAccessibilityFontTextAttribute](nsaccessibilityfonttextattribute.md) — Font keys (`NSDictionary`).
- [NSAccessibilityFontNameKey](nsaccessibility-swift.struct/fontattributekey/fontname.md) — A required key for a font name.
- [NSAccessibilityFontFamilyKey](nsaccessibility-swift.struct/fontattributekey/fontfamily.md) — An optional key for a font family.

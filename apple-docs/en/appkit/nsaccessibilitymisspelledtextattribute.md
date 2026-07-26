---
title: NSAccessibilityMisspelledTextAttribute
framework: AppKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsaccessibilitymisspelledtextattribute
source_url: 'https://developer.apple.com/documentation/appkit/nsaccessibilitymisspelledtextattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsaccessibilitymisspelledtextattribute.json'
content_hash: 'sha256:a1474cdb8f3280bb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSAccessibilityMisspelledTextAttribute

<sub>Global Variable</sub>

Misspelled text that isn’t necessarily visibly marked as misspelled (`NSNumber` as a Boolean value).

<sub>Mac Catalyst, macOS</sub>

```objc
extern NSAttributedStringKey const NSAccessibilityMisspelledTextAttribute;
```

## Discussion

Beginning in macOS 10.9, VoiceOver no longer checks for this attribute; instead, VoiceOver uses [NSAccessibilityMarkedMisspelledTextAttribute](nsaccessibilitymarkedmisspelledtextattribute.md).

## See Also

### Constants

- [NSAccessibilityAttachmentTextAttribute](nsaccessibilityattachmenttextattribute.md) — Text attachment (`id`). _(deprecated)_
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
- [NSAccessibilityFontTextAttribute](nsaccessibilityfonttextattribute.md) — Font keys (`NSDictionary`).
- [NSAccessibilityFontNameKey](nsaccessibility-swift.struct/fontattributekey/fontname.md) — A required key for a font name.
- [NSAccessibilityFontFamilyKey](nsaccessibility-swift.struct/fontattributekey/fontfamily.md) — An optional key for a font family.

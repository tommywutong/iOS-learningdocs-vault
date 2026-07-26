---
title: symbolicClass
framework: Core Text
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coretext/ctfontstylisticclass/symbolicclass
source_url: 'https://developer.apple.com/documentation/coretext/ctfontstylisticclass/symbolicclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontstylisticclass/symbolicclass.json'
content_hash: 'sha256:850278beda9d0c8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTFontStylisticClass](../ctfontstylisticclass.md)

# symbolicClass

<sub>Type Property</sub>

The font’s style is generally design independent.

> [!warning] Deprecated
> Use [kCTFontClassSymbolic](classsymbolic.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var symbolicClass: CTFontStylisticClass { get }
```

## Discussion

Typically assigned to fonts for special characters, such as icons, dingbats, technical symbols, and so on.

## See Also

### Deprecated Constants

- [kCTFontOldStyleSerifsClass](oldstyleserifsclass.md) — The font’s style is based on the Latin printing style of the 15th to 17th century. _(deprecated)_
- [kCTFontTransitionalSerifsClass](transitionalserifsclass.md) — The font’s style is based on the Latin printing style of the 18th to 19th century. _(deprecated)_
- [kCTFontModernSerifsClass](modernserifsclass.md) — The font’s style is based on the Latin printing style of the 20th century. _(deprecated)_
- [kCTFontClarendonSerifsClass](clarendonserifsclass.md) — The font’s style is a variation of the Oldstyle Serifs and the Transitional Serifs. _(deprecated)_
- [kCTFontSlabSerifsClass](slabserifsclass.md) — The font’s style is characterized by serifs with a square transition between the strokes and the serifs (no brackets). _(deprecated)_
- [kCTFontFreeformSerifsClass](freeformserifsclass.md) — The font’s style includes serifs but expresses a design freedom that doesn’t generally fit within the other serif design classifications. _(deprecated)_
- [kCTFontSansSerifClass](sansserifclass.md) — The font’s style includes most basic letter forms (excluding Scripts and Ornamentals) that do not have serifs on the strokes. _(deprecated)_
- [kCTFontOrnamentalsClass](ornamentalsclass.md) — The font’s style includes highly decorated or stylized character shapes such as those typically used in headlines. _(deprecated)_
- [kCTFontScriptsClass](scriptsclass.md) — The font’s style is among those typefaces designed to simulate handwriting. _(deprecated)_

---
title: CTFontStylisticClass
framework: Core Text
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontstylisticclass
source_url: 'https://developer.apple.com/documentation/coretext/ctfontstylisticclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontstylisticclass.json'
content_hash: 'sha256:721632866d6bc48d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontStylisticClass

<sub>Structure</sub>

The stylistic class values of the font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CTFontStylisticClass
```

## Overview

`CTFontStylisticClass` identifies certain stylistic qualities of the font. These values correspond closely to the font class values in the OpenType OS/2 table. The class values are bundled in the upper four bits of the [CTFontSymbolicTraits](ctfontsymbolictraits.md) and can be obtained via [kCTFontClassMaskTrait](ctfontsymbolictraits/classmasktrait.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<ctfontstylisticclass/init(rawvalue_).md>) — Creates a stylistic class structure with the specified raw value.

### Stylistic Classes

- [kCTFontClassOldStyleSerifs](ctfontstylisticclass/classoldstyleserifs.md) — A font style based on the Latin printing style of the 15th to 17th century.
- [kCTFontClassTransitionalSerifs](ctfontstylisticclass/classtransitionalserifs.md) — A font style based on the Latin printing style of the 18th to 19th century.
- [kCTFontClassModernSerifs](ctfontstylisticclass/classmodernserifs.md) — A font style based on the Latin printing style of the 20th century.
- [kCTFontClassClarendonSerifs](ctfontstylisticclass/classclarendonserifs.md) — A font style variation of the Oldstyle Serifs and the Transitional Serifs.
- [kCTFontClassSlabSerifs](ctfontstylisticclass/classslabserifs.md) — A font style characterized by serifs with a square transition between the strokes and the serifs (no brackets).
- [kCTFontClassFreeformSerifs](ctfontstylisticclass/classfreeformserifs.md) — A font style that includes serifs but expresses a design freedom that doesn’t generally fit within the other serif design classifications.
- [kCTFontClassSansSerif](ctfontstylisticclass/classsansserif.md) — A font style that includes most basic letter forms (excluding Scripts and Ornamentals) that do not have serifs on the strokes.
- [kCTFontClassOrnamentals](ctfontstylisticclass/classornamentals.md) — A font style that includes highly decorated or stylized character shapes such as those typically used in headlines.
- [kCTFontClassScripts](ctfontstylisticclass/classscripts.md) — A font style among those typefaces designed to simulate handwriting.
- [kCTFontClassSymbolic](ctfontstylisticclass/classsymbolic.md) — A generally design-independent font style.

### Deprecated Constants

- [kCTFontOldStyleSerifsClass](ctfontstylisticclass/oldstyleserifsclass.md) — The font’s style is based on the Latin printing style of the 15th to 17th century. _(deprecated)_
- [kCTFontTransitionalSerifsClass](ctfontstylisticclass/transitionalserifsclass.md) — The font’s style is based on the Latin printing style of the 18th to 19th century. _(deprecated)_
- [kCTFontModernSerifsClass](ctfontstylisticclass/modernserifsclass.md) — The font’s style is based on the Latin printing style of the 20th century. _(deprecated)_
- [kCTFontClarendonSerifsClass](ctfontstylisticclass/clarendonserifsclass.md) — The font’s style is a variation of the Oldstyle Serifs and the Transitional Serifs. _(deprecated)_
- [kCTFontSlabSerifsClass](ctfontstylisticclass/slabserifsclass.md) — The font’s style is characterized by serifs with a square transition between the strokes and the serifs (no brackets). _(deprecated)_
- [kCTFontFreeformSerifsClass](ctfontstylisticclass/freeformserifsclass.md) — The font’s style includes serifs but expresses a design freedom that doesn’t generally fit within the other serif design classifications. _(deprecated)_
- [kCTFontSansSerifClass](ctfontstylisticclass/sansserifclass.md) — The font’s style includes most basic letter forms (excluding Scripts and Ornamentals) that do not have serifs on the strokes. _(deprecated)_
- [kCTFontOrnamentalsClass](ctfontstylisticclass/ornamentalsclass.md) — The font’s style includes highly decorated or stylized character shapes such as those typically used in headlines. _(deprecated)_
- [kCTFontScriptsClass](ctfontstylisticclass/scriptsclass.md) — The font’s style is among those typefaces designed to simulate handwriting. _(deprecated)_
- [kCTFontSymbolicClass](ctfontstylisticclass/symbolicclass.md) — The font’s style is generally design independent. _(deprecated)_

## See Also

### Accessing Font Traits

- [Font Traits](font-traits.md) — The keys for accessing font traits from a font descriptor.
- [Font Class Mask Shift Constants](font-class-mask-shift-constants.md) — These constants represent the font class mask shift.
- [CTFontSymbolicTraits](ctfontsymbolictraits.md) — The symbolic representation of stylistic font attributes.

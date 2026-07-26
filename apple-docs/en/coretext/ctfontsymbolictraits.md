---
title: CTFontSymbolicTraits
framework: Core Text
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontsymbolictraits
source_url: 'https://developer.apple.com/documentation/coretext/ctfontsymbolictraits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontsymbolictraits.json'
content_hash: 'sha256:950d656c85c28c61'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontSymbolicTraits

<sub>Structure</sub>

The symbolic representation of stylistic font attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CTFontSymbolicTraits
```

## Overview

`CTFontSymbolicTraits` symbolically describes stylistic aspects of a font. The upper 16 bits are used to describe appearance of the font, whereas the lower 16 bits are for typeface information. The font appearance information represented by the upper 16 bits can be used for stylistic font matching.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<ctfontsymbolictraits/init(rawvalue_).md>) — Creates a symbolic traits structure with the specified raw value.

### Symbolic Traits

- [kCTFontTraitItalic](ctfontsymbolictraits/traititalic.md) — The font typestyle is italic.
- [kCTFontTraitBold](ctfontsymbolictraits/traitbold.md) — The font typestyle is boldface.
- [kCTFontTraitExpanded](ctfontsymbolictraits/traitexpanded.md) — The font typestyle is expanded.
- [kCTFontTraitCondensed](ctfontsymbolictraits/traitcondensed.md) — The font typestyle is condensed.
- [kCTFontTraitMonoSpace](ctfontsymbolictraits/traitmonospace.md) — The font uses fixed-pitch glyphs if available.
- [kCTFontTraitVertical](ctfontsymbolictraits/traitvertical.md) — The font uses vertical glyph variants and metrics.
- [kCTFontTraitUIOptimized](ctfontsymbolictraits/traituioptimized.md) — The font synthesizes appropriate attributes for user interface rendering, such as control titles, if necessary.
- [kCTFontTraitColorGlyphs](ctfontsymbolictraits/traitcolorglyphs.md) — The font contains color glyphs.
- [kCTFontTraitComposite](ctfontsymbolictraits/traitcomposite.md) — The font is in Composite Font Reference format.
- [kCTFontTraitClassMask](ctfontsymbolictraits/traitclassmask.md) — Mask for the font class.

### Deprecated Constants

- [kCTFontItalicTrait](ctfontsymbolictraits/italictrait.md) — The font typestyle is italic. _(deprecated)_
- [kCTFontBoldTrait](ctfontsymbolictraits/boldtrait.md) — The font typestyle is boldface. _(deprecated)_
- [kCTFontExpandedTrait](ctfontsymbolictraits/expandedtrait.md) — The font typestyle is expanded. _(deprecated)_
- [kCTFontCondensedTrait](ctfontsymbolictraits/condensedtrait.md) — The font typestyle is condensed. _(deprecated)_
- [kCTFontMonoSpaceTrait](ctfontsymbolictraits/monospacetrait.md) — The font uses fixed-pitch glyphs if available. _(deprecated)_
- [kCTFontVerticalTrait](ctfontsymbolictraits/verticaltrait.md) — The font uses vertical glyph variants and metrics. _(deprecated)_
- [kCTFontUIOptimizedTrait](ctfontsymbolictraits/uioptimizedtrait.md) — The font synthesizes appropriate attributes for user interface rendering, such as control titles, if necessary. _(deprecated)_
- [kCTFontColorGlyphsTrait](ctfontsymbolictraits/colorglyphstrait.md) — The font contains color glyphs. _(deprecated)_
- [kCTFontCompositeTrait](ctfontsymbolictraits/compositetrait.md) — The font is in Composite Font Reference format. _(deprecated)_
- [kCTFontClassMaskTrait](ctfontsymbolictraits/classmasktrait.md) — Mask for the font class. _(deprecated)_

## See Also

### Accessing Font Traits

- [Font Traits](font-traits.md) — The keys for accessing font traits from a font descriptor.
- [Font Class Mask Shift Constants](font-class-mask-shift-constants.md) — These constants represent the font class mask shift.
- [CTFontStylisticClass](ctfontstylisticclass.md) — The stylistic class values of the font.

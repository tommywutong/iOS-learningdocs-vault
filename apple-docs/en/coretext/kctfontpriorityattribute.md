---
title: kCTFontPriorityAttribute
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontpriorityattribute
source_url: 'https://developer.apple.com/documentation/coretext/kctfontpriorityattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontpriorityattribute.json'
content_hash: 'sha256:e2a9a20c28a0d7be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontPriorityAttribute

<sub>Global Variable</sub>

The font priority used by font descriptors when resolving duplicates and sorting match results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFontPriorityAttribute: CFString
```

## Discussion

The value associated with this key is an integer represented as a [CFNumber](../corefoundation/cfnumber.md) object containing one of the values enumerated in [CTFontPriority](ctfontpriority.md). The higher the value, the higher the priority of the font. Only registered fonts have a priority. Unregistered font descriptors return `NULL`.

## See Also

### Related Documentation

- [CTFontPriority](ctfontpriority.md) — The priority of font descriptors when resolving duplicates and sorting match results.

### Font Attribute Keys

- [kCTFontURLAttribute](kctfonturlattribute.md) — The font URL from the font descriptor.
- [kCTFontNameAttribute](kctfontnameattribute.md) — The PostScript name from the font descriptor.
- [kCTFontDisplayNameAttribute](kctfontdisplaynameattribute.md) — The name used to display the font.
- [kCTFontFamilyNameAttribute](kctfontfamilynameattribute.md) — The font family name from the font descriptor.
- [kCTFontStyleNameAttribute](kctfontstylenameattribute.md) — The style name of the font.
- [kCTFontTraitsAttribute](kctfonttraitsattribute.md) — The dictionary of font traits for stylistic information.
- [kCTFontVariationAttribute](kctfontvariationattribute.md) — The dictionary of font variation.
- [kCTFontSizeAttribute](kctfontsizeattribute.md) — The font point size.
- [kCTFontMatrixAttribute](kctfontmatrixattribute.md) — The font transformation matrix when creating a font.
- [kCTFontCascadeListAttribute](kctfontcascadelistattribute.md) — The cascade list used for a font reference.
- [kCTFontCharacterSetAttribute](kctfontcharactersetattribute.md) — The Unicode character coverage set for a font reference.
- [kCTFontLanguagesAttribute](kctfontlanguagesattribute.md) — A list of covered languages for a font reference.
- [kCTFontBaselineAdjustAttribute](kctfontbaselineadjustattribute.md) — The baseline adjustment for a font reference.
- [kCTFontMacintoshEncodingsAttribute](kctfontmacintoshencodingsattribute.md) — The Macintosh encodings for a font reference.
- [kCTFontFeaturesAttribute](kctfontfeaturesattribute.md) — The font features for a font reference.

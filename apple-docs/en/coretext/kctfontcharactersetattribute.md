---
title: kCTFontCharacterSetAttribute
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontcharactersetattribute
source_url: 'https://developer.apple.com/documentation/coretext/kctfontcharactersetattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontcharactersetattribute.json'
content_hash: 'sha256:edfda82f481b03f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontCharacterSetAttribute

<sub>Global Variable</sub>

The Unicode character coverage set for a font reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFontCharacterSetAttribute: CFString
```

## Discussion

The value for this key is a [CFCharacterSet](../corefoundation/cfcharacterset.md) object. If specified, this attribute can be used to restrict the font to a subset of its actual character set. If unspecified, this attribute is ignored and the actual character set is used.

## See Also

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
- [kCTFontLanguagesAttribute](kctfontlanguagesattribute.md) — A list of covered languages for a font reference.
- [kCTFontBaselineAdjustAttribute](kctfontbaselineadjustattribute.md) — The baseline adjustment for a font reference.
- [kCTFontMacintoshEncodingsAttribute](kctfontmacintoshencodingsattribute.md) — The Macintosh encodings for a font reference.
- [kCTFontFeaturesAttribute](kctfontfeaturesattribute.md) — The font features for a font reference.
- [kCTFontFeatureSettingsAttribute](kctfontfeaturesettingsattribute.md) — The font features settings for a font reference.

---
title: Font Attributes
framework: Core Text
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/font-attributes
source_url: 'https://developer.apple.com/documentation/coretext/font-attributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/font-attributes.json'
content_hash: 'sha256:dffd5d450febb351'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md) · [CTFontDescriptor](ctfontdescriptor.md)

# Font Attributes

<sub>API Collection</sub>

The keys for accessing font attributes from a font descriptor.

## Topics

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
- [kCTFontFeatureSettingsAttribute](kctfontfeaturesettingsattribute.md) — The font features settings for a font reference.
- [kCTFontFixedAdvanceAttribute](kctfontfixedadvanceattribute.md) — A fixed advance to be used for a font reference.
- [kCTFontOrientationAttribute](kctfontorientationattribute.md) — The orientation for the glyphs of the font.
- [kCTFontFormatAttribute](kctfontformatattribute.md) — The recognized format of the font.
- [kCTFontRegistrationScopeAttribute](kctfontregistrationscopeattribute.md) — The font descriptor’s registration scope.
- [kCTFontPriorityAttribute](kctfontpriorityattribute.md) — The font priority used by font descriptors when resolving duplicates and sorting match results.
- [kCTFontEnabledAttribute](kctfontenabledattribute.md) — The font enabled state.
- [kCTFontDownloadableAttribute](kctfontdownloadableattribute.md) — The font downloadable state.
- [kCTFontDownloadedAttribute](kctfontdownloadedattribute.md) — The download state.

## See Also

### Related Documentation

- [CTFontDescriptorCopyAttribute](<ctfontdescriptorcopyattribute(____).md>) — Returns the value associated with an arbitrary attribute.
- [CTFontDescriptorCopyAttributes](<ctfontdescriptorcopyattributes(__).md>) — Returns the attributes dictionary of the font descriptor.
- [CTFontCopyAttribute](<ctfontcopyattribute(____).md>) — Returns the value associated with an arbitrary attribute of the given font.

### Accessing Font Attributes

- [CTFontOrientation](ctfontorientation.md) — The intended rendering orientation of the font for obtaining glyph metrics.
- [CTFontFormat](ctfontformat.md) — The recognized format of the font.
- [CTFontPriority](ctfontpriority.md) — The priority of font descriptors when resolving duplicates and sorting match results.

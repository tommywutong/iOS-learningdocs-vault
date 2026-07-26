---
title: Core Text Functions
framework: Core Text
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/core-text-functions
source_url: 'https://developer.apple.com/documentation/coretext/core-text-functions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/core-text-functions.json'
content_hash: 'sha256:d3a1c27532528c58'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# Core Text Functions

<sub>API Collection</sub>

## Topics

### Functions

- [CTFontDescriptorMatchFontDescriptorsWithProgressHandler](<ctfontdescriptormatchfontdescriptorswithprogresshandler(______).md>) — Matches font descriptors and tracks progress with a progress handler.
- [CTFontManagerCompareFontFamilyNames](<ctfontmanagercomparefontfamilynames(______).md>) — A comparator function to compare font family names and sort them according to Apple guidelines.
- [CTFontManagerCopyAvailableFontFamilyNames](<ctfontmanagercopyavailablefontfamilynames().md>) — Returns an array of visible font family names sorted for user interface display.
- [CTFontManagerCopyAvailableFontURLs](<ctfontmanagercopyavailablefonturls().md>) — Returns an array of font URLs.
- [CTFontManagerCopyAvailablePostScriptNames](<ctfontmanagercopyavailablepostscriptnames().md>) — Returns an array of unique PostScript font names for the fonts.
- [CTFontManagerCreateFontDescriptorFromData](<ctfontmanagercreatefontdescriptorfromdata(__).md>) — Creates a font descriptor representing the font in the supplied data.
- [CTFontManagerCreateFontDescriptorsFromURL](<ctfontmanagercreatefontdescriptorsfromurl(__).md>) — Returns an array of font descriptors representing each of the fonts in the specified URL.
- [CTFontManagerCreateFontRequestRunLoopSource](<ctfontmanagercreatefontrequestrunloopsource(____).md>) — Creates a reference to a run loop source used to convey font requests from the Font Manager. _(deprecated)_
- [CTFontManagerEnableFontDescriptors](<ctfontmanagerenablefontdescriptors(____).md>) — Enables or disables the matching font descriptors for font descriptor matching.
- [CTFontManagerGetAutoActivationSetting](<ctfontmanagergetautoactivationsetting(__).md>) — Gets the auto-activation setting for the specified bundle identifier.
- [CTFontManagerGetScopeForURL](<ctfontmanagergetscopeforurl(__).md>) — Returns the registration scope of the specified URL.
- [CTFontManagerIsSupportedFont](<ctfontmanagerissupportedfont(__).md>) — Determines whether a file is in a supported font format.
- [CTFontManagerRegisterFontsForURL](<ctfontmanagerregisterfontsforurl(______).md>) — Registers fonts from the specified font URL with the Font Manager. Registered fonts are discoverable through font descriptor matching.
- [CTFontManagerRegisterFontsForURLs](<ctfontmanagerregisterfontsforurls(______).md>) — Registers fonts from the specified array of font URLs with the Font Manager. Registered fonts are discoverable through font descriptor matching. _(deprecated)_
- [CTFontManagerRegisterGraphicsFont](<ctfontmanagerregistergraphicsfont(____).md>) — Registers the specified graphics font with the font manager. _(deprecated)_
- [CTFontManagerSetAutoActivationSetting](<ctfontmanagersetautoactivationsetting(____).md>) — Sets the auto-activation setting for the specified bundle identifier.
- [CTFontManagerUnregisterFontsForURL](<ctfontmanagerunregisterfontsforurl(______).md>) — Unregisters fonts from the specified font URL with the Font Manager. Unregistered fonts are no longer discoverable through font descriptor matching.
- [CTFontManagerUnregisterFontsForURLs](<ctfontmanagerunregisterfontsforurls(______).md>) — Unregisters fonts from the specified array of font URLs with the Font Manager. Unregistered fonts are no longer discoverable through font descriptor matching. _(deprecated)_
- [CTFontManagerUnregisterGraphicsFont](<ctfontmanagerunregistergraphicsfont(____).md>) — Unregisters the specified graphics font with the font manager. _(deprecated)_
- [CTFontManagerCopyRegisteredFontDescriptors](<ctfontmanagercopyregisteredfontdescriptors(____).md>) — Retrieves the font descriptors that were registered with the font manager.
- [CTFontManagerCreateFontDescriptorsFromData](<ctfontmanagercreatefontdescriptorsfromdata(__).md>) — Creates an array of font descriptors for the fonts in the supplied data.
- [CTFontManagerRegisterFontDescriptors](<ctfontmanagerregisterfontdescriptors(________).md>) — Registers font descriptors with the font manager.
- [CTFontManagerRegisterFontURLs](<ctfontmanagerregisterfonturls(________).md>) — Registers fonts from the specified font URLs with the font manager.
- [CTFontManagerRegisterFontsWithAssetNames](<ctfontmanagerregisterfontswithassetnames(__________).md>) — Registers named font assets in the specified bundle with the font manager.
- [CTFontManagerRequestFonts](<ctfontmanagerrequestfonts(____).md>) — Resolves font descriptors specified on input.
- [CTFontManagerUnregisterFontDescriptors](<ctfontmanagerunregisterfontdescriptors(______).md>) — Unregisters font descriptors with the font manager.
- [CTFontManagerUnregisterFontURLs](<ctfontmanagerunregisterfonturls(______).md>) — Unregisters fonts from the specified font URLs with the font manager.
- [CTGetCoreTextVersion](<ctgetcoretextversion().md>) — Returns the version of the Core Text framework. _(deprecated)_
- [CTRubyAnnotationCreate](<ctrubyannotationcreate(________).md>) — Creates an immutable ruby annotation object.
- [CTRubyAnnotationCreateCopy](<ctrubyannotationcreatecopy(__).md>) — Creates an immutable copy of a ruby annotation object.
- [CTRubyAnnotationCreateWithAttributes](<ctrubyannotationcreatewithattributes(__________).md>) — Creates an immutable ruby annotation object with the specified attributes.
- [CTRubyAnnotationGetAlignment](<ctrubyannotationgetalignment(__).md>) — Retrieves the alignment value of a ruby annotation object.
- [CTRubyAnnotationGetOverhang](<ctrubyannotationgetoverhang(__).md>) — Retrieves the overhang value of a ruby annotation object.
- [CTRubyAnnotationGetSizeFactor](<ctrubyannotationgetsizefactor(__).md>) — Retrieves the size factor of a ruby annotation object.
- [CTRubyAnnotationGetTextForPosition](<ctrubyannotationgettextforposition(____).md>) — Retrieves the ruby text for a particular position in a ruby annotation.
- [CTRubyAnnotationGetTypeID](<ctrubyannotationgettypeid().md>) — Retrieves the type of the ruby annotation object.
- [CTFontCopyNameForGlyph](<ctfontcopynameforglyph(____).md>) — Retrieves the name for the specified glyph.
- [CTFontDrawImageFromAdaptiveImageProviderAtPoint](<ctfontdrawimagefromadaptiveimageprovideratpoint(________).md>)
- [CTFontGetTypographicBoundsForAdaptiveImageProvider](<ctfontgettypographicboundsforadaptiveimageprovider(____).md>)
- [CTFontHasTable](<ctfonthastable(____).md>)

## See Also

### Reference

- [Styling Attributed Strings](styling-attributed-strings.md) — Attributes to which Core Text responds when placed in a `CFAttributedString` object.
- [Core Text Structures](core-text-structures.md)
- [Core Text Enumerations](core-text-enumerations.md)
- [Core Text Constants](core-text-constants.md)
- [Core Text Data Types](core-text-data-types.md)
- [SFNT Support](sfnt-support.md)

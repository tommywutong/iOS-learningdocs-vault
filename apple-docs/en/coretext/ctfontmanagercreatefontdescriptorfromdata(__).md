---
title: 'CTFontManagerCreateFontDescriptorFromData(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontmanagercreatefontdescriptorfromdata(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagercreatefontdescriptorfromdata(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagercreatefontdescriptorfromdata%28_%3A%29.json'
content_hash: 'sha256:17943b07ccb02a75'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontManagerCreateFontDescriptorFromData(_:)

<sub>Function</sub>

Creates a font descriptor representing the font in the supplied data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontManagerCreateFontDescriptorFromData(_ data: CFData) -> CTFontDescriptor?
```

## Parameters

- `data` — The font data.

## Return Value

A font descriptor created from the data or `NULL` if it is not a valid font.

## Discussion

If the data contains a font collection (TTC or OTC), only the first font in the collection will be returned. Use [CTFontManagerCreateFontDescriptorsFromData](<ctfontmanagercreatefontdescriptorsfromdata(__).md>) in that case.

> [!note] Note
> The font descriptor returned by this function is not available through font descriptor matching. As a result, you can’t directly look for the font by name with functions like [CTFontCreateWithName](<ctfontcreatewithname(______).md>). If you wish to make the font available for name matching, use [CTFontManagerRegisterFontURLs](<ctfontmanagerregisterfonturls(________).md>) instead.

## See Also

### Related Documentation

- [CTFontManagerCreateFontDescriptorsFromData](<ctfontmanagercreatefontdescriptorsfromdata(__).md>) — Creates an array of font descriptors for the fonts in the supplied data.
- [CTFontManagerRegisterFontURLs](<ctfontmanagerregisterfonturls(________).md>) — Registers fonts from the specified font URLs with the font manager.

### Functions

- [CTFontDescriptorMatchFontDescriptorsWithProgressHandler](<ctfontdescriptormatchfontdescriptorswithprogresshandler(______).md>) — Matches font descriptors and tracks progress with a progress handler.
- [CTFontManagerCompareFontFamilyNames](<ctfontmanagercomparefontfamilynames(______).md>) — A comparator function to compare font family names and sort them according to Apple guidelines.
- [CTFontManagerCopyAvailableFontFamilyNames](<ctfontmanagercopyavailablefontfamilynames().md>) — Returns an array of visible font family names sorted for user interface display.
- [CTFontManagerCopyAvailableFontURLs](<ctfontmanagercopyavailablefonturls().md>) — Returns an array of font URLs.
- [CTFontManagerCopyAvailablePostScriptNames](<ctfontmanagercopyavailablepostscriptnames().md>) — Returns an array of unique PostScript font names for the fonts.
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

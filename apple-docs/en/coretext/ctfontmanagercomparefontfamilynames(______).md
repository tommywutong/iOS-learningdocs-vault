---
title: 'CTFontManagerCompareFontFamilyNames(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.6+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontmanagercomparefontfamilynames(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagercomparefontfamilynames(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagercomparefontfamilynames%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:9a15b16d5b9a647e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontManagerCompareFontFamilyNames(_:_:_:)

<sub>Function</sub>

A comparator function to compare font family names and sort them according to Apple guidelines.

<sub>macOS</sub>

```swift
func CTFontManagerCompareFontFamilyNames(_ family1: UnsafeRawPointer, _ family2: UnsafeRawPointer, _ context: UnsafeMutableRawPointer?) -> CFComparisonResult
```

## Parameters

- `family1` — The first localized font family name to compare, as a `CFStringRef` object.

- `family2` — The second localized font family name to compare, as a `CFStringRef` object.

- `context` — Unused. Can be `NULL`.

## Return Value

A `CFComparisonResult` value indicating the sort order for the two family names. `kCFComparisonResultGreatherThan` if `family1` is greater than `family2`, `kCFComparisonResultLessThan` if `family1` is less than `family2`, and `kCFComparisonResultEqualTo` if they are equal.

## Discussion

This `CFComparatorFunction` function compares font family names and sorts them in the Apple preferred order, accounting for foundry prefix. Family names with recognized prefixes are sorted after the unprefixed names in prefix order.

## See Also

### Functions

- [CTFontDescriptorMatchFontDescriptorsWithProgressHandler](<ctfontdescriptormatchfontdescriptorswithprogresshandler(______).md>) — Matches font descriptors and tracks progress with a progress handler.
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

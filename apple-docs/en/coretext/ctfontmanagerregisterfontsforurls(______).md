---
title: 'CTFontManagerRegisterFontsForURLs(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.1+（13.0 起废弃）, iPadOS 4.1+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.6+（10.15 起废弃）, tvOS 9.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（6.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coretext/ctfontmanagerregisterfontsforurls(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagerregisterfontsforurls(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagerregisterfontsforurls%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:fb87939598ae8709'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontManagerRegisterFontsForURLs(_:_:_:)

<sub>Function</sub>

Registers fonts from the specified array of font URLs with the Font Manager. Registered fonts are discoverable through font descriptor matching.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontManagerRegisterFontsForURLs(_ fontURLs: CFArray, _ scope: CTFontManagerScope, _ errors: UnsafeMutablePointer<Unmanaged<CFArray>?>?) -> Bool
```

## Parameters

- `fontURLs` — Array of font URLs.

- `scope` — Scope constant defining the availability and lifetime of the registration. See [CTFontManagerScope](ctfontmanagerscope.md) for values to pass for this parameter.

- `errors` — Pointer to an array of CFError objects which, in case of failed registration, contain error information. Each error contains a CFArray of font URLs corresponding to [kCTFontManagerErrorFontURLsKey](kctfontmanagererrorfonturlskey.md). These URLs represent the font files that caused the error and were not successfully registered. The array must be released by the caller. Can be `NULL`.

## Return Value

Returns `true` if registration of all font URLs was successful, otherwise `false`.

## See Also

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
- [CTFontManagerRegisterGraphicsFont](<ctfontmanagerregistergraphicsfont(____).md>) — Registers the specified graphics font with the font manager. _(deprecated)_
- [CTFontManagerSetAutoActivationSetting](<ctfontmanagersetautoactivationsetting(____).md>) — Sets the auto-activation setting for the specified bundle identifier.

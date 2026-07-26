---
title: 'CTFontManagerRequestFonts(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontmanagerrequestfonts(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagerrequestfonts(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagerrequestfonts%28_%3A_%3A%29.json'
content_hash: 'sha256:900dbc44ed48f41e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontManagerRequestFonts(_:_:)

<sub>Function</sub>

Resolves font descriptors specified on input.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func CTFontManagerRequestFonts(_ fontDescriptors: CFArray, _ completionHandler: @escaping (CFArray) -> Void)
```

## Parameters

- `fontDescriptors` — An array of font descriptors to make available to the process.  The keys for describing the fonts may be a combination of [kCTFontNameAttribute](kctfontnameattribute.md), [kCTFontFamilyNameAttribute](kctfontfamilynameattribute.md), or [kCTFontRegistrationUserInfoAttribute](kctfontregistrationuserinfoattribute.md).

- `completionHandler` — A block called after the request operation completes. This block takes a `unresolvedFontDescriptors` parameter that contains an array of descriptors that couldn’t be resolved or found. The array can be empty if all descriptors resolved.

## Discussion

On iOS, fonts registered by font provider apps in the [kCTFontManagerScopePersistent](ctfontmanagerscope/persistent.md) scope aren’t automatically available to other apps. Other apps must call this function to make the fonts available for font descriptor matching.

On iOS, if the font descriptors can’t be found, the system presents the user with a dialog that indicates which fonts couldn’t be resolved. The system may provide the user with a way to resolve the missing fonts, if the font manager has a way to enable them.

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
- [CTFontManagerRegisterFontsForURLs](<ctfontmanagerregisterfontsforurls(______).md>) — Registers fonts from the specified array of font URLs with the Font Manager. Registered fonts are discoverable through font descriptor matching. _(deprecated)_
- [CTFontManagerRegisterGraphicsFont](<ctfontmanagerregistergraphicsfont(____).md>) — Registers the specified graphics font with the font manager. _(deprecated)_

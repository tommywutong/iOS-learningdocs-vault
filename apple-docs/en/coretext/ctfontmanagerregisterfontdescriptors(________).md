---
title: 'CTFontManagerRegisterFontDescriptors(_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontmanagerregisterfontdescriptors(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagerregisterfontdescriptors(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagerregisterfontdescriptors%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:a795b4cc68b9b804'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontManagerRegisterFontDescriptors(_:_:_:_:)

<sub>Function</sub>

Registers font descriptors with the font manager.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontManagerRegisterFontDescriptors(_ fontDescriptors: CFArray, _ scope: CTFontManagerScope, _ enabled: Bool, _ registrationHandler: ((CFArray, Bool) -> Bool)?)
```

## Parameters

- `fontDescriptors` — An array of font descriptors to register. The font descriptor keys for registration are [kCTFontURLAttribute](kctfonturlattribute.md), [kCTFontNameAttribute](kctfontnameattribute.md), [kCTFontFamilyNameAttribute](kctfontfamilynameattribute.md), or [kCTFontRegistrationUserInfoAttribute](kctfontregistrationuserinfoattribute.md).

- `scope` — A scope constant that defines the availability and lifetime of the registration. If you specify [kCTFontManagerScopePersistent](ctfontmanagerscope/persistent.md) when you register fonts on iOS, those fonts aren’t automatically available to other processes. Other processes can call [CTFontManagerRequestFonts](<ctfontmanagerrequestfonts(____).md>) to get access to those fonts. See [CTFontManagerScope](ctfontmanagerscope.md) for more details.

- `enabled` — A Boolean value that indicates whether the font descriptors should be enabled for font descriptor matching and discoverable though [CTFontManagerRequestFonts](<ctfontmanagerrequestfonts(____).md>).

- `registrationHandler` — A block called as errors arise or upon completion. The block’s `errors` parameter contains an array of [CFError](../corefoundation/cferror.md) references; an empty array indicates no errors. Each error reference contains a [CFArray](../corefoundation/cfarray.md) of font descriptors corresponding to [kCTFontManagerErrorFontDescriptorsKey](kctfontmanagererrorfontdescriptorskey.md). These represent the font descriptors causing the error and failing to register successfully. This block may be called multiple times during the registration process. The `done` parameter becomes [true](../swift/true.md) when the registration process completes. Return [false](../swift/false.md) from the block to stop the registration operation, like after receiving an error.

## Discussion

Registered fonts are discoverable through font descriptor matching in the calling process.

Fonts descriptors registered in a disabled state (the `enabled` parameter set to [false](../swift/false.md)) aren’t immediately available for descriptor matching, but the font manager knows the descriptors can be made available if necessary. You can enable these descriptors by calling this function again with the `enabled` parameter set to [true](../swift/true.md). This operation may fail if there’s another registered and enabled font with the same PostScript name.

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

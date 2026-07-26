---
title: 'CTFontManagerUnregisterFontURLs(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontmanagerunregisterfonturls(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagerunregisterfonturls(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagerunregisterfonturls%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:05c47b12ea0b96d0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontManagerUnregisterFontURLs(_:_:_:)

<sub>Function</sub>

Unregisters fonts from the specified font URLs with the font manager.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontManagerUnregisterFontURLs(_ fontURLs: CFArray, _ scope: CTFontManagerScope, _ registrationHandler: ((CFArray, Bool) -> Bool)?)
```

## Parameters

- `fontURLs` — An array of font URLs.

- `scope` — A scope constant that defines the availability and lifetime of the registration. This value should match the scope the fonts are registered in. See [CTFontManagerScope](ctfontmanagerscope.md) for more details.

- `registrationHandler` — A block called as errors arise or upon completion. The block’s `errors` parameter contains an array of [CFError](../corefoundation/cferror.md) references; an empty array indicates no errors unregistering the files. Each error reference contains a [CFArray](../corefoundation/cfarray.md) of font URLs corresponding to [kCTFontManagerErrorFontURLsKey](kctfontmanagererrorfonturlskey.md). These URLs represent the font files causing the error and failing to unregister successfully. This block may be called multiple times during the unregistration process. The `done` parameter becomes [true](../swift/true.md) when the unregistration process completes. Return [false](../swift/false.md) from the block to stop the unregistration operation, like after receiving an error.

## Discussion

Unregistered fonts don’t participate in font descriptor matching.

> [!note] Note
> On iOS, you can only use this function to unregister fonts that you registered using [CTFontManagerRegisterFontsForURL](<ctfontmanagerregisterfontsforurl(______).md>) or [CTFontManagerRegisterFontsForURLs](<ctfontmanagerregisterfontsforurls(______).md>).

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

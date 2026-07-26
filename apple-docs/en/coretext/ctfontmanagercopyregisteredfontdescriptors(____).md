---
title: 'CTFontManagerCopyRegisteredFontDescriptors(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontmanagercopyregisteredfontdescriptors(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagercopyregisteredfontdescriptors(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagercopyregisteredfontdescriptors%28_%3A_%3A%29.json'
content_hash: 'sha256:9ab08e3e389f4587'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontManagerCopyRegisteredFontDescriptors(_:_:)

<sub>Function</sub>

Retrieves the font descriptors that were registered with the font manager.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func CTFontManagerCopyRegisteredFontDescriptors(_ scope: CTFontManagerScope, _ enabled: Bool) -> CFArray
```

## Parameters

- `scope` — A scope constant that defines the availability and lifetime of the registration. If you specify [kCTFontManagerScopePersistent](ctfontmanagerscope/persistent.md), only macOS can return fonts registered by any process. Other platforms can only return font descriptors registered by the app’s process. See [CTFontManagerScope](ctfontmanagerscope.md) for more details.

- `enabled` — A Boolean value that indicates whether to return registered font descriptors that are enabled or disabled.

## Return Value

An array of font descriptors registered by the app. The array may be empty if nothing is registered.

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

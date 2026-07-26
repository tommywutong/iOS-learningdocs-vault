---
title: 'CTFontManagerGetAutoActivationSetting(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.6+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontmanagergetautoactivationsetting(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagergetautoactivationsetting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagergetautoactivationsetting%28_%3A%29.json'
content_hash: 'sha256:484f9c4079ab1b89'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontManagerGetAutoActivationSetting(_:)

<sub>Function</sub>

Gets the auto-activation setting for the specified bundle identifier.

<sub>macOS</sub>

```swift
func CTFontManagerGetAutoActivationSetting(_ bundleIdentifier: CFString?) -> CTFontManagerAutoActivationSetting
```

## Parameters

- `bundleIdentifier` — The bundle identifier used to specify a particular application bundle. If `NULL`, the current application bundle is used. If `kCTFontManagerBundleIdentifier` is specified, gets the global auto-activation setting.

## Return Value

The auto-activation setting for the specified bundle identifier. See [CTFontManagerAutoActivationSetting](ctfontmanagerautoactivationsetting.md) for possible values.

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
- [CTFontManagerGetScopeForURL](<ctfontmanagergetscopeforurl(__).md>) — Returns the registration scope of the specified URL.
- [CTFontManagerIsSupportedFont](<ctfontmanagerissupportedfont(__).md>) — Determines whether a file is in a supported font format.
- [CTFontManagerRegisterFontsForURL](<ctfontmanagerregisterfontsforurl(______).md>) — Registers fonts from the specified font URL with the Font Manager. Registered fonts are discoverable through font descriptor matching.
- [CTFontManagerRegisterFontsForURLs](<ctfontmanagerregisterfontsforurls(______).md>) — Registers fonts from the specified array of font URLs with the Font Manager. Registered fonts are discoverable through font descriptor matching. _(deprecated)_
- [CTFontManagerRegisterGraphicsFont](<ctfontmanagerregistergraphicsfont(____).md>) — Registers the specified graphics font with the font manager. _(deprecated)_
- [CTFontManagerSetAutoActivationSetting](<ctfontmanagersetautoactivationsetting(____).md>) — Sets the auto-activation setting for the specified bundle identifier.

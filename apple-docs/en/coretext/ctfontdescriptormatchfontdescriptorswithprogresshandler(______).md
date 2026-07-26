---
title: 'CTFontDescriptorMatchFontDescriptorsWithProgressHandler(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontdescriptormatchfontdescriptorswithprogresshandler(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontdescriptormatchfontdescriptorswithprogresshandler(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontdescriptormatchfontdescriptorswithprogresshandler%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c145a995834c5fda'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontDescriptorMatchFontDescriptorsWithProgressHandler(_:_:_:)

<sub>Function</sub>

Matches font descriptors and tracks progress with a progress handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontDescriptorMatchFontDescriptorsWithProgressHandler(_ descriptors: CFArray, _ mandatoryAttributes: CFSet?, _ progressBlock: @escaping CTFontDescriptorProgressHandler) -> Bool
```

## Parameters

- `descriptors` — An array of descriptors to process.

- `mandatoryAttributes` — A set of attributes to match.

- `progressBlock` — A callback block that indicates the progress of the matching process. Return [true](../swift/true.md) to continue or [false](../swift/false.md) to cancel the process. This block is called on a private serial queue.

## Return Value

[false](../swift/false.md) if the system couldn’t start the matching process.

## Discussion

This function returns immediately, but it can take longer to finish the process. The `progressBlock` handler tracks the progress.

## See Also

### Functions

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

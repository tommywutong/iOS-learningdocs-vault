---
title: 'CTFontManagerRegisterFontsWithAssetNames(_:_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontmanagerregisterfontswithassetnames(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontmanagerregisterfontswithassetnames(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontmanagerregisterfontswithassetnames%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:b628f1ccf1645d02'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontManagerRegisterFontsWithAssetNames(_:_:_:_:_:)

<sub>Function</sub>

Registers named font assets in the specified bundle with the font manager.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func CTFontManagerRegisterFontsWithAssetNames(_ fontAssetNames: CFArray, _ bundle: CFBundle?, _ scope: CTFontManagerScope, _ enabled: Bool, _ registrationHandler: ((CFArray, Bool) -> Bool)?)
```

## Parameters

- `fontAssetNames` — An array of font name assets in the asset catalog.

- `bundle` — A bundle that contains the asset catalog. Passing `NULL` resolves to the main bundle.

- `scope` — A scope constant that defines the availability and lifetime of the registration. On iOS, the only supported scope is [kCTFontManagerScopePersistent](ctfontmanagerscope/persistent.md), which means the fonts aren’t automatically available to other processes. Other processes can call [CTFontManagerRequestFonts](<ctfontmanagerrequestfonts(____).md>) to get access to the fonts. See [CTFontManagerScope](ctfontmanagerscope.md) for more details.

- `enabled` — A Boolean value that indicates whether the font assets should be enabled for font descriptor matching and discoverable through [CTFontManagerRequestFonts](<ctfontmanagerrequestfonts(____).md>).

- `registrationHandler` — A block called as errors arise or upon completion. The block’s `errors` parameter contains an array of [CFError](../corefoundation/cferror.md) references; an empty array indicates no errors. Each error reference contains a [CFArray](../corefoundation/cfarray.md) of font asset names corresponding to [kCTFontManagerErrorFontAssetNameKey](kctfontmanagererrorfontassetnamekey.md). These represent the font asset names causing the error and failing to register successfully. This block may be called multiple times during the registration process. The `done` parameter becomes [true](../swift/true.md) when the registration process completes. Return [false](../swift/false.md) from the block to stop the registration operation, like after receiving an error.

## Discussion

Registered fonts are discoverable through font descriptor matching in the calling process.

Calling this function extracts the font assets from the asset catalog and registers them. You must make this call after the completion handler of either [beginAccessingResources(completionHandler:)](<../foundation/nsbundleresourcerequest/beginaccessingresources(completionhandler_).md>): or [conditionallyBeginAccessingResources(completionHandler:)](<../foundation/nsbundleresourcerequest/conditionallybeginaccessingresources(completionhandler_).md>) is called successfully.

Name the assets using PostScript names for individual faces, or family names for variable or collection fonts. You can use the same names to unregister the fonts with [CTFontManagerUnregisterFontDescriptors](<ctfontmanagerunregisterfontdescriptors(______).md>).

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

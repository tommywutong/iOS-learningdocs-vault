---
title: 'CTRubyAnnotationCreate(_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctrubyannotationcreate(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctrubyannotationcreate(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrubyannotationcreate%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c4faf6e68bcc170d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTRubyAnnotationCreate(_:_:_:_:)

<sub>Function</sub>

Creates an immutable ruby annotation object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTRubyAnnotationCreate(_ alignment: CTRubyAlignment, _ overhang: CTRubyOverhang, _ sizeFactor: CGFloat, _ text: UnsafeMutablePointer<Unmanaged<CFString>?>) -> CTRubyAnnotation
```

## Parameters

- `alignment` — An alignment value that specifies how the ruby text and the base text align relative to each other.

- `overhang` — An overhang value that specifies how the ruby text overhangs adjacent characters.

- `sizeFactor` — A size factor that specifies the annotation text size as a percentage of the base text size.

- `text` — An array of [CFString](../corefoundation/cfstring.md) objects, indexed by [CTRubyPosition](ctrubyposition.md). Pass in `NULL` for any unused positions.

## Return Value

A reference to a [CTRubyAnnotation](ctrubyannotation.md) object.

## Discussion

Use this function to create a ruby annotation object in the most straightforward and efficient way.

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

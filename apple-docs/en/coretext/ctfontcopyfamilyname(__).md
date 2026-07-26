---
title: 'CTFontCopyFamilyName(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcopyfamilyname(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcopyfamilyname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcopyfamilyname%28_%3A%29.json'
content_hash: 'sha256:927dee88557313ac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCopyFamilyName(_:)

<sub>Function</sub>

Returns the family name of the given font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCopyFamilyName(_ font: CTFont) -> CFString
```

## Parameters

- `font` — The font reference.

## Return Value

A retained reference to the family name of the font.

## See Also

### Getting Font Names

- [CTFontCopyPostScriptName](<ctfontcopypostscriptname(__).md>) — Returns the PostScript name of the given font.
- [CTFontCopyFullName](<ctfontcopyfullname(__).md>) — Returns the full name of the given font.
- [CTFontCopyDisplayName](<ctfontcopydisplayname(__).md>) — Returns the display name of the given font.
- [CTFontCopyName](<ctfontcopyname(____).md>) — Returns a reference to the requested name of the given font.
- [CTFontCopyLocalizedName](<ctfontcopylocalizedname(______).md>) — Returns a reference to a localized name for the given font.

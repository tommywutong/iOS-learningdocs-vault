---
title: 'CTFontCopyName(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcopyname(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcopyname(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcopyname%28_%3A_%3A%29.json'
content_hash: 'sha256:a53fe1a32e10daea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCopyName(_:_:)

<sub>Function</sub>

Returns a reference to the requested name of the given font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCopyName(_ font: CTFont, _ nameKey: CFString) -> CFString?
```

## Parameters

- `font` — The font reference.

- `nameKey` — The name specifier. See [Name Specifier Constants](name-specifier-constants.md) for possible values.

## Return Value

The requested name for the font, or `NULL` if the font does not have an entry for the requested name. The Unicode version of the name is preferred, otherwise the first available version is returned.

## See Also

### Getting Font Names

- [CTFontCopyPostScriptName](<ctfontcopypostscriptname(__).md>) — Returns the PostScript name of the given font.
- [CTFontCopyFamilyName](<ctfontcopyfamilyname(__).md>) — Returns the family name of the given font.
- [CTFontCopyFullName](<ctfontcopyfullname(__).md>) — Returns the full name of the given font.
- [CTFontCopyDisplayName](<ctfontcopydisplayname(__).md>) — Returns the display name of the given font.
- [CTFontCopyLocalizedName](<ctfontcopylocalizedname(______).md>) — Returns a reference to a localized name for the given font.

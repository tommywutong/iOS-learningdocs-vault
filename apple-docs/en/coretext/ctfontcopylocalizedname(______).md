---
title: 'CTFontCopyLocalizedName(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcopylocalizedname(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcopylocalizedname(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcopylocalizedname%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:890aa1c703c9dc2b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCopyLocalizedName(_:_:_:)

<sub>Function</sub>

Returns a reference to a localized name for the given font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCopyLocalizedName(_ font: CTFont, _ nameKey: CFString, _ actualLanguage: UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFString?
```

## Parameters

- `font` — The font reference.

- `nameKey` — The name specifier. See [Name Specifier Constants](name-specifier-constants.md) for possible values.

- `actualLanguage` — On output, points to the language string of the returned name string. The format of the language identifier conforms to the RFC 3066bis standard.

## Return Value

A specific localized name from the font reference or `NULL` if the font does not have an entry for the requested name key.

## Discussion

The name is localized based on the user’s global language preference precedence. That is, the user’s language preference is a list of languages in order of precedence. So, for example, if the list had Japanese and English, in that order, then a font that did not have Japanese name strings but had English strings would return the English strings.

## See Also

### Getting Font Names

- [CTFontCopyPostScriptName](<ctfontcopypostscriptname(__).md>) — Returns the PostScript name of the given font.
- [CTFontCopyFamilyName](<ctfontcopyfamilyname(__).md>) — Returns the family name of the given font.
- [CTFontCopyFullName](<ctfontcopyfullname(__).md>) — Returns the full name of the given font.
- [CTFontCopyDisplayName](<ctfontcopydisplayname(__).md>) — Returns the display name of the given font.
- [CTFontCopyName](<ctfontcopyname(____).md>) — Returns a reference to the requested name of the given font.

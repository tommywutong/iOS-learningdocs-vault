---
title: 'CTFontCopySupportedLanguages(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcopysupportedlanguages(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcopysupportedlanguages(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcopysupportedlanguages%28_%3A%29.json'
content_hash: 'sha256:73e76ea6d1ba710f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCopySupportedLanguages(_:)

<sub>Function</sub>

Returns an array of languages supported by the font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCopySupportedLanguages(_ font: CTFont) -> CFArray
```

## Parameters

- `font` — The font reference.

## Return Value

A retained reference to an array of languages supported by the font. The array contains language identifier strings as `CFStringRef` objects. The format of the language identifier conforms to the RFC 3066bis standard.

## See Also

### Working With Encoding

- [CTFontCopyCharacterSet](<ctfontcopycharacterset(__).md>) — Returns the Unicode character set of the font.
- [CTFontGetStringEncoding](<ctfontgetstringencoding(__).md>) — Returns the best string encoding for legacy format support.

---
title: 'CTFontGetStringEncoding(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontgetstringencoding(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontgetstringencoding(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontgetstringencoding%28_%3A%29.json'
content_hash: 'sha256:9a6b279673ceaa48'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontGetStringEncoding(_:)

<sub>Function</sub>

Returns the best string encoding for legacy format support.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontGetStringEncoding(_ font: CTFont) -> CFStringEncoding
```

## Parameters

- `font` — The font reference.

## Return Value

The best string encoding for the font.

## See Also

### Working With Encoding

- [CTFontCopyCharacterSet](<ctfontcopycharacterset(__).md>) — Returns the Unicode character set of the font.
- [CTFontCopySupportedLanguages](<ctfontcopysupportedlanguages(__).md>) — Returns an array of languages supported by the font.

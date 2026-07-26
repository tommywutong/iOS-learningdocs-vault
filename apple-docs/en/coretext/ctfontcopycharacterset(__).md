---
title: 'CTFontCopyCharacterSet(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctfontcopycharacterset(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctfontcopycharacterset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontcopycharacterset%28_%3A%29.json'
content_hash: 'sha256:d437464eb8daa933'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontCopyCharacterSet(_:)

<sub>Function</sub>

Returns the Unicode character set of the font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontCopyCharacterSet(_ font: CTFont) -> CFCharacterSet
```

## Parameters

- `font` — The font reference.

## Return Value

A retained reference to the font’s character set.

## Discussion

The returned character set covers the nominal referenced by the font’s Unicode `'cmap’` table.

## See Also

### Working With Encoding

- [CTFontGetStringEncoding](<ctfontgetstringencoding(__).md>) — Returns the best string encoding for legacy format support.
- [CTFontCopySupportedLanguages](<ctfontcopysupportedlanguages(__).md>) — Returns an array of languages supported by the font.

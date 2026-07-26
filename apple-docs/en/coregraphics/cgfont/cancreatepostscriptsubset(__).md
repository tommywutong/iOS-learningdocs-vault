---
title: 'canCreatePostScriptSubset(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgfont/cancreatepostscriptsubset(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/cancreatepostscriptsubset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/cancreatepostscriptsubset%28_%3A%29.json'
content_hash: 'sha256:613da2b15bfabf68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# canCreatePostScriptSubset(_:)

<sub>Instance Method</sub>

Determines whether Core Graphics can create a subset of the font in PostScript format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func canCreatePostScriptSubset(_ format: CGFontPostScriptFormat) -> Bool
```

## Parameters

- `format` — A PostScript font format.

## Return Value

Returns `true` if a subset in the PostScript format can be created for the font; `false` otherwise.

## Discussion

For more information on PostScript format, see _Adobe Type 1 Font Format_, which is available from [http://partners.adobe.com/](http://partners.adobe.com/).

## See Also

### Working with PostScript Fonts

- [CGFontCopyPostScriptName](postscriptname.md) — Obtains the PostScript name of a font.
- [CGFontCreatePostScriptSubset](<createpostscriptsubset(subsetname_format_glyphs_count_encoding_).md>) — Creates a subset of the font in the specified PostScript format.
- [CGFontPostScriptFormat](../cgfontpostscriptformat.md) — Possible formats for a PostScript font subset.
- [CGFontCreatePostScriptEncoding](<createpostscriptencoding(encoding_).md>) — Creates a PostScript encoding of a font.

---
title: 'createPostScriptEncoding(encoding:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgfont/createpostscriptencoding(encoding:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/createpostscriptencoding(encoding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/createpostscriptencoding%28encoding%3A%29.json'
content_hash: 'sha256:7caa6033dc818a4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# createPostScriptEncoding(encoding:)

<sub>Instance Method</sub>

Creates a PostScript encoding of a font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func createPostScriptEncoding(encoding: UnsafePointer<CGGlyph>?) -> CFData?
```

## Parameters

- `encoding` — The encoding to use.

## Return Value

A PostScript encoding of the font that contains glyphs in the specified encoding.

## Discussion

For more information on PostScript format, see _Adobe Type 1 Font Format_, which is available from [http://partners.adobe.com/](http://partners.adobe.com/).

## See Also

### Working with PostScript Fonts

- [CGFontCopyPostScriptName](postscriptname.md) — Obtains the PostScript name of a font.
- [CGFontCanCreatePostScriptSubset](<cancreatepostscriptsubset(__).md>) — Determines whether Core Graphics can create a subset of the font in PostScript format.
- [CGFontCreatePostScriptSubset](<createpostscriptsubset(subsetname_format_glyphs_count_encoding_).md>) — Creates a subset of the font in the specified PostScript format.
- [CGFontPostScriptFormat](../cgfontpostscriptformat.md) — Possible formats for a PostScript font subset.

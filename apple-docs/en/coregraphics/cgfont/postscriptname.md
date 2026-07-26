---
title: postScriptName
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfont/postscriptname
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/postscriptname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/postscriptname.json'
content_hash: 'sha256:7112b977900f02a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# postScriptName

<sub>Instance Property</sub>

Obtains the PostScript name of a font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var postScriptName: CFString? { get }
```

## Discussion

For more information on PostScript format, see _Adobe Type 1 Font Format_, which is available from [http://partners.adobe.com/](http://partners.adobe.com/).

## See Also

### Working with PostScript Fonts

- [CGFontCanCreatePostScriptSubset](<cancreatepostscriptsubset(__).md>) — Determines whether Core Graphics can create a subset of the font in PostScript format.
- [CGFontCreatePostScriptSubset](<createpostscriptsubset(subsetname_format_glyphs_count_encoding_).md>) — Creates a subset of the font in the specified PostScript format.
- [CGFontPostScriptFormat](../cgfontpostscriptformat.md) — Possible formats for a PostScript font subset.
- [CGFontCreatePostScriptEncoding](<createpostscriptencoding(encoding_).md>) — Creates a PostScript encoding of a font.

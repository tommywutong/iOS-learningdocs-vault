---
title: 'createPostScriptSubset(subsetName:format:glyphs:count:encoding:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgfont/createpostscriptsubset(subsetname:format:glyphs:count:encoding:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/createpostscriptsubset(subsetname:format:glyphs:count:encoding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/createpostscriptsubset%28subsetname%3Aformat%3Aglyphs%3Acount%3Aencoding%3A%29.json'
content_hash: 'sha256:9d3842434acd85e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# createPostScriptSubset(subsetName:format:glyphs:count:encoding:)

<sub>Instance Method</sub>

Creates a subset of the font in the specified PostScript format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func createPostScriptSubset(subsetName: CFString, format: CGFontPostScriptFormat, glyphs: UnsafePointer<CGGlyph>?, count: Int, encoding: UnsafePointer<CGGlyph>?) -> CFData?
```

## Parameters

- `subsetName` — The name of the subset.

- `format` — The PostScript format of the font.

- `glyphs` — An array that contains the glyphs in the subset.

- `count` — The number of glyphs specified by the `glyphs` array.

- `encoding` — The default encoding for the subset. You can pass `nil` if you do not want to specify an encoding.

## Return Value

A subset of the font created from the supplied parameters.

## Discussion

For more information on PostScript format, see _Adobe Type 1 Font Format_, which is available from [http://partners.adobe.com/](http://partners.adobe.com/).

## See Also

### Working with PostScript Fonts

- [CGFontCopyPostScriptName](postscriptname.md) — Obtains the PostScript name of a font.
- [CGFontCanCreatePostScriptSubset](<cancreatepostscriptsubset(__).md>) — Determines whether Core Graphics can create a subset of the font in PostScript format.
- [CGFontPostScriptFormat](../cgfontpostscriptformat.md) — Possible formats for a PostScript font subset.
- [CGFontCreatePostScriptEncoding](<createpostscriptencoding(encoding_).md>) — Creates a PostScript encoding of a font.

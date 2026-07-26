---
title: CGFontPostScriptFormat
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfontpostscriptformat
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfontpostscriptformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfontpostscriptformat.json'
content_hash: 'sha256:9b86d1c88fb8cc51'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGFontPostScriptFormat

<sub>Enumeration</sub>

Possible formats for a PostScript font subset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGFontPostScriptFormat
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGFontPostScriptFormatType1](cgfontpostscriptformat/type1.md) — A Type 1 font format.
- [kCGFontPostScriptFormatType3](cgfontpostscriptformat/type3.md) — A Type 3 PostScript format.
- [kCGFontPostScriptFormatType42](cgfontpostscriptformat/type42.md) — A constant representing a Type 42 font format.

### Initializers

- [init(rawValue:)](<cgfontpostscriptformat/init(rawvalue_).md>)

## See Also

### Working with PostScript Fonts

- [CGFontCopyPostScriptName](cgfont/postscriptname.md) — Obtains the PostScript name of a font.
- [CGFontCanCreatePostScriptSubset](<cgfont/cancreatepostscriptsubset(__).md>) — Determines whether Core Graphics can create a subset of the font in PostScript format.
- [CGFontCreatePostScriptSubset](<cgfont/createpostscriptsubset(subsetname_format_glyphs_count_encoding_).md>) — Creates a subset of the font in the specified PostScript format.
- [CGFontCreatePostScriptEncoding](<cgfont/createpostscriptencoding(encoding_).md>) — Creates a PostScript encoding of a font.

---
title: noteProgress
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst, macOS]
languages: [swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpsconvertercallbacks/noteprogress
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpsconvertercallbacks/noteprogress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpsconvertercallbacks/noteprogress.json'
content_hash: 'sha256:75e96d3d37bda1de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPSConverterCallbacks](../cgpsconvertercallbacks.md)

# noteProgress

<sub>Instance Property</sub>

The callback called periodically during the conversion to indicate that conversion is proceeding, or `NULL`.

<sub>Mac Catalyst, macOS</sub>

```swift
var noteProgress: CGPSConverterProgressCallback?
```

## See Also

### Instance Properties

- [beginDocument](begindocument.md) — The callback called at the beginning of the conversion of the PostScript document, or `NULL`.
- [beginPage](beginpage.md) — The callback called at the start of the conversion of each page in the PostScript document, or `NULL`.
- [endDocument](enddocument.md) — The callback called at the end of conversion of the PostScript document, or `NULL`.
- [endPage](endpage.md) — The callback called at the end of the conversion of each page in the PostScript document, or `NULL`.
- [noteMessage](notemessage.md) — The callback called to pass any messages that might result during the conversion, or `NULL`.
- [releaseInfo](releaseinfo.md) — The callback called when the converter is deallocated, or `NULL`.
- [version](version.md) — The version number of the structure passed in as a parameter to the converter creation functions. The structure defined below is version `0`.

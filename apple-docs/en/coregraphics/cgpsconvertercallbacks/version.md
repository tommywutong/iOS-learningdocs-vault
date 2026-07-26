---
title: version
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst, macOS]
languages: [swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpsconvertercallbacks/version
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpsconvertercallbacks/version'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpsconvertercallbacks/version.json'
content_hash: 'sha256:90c8575fa5ef1f5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPSConverterCallbacks](../cgpsconvertercallbacks.md)

# version

<sub>Instance Property</sub>

The version number of the structure passed in as a parameter to the converter creation functions. The structure defined below is version `0`.

<sub>Mac Catalyst, macOS</sub>

```swift
var version: UInt32
```

## See Also

### Instance Properties

- [beginDocument](begindocument.md) — The callback called at the beginning of the conversion of the PostScript document, or `NULL`.
- [beginPage](beginpage.md) — The callback called at the start of the conversion of each page in the PostScript document, or `NULL`.
- [endDocument](enddocument.md) — The callback called at the end of conversion of the PostScript document, or `NULL`.
- [endPage](endpage.md) — The callback called at the end of the conversion of each page in the PostScript document, or `NULL`.
- [noteMessage](notemessage.md) — The callback called to pass any messages that might result during the conversion, or `NULL`.
- [noteProgress](noteprogress.md) — The callback called periodically during the conversion to indicate that conversion is proceeding, or `NULL`.
- [releaseInfo](releaseinfo.md) — The callback called when the converter is deallocated, or `NULL`.

---
title: CGPSConverterCallbacks
framework: Core Graphics
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst, macOS]
languages: [swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpsconvertercallbacks
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpsconvertercallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpsconvertercallbacks.json'
content_hash: 'sha256:85c8c2537d7bcd34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPSConverterCallbacks

<sub>Structure</sub>

A structure for holding the callbacks provided when you create a PostScript converter object.

<sub>Mac Catalyst, macOS</sub>

```swift
struct CGPSConverterCallbacks
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cgpsconvertercallbacks/init().md>)
- [init(version:beginDocument:endDocument:beginPage:endPage:noteProgress:noteMessage:releaseInfo:)](<cgpsconvertercallbacks/init(version_begindocument_enddocument_beginpage_endpage_noteprogress_notemessage_releaseinfo_).md>)

### Instance Properties

- [beginDocument](cgpsconvertercallbacks/begindocument.md) — The callback called at the beginning of the conversion of the PostScript document, or `NULL`.
- [beginPage](cgpsconvertercallbacks/beginpage.md) — The callback called at the start of the conversion of each page in the PostScript document, or `NULL`.
- [endDocument](cgpsconvertercallbacks/enddocument.md) — The callback called at the end of conversion of the PostScript document, or `NULL`.
- [endPage](cgpsconvertercallbacks/endpage.md) — The callback called at the end of the conversion of each page in the PostScript document, or `NULL`.
- [noteMessage](cgpsconvertercallbacks/notemessage.md) — The callback called to pass any messages that might result during the conversion, or `NULL`.
- [noteProgress](cgpsconvertercallbacks/noteprogress.md) — The callback called periodically during the conversion to indicate that conversion is proceeding, or `NULL`.
- [releaseInfo](cgpsconvertercallbacks/releaseinfo.md) — The callback called when the converter is deallocated, or `NULL`.
- [version](cgpsconvertercallbacks/version.md) — The version number of the structure passed in as a parameter to the converter creation functions. The structure defined below is version `0`.

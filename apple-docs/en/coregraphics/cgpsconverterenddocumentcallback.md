---
title: CGPSConverterEndDocumentCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst, macOS]
languages: [swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpsconverterenddocumentcallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpsconverterenddocumentcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpsconverterenddocumentcallback.json'
content_hash: 'sha256:69d8108e0adc1cd7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPSConverterEndDocumentCallback

<sub>Type Alias</sub>

Performs custom tasks at the end of a PostScript conversion process.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias CGPSConverterEndDocumentCallback = (UnsafeMutableRawPointer?, Bool) -> Void
```

## Parameters

- `info` — A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [CGPSConverterCreate](<cgpsconverter/init(info_callbacks_options_).md>).

- `success` — A Boolean value that indicates whether the PostScript conversion completed successfully ([true](../swift/true.md) if it did).

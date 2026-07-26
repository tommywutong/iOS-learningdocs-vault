---
title: CGPSConverterProgressCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst, macOS]
languages: [swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpsconverterprogresscallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpsconverterprogresscallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpsconverterprogresscallback.json'
content_hash: 'sha256:2043426ba8065020'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPSConverterProgressCallback

<sub>Type Alias</sub>

Reports progress periodically during a PostScript conversion process.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias CGPSConverterProgressCallback = (UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `info` — A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [CGPSConverterCreate](<cgpsconverter/init(info_callbacks_options_).md>).

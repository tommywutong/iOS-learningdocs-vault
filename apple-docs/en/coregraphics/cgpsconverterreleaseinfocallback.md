---
title: CGPSConverterReleaseInfoCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst, macOS]
languages: [swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpsconverterreleaseinfocallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpsconverterreleaseinfocallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpsconverterreleaseinfocallback.json'
content_hash: 'sha256:4dc663b0b3b739be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPSConverterReleaseInfoCallback

<sub>Type Alias</sub>

Performs custom tasks when a PostScript converter is released.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias CGPSConverterReleaseInfoCallback = (UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `info` — A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [CGPSConverterCreate](<cgpsconverter/init(info_callbacks_options_).md>).

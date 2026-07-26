---
title: CGPSConverterBeginPageCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst, macOS]
languages: [swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpsconverterbeginpagecallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpsconverterbeginpagecallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpsconverterbeginpagecallback.json'
content_hash: 'sha256:5a2c27a9399cdebd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPSConverterBeginPageCallback

<sub>Type Alias</sub>

Performs custom tasks at the beginning of each page in a PostScript conversion process.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias CGPSConverterBeginPageCallback = (UnsafeMutableRawPointer?, Int, CFDictionary) -> Void
```

## Parameters

- `info` — A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [CGPSConverterCreate](<cgpsconverter/init(info_callbacks_options_).md>).

- `pageNumber` — The current page number. Page numbers start at `1`.

- `pageInfo` — A dictionary that contains contextual information about the page. This parameter is reserved for future API expansion, and is currently unused.

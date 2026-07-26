---
title: CGPSConverterEndPageCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst, macOS]
languages: [swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpsconverterendpagecallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpsconverterendpagecallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpsconverterendpagecallback.json'
content_hash: 'sha256:385d43f99c3482dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPSConverterEndPageCallback

<sub>Type Alias</sub>

Performs custom tasks at the end of each page of a PostScript conversion process.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias CGPSConverterEndPageCallback = (UnsafeMutableRawPointer?, Int, CFDictionary) -> Void
```

## Parameters

- `info` — A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [CGPSConverterCreate](<cgpsconverter/init(info_callbacks_options_).md>).

- `pageNumber` — The current page number. Page numbers start at `1`.

- `pageInfo` — A dictionary that contains contextual information about the page. This parameter is reserved for future API expansion, and is currently unused.

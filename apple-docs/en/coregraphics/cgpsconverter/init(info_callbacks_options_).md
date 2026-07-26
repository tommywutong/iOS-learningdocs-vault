---
title: 'init(info:callbacks:options:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.1+, macOS 10.3+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpsconverter/init(info:callbacks:options:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpsconverter/init(info:callbacks:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpsconverter/init%28info%3Acallbacks%3Aoptions%3A%29.json'
content_hash: 'sha256:2b7eeb51b252d378'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPSConverter](../cgpsconverter.md)

# init(info:callbacks:options:)

<sub>Initializer</sub>

Creates a new PostScript converter.

<sub>Mac Catalyst, macOS</sub>

```swift
init?(info: UnsafeMutableRawPointer?, callbacks: UnsafePointer<CGPSConverterCallbacks>, options: CFDictionary?)
```

## Parameters

- `info` — A pointer to the data that will be passed to the callbacks.

- `callbacks` — A pointer to a PostScript converter callbacks structure that specifies the callbacks to be used during a conversion process.

- `options` — This parameter should be `NULL`; it is reserved for future expansion of the API.

## Return Value

A new PostScript converter, or `NULL` if a converter could not be created. You are responsible for releasing this object.

---
title: CGPSConverterMessageCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst, macOS]
languages: [swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpsconvertermessagecallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpsconvertermessagecallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpsconvertermessagecallback.json'
content_hash: 'sha256:4d3c578adb0ca368'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPSConverterMessageCallback

<sub>Type Alias</sub>

Passes messages generated during a PostScript conversion process.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias CGPSConverterMessageCallback = (UnsafeMutableRawPointer?, CFString) -> Void
```

## Parameters

- `info` — A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [CGPSConverterCreate](<cgpsconverter/init(info_callbacks_options_).md>).

- `message` — A string containing the message from the PostScript conversion process.

## Discussion

There are several kinds of message that might be sent during a conversion process. The most likely are font substitution messages, and any messages that the PostScript code itself generates. Any PostScript messages written to `stdout` are routed through this callback—typically these are debugging or status messages and, although uncommon, can be useful in debugging. In addition, there may be error messages if the document is malformed.

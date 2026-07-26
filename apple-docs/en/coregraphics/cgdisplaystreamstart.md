---
title: CGDisplayStreamStart
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaystreamstart
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaystreamstart'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaystreamstart.json'
content_hash: 'sha256:c09ca42267be0eb9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayStreamStart

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
extern CGError CGDisplayStreamStart(CGDisplayStreamRef displayStream);
```

## Parameters

- `displayStream` — To be started

## Return Value

kCGErrorSuccess If the display stream was started, otherwise an error.

## Discussion

Begin delivering frame updates to the handler block.

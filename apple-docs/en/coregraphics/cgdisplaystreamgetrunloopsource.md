---
title: CGDisplayStreamGetRunLoopSource
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaystreamgetrunloopsource
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaystreamgetrunloopsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaystreamgetrunloopsource.json'
content_hash: 'sha256:9800cbb7019ef667'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayStreamGetRunLoopSource

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
extern CFRunLoopSourceRefCGDisplayStreamGetRunLoopSource(CGDisplayStreamRef displayStream);
```

## Parameters

- `displayStream` — The CGDisplayStream object

## Return Value

The CFRunLoopSource for this displayStream.  Note: This function will return NULL if the display stream was created via  CGDisplayStreamCreateWithDispatchQueue().

## Discussion

Return the singleton CFRunLoopSourceRef for a CGDisplayStream.

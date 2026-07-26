---
title: CGDisplayStreamStop
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaystreamstop
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaystreamstop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaystreamstop.json'
content_hash: 'sha256:366bc83289315c28'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayStreamStop

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
extern CGError CGDisplayStreamStop(CGDisplayStreamRef displayStream);
```

## Parameters

- `displayStream` — To be stopped

## Return Value

kCGErrorSuccess If the display stream was stopped, otherwise an error.

## Discussion

End delivery of frame updates to the handler block.

After this call returns, the CGDisplayStream callback function will eventually be called with a status of kCGDisplayStreamFrameStatusStopped.  After that point it is safe to release the CGDisplayStream. It is safe to call this function from within the handler block, but the previous caveat still applies.

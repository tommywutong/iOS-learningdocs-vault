---
title: CGDisplayStreamUpdateGetDropCount
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaystreamupdategetdropcount
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdategetdropcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaystreamupdategetdropcount.json'
content_hash: 'sha256:3aed9cd86ce064a0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayStreamUpdateGetDropCount

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
extern size_t CGDisplayStreamUpdateGetDropCount(CGDisplayStreamUpdateRef updateRef);
```

## Parameters

- `updateRef` — The CGDisplayStreamUpdateRef

## Return Value

The number of dropped frames

## Discussion

Return how many frames (if any) have been dropped since the last call to the handler.

This call is primarily useful for performance measurement to determine if the client is keeping up with all WindowServer updates.

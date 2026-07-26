---
title: CGDisplayStreamUpdateGetRects
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaystreamupdategetrects
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdategetrects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaystreamupdategetrects.json'
content_hash: 'sha256:279bd2535aaca7d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayStreamUpdateGetRects

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
extern const CGRect *CGDisplayStreamUpdateGetRects(CGDisplayStreamUpdateRef updateRef, CGDisplayStreamUpdateRectType rectType, size_t *rectCount);
```

## Parameters

- `updateRef` — The CGDisplayStreamUpdateRef

- `rectCount` — A pointer to where the count of the number of rectangles in the array is to be returned. Must not be NULL.

## Return Value

A pointer to the array of CGRectangles.  This array should not be freed by the caller.

## Discussion

Returns a pointer to an array of CGRect structs that describe what parts of the frame have changed relative to the previously delivered frame.   This rectangle list encapsulates both the update rectangles and movement rectangles.

---
title: CGDisplayStreamUpdateGetMovedRectsDelta
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaystreamupdategetmovedrectsdelta
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdategetmovedrectsdelta'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaystreamupdategetmovedrectsdelta.json'
content_hash: 'sha256:3f6d487233a9afe0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayStreamUpdateGetMovedRectsDelta

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
extern void CGDisplayStreamUpdateGetMovedRectsDelta(CGDisplayStreamUpdateRef updateRef, CGFloat *dx, CGFloat *dy);
```

## Parameters

- `updateRef` — The CGDisplayStreamUpdateRef

- `dx` — A pointer to a CGFloat to store the x component of the movement delta

- `dy` — A pointer to a CGFloat to store the y component of the movement delta

## Discussion

Return the movement dx and dy values for a single update

The delta values describe the offset from the moved rectangles back to the source location.

---
title: CGDisplayStreamUpdateCreateMergedUpdate
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaystreamupdatecreatemergedupdate
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdatecreatemergedupdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaystreamupdatecreatemergedupdate.json'
content_hash: 'sha256:3e3338ff402e3f97'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayStreamUpdateCreateMergedUpdate

<sub>Function</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
extern CGDisplayStreamUpdateRefCGDisplayStreamUpdateCreateMergedUpdate(CGDisplayStreamUpdateRef firstUpdate, CGDisplayStreamUpdateRef secondUpdate);
```

## Parameters

- `firstUpdate` — The first update (in a temporal sense)

- `secondUpdate` — The second update (in a temporal sense)

## Return Value

The new CGDisplayStreamUpdateRef

## Discussion

Merge two CGDisplayUpdateRefs into a new one.

In cases where the client wishes to drop certain frame updates, this function may be used to merge two CGDisplayUpdateRefs together.  The core bit of functionality here is generating a new set of refresh/move/dirty rectangle arrays that properly represent the union of the deltas between the two frames.  Note that the ordering of the two refs is important.

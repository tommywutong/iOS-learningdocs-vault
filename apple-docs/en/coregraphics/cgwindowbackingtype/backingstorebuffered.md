---
title: CGWindowBackingType.backingStoreBuffered
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowbackingtype/backingstorebuffered
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowbackingtype/backingstorebuffered'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowbackingtype/backingstorebuffered.json'
content_hash: 'sha256:70b7fc3ab3d2aa2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGWindowBackingType](../cgwindowbackingtype.md)

# CGWindowBackingType.backingStoreBuffered

<sub>Case</sub>

<sub>Mac Catalyst, macOS</sub>

```swift
case backingStoreBuffered
```

## Discussion

The window draws into a display buffer and then flushes that buffer to the screen.

You should typically use this mode. It supports hardware acceleration, Quartz drawing, and takes advantage of the GPU when possible. It also supports alpha channel drawing, opacity controls, using the compositor.

## See Also

### Constants

- [kCGBackingStoreNonretained](backingstorenonretained.md)
- [kCGBackingStoreRetained](backingstoreretained.md)

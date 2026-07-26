---
title: CGWindowBackingType.backingStoreNonretained
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowbackingtype/backingstorenonretained
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowbackingtype/backingstorenonretained'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowbackingtype/backingstorenonretained.json'
content_hash: 'sha256:09e92831bfbcd6cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGWindowBackingType](../cgwindowbackingtype.md)

# CGWindowBackingType.backingStoreNonretained

<sub>Case</sub>

<sub>Mac Catalyst, macOS</sub>

```swift
case backingStoreNonretained
```

## Discussion

The window draws directly to the screen without using any buffer.

You should typically not use this mode. It exists primarily for use in the original Classic Blue Box. It does not support Quartz drawing, alpha blending, or opacity. Moreover, it does not support hardware acceleration, and interferes with system-wide display acceleration. If you use this mode, your application must manage visibility region clipping itself, and manage repainting on visibility changes.

## See Also

### Constants

- [kCGBackingStoreBuffered](backingstorebuffered.md)
- [kCGBackingStoreRetained](backingstoreretained.md)

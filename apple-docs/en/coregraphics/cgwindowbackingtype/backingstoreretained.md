---
title: CGWindowBackingType.backingStoreRetained
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowbackingtype/backingstoreretained
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowbackingtype/backingstoreretained'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowbackingtype/backingstoreretained.json'
content_hash: 'sha256:cdda190384b39dc6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGWindowBackingType](../cgwindowbackingtype.md)

# CGWindowBackingType.backingStoreRetained

<sub>Case</sub>

<sub>Mac Catalyst, macOS</sub>

```swift
case backingStoreRetained
```

## Discussion

The window uses a buffer, but draws directly to the screen where possible and to the buffer for obscured portions.

You should typically not use this mode. It combines the limitations of [kCGBackingStoreNonretained](backingstorenonretained.md) with the memory use of [kCGBackingStoreBuffered](backingstorebuffered.md). The original NeXTSTEP implementation was an interesting compromise that worked well with fast memory mapped framebuffers on the CPU bus—something that hasn’t been in general use since around 1994. These tend to have performance problems.

In macOS 10.5 and later, requests for retained windows will result in the window system creating a buffered window, as that better matches actual use

## See Also

### Constants

- [kCGBackingStoreBuffered](backingstorebuffered.md)
- [kCGBackingStoreNonretained](backingstorenonretained.md)

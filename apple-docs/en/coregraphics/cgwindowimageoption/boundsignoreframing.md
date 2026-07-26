---
title: boundsIgnoreFraming
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowimageoption/boundsignoreframing
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/boundsignoreframing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowimageoption/boundsignoreframing.json'
content_hash: 'sha256:f75d0140ac4eefc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGWindowImageOption](../cgwindowimageoption.md)

# boundsIgnoreFraming

<sub>Type Property</sub>

<sub>Mac Catalyst, macOS</sub>

```swift
static var boundsIgnoreFraming: CGWindowImageOption { get }
```

## Discussion

When the requested capture rectangle is [CGRectNull](../cgrectnull.md), using this option captures the window area only and does not capture the area occupied by any window framing effects.

## See Also

### Type Properties

- [kCGWindowImageBestResolution](bestresolution.md) — When capturing the window, return the best image resolution. The returned image size may be different than the screen size.
- [kCGWindowImageNominalResolution](nominalresolution.md) — When capturing the window, return the nominal image resolution. The returned image size is the same as the screen size.
- [kCGWindowImageOnlyShadows](onlyshadows.md)
- [kCGWindowImageShouldBeOpaque](shouldbeopaque.md)

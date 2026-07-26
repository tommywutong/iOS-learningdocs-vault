---
title: onlyShadows
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowimageoption/onlyshadows
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/onlyshadows'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowimageoption/onlyshadows.json'
content_hash: 'sha256:195e467715f82819'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGWindowImageOption](../cgwindowimageoption.md)

# onlyShadows

<sub>Type Property</sub>

<sub>Mac Catalyst, macOS</sub>

```swift
static var onlyShadows: CGWindowImageOption { get }
```

## Discussion

When capturing the window, only the shadow effects are captured.

## See Also

### Type Properties

- [kCGWindowImageBestResolution](bestresolution.md) — When capturing the window, return the best image resolution. The returned image size may be different than the screen size.
- [kCGWindowImageBoundsIgnoreFraming](boundsignoreframing.md)
- [kCGWindowImageNominalResolution](nominalresolution.md) — When capturing the window, return the nominal image resolution. The returned image size is the same as the screen size.
- [kCGWindowImageShouldBeOpaque](shouldbeopaque.md)

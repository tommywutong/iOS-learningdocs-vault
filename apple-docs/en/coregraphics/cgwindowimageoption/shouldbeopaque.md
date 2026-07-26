---
title: shouldBeOpaque
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowimageoption/shouldbeopaque
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/shouldbeopaque'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowimageoption/shouldbeopaque.json'
content_hash: 'sha256:4beb296eebb1bf54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGWindowImageOption](../cgwindowimageoption.md)

# shouldBeOpaque

<sub>Type Property</sub>

<sub>Mac Catalyst, macOS</sub>

```swift
static var shouldBeOpaque: CGWindowImageOption { get }
```

## Discussion

When capturing the window, partially transparent areas are backed by a solid white color so that the resulting image is fully opaque. You can combine this option with other options.

## See Also

### Type Properties

- [kCGWindowImageBestResolution](bestresolution.md) — When capturing the window, return the best image resolution. The returned image size may be different than the screen size.
- [kCGWindowImageBoundsIgnoreFraming](boundsignoreframing.md)
- [kCGWindowImageNominalResolution](nominalresolution.md) — When capturing the window, return the nominal image resolution. The returned image size is the same as the screen size.
- [kCGWindowImageOnlyShadows](onlyshadows.md)

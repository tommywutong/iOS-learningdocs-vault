---
title: bestResolution
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowimageoption/bestresolution
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/bestresolution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowimageoption/bestresolution.json'
content_hash: 'sha256:0301ad8970fe4852'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGWindowImageOption](../cgwindowimageoption.md)

# bestResolution

<sub>Type Property</sub>

When capturing the window, return the best image resolution. The returned image size may be different than the screen size.

<sub>Mac Catalyst, macOS</sub>

```swift
static var bestResolution: CGWindowImageOption { get }
```

## See Also

### Type Properties

- [kCGWindowImageBoundsIgnoreFraming](boundsignoreframing.md)
- [kCGWindowImageNominalResolution](nominalresolution.md) — When capturing the window, return the nominal image resolution. The returned image size is the same as the screen size.
- [kCGWindowImageOnlyShadows](onlyshadows.md)
- [kCGWindowImageShouldBeOpaque](shouldbeopaque.md)

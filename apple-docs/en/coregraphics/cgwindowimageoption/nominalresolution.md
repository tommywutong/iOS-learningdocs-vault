---
title: nominalResolution
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst, macOS]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowimageoption/nominalresolution
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/nominalresolution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowimageoption/nominalresolution.json'
content_hash: 'sha256:b0f05d84f66162f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGWindowImageOption](../cgwindowimageoption.md)

# nominalResolution

<sub>Type Property</sub>

When capturing the window, return the nominal image resolution. The returned image size is the same as the screen size.

<sub>Mac Catalyst, macOS</sub>

```swift
static var nominalResolution: CGWindowImageOption { get }
```

## See Also

### Type Properties

- [kCGWindowImageBestResolution](bestresolution.md) — When capturing the window, return the best image resolution. The returned image size may be different than the screen size.
- [kCGWindowImageBoundsIgnoreFraming](boundsignoreframing.md)
- [kCGWindowImageOnlyShadows](onlyshadows.md)
- [kCGWindowImageShouldBeOpaque](shouldbeopaque.md)

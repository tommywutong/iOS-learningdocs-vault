---
title: kCGWindowImageDefault
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [Mac Catalyst, macOS]
languages: [occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowimageoption/kcgwindowimagedefault
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/kcgwindowimagedefault'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowimageoption/kcgwindowimagedefault.json'
content_hash: 'sha256:1ec8a4d1ec9746c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGWindowImageOption](../cgwindowimageoption.md)

# kCGWindowImageDefault

<sub>Enumeration Case</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
kCGWindowImageDefault
```

## Discussion

When the requested capture rectangle is [CGRectNull](../cgrectnull.md), using this option captures the entire window plus the area required to display any framing effects, such as the window’s shadow. This is the default behavior.

## See Also

### Type Properties

- [kCGWindowImageBestResolution](bestresolution.md) — When capturing the window, return the best image resolution. The returned image size may be different than the screen size.
- [kCGWindowImageBoundsIgnoreFraming](boundsignoreframing.md)
- [kCGWindowImageNominalResolution](nominalresolution.md) — When capturing the window, return the nominal image resolution. The returned image size is the same as the screen size.
- [kCGWindowImageOnlyShadows](onlyshadows.md)
- [kCGWindowImageShouldBeOpaque](shouldbeopaque.md)

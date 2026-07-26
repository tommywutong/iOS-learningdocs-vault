---
title: kCIApplyOptionColorSpace
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/kciapplyoptioncolorspace
source_url: 'https://developer.apple.com/documentation/coreimage/kciapplyoptioncolorspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/kciapplyoptioncolorspace.json'
content_hash: 'sha256:887a7c4a5e309f6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# kCIApplyOptionColorSpace

<sub>Global Variable</sub>

The color space of the produced image.

<sub>macOS</sub>

```swift
let kCIApplyOptionColorSpace: String
```

## Discussion

The associated value must be an RGB [CGColorSpace](../coregraphics/cgcolorspace.md) object. If not specified, the output of the kernel is in the working color space of the Core Image context used to render the image.

## See Also

### Constants

- [kCIApplyOptionExtent](kciapplyoptionextent.md) — The extent of the image.
- [kCIApplyOptionDefinition](kciapplyoptiondefinition.md) — The domain of definition (DOD) of the produced image.
- [kCIApplyOptionUserInfo](kciapplyoptionuserinfo.md) — Information needed by a callback. The associated value is an object that Core Image will pass to any callbacks invoked for that filter.

---
title: kCIApplyOptionExtent
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/kciapplyoptionextent
source_url: 'https://developer.apple.com/documentation/coreimage/kciapplyoptionextent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/kciapplyoptionextent.json'
content_hash: 'sha256:7f4521c30c4daef0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# kCIApplyOptionExtent

<sub>Global Variable</sub>

The extent of the image.

<sub>macOS</sub>

```swift
let kCIApplyOptionExtent: String
```

## Discussion

The size of the produced image. The associated value is a four-element array ([NSArray](../foundation/nsarray.md)) that specifies the x-value of the rectangle origin, the y-value of the rectangle origin, and the width and height.

## See Also

### Constants

- [kCIApplyOptionDefinition](kciapplyoptiondefinition.md) — The domain of definition (DOD) of the produced image.
- [kCIApplyOptionUserInfo](kciapplyoptionuserinfo.md) — Information needed by a callback. The associated value is an object that Core Image will pass to any callbacks invoked for that filter.
- [kCIApplyOptionColorSpace](kciapplyoptioncolorspace.md) — The color space of the produced image.

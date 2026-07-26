---
title: kCIApplyOptionDefinition
framework: Core Image
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/kciapplyoptiondefinition
source_url: 'https://developer.apple.com/documentation/coreimage/kciapplyoptiondefinition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/kciapplyoptiondefinition.json'
content_hash: 'sha256:3676aaea02cd3cbe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# kCIApplyOptionDefinition

<sub>Global Variable</sub>

The domain of definition (DOD) of the produced image.

<sub>macOS</sub>

```swift
let kCIApplyOptionDefinition: String
```

## Discussion

The associated value is either a Core Image filter shape or a four-element array ([NSArray](../foundation/nsarray.md)) that specifies a rectangle.

## See Also

### Constants

- [kCIApplyOptionExtent](kciapplyoptionextent.md) — The extent of the image.
- [kCIApplyOptionUserInfo](kciapplyoptionuserinfo.md) — Information needed by a callback. The associated value is an object that Core Image will pass to any callbacks invoked for that filter.
- [kCIApplyOptionColorSpace](kciapplyoptioncolorspace.md) — The color space of the produced image.

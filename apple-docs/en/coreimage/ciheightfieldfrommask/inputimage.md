---
title: inputImage
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciheightfieldfrommask/inputimage
source_url: 'https://developer.apple.com/documentation/coreimage/ciheightfieldfrommask/inputimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciheightfieldfrommask/inputimage.json'
content_hash: 'sha256:87add39744749483'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIHeightFieldFromMask](../ciheightfieldfrommask.md)

# inputImage

<sub>Instance Property</sub>

The image to use as an input image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var inputImage: CIImage? { get set }
```

## Discussion

The white values of the input image define those pixels that are inside the height field while the black values define those pixels that are outside. The field varies smoothly and continuously inside the mask, reaching the value 0 at the edge of the mask.

## See Also

### Instance Properties

- [radius](radius.md) — The length of the height-field transition.

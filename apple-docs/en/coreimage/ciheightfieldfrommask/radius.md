---
title: radius
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciheightfieldfrommask/radius
source_url: 'https://developer.apple.com/documentation/coreimage/ciheightfieldfrommask/radius'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciheightfieldfrommask/radius.json'
content_hash: 'sha256:ca68c588db1832c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIHeightFieldFromMask](../ciheightfieldfrommask.md)

# radius

<sub>Instance Property</sub>

The length of the height-field transition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var radius: Float { get set }
```

## Discussion

Larger values make the transition smoother and more pronounced. Smaller values make the transition approximate a fillet radius.

## See Also

### Instance Properties

- [inputImage](inputimage.md) — The image to use as an input image.

---
title: extent
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimageaccumulator/extent
source_url: 'https://developer.apple.com/documentation/coreimage/ciimageaccumulator/extent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimageaccumulator/extent.json'
content_hash: 'sha256:0f24303318c615de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImageAccumulator](../ciimageaccumulator.md)

# extent

<sub>Instance Property</sub>

The extent of the image associated with the image accumulator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var extent: CGRect { get }
```

## Discussion

Extent is a rectangle that specifies the size of the image associated with the image accumulator. This rectangle is the size of the complete region of the working coordinate space, and is a fixed area. It specifies the x-value of the rectangle origin, the y-value of the rectangle origin, and the width and height.

## See Also

### Obtaining Data From an Image Accumulator

- [format](format.md) — The pixel format of the image accumulator.
- [- image](<image().md>) — Returns the current contents of the image accumulator.

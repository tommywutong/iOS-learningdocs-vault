---
title: faceAngle
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifacefeature/faceangle-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/cifacefeature/faceangle-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifacefeature/faceangle-swift.property.json'
content_hash: 'sha256:e0e434a70e147779'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFaceFeature](../cifacefeature.md)

# faceAngle

<sub>Instance Property</sub>

The rotation of the face.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var faceAngle: Float { get }
```

## Discussion

Rotation is measured counterclockwise in degrees, with zero indicating that a line drawn between the eyes is horizontal relative to the image orientation.

## See Also

### Locating Faces

- [bounds](bounds-swift.property.md) — A rectangle indicating the position and extent of the face feature in image coordinates.
- [hasFaceAngle](hasfaceangle-swift.property.md) — A Boolean value that indicates whether information about face rotation is available.

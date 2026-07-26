---
title: leftEyePosition
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifacefeature/lefteyeposition-swift.property
source_url: 'https://developer.apple.com/documentation/coreimage/cifacefeature/lefteyeposition-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifacefeature/lefteyeposition-swift.property.json'
content_hash: 'sha256:31ce6a3400bfa80f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFaceFeature](../cifacefeature.md)

# leftEyePosition

<sub>Instance Property</sub>

The image coordinate of the center of the left eye.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var leftEyePosition: CGPoint { get }
```

## Discussion

> [!note] Note
> The left eye is on the left side of the face from the observer’s perspective. It is not the left eye from the subject’s perspective.

## See Also

### Identifying Facial Features

- [hasLeftEyePosition](haslefteyeposition-swift.property.md) — A Boolean value that indicates whether the detector found the face’s left eye.
- [hasRightEyePosition](hasrighteyeposition-swift.property.md) — A Boolean value that indicates whether the detector found the face’s right eye.
- [hasMouthPosition](hasmouthposition-swift.property.md) — A Boolean value that indicates whether the detector found the face’s mouth.
- [rightEyePosition](righteyeposition-swift.property.md) — The image coordinate of the center of the right eye.
- [mouthPosition](mouthposition-swift.property.md) — The image coordinate of the center of the mouth.
- [hasSmile](hassmile-swift.property.md) — A Boolean value that indicates whether a smile is detected in the face.
- [leftEyeClosed](lefteyeclosed-swift.property.md) — A Boolean value that indicates whether a closed left eye is detected in the face.
- [rightEyeClosed](righteyeclosed-swift.property.md) — A Boolean value that indicates whether a closed right eye is detected in the face.

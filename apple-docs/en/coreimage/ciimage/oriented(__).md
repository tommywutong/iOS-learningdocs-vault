---
title: 'oriented(_:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/oriented(_:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/oriented(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/oriented%28_%3A%29.json'
content_hash: 'sha256:8ec4731e397b9152'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# oriented(_:)

<sub>Instance Method</sub>

Transforms the original image by a given orientation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func oriented(_ orientation: CGImagePropertyOrientation) -> CIImage
```

## Discussion

Returns a new image representing the original image transformed for the given [CGImagePropertyOrientation](../../imageio/cgimagepropertyorientation.md).

## See Also

### Working with Orientation

- [- imageTransformForCGOrientation:](<orientationtransform(for_).md>) — The affine transform for changing the image to the given orientation.

---
title: 'orientationTransform(for:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/orientationtransform(for:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/orientationtransform(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/orientationtransform%28for%3A%29.json'
content_hash: 'sha256:158b74a7d7db5044'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# orientationTransform(for:)

<sub>Instance Method</sub>

The affine transform for changing the image to the given orientation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func orientationTransform(for orientation: CGImagePropertyOrientation) -> CGAffineTransform
```

## Discussion

Returns a [CGAffineTransform](../../corefoundation/cgaffinetransform.md) for the [CGImagePropertyOrientation](../../imageio/cgimagepropertyorientation.md) value to apply to the image.

## See Also

### Working with Orientation

- [- imageByApplyingCGOrientation:](<oriented(__).md>) — Transforms the original image by a given orientation.

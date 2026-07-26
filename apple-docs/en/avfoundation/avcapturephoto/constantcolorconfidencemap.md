---
title: constantColorConfidenceMap
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/constantcolorconfidencemap
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/constantcolorconfidencemap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/constantcolorconfidencemap.json'
content_hash: 'sha256:266a508a386a4435'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# constantColorConfidenceMap

<sub>Instance Property</sub>

A pixel buffer where each pixel value indicates how fully the system achieves the constant color effect in the corresponding region of the photo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var constantColorConfidenceMap: CVPixelBuffer? { get }
```

## Discussion

A value of `255` means full confidence and `0` means zero confidence.

This property provides a valid value only for constant color photos. The value is `nil` in all other cases.

## See Also

### Enabling constant color

- [constantColorCenterWeightedMeanConfidenceLevel](constantcolorcenterweightedmeanconfidencelevel.md) — A score that summarizes the overall confidence level of a constant color photo.
- [constantColorFallbackPhoto](isconstantcolorfallbackphoto.md) — A Boolean value that Indicates whether this photo is a fallback photo for a constant color capture.

---
title: constantColorCenterWeightedMeanConfidenceLevel
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/constantcolorcenterweightedmeanconfidencelevel
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/constantcolorcenterweightedmeanconfidencelevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/constantcolorcenterweightedmeanconfidencelevel.json'
content_hash: 'sha256:a7a734e11d2b90ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# constantColorCenterWeightedMeanConfidenceLevel

<sub>Instance Property</sub>

A score that summarizes the overall confidence level of a constant color photo.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var constantColorCenterWeightedMeanConfidenceLevel: Float { get }
```

## Discussion

A value of `1.0` means full confidence and `0.0` means zero confidence. The default is `0.0.`

In most use cases, such as document scanning, the system considers the central region of the photo more important than its edges. The system weights the confidence level of the central pixels more heavily than pixels on the edges of the photo.

Use [constantColorConfidenceMap](constantcolorconfidencemap.md) for more use case specific analyses of the confidence level.

## See Also

### Enabling constant color

- [constantColorConfidenceMap](constantcolorconfidencemap.md) — A pixel buffer where each pixel value indicates how fully the system achieves the constant color effect in the corresponding region of the photo.
- [constantColorFallbackPhoto](isconstantcolorfallbackphoto.md) — A Boolean value that Indicates whether this photo is a fallback photo for a constant color capture.

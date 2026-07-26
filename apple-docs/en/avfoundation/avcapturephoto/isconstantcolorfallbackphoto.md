---
title: isConstantColorFallbackPhoto
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/isconstantcolorfallbackphoto
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/isconstantcolorfallbackphoto'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/isconstantcolorfallbackphoto.json'
content_hash: 'sha256:034aed608696e0ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# isConstantColorFallbackPhoto

<sub>Instance Property</sub>

A Boolean value that Indicates whether this photo is a fallback photo for a constant color capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isConstantColorFallbackPhoto: Bool { get }
```

## See Also

### Enabling constant color

- [constantColorCenterWeightedMeanConfidenceLevel](constantcolorcenterweightedmeanconfidencelevel.md) — A score that summarizes the overall confidence level of a constant color photo.
- [constantColorConfidenceMap](constantcolorconfidencemap.md) — A pixel buffer where each pixel value indicates how fully the system achieves the constant color effect in the corresponding region of the photo.

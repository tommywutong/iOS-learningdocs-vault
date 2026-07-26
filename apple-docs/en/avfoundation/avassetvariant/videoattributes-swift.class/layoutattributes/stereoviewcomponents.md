---
title: stereoViewComponents
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetvariant/videoattributes-swift.class/layoutattributes/stereoviewcomponents
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetvariant/videoattributes-swift.class/layoutattributes/stereoviewcomponents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetvariant/videoattributes-swift.class/layoutattributes/stereoviewcomponents.json'
content_hash: 'sha256:3c667c782202e4e6'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVAssetVariant](../../../avassetvariant.md) · [VideoAttributes](../../videoattributes-swift.class.md) · [LayoutAttributes](../layoutattributes.md)

# stereoViewComponents

<sub>Instance Property</sub>

Attributes that describe the video’s stereo components.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var stereoViewComponents: CMStereoViewComponents { get }
```

## Discussion

In the case of 3D or stereoscopic content, the value contains [leftEye](../../../../coremedia/cmstereoviewcomponents/lefteye.md) and [rightEye](../../../../coremedia/cmstereoviewcomponents/righteye.md) components. In the case of monoscopic content, this value is [kCMStereoView_None](../../../../coremedia/cmstereoviewcomponents/kcmstereoview_none.md).

## See Also

### Accessing attributes

- [projectionType](projectiontype.md) — Describes the video projection.

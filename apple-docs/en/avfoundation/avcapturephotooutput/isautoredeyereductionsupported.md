---
title: isAutoRedEyeReductionSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/isautoredeyereductionsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isautoredeyereductionsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isautoredeyereductionsupported.json'
content_hash: 'sha256:3091684c932f5b75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isAutoRedEyeReductionSupported

<sub>Instance Property</sub>

A Boolean value indicating whether the capture output supports automatic red-eye reduction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isAutoRedEyeReductionSupported: Bool { get }
```

## Discussion

In iOS 12 and later, AVFoundation applies a red-eye reduction effect only when needed. It won’t apply red-eye reduction in the following situations:

- When you force a flash capture in good light
- When only one eye is visible
- When doing a bracketed capture
- When taking a picture with depth on the dual camera

When taking RAW + processed (JPEG or HEIC) still-photo capture with auto red-eye reduction enabled, AVFoundation applies correction to only the processed photo, _not_ the RAW photo.

## See Also

### Determining available settings

- [contentAwareDistortionCorrectionSupported](iscontentawaredistortioncorrectionsupported.md) — A Boolean value that indicates whether the session’s current configuration supports content-aware distortion correction.
- [contentAwareDistortionCorrectionEnabled](iscontentawaredistortioncorrectionenabled.md) — A Boolean value that indicates whether the photo render pipeline can perform content-aware distortion correction.
- [lensStabilizationDuringBracketedCaptureSupported](islensstabilizationduringbracketedcapturesupported.md) — A Boolean value indicating whether the capture output currently supports lens stabilization during bracketed image capture.
- [maxBracketedCapturePhotoCount](maxbracketedcapturephotocount.md) — The maximum number of images that the photo capture output can support in a single bracketed capture.
- [supportedFlashModes](supportedflashmodes-1n6nm.md) — A Swift array of flash settings this capture output currently supports.

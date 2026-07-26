---
title: isContentAwareDistortionCorrectionSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.1+, iPadOS 14.1+, Mac Catalyst 14.1+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/iscontentawaredistortioncorrectionsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/iscontentawaredistortioncorrectionsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/iscontentawaredistortioncorrectionsupported.json'
content_hash: 'sha256:ec0ed5c32bbbeb65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isContentAwareDistortionCorrectionSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the session’s current configuration supports content-aware distortion correction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isContentAwareDistortionCorrectionSupported: Bool { get }
```

## Discussion

Optical design and geometric distortion correction use a rectilinear model that preserves lines but not area, angles, or distance. The wider the field of view of a lens, the greater the areal distortion along the edges of images. Content-aware distortion correction intelligently adjusts its behavior to correct distortions based on the photo’s content. For example, the algorithm may not apply correction to faces in the center of a photo, but may apply it to faces near the photo’s edges.

Switching cameras or formats, or enabling depth data delivery, may result in a change to this property value. When the property changes from [true](../../swift/true.md) to [false](../../swift/false.md), [contentAwareDistortionCorrectionEnabled](iscontentawaredistortioncorrectionenabled.md) also reverts to [false](../../swift/false.md).

This property is key-value observable.

## See Also

### Determining available settings

- [contentAwareDistortionCorrectionEnabled](iscontentawaredistortioncorrectionenabled.md) — A Boolean value that indicates whether the photo render pipeline can perform content-aware distortion correction.
- [lensStabilizationDuringBracketedCaptureSupported](islensstabilizationduringbracketedcapturesupported.md) — A Boolean value indicating whether the capture output currently supports lens stabilization during bracketed image capture.
- [maxBracketedCapturePhotoCount](maxbracketedcapturephotocount.md) — The maximum number of images that the photo capture output can support in a single bracketed capture.
- [supportedFlashModes](supportedflashmodes-1n6nm.md) — A Swift array of flash settings this capture output currently supports.
- [autoRedEyeReductionSupported](isautoredeyereductionsupported.md) — A Boolean value indicating whether the capture output supports automatic red-eye reduction.

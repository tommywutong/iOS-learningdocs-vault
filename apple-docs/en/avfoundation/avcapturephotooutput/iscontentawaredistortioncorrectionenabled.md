---
title: isContentAwareDistortionCorrectionEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.1+, iPadOS 14.1+, Mac Catalyst 14.1+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/iscontentawaredistortioncorrectionenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/iscontentawaredistortioncorrectionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/iscontentawaredistortioncorrectionenabled.json'
content_hash: 'sha256:961087f2ce8bdd1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isContentAwareDistortionCorrectionEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the photo render pipeline can perform content-aware distortion correction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isContentAwareDistortionCorrectionEnabled: Bool { get set }
```

## Discussion

You can set this value to true only if [contentAwareDistortionCorrectionSupported](iscontentawaredistortioncorrectionsupported.md) returns true.

Applying distortion correction to preserve natural-looking content may result in a small change in the field of view compared to what you see in [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md). The amount lost or gained is content specific and varies from photo to photo.

Enabling this property requires a lengthy reconfiguration of the capture render pipeline, so set this property to [true](../../swift/true.md) before calling [- startRunning](<../avcapturesession/startrunning().md>) on the capture session.

## See Also

### Determining available settings

- [contentAwareDistortionCorrectionSupported](iscontentawaredistortioncorrectionsupported.md) — A Boolean value that indicates whether the session’s current configuration supports content-aware distortion correction.
- [lensStabilizationDuringBracketedCaptureSupported](islensstabilizationduringbracketedcapturesupported.md) — A Boolean value indicating whether the capture output currently supports lens stabilization during bracketed image capture.
- [maxBracketedCapturePhotoCount](maxbracketedcapturephotocount.md) — The maximum number of images that the photo capture output can support in a single bracketed capture.
- [supportedFlashModes](supportedflashmodes-1n6nm.md) — A Swift array of flash settings this capture output currently supports.
- [autoRedEyeReductionSupported](isautoredeyereductionsupported.md) — A Boolean value indicating whether the capture output supports automatic red-eye reduction.

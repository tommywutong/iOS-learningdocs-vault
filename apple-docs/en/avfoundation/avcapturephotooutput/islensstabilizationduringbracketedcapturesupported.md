---
title: isLensStabilizationDuringBracketedCaptureSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/islensstabilizationduringbracketedcapturesupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/islensstabilizationduringbracketedcapturesupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/islensstabilizationduringbracketedcapturesupported.json'
content_hash: 'sha256:6e9344ff7f48ab92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isLensStabilizationDuringBracketedCaptureSupported

<sub>Instance Property</sub>

A Boolean value indicating whether the capture output currently supports lens stabilization during bracketed image capture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isLensStabilizationDuringBracketedCaptureSupported: Bool { get }
```

## Discussion

To make use of optical image stabilization across the entire duration of a bracketed capture, set the [lensStabilizationEnabled](../avcapturephotobracketsettings/islensstabilizationenabled.md) property of your bracketed photo settings object.

> [!note] Note
> This property’s value can change if the [sessionPreset](../avcapturesession/sessionpreset.md) property of the current capture session or the [activeFormat](../avcapturedevice/activeformat.md) property of the underlying capture device changes.

This property supports key-value observing.

## See Also

### Determining available settings

- [contentAwareDistortionCorrectionSupported](iscontentawaredistortioncorrectionsupported.md) — A Boolean value that indicates whether the session’s current configuration supports content-aware distortion correction.
- [contentAwareDistortionCorrectionEnabled](iscontentawaredistortioncorrectionenabled.md) — A Boolean value that indicates whether the photo render pipeline can perform content-aware distortion correction.
- [maxBracketedCapturePhotoCount](maxbracketedcapturephotocount.md) — The maximum number of images that the photo capture output can support in a single bracketed capture.
- [supportedFlashModes](supportedflashmodes-1n6nm.md) — A Swift array of flash settings this capture output currently supports.
- [autoRedEyeReductionSupported](isautoredeyereductionsupported.md) — A Boolean value indicating whether the capture output supports automatic red-eye reduction.

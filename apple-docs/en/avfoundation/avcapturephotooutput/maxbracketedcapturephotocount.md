---
title: maxBracketedCapturePhotoCount
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/maxbracketedcapturephotocount
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/maxbracketedcapturephotocount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/maxbracketedcapturephotocount.json'
content_hash: 'sha256:d8ec01e030cd59c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# maxBracketedCapturePhotoCount

<sub>Instance Property</sub>

The maximum number of images that the photo capture output can support in a single bracketed capture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var maxBracketedCapturePhotoCount: Int { get }
```

## Discussion

To perform a bracketed capture of multiple images with varied capture settings, create a [AVCapturePhotoBracketSettings](../avcapturephotobracketsettings.md) instance containing the combination of settings and bracketed variations you want. The maximum number of photos per capture depends on the size and format of images to be captured.

> [!note] Note
> This property’s value can change if the [sessionPreset](../avcapturesession/sessionpreset.md) property of the current capture session or the [activeFormat](../avcapturedevice/activeformat.md) property of the underlying capture device changes.
>
> Not all devices and capture formats support bracketed capture. If the current device or active format does not support bracketed capture, this property’s value is zero.

This property supports key-value observing.

## See Also

### Determining available settings

- [contentAwareDistortionCorrectionSupported](iscontentawaredistortioncorrectionsupported.md) — A Boolean value that indicates whether the session’s current configuration supports content-aware distortion correction.
- [contentAwareDistortionCorrectionEnabled](iscontentawaredistortioncorrectionenabled.md) — A Boolean value that indicates whether the photo render pipeline can perform content-aware distortion correction.
- [lensStabilizationDuringBracketedCaptureSupported](islensstabilizationduringbracketedcapturesupported.md) — A Boolean value indicating whether the capture output currently supports lens stabilization during bracketed image capture.
- [supportedFlashModes](supportedflashmodes-1n6nm.md) — A Swift array of flash settings this capture output currently supports.
- [autoRedEyeReductionSupported](isautoredeyereductionsupported.md) — A Boolean value indicating whether the capture output supports automatic red-eye reduction.

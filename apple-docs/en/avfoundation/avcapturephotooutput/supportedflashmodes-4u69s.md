---
title: supportedFlashModes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 13.0+, tvOS 17.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/supportedflashmodes-4u69s
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/supportedflashmodes-4u69s'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/supportedflashmodes-4u69s.json'
content_hash: 'sha256:7c336f2e87727661'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# supportedFlashModes

<sub>Instance Property</sub>

The flash settings this capture output currently supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * supportedFlashModes;
```

## Discussion

To set the flash mode for a capture, set the [flashMode](../avcapturephotosettings/flashmode.md) property of your photo settings object to one of the [FlashMode](../avcapturedevice/flashmode-swift.enum.md) values listed in this array.

This property supports key-value observing.

## See Also

### Determining available settings

- [contentAwareDistortionCorrectionSupported](iscontentawaredistortioncorrectionsupported.md) — A Boolean value that indicates whether the session’s current configuration supports content-aware distortion correction.
- [contentAwareDistortionCorrectionEnabled](iscontentawaredistortioncorrectionenabled.md) — A Boolean value that indicates whether the photo render pipeline can perform content-aware distortion correction.
- [lensStabilizationDuringBracketedCaptureSupported](islensstabilizationduringbracketedcapturesupported.md) — A Boolean value indicating whether the capture output currently supports lens stabilization during bracketed image capture.
- [maxBracketedCapturePhotoCount](maxbracketedcapturephotocount.md) — The maximum number of images that the photo capture output can support in a single bracketed capture.
- [autoRedEyeReductionSupported](isautoredeyereductionsupported.md) — A Boolean value indicating whether the capture output supports automatic red-eye reduction.

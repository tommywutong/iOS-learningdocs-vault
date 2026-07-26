---
title: isLensStabilizationDuringBracketedCaptureEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（10.0 起废弃）, iPadOS 9.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturestillimageoutput/islensstabilizationduringbracketedcaptureenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/islensstabilizationduringbracketedcaptureenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput/islensstabilizationduringbracketedcaptureenabled.json'
content_hash: 'sha256:4ac4520f25d541f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureStillImageOutput](../avcapturestillimageoutput.md)

# isLensStabilizationDuringBracketedCaptureEnabled

<sub>Instance Property</sub>

A Boolean value that specifies whether to stabilize the lens across the duration of a bracketed capture.

> [!warning] Deprecated
> Use AVCapturePhotoOutput with AVCapturePhotoBracketSettings instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isLensStabilizationDuringBracketedCaptureEnabled: Bool { get set }
```

## Discussion

Applying lens stabilization to bracketed capture attempts to keep the lens steady for the entire duration of the bracket, resulting in more consistent images across the bracket. When lens stabilization is enabled, bracketed still image captures incur additional latency. Lens stabilization is more effective with longer-exposure captures, and offers limited or no benefit for exposure durations shorter than 1/30 of a second. It is possible that during the bracket, the lens stabilization module may run out of correction range and therefore will not be active for every frame in the bracket. Each emitted sample buffer from the bracket has an attachment of `kCMSampleBufferAttachmentKey_StillImageLensStabilizationInfo` indicating additional information about stabilization applied to the buffer.

This property’s default value is [false](../../swift/false.md). You may set this property’s value to [true](../../swift/true.md) only if the [lensStabilizationDuringBracketedCaptureSupported](islensstabilizationduringbracketedcapturesupported.md) value is [true](../../swift/true.md). Otherwise, setting this property raises an exception ([invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md)). If the [lensStabilizationDuringBracketedCaptureSupported](islensstabilizationduringbracketedcapturesupported.md) property’s value changes to [false](../../swift/false.md), this property’s value also becomes [false](../../swift/false.md).

This property supports key-value observing.

## See Also

### Still image bracketed capture

- [- captureStillImageBracketAsynchronouslyFromConnection:withSettingsArray:completionHandler:](<capturestillimagebracketasynchronously(from_withsettingsarray_completionhandler_).md>) — Captures a still image bracket. _(deprecated)_
- [maxBracketedCaptureStillImageCount](maxbracketedcapturestillimagecount.md) — Specifies the maximum number of still images that may be taken in a single bracket. _(deprecated)_
- [- prepareToCaptureStillImageBracketFromConnection:withSettingsArray:completionHandler:](<preparetocapturestillimagebracket(from_withsettingsarray_completionhandler_).md>) — Allows the receiver to prepare resources in advance of capturing a still image bracket. _(deprecated)_
- [lensStabilizationDuringBracketedCaptureSupported](islensstabilizationduringbracketedcapturesupported.md) — A Boolean value that indicates whether the capture output supports lens stabilization across the duration of a bracketed capture. _(deprecated)_

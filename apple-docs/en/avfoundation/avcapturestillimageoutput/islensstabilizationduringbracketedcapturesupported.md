---
title: isLensStabilizationDuringBracketedCaptureSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（10.0 起废弃）, iPadOS 9.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturestillimageoutput/islensstabilizationduringbracketedcapturesupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/islensstabilizationduringbracketedcapturesupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput/islensstabilizationduringbracketedcapturesupported.json'
content_hash: 'sha256:60bd4bcb9ef6ab62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureStillImageOutput](../avcapturestillimageoutput.md)

# isLensStabilizationDuringBracketedCaptureSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the capture output supports lens stabilization across the duration of a bracketed capture.

> [!warning] Deprecated
> Use AVCapturePhotoOutput lensStabilizationDuringBracketedCaptureSupported instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isLensStabilizationDuringBracketedCaptureSupported: Bool { get }
```

## Discussion

You may set the [lensStabilizationDuringBracketedCaptureEnabled](islensstabilizationduringbracketedcaptureenabled.md) property only if this property’s value is [true](../../swift/true.md). This value may change as the session’s [sessionPreset](../avcapturesession/sessionpreset.md) property or the input device’s [activeFormat](../avcapturedevice/activeformat.md) property changes.

This property supports key-value observing.

## See Also

### Still image bracketed capture

- [- captureStillImageBracketAsynchronouslyFromConnection:withSettingsArray:completionHandler:](<capturestillimagebracketasynchronously(from_withsettingsarray_completionhandler_).md>) — Captures a still image bracket. _(deprecated)_
- [maxBracketedCaptureStillImageCount](maxbracketedcapturestillimagecount.md) — Specifies the maximum number of still images that may be taken in a single bracket. _(deprecated)_
- [- prepareToCaptureStillImageBracketFromConnection:withSettingsArray:completionHandler:](<preparetocapturestillimagebracket(from_withsettingsarray_completionhandler_).md>) — Allows the receiver to prepare resources in advance of capturing a still image bracket. _(deprecated)_
- [lensStabilizationDuringBracketedCaptureEnabled](islensstabilizationduringbracketedcaptureenabled.md) — A Boolean value that specifies whether to stabilize the lens across the duration of a bracketed capture. _(deprecated)_

---
title: maxBracketedCaptureStillImageCount
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturestillimageoutput/maxbracketedcapturestillimagecount
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/maxbracketedcapturestillimagecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput/maxbracketedcapturestillimagecount.json'
content_hash: 'sha256:bd03bd00cdb1ec15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureStillImageOutput](../avcapturestillimageoutput.md)

# maxBracketedCaptureStillImageCount

<sub>Instance Property</sub>

Specifies the maximum number of still images that may be taken in a single bracket.

> [!warning] Deprecated
> Use AVCapturePhotoOutput maxBracketedCapturePhotoCount instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var maxBracketedCaptureStillImageCount: Int { get }
```

## Discussion

AVCaptureStillImageOutput can only satisfy a limited number of image requests in a single bracket without exhausting system resources.

The maximum number of still images that may be taken in a single bracket depends on the size of the images being captured, and consequently may vary with AVCaptureSession -sessionPreset and AVCaptureDevice -activeFormat values.

## See Also

### Related Documentation

- [- captureStillImageAsynchronouslyFromConnection:completionHandler:](<capturestillimageasynchronously(from_completionhandler_).md>) — Initiates a still image capture and returns immediately. _(deprecated)_

### Still image bracketed capture

- [- captureStillImageBracketAsynchronouslyFromConnection:withSettingsArray:completionHandler:](<capturestillimagebracketasynchronously(from_withsettingsarray_completionhandler_).md>) — Captures a still image bracket. _(deprecated)_
- [- prepareToCaptureStillImageBracketFromConnection:withSettingsArray:completionHandler:](<preparetocapturestillimagebracket(from_withsettingsarray_completionhandler_).md>) — Allows the receiver to prepare resources in advance of capturing a still image bracket. _(deprecated)_
- [lensStabilizationDuringBracketedCaptureSupported](islensstabilizationduringbracketedcapturesupported.md) — A Boolean value that indicates whether the capture output supports lens stabilization across the duration of a bracketed capture. _(deprecated)_
- [lensStabilizationDuringBracketedCaptureEnabled](islensstabilizationduringbracketedcaptureenabled.md) — A Boolean value that specifies whether to stabilize the lens across the duration of a bracketed capture. _(deprecated)_

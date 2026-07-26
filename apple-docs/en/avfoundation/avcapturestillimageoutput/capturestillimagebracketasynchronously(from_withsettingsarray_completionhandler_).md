---
title: 'captureStillImageBracketAsynchronously(from:withSettingsArray:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avcapturestillimageoutput/capturestillimagebracketasynchronously(from:withsettingsarray:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/capturestillimagebracketasynchronously(from:withsettingsarray:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput/capturestillimagebracketasynchronously%28from%3Awithsettingsarray%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:5aaeffef42a31d65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureStillImageOutput](../avcapturestillimageoutput.md)

# captureStillImageBracketAsynchronously(from:withSettingsArray:completionHandler:)

<sub>Instance Method</sub>

Captures a still image bracket.

> [!warning] Deprecated
> Use AVCapturePhotoOutput capturePhotoWithSettings:delegate: instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func captureStillImageBracketAsynchronously(from connection: AVCaptureConnection, withSettingsArray settings: [AVCaptureBracketedStillImageSettings], completionHandler handler: @escaping (CMSampleBuffer?, AVCaptureBracketedStillImageSettings?, (any Error)?) -> Void)
```

## Parameters

- `connection` — The connection through which the still image bracket should be captured.

- `settings` — An array of [AVCaptureBracketedStillImageSettings](../avcapturebracketedstillimagesettings.md) objects. All the array items must be of the same [AVCaptureBracketedStillImageSettings](../avcapturebracketedstillimagesettings.md) subclass, or an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) exception is thrown.

- `handler` — A user provided block that will be called asynchronously as each still image in the bracket is captured. The block has three parameters: - **sampleBuffer** — If the capture request is successful,  contains a valid CMSampleBuffer. - **stillImageSettings** — Contains the [AVCaptureBracketedStillImageSettings](../avcapturebracketedstillimagesettings.md) object corresponding to this still image. - **error** — If the bracketed capture fails, `sampleBuffer` is `NULL` and error is non-`nil`. If the count of the `settings` parameter exceeds [maxBracketedCaptureStillImageCount](maxbracketedcapturestillimagecount.md), then `AVErrorMaximumStillImageCaptureRequestsExceeded` is returned. You should not assume that the completion handler will be called on a specific thread.

## Discussion

If you have not invoked [- prepareToCaptureStillImageBracketFromConnection:withSettingsArray:completionHandler:](<preparetocapturestillimagebracket(from_withsettingsarray_completionhandler_).md>) for this still image bracket request, the bracket may not be taken immediately, as the receiver may internally need to prepare resources.

## See Also

### Related Documentation

- [- captureStillImageAsynchronouslyFromConnection:completionHandler:](<capturestillimageasynchronously(from_completionhandler_).md>) — Initiates a still image capture and returns immediately. _(deprecated)_

### Still image bracketed capture

- [maxBracketedCaptureStillImageCount](maxbracketedcapturestillimagecount.md) — Specifies the maximum number of still images that may be taken in a single bracket. _(deprecated)_
- [- prepareToCaptureStillImageBracketFromConnection:withSettingsArray:completionHandler:](<preparetocapturestillimagebracket(from_withsettingsarray_completionhandler_).md>) — Allows the receiver to prepare resources in advance of capturing a still image bracket. _(deprecated)_
- [lensStabilizationDuringBracketedCaptureSupported](islensstabilizationduringbracketedcapturesupported.md) — A Boolean value that indicates whether the capture output supports lens stabilization across the duration of a bracketed capture. _(deprecated)_
- [lensStabilizationDuringBracketedCaptureEnabled](islensstabilizationduringbracketedcaptureenabled.md) — A Boolean value that specifies whether to stabilize the lens across the duration of a bracketed capture. _(deprecated)_

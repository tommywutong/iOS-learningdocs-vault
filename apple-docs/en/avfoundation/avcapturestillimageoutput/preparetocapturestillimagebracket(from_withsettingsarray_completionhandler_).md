---
title: 'prepareToCaptureStillImageBracket(from:withSettingsArray:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avcapturestillimageoutput/preparetocapturestillimagebracket(from:withsettingsarray:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/preparetocapturestillimagebracket(from:withsettingsarray:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput/preparetocapturestillimagebracket%28from%3Awithsettingsarray%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:c57a5a397957337d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureStillImageOutput](../avcapturestillimageoutput.md)

# prepareToCaptureStillImageBracket(from:withSettingsArray:completionHandler:)

<sub>Instance Method</sub>

Allows the receiver to prepare resources in advance of capturing a still image bracket.

> [!warning] Deprecated
> Use AVCapturePhotoOutput setPreparedPhotoSettingsArray:completionHandler: instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func prepareToCaptureStillImageBracket(from connection: AVCaptureConnection, withSettingsArray settings: [AVCaptureBracketedStillImageSettings], completionHandler handler: @escaping (Bool, (any Error)?) -> Void)
```

## Parameters

- `connection` — The connection through which the still image bracket should be captured.

- `settings` — An array of [AVCaptureBracketedStillImageSettings](../avcapturebracketedstillimagesettings.md) objects. All the array items must be of the same [AVCaptureBracketedStillImageSettings](../avcapturebracketedstillimagesettings.md) subclass, or an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) exception is thrown.

- `handler` — A user provided block that will be called asynchronously once resources have successfully been allocated for the specified bracketed capture operation. The block has two parameters: - **prepared** — If sufficient resources could not be allocated, this parameter is [false](../../swift/false.md), and the `error` parameter contains a non-`nil` error value. - **error** — The value is non-`nil` if an error is encountered. If the count of the `settings` parameter exceeds [maxBracketedCaptureStillImageCount](maxbracketedcapturestillimagecount.md), then `AVErrorMaximumStillImageCaptureRequestsExceeded` is returned. You should not assume that the completion handler will be called on a specific thread.

## Discussion

Before taking a still image bracket, additional resources may need to be allocated. By calling this method first, you are able to know when the receiver is ready to capture the bracket with the specified settings array.

## See Also

### Related Documentation

- [- captureStillImageAsynchronouslyFromConnection:completionHandler:](<capturestillimageasynchronously(from_completionhandler_).md>) — Initiates a still image capture and returns immediately. _(deprecated)_

### Still image bracketed capture

- [- captureStillImageBracketAsynchronouslyFromConnection:withSettingsArray:completionHandler:](<capturestillimagebracketasynchronously(from_withsettingsarray_completionhandler_).md>) — Captures a still image bracket. _(deprecated)_
- [maxBracketedCaptureStillImageCount](maxbracketedcapturestillimagecount.md) — Specifies the maximum number of still images that may be taken in a single bracket. _(deprecated)_
- [lensStabilizationDuringBracketedCaptureSupported](islensstabilizationduringbracketedcapturesupported.md) — A Boolean value that indicates whether the capture output supports lens stabilization across the duration of a bracketed capture. _(deprecated)_
- [lensStabilizationDuringBracketedCaptureEnabled](islensstabilizationduringbracketedcaptureenabled.md) — A Boolean value that specifies whether to stabilize the lens across the duration of a bracketed capture. _(deprecated)_

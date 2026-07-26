---
title: 'captureStillImageAsynchronously(from:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avcapturestillimageoutput/capturestillimageasynchronously(from:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/capturestillimageasynchronously(from:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput/capturestillimageasynchronously%28from%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:4a4ae6be4fe14266'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureStillImageOutput](../avcapturestillimageoutput.md)

# captureStillImageAsynchronously(from:completionHandler:)

<sub>Instance Method</sub>

Initiates a still image capture and returns immediately.

> [!warning] Deprecated
> Use AVCapturePhotoOutput instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func captureStillImageAsynchronously(from connection: AVCaptureConnection, completionHandler handler: @escaping (CMSampleBuffer?, (any Error)?) -> Void)
```

## Parameters

- `connection` — The connection from which to capture the image.

- `handler` — A block to invoke after the image has been captured. The block parameters are as follows: - **imageDataSampleBuffer** — The data that was captured. The buffer attachments may contain metadata appropriate to the image data format. For example, a buffer containing JPEG data may carry a [kCGImagePropertyExifDictionary](../../imageio/kcgimagepropertyexifdictionary.md) as an attachment. See ImageIO/CGImageProperties.h for a list of keys and value types. - **error** — If the request could not be completed, an `NSError` object that describes the problem; otherwise `nil`.

## Discussion

This method returns immediately after it is invoked, later calling the provided completion handler block when image data is ready. If the request could not be completed, the error parameter will contain an `NSError` object describing the failure.

You should not assume that the completion handler will be called on a specific thread.

## See Also

### Capturing an image

- [capturingStillImage](iscapturingstillimage.md) — Indicates whether a still image is being captured. _(deprecated)_

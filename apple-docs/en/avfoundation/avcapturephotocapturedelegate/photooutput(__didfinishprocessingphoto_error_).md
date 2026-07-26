---
title: 'photoOutput(_:didFinishProcessingPhoto:error:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotocapturedelegate/photooutput%28_%3Adidfinishprocessingphoto%3Aerror%3A%29.json'
content_hash: 'sha256:8c6f046144653999'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoCaptureDelegate](../avcapturephotocapturedelegate.md)

# photoOutput(_:didFinishProcessingPhoto:error:)

<sub>Instance Method</sub>

Provides the delegate with the captured image and associated metadata resulting from a photo capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, didFinishProcessingPhoto photo: AVCapturePhoto, error: (any Error)?)
```

## Parameters

- `output` — The photo output performing the capture.

- `photo` — An object containing the captured image pixel buffer, along with any metadata and attachments captured along with the photo (such as a preview image or depth map). This parameter is always non-`nil`: if an error prevented successful capture, this object still contains metadata for the intended capture.

- `error` — If the capture process could not proceed successfully, an error object describing the failure; otherwise, `nil`.

## Discussion

Use this method to receive the results of photo capture regardless of format.

> [!important] Important
> Implementing this method is recommended for all still image (as opposed to Live Photo) capture workflows, and required if you request depth data delivery. The photo output validates this requirement when you call its [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method; if your delegate does not implement the correct methods, the photo output raises an exception.

The photo output calls this method once for each primary image to be delivered in a capture request. If you request capture in both RAW and processed formats, this method fires once for each format. If you request a bracketed capture with multiple exposures, this method fires once for each exposure.

## See Also

### Receiving capture results

- [- captureOutput:didFinishRecordingLivePhotoMovieForEventualFileAtURL:resolvedSettings:](<photooutput(__didfinishrecordinglivephotomovieforeventualfileat_resolvedsettings_).md>) — Notifies the delegate that the movie content of a Live Photo has finished recording.
- [- captureOutput:didFinishProcessingLivePhotoToMovieFileAtURL:duration:photoDisplayTime:resolvedSettings:error:](<photooutput(__didfinishprocessinglivephototomoviefileat_duration_photodisplaytime_resolvedsettings_error_).md>) — Provides the delegate the movie file URL resulting from a Live Photo capture.
- [- captureOutput:didFinishCapturingDeferredPhotoProxy:error:](<photooutput(__didfinishcapturingdeferredphotoproxy_error_).md>) — Tells the delegate when the system finishes capturing the photo proxy.
- [- captureOutput:didFinishProcessingPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<photooutput(__didfinishprocessingphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) — Provides the delegate a captured image in a processed format (such as JPEG). _(deprecated)_
- [- captureOutput:didFinishProcessingRawPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<photooutput(__didfinishprocessingrawphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) — Provides the delegate a captured image in RAW format. _(deprecated)_

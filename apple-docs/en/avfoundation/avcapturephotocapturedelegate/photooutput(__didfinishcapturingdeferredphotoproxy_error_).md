---
title: 'photoOutput(_:didFinishCapturingDeferredPhotoProxy:error:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishcapturingdeferredphotoproxy:error:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishcapturingdeferredphotoproxy:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotocapturedelegate/photooutput%28_%3Adidfinishcapturingdeferredphotoproxy%3Aerror%3A%29.json'
content_hash: 'sha256:60e1161d2ed796a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoCaptureDelegate](../avcapturephotocapturedelegate.md)

# photoOutput(_:didFinishCapturingDeferredPhotoProxy:error:)

<sub>Instance Method</sub>

Tells the delegate when the system finishes capturing the photo proxy.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, didFinishCapturingDeferredPhotoProxy deferredPhotoProxy: AVCaptureDeferredPhotoProxy?, error: (any Error)?)
```

## Parameters

- `output` — The output instance.

- `deferredPhotoProxy` — A [AVCaptureDeferredPhotoProxy](../avcapturedeferredphotoproxy.md) instance that contains a proxy [CVPixelBuffer](../../corevideo/cvpixelbuffer-q2e.md) as a placeholder for the final image.

- `error` — If the system couldn’t create the photo proxy, or any of the underlying intermediate files, an error object that describes the failure.

## Discussion

You can use the output’s [- fileDataRepresentation](<../avcapturephoto/filedatarepresentation().md>) with [PHAssetCreationRequest](../../photos/phassetcreationrequest.md) to eventually produce the final, processed photo into the user’s Photo Library. Add the in-memory proxy file data representation to the photo library as quickly as possible after this call to ensure that the photo library can begin background processing. It’s also important so that the intermediates aren’t removed by a periodic clean-up job looking for abandoned intermediates produced by using the deferred photo processing APIs.

Your delegate implementation must adopt this method to opt into deferred photo processing, otherwise calling [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) throws an exception.

## See Also

### Receiving capture results

- [- captureOutput:didFinishProcessingPhoto:error:](<photooutput(__didfinishprocessingphoto_error_).md>) — Provides the delegate with the captured image and associated metadata resulting from a photo capture.
- [- captureOutput:didFinishRecordingLivePhotoMovieForEventualFileAtURL:resolvedSettings:](<photooutput(__didfinishrecordinglivephotomovieforeventualfileat_resolvedsettings_).md>) — Notifies the delegate that the movie content of a Live Photo has finished recording.
- [- captureOutput:didFinishProcessingLivePhotoToMovieFileAtURL:duration:photoDisplayTime:resolvedSettings:error:](<photooutput(__didfinishprocessinglivephototomoviefileat_duration_photodisplaytime_resolvedsettings_error_).md>) — Provides the delegate the movie file URL resulting from a Live Photo capture.
- [- captureOutput:didFinishProcessingPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<photooutput(__didfinishprocessingphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) — Provides the delegate a captured image in a processed format (such as JPEG). _(deprecated)_
- [- captureOutput:didFinishProcessingRawPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<photooutput(__didfinishprocessingrawphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) — Provides the delegate a captured image in RAW format. _(deprecated)_

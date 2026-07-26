---
title: 'photoOutput(_:didFinishProcessingLivePhotoToMovieFileAt:duration:photoDisplayTime:resolvedSettings:error:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishprocessinglivephototomoviefileat:duration:photodisplaytime:resolvedsettings:error:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishprocessinglivephototomoviefileat:duration:photodisplaytime:resolvedsettings:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotocapturedelegate/photooutput%28_%3Adidfinishprocessinglivephototomoviefileat%3Aduration%3Aphotodisplaytime%3Aresolvedsettings%3Aerror%3A%29.json'
content_hash: 'sha256:44c486f858e20507'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoCaptureDelegate](../avcapturephotocapturedelegate.md)

# photoOutput(_:didFinishProcessingLivePhotoToMovieFileAt:duration:photoDisplayTime:resolvedSettings:error:)

<sub>Instance Method</sub>

Provides the delegate the movie file URL resulting from a Live Photo capture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, didFinishProcessingLivePhotoToMovieFileAt outputFileURL: URL, duration: CMTime, photoDisplayTime: CMTime, resolvedSettings: AVCaptureResolvedPhotoSettings, error: (any Error)?)
```

## Parameters

- `output` — The photo output performing the capture.

- `outputFileURL` — The file URL at which the movie content of the Live Photo was written.

- `duration` — The duration of the Live Photo movie.

- `photoDisplayTime` — The timestamp within the movie to which the still image part of the Live Photo corresponds.

- `resolvedSettings` — An object describing the settings used for this capture. Match this object’s [uniqueID](../avcapturephotosettings/uniqueid.md) value to the [uniqueID](../avcapturephotosettings/uniqueid.md) property of the photo settings object you initiated capture with to determine which capture request this delegate call corresponds to. You can also use this object to find out which values the photo output has chosen for automatic settings.

- `error` — If the capture process could not proceed successfully, an error object describing the failure; otherwise, `nil`.

## Discussion

Use this method to receive the results of a Live Photo capture. When the photo output calls this method, the movie component of the Live Photo has been written to the location specified by the `outputFileURL` parameter and the Live Photo is ready for consumption. (To receive the still image component of the Live Photo, implement the [- captureOutput:didFinishProcessingPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<photooutput(__didfinishprocessingphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) method.)

> [!tip] Tip
> To add captured Live Photos to the user’s Photos library, use the [PHAssetCreationRequest](../../photos/phassetcreationrequest.md) class. To use Live Photos from the Photos library, use the [PHLivePhoto](../../photos/phlivephoto.md) and [PHLivePhotoView](../../photosui/phlivephotoview.md) classes. To display Live Photo content on the web, use the [LivePhotosKit JS](../../livephotoskitjs.md) framework.

You don’t need to implement this method if you’re not requesting Live Photo capture.

> [!important] Important
> You must implement this method if you request Live Photo capture (by setting the [livePhotoMovieFileURL](../avcapturephotosettings/livephotomoviefileurl.md) property of your photo settings object). The photo output validates this requirement when you call its [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method; if your delegate does not implement the correct methods, the photo output raises an exception.

The photo output calls this method only once for each Live Photo capture.

## See Also

### Receiving capture results

- [- captureOutput:didFinishProcessingPhoto:error:](<photooutput(__didfinishprocessingphoto_error_).md>) — Provides the delegate with the captured image and associated metadata resulting from a photo capture.
- [- captureOutput:didFinishRecordingLivePhotoMovieForEventualFileAtURL:resolvedSettings:](<photooutput(__didfinishrecordinglivephotomovieforeventualfileat_resolvedsettings_).md>) — Notifies the delegate that the movie content of a Live Photo has finished recording.
- [- captureOutput:didFinishCapturingDeferredPhotoProxy:error:](<photooutput(__didfinishcapturingdeferredphotoproxy_error_).md>) — Tells the delegate when the system finishes capturing the photo proxy.
- [- captureOutput:didFinishProcessingPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<photooutput(__didfinishprocessingphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) — Provides the delegate a captured image in a processed format (such as JPEG). _(deprecated)_
- [- captureOutput:didFinishProcessingRawPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<photooutput(__didfinishprocessingrawphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) — Provides the delegate a captured image in RAW format. _(deprecated)_

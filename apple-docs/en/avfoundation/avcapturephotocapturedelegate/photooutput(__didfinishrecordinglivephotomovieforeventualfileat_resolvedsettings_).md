---
title: 'photoOutput(_:didFinishRecordingLivePhotoMovieForEventualFileAt:resolvedSettings:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishrecordinglivephotomovieforeventualfileat:resolvedsettings:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishrecordinglivephotomovieforeventualfileat:resolvedsettings:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotocapturedelegate/photooutput%28_%3Adidfinishrecordinglivephotomovieforeventualfileat%3Aresolvedsettings%3A%29.json'
content_hash: 'sha256:db2dee6d842b6884'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoCaptureDelegate](../avcapturephotocapturedelegate.md)

# photoOutput(_:didFinishRecordingLivePhotoMovieForEventualFileAt:resolvedSettings:)

<sub>Instance Method</sub>

Notifies the delegate that the movie content of a Live Photo has finished recording.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, didFinishRecordingLivePhotoMovieForEventualFileAt outputFileURL: URL, resolvedSettings: AVCaptureResolvedPhotoSettings)
```

## Parameters

- `output` — The photo output performing the capture.

- `outputFileURL` — The file URL at which the Live Photo movie will be written.

- `resolvedSettings` — An object describing the settings used for this capture. Match this object’s [uniqueID](../avcapturephotosettings/uniqueid.md) value to the [uniqueID](../avcapturephotosettings/uniqueid.md) property of the photo settings object you initiated capture with to determine which capture request this delegate call corresponds to. You can also use this object to find out which values the photo output has chosen for automatic settings.

## Discussion

The photo output calls this method as soon as it has captured all movie data for a Live Photo. However, at this moment, that media content has not yet been processed or written to storage. (To be notified when the complete movie file has finished writing and is ready for consumption, implement the [- captureOutput:didFinishProcessingLivePhotoToMovieFileAtURL:duration:photoDisplayTime:resolvedSettings:error:](<photooutput(__didfinishprocessinglivephototomoviefileat_duration_photodisplaytime_resolvedsettings_error_).md>) method.)

Use this method to determine when it is appropriate to change your displayed UI to indicate that Live Photo movie capture is no longer in progress. For example, the Camera app displays a “LIVE” icon when the user presses the shutter button, then hides that icon when movie capture ends.

The photo output calls this method only once for each Live Photo capture.

## See Also

### Receiving capture results

- [- captureOutput:didFinishProcessingPhoto:error:](<photooutput(__didfinishprocessingphoto_error_).md>) — Provides the delegate with the captured image and associated metadata resulting from a photo capture.
- [- captureOutput:didFinishProcessingLivePhotoToMovieFileAtURL:duration:photoDisplayTime:resolvedSettings:error:](<photooutput(__didfinishprocessinglivephototomoviefileat_duration_photodisplaytime_resolvedsettings_error_).md>) — Provides the delegate the movie file URL resulting from a Live Photo capture.
- [- captureOutput:didFinishCapturingDeferredPhotoProxy:error:](<photooutput(__didfinishcapturingdeferredphotoproxy_error_).md>) — Tells the delegate when the system finishes capturing the photo proxy.
- [- captureOutput:didFinishProcessingPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<photooutput(__didfinishprocessingphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) — Provides the delegate a captured image in a processed format (such as JPEG). _(deprecated)_
- [- captureOutput:didFinishProcessingRawPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<photooutput(__didfinishprocessingrawphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) — Provides the delegate a captured image in RAW format. _(deprecated)_

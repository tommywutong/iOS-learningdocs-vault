---
title: 'photoOutput(_:didFinishProcessingRawPhoto:previewPhoto:resolvedSettings:bracketSettings:error:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+（11.0 起废弃）, iPadOS 10.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishprocessingrawphoto:previewphoto:resolvedsettings:bracketsettings:error:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishprocessingrawphoto:previewphoto:resolvedsettings:bracketsettings:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotocapturedelegate/photooutput%28_%3Adidfinishprocessingrawphoto%3Apreviewphoto%3Aresolvedsettings%3Abracketsettings%3Aerror%3A%29.json'
content_hash: 'sha256:4537edb952d9a798'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoCaptureDelegate](../avcapturephotocapturedelegate.md)

# photoOutput(_:didFinishProcessingRawPhoto:previewPhoto:resolvedSettings:bracketSettings:error:)

<sub>Instance Method</sub>

Provides the delegate a captured image in RAW format.

> [!warning] Deprecated
> In iOS 11 and later, implement the [- captureOutput:didFinishProcessingPhoto:error:](<photooutput(__didfinishprocessingphoto_error_).md>) method instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, didFinishProcessingRawPhoto rawSampleBuffer: CMSampleBuffer?, previewPhoto previewPhotoSampleBuffer: CMSampleBuffer?, resolvedSettings: AVCaptureResolvedPhotoSettings, bracketSettings: AVCaptureBracketedStillImageSettings?, error: (any Error)?)
```

## Parameters

- `output` — The photo output performing the capture.

- `rawSampleBuffer` — A sample buffer containing the captured RAW image. The format of this buffer matches the format you requested for the RAW image (see the [rawPhotoPixelFormatType](../avcapturephotosettings/rawphotopixelformattype.md) property of your photo settings). If an error prevented successful capture, this parameter is `nil`—see the `error` parameter for a description of the failure.

- `previewPhotoSampleBuffer` — If you requested a thumbnail-sized version of the photo (with the [previewPhotoFormat](../avcapturephotosettings/previewphotoformat.md) property of your photo settings object), a sample buffer containing the thumbnail photo in the requested format. If you did not request preview delivery, or if an error prevented capture, this parameter is `nil`.

- `resolvedSettings` — An object describing the settings used for this capture. Match this object’s [uniqueID](../avcapturephotosettings/uniqueid.md) value to the [uniqueID](../avcapturephotosettings/uniqueid.md) property of the photo settings object you initiated capture with to determine which capture request this delegate call corresponds to. You can also use this object to find out which values the photo output has chosen for automatic settings.

- `bracketSettings` — If you requested a bracketed capture of multiple images with a [AVCapturePhotoBracketSettings](../avcapturephotobracketsettings.md), a bracketed still image settings object describing which image in the bracket this delegate call corresponds to. If you did not request bracketed capture, this parameter is `nil`.

- `error` — If an the capture process could not proceed successfully, an error object describing the failure; otherwise, `nil`.

## Discussion

Use this method to receive the results of a RAW format capture. (If you request capture in both RAW and a processed format, the photo output calls both this method and the [- captureOutput:didFinishProcessingPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<photooutput(__didfinishprocessingphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) method.)

> [!important] Important
> You must implement either this method or the [- captureOutput:didFinishProcessingPhoto:error:](<photooutput(__didfinishprocessingphoto_error_).md>) method if you request capture in a RAW format. The photo output validates this requirement when you call its [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method; if your delegate does not implement the correct methods, the photo output raises an exception.

If you request RAW format capture, the photo output calls this method once for each exposure in the capture request. If you request a single image capture, this method is called once. If you request a bracketed capture with multiple exposures, this method is called once for each exposure.

## See Also

### Receiving capture results

- [- captureOutput:didFinishProcessingPhoto:error:](<photooutput(__didfinishprocessingphoto_error_).md>) — Provides the delegate with the captured image and associated metadata resulting from a photo capture.
- [- captureOutput:didFinishRecordingLivePhotoMovieForEventualFileAtURL:resolvedSettings:](<photooutput(__didfinishrecordinglivephotomovieforeventualfileat_resolvedsettings_).md>) — Notifies the delegate that the movie content of a Live Photo has finished recording.
- [- captureOutput:didFinishProcessingLivePhotoToMovieFileAtURL:duration:photoDisplayTime:resolvedSettings:error:](<photooutput(__didfinishprocessinglivephototomoviefileat_duration_photodisplaytime_resolvedsettings_error_).md>) — Provides the delegate the movie file URL resulting from a Live Photo capture.
- [- captureOutput:didFinishCapturingDeferredPhotoProxy:error:](<photooutput(__didfinishcapturingdeferredphotoproxy_error_).md>) — Tells the delegate when the system finishes capturing the photo proxy.
- [- captureOutput:didFinishProcessingPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<photooutput(__didfinishprocessingphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) — Provides the delegate a captured image in a processed format (such as JPEG). _(deprecated)_

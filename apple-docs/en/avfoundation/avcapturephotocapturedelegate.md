---
title: AVCapturePhotoCaptureDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotocapturedelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotocapturedelegate.json'
content_hash: 'sha256:28e06aa12a88d093'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCapturePhotoCaptureDelegate

<sub>Protocol</sub>

Methods for monitoring progress and receiving results from a photo capture output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
protocol AVCapturePhotoCaptureDelegate : NSObjectProtocol
```

## Overview

You implement methods in the [AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md) protocol to be notified of progress and results when capturing photos with the [AVCapturePhotoOutput](avcapturephotooutput.md) class.

To capture a photo, you pass an object implementing this protocol to the [- capturePhotoWithSettings:delegate:](<avcapturephotooutput/capturephoto(with_delegate_).md>) method, along with a settings object that describes the capture to be performed. As the capture proceeds, the photo output calls several of the methods in this protocol on your delegate object, providing information about the capture’s progress and delivering the resulting photos.

Which delegate methods the photo output calls depends on the photo settings you initiate capture with. All methods in this protocol are optional at compile time, but at run time your delegate object must respond to certain methods depending on your photo settings:

- If you request a still photo capture (by specifying image formats or file types), your delegate either must implement the [- captureOutput:didFinishProcessingPhoto:error:](<avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) method, or must implement methods listed in `Receiving Capture Results (Deprecated)` corresponding to whether you request capture in RAW format, processed format, or both.
- If you request Live Photo capture (by setting the [livePhotoMovieFileURL](avcapturephotosettings/livephotomoviefileurl.md) property to a non-`nil` value), your delegate must implement the [- captureOutput:didFinishProcessingLivePhotoToMovieFileAtURL:duration:photoDisplayTime:resolvedSettings:error:](<avcapturephotocapturedelegate/photooutput(__didfinishprocessinglivephototomoviefileat_duration_photodisplaytime_resolvedsettings_error_).md>) method.

The capture output validates these requirements when you call the [- capturePhotoWithSettings:delegate:](<avcapturephotooutput/capturephoto(with_delegate_).md>) method. If your delegate does not meet these requirements, that method raises an exception.

You must use a unique [AVCapturePhotoSettings](avcapturephotosettings.md) object for each capture request. When the photo output calls your delegate methods, it provides an [AVCaptureResolvedPhotoSettings](avcaptureresolvedphotosettings.md) object whose [uniqueID](avcapturephotosettings/uniqueid.md) property matches that of the photo settings you requested capture with. When making multiple captures, use this unique ID to determine which delegate method calls correspond to which requests.

The photo output always calls each method listed in Monitoring Capture Progress exactly once for each capture request. For methods listed in Receiving Capture Results, you may receive a call more than once, or not at all, depending on your photo settings. See the description of each method for details.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Monitoring capture progress

- [- captureOutput:willBeginCaptureForResolvedSettings:](<avcapturephotocapturedelegate/photooutput(__willbegincapturefor_).md>) — Notifies the delegate that the capture output has resolved settings and will soon begin its capture process.
- [- captureOutput:willCapturePhotoForResolvedSettings:](<avcapturephotocapturedelegate/photooutput(__willcapturephotofor_).md>) — Notifies the delegate that photo capture is about to occur.
- [- captureOutput:didCapturePhotoForResolvedSettings:](<avcapturephotocapturedelegate/photooutput(__didcapturephotofor_).md>) — Notifies the delegate that the photo has been taken.
- [- captureOutput:didFinishCaptureForResolvedSettings:error:](<avcapturephotocapturedelegate/photooutput(__didfinishcapturefor_error_).md>) — Notifies the delegate that the capture process is complete.

### Receiving capture results

- [- captureOutput:didFinishProcessingPhoto:error:](<avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) — Provides the delegate with the captured image and associated metadata resulting from a photo capture.
- [- captureOutput:didFinishRecordingLivePhotoMovieForEventualFileAtURL:resolvedSettings:](<avcapturephotocapturedelegate/photooutput(__didfinishrecordinglivephotomovieforeventualfileat_resolvedsettings_).md>) — Notifies the delegate that the movie content of a Live Photo has finished recording.
- [- captureOutput:didFinishProcessingLivePhotoToMovieFileAtURL:duration:photoDisplayTime:resolvedSettings:error:](<avcapturephotocapturedelegate/photooutput(__didfinishprocessinglivephototomoviefileat_duration_photodisplaytime_resolvedsettings_error_).md>) — Provides the delegate the movie file URL resulting from a Live Photo capture.
- [- captureOutput:didFinishCapturingDeferredPhotoProxy:error:](<avcapturephotocapturedelegate/photooutput(__didfinishcapturingdeferredphotoproxy_error_).md>) — Tells the delegate when the system finishes capturing the photo proxy.
- [- captureOutput:didFinishProcessingPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) — Provides the delegate a captured image in a processed format (such as JPEG). _(deprecated)_
- [- captureOutput:didFinishProcessingRawPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<avcapturephotocapturedelegate/photooutput(__didfinishprocessingrawphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) — Provides the delegate a captured image in RAW format. _(deprecated)_

## See Also

### Photo capture

- [Capturing consistent color images](capturing-consistent-color-images.md) — Add the power of a photography studio and lighting rig to your app with the new Constant Color API.
- [Capturing still and Live Photos](capturing-still-and-live-photos.md) — Configure and capture single or multiple still images, Live Photos, and other forms of photography.
- [Capturing photos in RAW and Apple ProRAW formats](capturing-photos-in-raw-and-apple-proraw-formats.md) — Support professional photography workflows by enabling minimally processed image capture in your camera app.
- [Supporting Continuity Camera in Your Mac App](../appkit/supporting-continuity-camera-in-your-mac-app.md) — Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [AVCapturePhoto](avcapturephoto.md) — A container for image data from a photo capture output.
- [AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md) — A lightly-processed photo with data that the system may use to process and fetch a higher-resolution asset at a later time.
- [AVCapturePhotoOutput](avcapturephotooutput.md) — A capture output for still image, Live Photos, and other photography workflows.
- [AVCapturePhotoOutputReadinessCoordinator](avcapturephotooutputreadinesscoordinator.md) — An object that monitors changes to a photo output’s capture readiness.
- [AVCapturePhotoOutputReadinessCoordinatorDelegate](avcapturephotooutputreadinesscoordinatordelegate.md) — A delegate protocol to receive updates about a photo output’s capture readiness.
- [AVCaptureStillImageOutput](avcapturestillimageoutput.md) — A capture output for capturing still photos. _(deprecated)_

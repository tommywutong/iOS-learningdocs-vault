---
title: AVCapturePhotoOutputReadinessCoordinator
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutputreadinesscoordinator
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutputreadinesscoordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutputreadinesscoordinator.json'
content_hash: 'sha256:110b2ae44286c632'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCapturePhotoOutputReadinessCoordinator

<sub>Class</sub>

An object that monitors changes to a photo output’s capture readiness.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCapturePhotoOutputReadinessCoordinator
```

## Overview

Use this object to coordinate user interface updates on the main queue with a [AVCapturePhotoOutput](avcapturephotooutput.md) that runs on a background queue. Adopt the [AVCapturePhotoOutputReadinessCoordinatorDelegate](avcapturephotooutputreadinesscoordinatordelegate.md) protocol in your app and set its implementation as the coordinator’s delegate object to receive callbacks as the associated photo output’s [captureReadiness](avcapturephotooutput/capturereadiness-swift.property.md) state changes.

You can track additional capture requests with this object by calling its [- startTrackingCaptureRequestUsingPhotoSettings:](<avcapturephotooutputreadinesscoordinator/starttrackingcapturerequest(using_).md>) method. You can use it to synchronously update shutter button availability and appearance and on the main thread while calling the photo output’s [- capturePhotoWithSettings:delegate:](<avcapturephotooutput/capturephoto(with_delegate_).md>) method asynchronously on a background queue.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a coordinator

- [- initWithPhotoOutput:](<avcapturephotooutputreadinesscoordinator/init(photooutput_).md>) — Creates an object that helps coordinate user interface changes with a photo output that runs on a background queue.

### Setting the delegate object

- [delegate](avcapturephotooutputreadinesscoordinator/delegate.md) — The coordinator’s delegate object.

### Performing tracking requests

- [- startTrackingCaptureRequestUsingPhotoSettings:](<avcapturephotooutputreadinesscoordinator/starttrackingcapturerequest(using_).md>) — Tracks a capture request that uses the specified photo settings.
- [- stopTrackingCaptureRequestUsingPhotoSettingsUniqueID:](<avcapturephotooutputreadinesscoordinator/stoptrackingcapturerequest(using_).md>) — Stop tracking the capture request represented by the specified photo setting’s unique identifier.

### Determining readiness for capture

- [captureReadiness](avcapturephotooutputreadinesscoordinator/capturereadiness.md) — A value that indicates whether the coordinator’s photo output is ready to respond to new capture requests in a timely manner.

## See Also

### Photo capture

- [Capturing consistent color images](capturing-consistent-color-images.md) — Add the power of a photography studio and lighting rig to your app with the new Constant Color API.
- [Capturing still and Live Photos](capturing-still-and-live-photos.md) — Configure and capture single or multiple still images, Live Photos, and other forms of photography.
- [Capturing photos in RAW and Apple ProRAW formats](capturing-photos-in-raw-and-apple-proraw-formats.md) — Support professional photography workflows by enabling minimally processed image capture in your camera app.
- [Supporting Continuity Camera in Your Mac App](../appkit/supporting-continuity-camera-in-your-mac-app.md) — Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [AVCapturePhoto](avcapturephoto.md) — A container for image data from a photo capture output.
- [AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md) — A lightly-processed photo with data that the system may use to process and fetch a higher-resolution asset at a later time.
- [AVCapturePhotoOutput](avcapturephotooutput.md) — A capture output for still image, Live Photos, and other photography workflows.
- [AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md) — Methods for monitoring progress and receiving results from a photo capture output.
- [AVCapturePhotoOutputReadinessCoordinatorDelegate](avcapturephotooutputreadinesscoordinatordelegate.md) — A delegate protocol to receive updates about a photo output’s capture readiness.
- [AVCaptureStillImageOutput](avcapturestillimageoutput.md) — A capture output for capturing still photos. _(deprecated)_

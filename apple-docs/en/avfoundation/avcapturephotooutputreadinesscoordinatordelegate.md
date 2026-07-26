---
title: AVCapturePhotoOutputReadinessCoordinatorDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutputreadinesscoordinatordelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutputreadinesscoordinatordelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutputreadinesscoordinatordelegate.json'
content_hash: 'sha256:b6c9f0ce0f296856'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCapturePhotoOutputReadinessCoordinatorDelegate

<sub>Protocol</sub>

A delegate protocol to receive updates about a photo output’s capture readiness.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
protocol AVCapturePhotoOutputReadinessCoordinatorDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Monitoring capture readiness

- [- readinessCoordinator:captureReadinessDidChange:](<avcapturephotooutputreadinesscoordinatordelegate/readinesscoordinator(__capturereadinessdidchange_).md>) — Tells the delegate that the capture readiness state of a photo output changed.

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
- [AVCapturePhotoOutputReadinessCoordinator](avcapturephotooutputreadinesscoordinator.md) — An object that monitors changes to a photo output’s capture readiness.
- [AVCaptureStillImageOutput](avcapturestillimageoutput.md) — A capture output for capturing still photos. _(deprecated)_

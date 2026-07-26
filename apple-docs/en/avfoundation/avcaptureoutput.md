---
title: AVCaptureOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureoutput.json'
content_hash: 'sha256:bd8b9d4ae096deca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureOutput

<sub>Class</sub>

An abstract superclass for objects that provide media output destinations for a capture session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVCaptureOutput
```

## Overview

This class provides an abstract interface to connect capture output destinations, such as files and streams, to a capture session.

A capture output can have multiple connections, one for each stream of media that it receives from a capture input. A capture output doesn’t have any connections when you create it. When you add it to a capture session, the session automatically forms connections between compatible inputs and outputs.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVCaptureAudioDataOutput](avcaptureaudiodataoutput.md), [AVCaptureAudioPreviewOutput](avcaptureaudiopreviewoutput.md), [AVCaptureBroadcastVideoOutput](avcapturebroadcastvideooutput.md), [AVCaptureDepthDataOutput](avcapturedepthdataoutput.md), [AVCaptureFileOutput](avcapturefileoutput.md), [AVCaptureMetadataOutput](avcapturemetadataoutput.md), [AVCapturePhotoOutput](avcapturephotooutput.md), [AVCaptureStillImageOutput](avcapturestillimageoutput.md), [AVCaptureVideoDataOutput](avcapturevideodataoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing connections

- [connections](avcaptureoutput/connections.md) — The capture output object’s connections.
- [- connectionWithMediaType:](<avcaptureoutput/connection(with_).md>) — Returns the first connection with an input port of a specified media type.
- [DataDroppedReason](avcaptureoutput/datadroppedreason.md) — Constants that define reasons for why the system dropped a frame.

### Managing deferred start

- [deferredStartEnabled](avcaptureoutput/isdeferredstartenabled.md) — A Boolean value that indicates whether to defer starting this capture output.
- [deferredStartSupported](avcaptureoutput/isdeferredstartsupported.md) — A `BOOL` value that indicates whether the output supports deferred start.

### Converting between coordinate systems

- [- transformedMetadataObjectForMetadataObject:connection:](<avcaptureoutput/transformedmetadataobject(for_connection_).md>) — Converts a metadata object’s visual properties to layer coordinates.
- [- metadataOutputRectOfInterestForRect:](<avcaptureoutput/metadataoutputrectconverted(fromoutputrect_).md>) — Converts a rectangle in the capture output object’s coordinate system to one in the coordinate system used for metadata outputs.
- [- rectForMetadataOutputRectOfInterest:](<avcaptureoutput/outputrectconverted(frommetadataoutputrect_).md>) — Converts a rectangle in the coordinate system used for metadata outputs to one in the capture output object’s coordinate system.

## See Also

### Capture sessions

- [Setting up a capture session](setting-up-a-capture-session.md) — Configure input devices, output media, preview views, and basic settings before capturing photos or video.
- [Accessing the camera while multitasking on iPad](../avkit/accessing-the-camera-while-multitasking-on-ipad.md) — Operate the camera in Split View, Slide Over, Picture in Picture, and Stage Manager modes.
- [AVCam: Building a camera app](avcam-building-a-camera-app.md) — Capture photos and record video using the front and rear iPhone and iPad cameras.
- [Build a responsive camera app that launches quickly](build-a-responsive-camera-app-that-launches-quickly.md) — Build a fast camera launch experience for your iOS and iPadOS apps.
- [Capturing Cinematic video](capturing-cinematic-video.md) — Capture video with an adjustable depth of field and focus points.
- [Supporting Center Stage front camera in your iOS app](supporting-center-stage-front-camera-in-your-ios-app.md) — Enable Center Stage for photos and videos on the iPhone front camera.
- [AVMultiCamPiP: Capturing from Multiple Cameras](avmulticampip-capturing-from-multiple-cameras.md) — Simultaneously record the output from the front and back cameras into a single movie file by using a multi-camera capture session.
- [AVCamBarcode: detecting barcodes and faces](avcambarcode-detecting-barcodes-and-faces.md) — Identify machine readable codes or faces by using the camera.
- [AVCaptureSession](avcapturesession.md) — An object that configures capture behavior and coordinates the flow of data from input devices to capture outputs.
- [AVCaptureMultiCamSession](avcapturemulticamsession.md) — A capture session that supports simultaneous capture from multiple inputs of the same media type.
- [AVCaptureInput](avcaptureinput.md) — An abstract superclass for objects that provide input data to a capture session.
- [AVCaptureConnection](avcaptureconnection.md) — An object that represents a connection from a capture input to a capture output.

---
title: AVCaptureMultiCamSession
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemulticamsession
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemulticamsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemulticamsession.json'
content_hash: 'sha256:5d464bd83f34def4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureMultiCamSession

<sub>Class</sub>

A capture session that supports simultaneous capture from multiple inputs of the same media type.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class AVCaptureMultiCamSession
```

## Overview

The session preset for a multicamera session is always [AVCaptureSessionPresetInputPriority](avcapturesession/preset/inputpriority.md). Set each capture device’s [activeFormat](avcapturedevice/activeformat.md) value to the desired quality of service.

You can dynamically enable and disable this session’s individual camera inputs without interrupting capture preview. To stop an individual camera, disable all of its connections or connected ports. The camera then stops streaming data to save power and bandwidth. Other inputs that are streaming data through the session are unaffected.

> [!note] Note
> If your app only needs to capture from a single camera at a time, use [AVCaptureSession](avcapturesession.md) instead.

## Relationships

- **Inherits From**: [AVCaptureSession](avcapturesession.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Determining multi-camera support

- [multiCamSupported](avcapturemulticamsession/ismulticamsupported.md) — A Boolean value that indicates whether this device supports multi-camera sessions.

### Managing resources

- [hardwareCost](avcapturemulticamsession/hardwarecost.md) — A value that indicates the percentage of the session’s available hardware budget currently in use.
- [systemPressureCost](avcapturemulticamsession/systempressurecost.md) — A value that indicates the system pressure cost of the current session configuration.

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
- [AVCaptureInput](avcaptureinput.md) — An abstract superclass for objects that provide input data to a capture session.
- [AVCaptureOutput](avcaptureoutput.md) — An abstract superclass for objects that provide media output destinations for a capture session.
- [AVCaptureConnection](avcaptureconnection.md) — An object that represents a connection from a capture input to a capture output.

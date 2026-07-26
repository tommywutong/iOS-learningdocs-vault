---
title: AVCaptureConnection
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureconnection
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection.json'
content_hash: 'sha256:07496419bca9e870'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureConnection

<sub>Class</sub>

An object that represents a connection from a capture input to a capture output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVCaptureConnection
```

## Overview

Capture inputs have one or more input ports (instances of [Port](avcaptureinput/port.md)). Capture outputs can accept data from one or more sources (for example, an [AVCaptureMovieFileOutput](avcapturemoviefileoutput.md) object accepts both video and audio data).

You can add an `AVCaptureConnection` instance to a session using the [- addConnection:](<avcapturesession/addconnection(__).md>) method only if the [- canAddConnection:](<avcapturesession/canaddconnection(__).md>) method returns [true](../swift/true.md). When using the [- addInput:](<avcapturesession/addinput(__).md>) or [- addOutput:](<avcapturesession/addoutput(__).md>) method, the session forms connections automatically between all compatible inputs and outputs. You only need to add connections manually when adding an input or output with no connections. You can also use connections to enable or disable the flow of data from a given input or to a given output.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a connection

- [- initWithInputPorts:output:](<avcaptureconnection/init(inputports_output_).md>) — Creates a capture connection that represents a connection between multiple input ports and an output.
- [- initWithInputPort:videoPreviewLayer:](<avcaptureconnection/init(inputport_videopreviewlayer_).md>) — Creates a capture connection that represents a connection between an input port and a video preview layer.

### Enabling a connection

- [enabled](avcaptureconnection/isenabled.md) — Turns the connection on and off.
- [active](avcaptureconnection/isactive.md) — Indicates whether the connection is active.

### Inspecting a connection

- [inputPorts](avcaptureconnection/inputports.md) — An array of the connection’s input ports.
- [output](avcaptureconnection/output.md) — The connection’s output port, if applicable.
- [videoPreviewLayer](avcaptureconnection/videopreviewlayer.md) — The video preview layer associated with the connection.
- [audioChannels](avcaptureconnection/audiochannels.md) — An array of audio channels that the connection provides.

### Rotating a video

- [- isVideoRotationAngleSupported:](<avcaptureconnection/isvideorotationanglesupported(__).md>) — Returns a Boolean value that indicates whether the connection supports a rotation angle.
- [videoRotationAngle](avcaptureconnection/videorotationangle.md) — A rotation angle the connection applies to a video flowing through it.

### Mirroring a video

- [supportsVideoMirroring](avcaptureconnection/isvideomirroringsupported.md) — A Boolean value that indicates whether the connection supports video mirroring.
- [videoMirrored](avcaptureconnection/isvideomirrored.md) — A Boolean value that indicates whether the connection horizontally flips the video flowing through it.
- [automaticallyAdjustsVideoMirroring](avcaptureconnection/automaticallyadjustsvideomirroring.md) — A Boolean value that indicates whether you can enable mirroring based on a session’s configuration.

### Stabilizing video

- [supportsVideoStabilization](avcaptureconnection/isvideostabilizationsupported.md) — A Boolean value that indicates whether this connection supports video stabilization.
- [activeVideoStabilizationMode](avcaptureconnection/activevideostabilizationmode.md) — The connection’s current stabilization mode.
- [preferredVideoStabilizationMode](avcaptureconnection/preferredvideostabilizationmode.md) — The stabilization mode that’s the most appropriate for a video connection.

### Delivering camera calibration settings

- [cameraIntrinsicMatrixDeliverySupported](avcaptureconnection/iscameraintrinsicmatrixdeliverysupported.md) — A Boolean value that indicates whether the capture connection currently supports delivering camera intrinsics information.
- [cameraIntrinsicMatrixDeliveryEnabled](avcaptureconnection/iscameraintrinsicmatrixdeliveryenabled.md) — A Boolean value that indicates whether the connection can configure the capture pipeline to deliver camera intrinsics information.

### Configuring a video’s frame rate

- [supportsVideoMinFrameDuration](avcaptureconnection/isvideominframedurationsupported.md) — A Boolean value that indicates whether the connection supports a minimum frame duration. _(deprecated)_
- [videoMinFrameDuration](avcaptureconnection/videominframeduration.md) — The smallest time interval the connection can apply between consecutive video frames. _(deprecated)_
- [supportsVideoMaxFrameDuration](avcaptureconnection/isvideomaxframedurationsupported.md) — A Boolean value that indicates whether the connection supports a maximum frame duration. _(deprecated)_
- [videoMaxFrameDuration](avcaptureconnection/videomaxframeduration.md) — The largest time interval the connection can apply between consecutive video frames. _(deprecated)_

### Scaling a video

- [videoMaxScaleAndCropFactor](avcaptureconnection/videomaxscaleandcropfactor.md) — The connection’s maximum video scale and crop factor.
- [videoScaleAndCropFactor](avcaptureconnection/videoscaleandcropfactor.md) — The current scale and crop factor the video output uses.

### Interlacing video

- [supportsVideoFieldMode](avcaptureconnection/isvideofieldmodesupported.md) — A Boolean value that indicates whether the connection supports setting a video field mode.
- [videoFieldMode](avcaptureconnection/videofieldmode.md) — A setting that tells the connection how to interlace video flowing through it.
- [AVVideoFieldMode](avvideofieldmode.md) — Constants that indicate which interlacing modes the connection applies to video flowing through it.

### Deprecated

- [videoStabilizationEnabled](avcaptureconnection/isvideostabilizationenabled.md) — A Boolean value that indicates whether video stabilization is active for the connection. _(deprecated)_
- [enablesVideoStabilizationWhenAvailable](avcaptureconnection/enablesvideostabilizationwhenavailable.md) — A Boolean value that indicates whether the system enables video stabilization when it’s available. _(deprecated)_
- [supportsVideoOrientation](avcaptureconnection/isvideoorientationsupported.md) — A Boolean value that indicates whether the connection supports changing the orientation of the video. _(deprecated)_
- [videoOrientation](avcaptureconnection/videoorientation.md) — An orientation that tells the connection how to rotate a video flowing through it. _(deprecated)_
- [AVCaptureVideoOrientation](avcapturevideoorientation.md) — Constants indicating video orientation. _(deprecated)_

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
- [AVCaptureOutput](avcaptureoutput.md) — An abstract superclass for objects that provide media output destinations for a capture session.

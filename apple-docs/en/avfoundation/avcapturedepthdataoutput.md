---
title: AVCaptureDepthDataOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedepthdataoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedepthdataoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedepthdataoutput.json'
content_hash: 'sha256:45745bc71e7ce53f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureDepthDataOutput

<sub>Class</sub>

A capture output that records scene depth information on compatible camera devices.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class AVCaptureDepthDataOutput
```

## Overview

This output type captures [AVDepthData](avdepthdata.md) objects containing per-pixel depth or disparity information, following a streaming delivery model similar to that used by [AVCaptureVideoDataOutput](avcapturevideodataoutput.md). Alternatively, you can capture depth data alongside photos using [AVCapturePhotoOutput](avcapturephotooutput.md) (see the [AVCapturePhotoSettings](avcapturephotosettings.md) [depthDataDeliveryEnabled](avcapturephotosettings/isdepthdatadeliveryenabled.md) property).

This object always provides depth data in the format expressed by the source [AVCaptureDevice](avcapturedevice.md) object’s [activeDepthDataFormat](avcapturedevice/activedepthdataformat.md) property. If you wish to receive depth data in another format, choose a new value for that property from those listed in the [supportedDepthDataFormats](avcapturedevice/format/supporteddepthdataformats.md) array of the device’s [activeFormat](avcapturedevice/activeformat.md) object.

## Relationships

- **Inherits From**: [AVCaptureOutput](avcaptureoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a depth data output

- [- init](<avcapturedepthdataoutput/init().md>) — Initializes a depth data output object.

### Configuring depth data capture

- [alwaysDiscardsLateDepthData](avcapturedepthdataoutput/alwaysdiscardslatedepthdata.md) — A Boolean value that determines whether the capture output should discard any depth data that is not processed before the next depth data is captured.
- [filteringEnabled](avcapturedepthdataoutput/isfilteringenabled.md) — A Boolean value that determines whether the depth data output should filter depth data to smooth out noise and fill invalid values.

### Receiving captured depth data

- [- setDelegate:callbackQueue:](<avcapturedepthdataoutput/setdelegate(__callbackqueue_).md>) — Designates a delegate object to receive depth data and a dispatch queue for delivering that data.
- [delegate](avcapturedepthdataoutput/delegate.md) — A delegate object that receives depth data.
- [delegateCallbackQueue](avcapturedepthdataoutput/delegatecallbackqueue.md) — A dispatch queue for delivering depth data.
- [AVCaptureDepthDataOutputDelegate](avcapturedepthdataoutputdelegate.md) — Methods for receiving depth data produced by a depth capture output.

## See Also

### Depth data capture

- [Capturing photos with depth](capturing-photos-with-depth.md) — Get a depth map with a photo to create effects like the system camera’s Portrait mode (on compatible devices).
- [Creating auxiliary depth data manually](creating-auxiliary-depth-data-manually.md) — Generate a depth image and attach it to your own image.
- [Capturing depth using the LiDAR camera](capturing-depth-using-the-lidar-camera.md) — Access the LiDAR camera on supporting devices to capture precise depth data.
- [AVCamFilter: Applying filters to a capture stream](avcamfilter-applying-filters-to-a-capture-stream.md) — Render a capture stream with rose-colored filtering and depth effects.
- [Streaming depth data from the TrueDepth camera](streaming-depth-data-from-the-truedepth-camera.md) — Visualize depth data in 2D and 3D from the TrueDepth camera.
- [Enhancing live video by leveraging TrueDepth camera data](enhancing-live-video-by-leveraging-truedepth-camera-data.md) — Apply your own background to a live capture feed streamed from the front-facing TrueDepth camera.
- [AVDepthData](avdepthdata.md) — A container for per-pixel distance or disparity information captured by compatible camera devices.
- [AVCameraCalibrationData](avcameracalibrationdata.md) — Information about the camera characteristics used to capture images and depth data.

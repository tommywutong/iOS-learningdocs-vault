---
title: AVCaptureVideoPreviewLayer
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideopreviewlayer
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer.json'
content_hash: 'sha256:e5c681bf67191f6f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureVideoPreviewLayer

<sub>Class</sub>

A Core Animation layer that displays video from a camera device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCaptureVideoPreviewLayer
```

## Overview

Use this layer to provide a preview of the content the camera captures. A convenient way to use this class in iOS is to set it as the backing layer for a view as shown below.

```swift
class PreviewView: UIView {
    // Use a capture video preview layer as the view's backing layer.
    override class var layerClass: AnyClass {
        AVCaptureVideoPreviewLayer.self
    }
    
    var previewLayer: AVCaptureVideoPreviewLayer {
        layer as! AVCaptureVideoPreviewLayer
    }
    
    // Connect the layer to a capture session.
    var session: AVCaptureSession? {
        get { previewLayer.session }
        set { previewLayer.session = newValue }
    }
}
```

## Relationships

- **Inherits From**: [CALayer](../quartzcore/calayer.md)

- **Conforms To**: [CAMediaTiming](../quartzcore/camediatiming.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a preview layer

- [- initWithSession:](<avcapturevideopreviewlayer/init(session_).md>) — Creates a layer to preview the visual output of a capture session.
- [- initWithSessionWithNoConnection:](<avcapturevideopreviewlayer/init(sessionwithnoconnection_).md>) — Creates a layer to preview the visual output of a capture session, without making connections to eligible video inputs.

### Layer configuration

- [previewing](avcapturevideopreviewlayer/ispreviewing.md) — A Boolean value that indicates whether the layer is rendering video frames from its source.
- [videoGravity](avcapturevideopreviewlayer/videogravity.md) — A value that indicates how the layer displays video content within its bounds.

### Configuring deferred start

- [deferredStartSupported](avcapturevideopreviewlayer/isdeferredstartsupported.md) — A `BOOL` value that indicates whether the preview layer supports deferred start.
- [deferredStartEnabled](avcapturevideopreviewlayer/isdeferredstartenabled.md) — A `BOOL` value that indicates whether to defer starting this preview layer.

### Session configuration

- [session](avcapturevideopreviewlayer/session.md) — A capture session with visual output to preview.
- [connection](avcapturevideopreviewlayer/connection.md) — An object that describes the connection from the layer to a particular input port.
- [- setSessionWithNoConnection:](<avcapturevideopreviewlayer/setsessionwithnoconnection(__).md>) — Associates a session with the layer without automatically forming a connection to an eligible input port.

### Converting between coordinate spaces

- [- pointForCaptureDevicePointOfInterest:](<avcapturevideopreviewlayer/layerpointconverted(fromcapturedevicepoint_).md>) — Converts a point from the coordinate space of the capture device to the coordinate space of the layer.
- [- captureDevicePointOfInterestForPoint:](<avcapturevideopreviewlayer/capturedevicepointconverted(fromlayerpoint_).md>) — Converts a point from layer coordinates to the coordinate space of the capture device.
- [- rectForMetadataOutputRectOfInterest:](<avcapturevideopreviewlayer/layerrectconverted(frommetadataoutputrect_).md>) — Converts a rectangle from metadata output coordinates to the coordinate space of the layer.
- [- metadataOutputRectOfInterestForRect:](<avcapturevideopreviewlayer/metadataoutputrectconverted(fromlayerrect_).md>) — Converts a rectangle from layer coordinates to the coordinate space of the metadata output.
- [- transformedMetadataObjectForMetadataObject:](<avcapturevideopreviewlayer/transformedmetadataobject(for_).md>) — Converts a metadata object’s visual properties to layer coordinates.

### Deprecated

- [Deprecated symbols](avcapturevideopreviewlayer-deprecated-symbols.md) — Review unsupported symbols and their replacements.

## See Also

### Capture preview

- [AVCaptureAudioPreviewOutput](avcaptureaudiopreviewoutput.md) — A capture output that provides a preview of the captured audio.

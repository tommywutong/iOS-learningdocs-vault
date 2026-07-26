---
title: 'captureDevicePointConverted(fromLayerPoint:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturevideopreviewlayer/capturedevicepointconverted(fromlayerpoint:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/capturedevicepointconverted(fromlayerpoint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer/capturedevicepointconverted%28fromlayerpoint%3A%29.json'
content_hash: 'sha256:51923fefef2d401f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md)

# captureDevicePointConverted(fromLayerPoint:)

<sub>Instance Method</sub>

Converts a point from layer coordinates to the coordinate space of the capture device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func captureDevicePointConverted(fromLayerPoint pointInLayer: CGPoint) -> CGPoint
```

## Parameters

- `pointInLayer` — A point in layer coordinates to convert.

## Return Value

A point in capture device coordinates.

## Discussion

A capture device’s [focusPointOfInterest](../avcapturedevice/focuspointofinterest.md) and [exposurePointOfInterest](../avcapturedevice/exposurepointofinterest.md) properties provide a [CGPoint](../../corefoundation/cgpoint.md) value where `{0,0}` represents the top-left and `{1,1}` represents the bottom-right of the unrotated image.

The conversion performed by this method takes the layer’s frame size and its [videoGravity](videogravity.md) into consideration.

## See Also

### Converting between coordinate spaces

- [- pointForCaptureDevicePointOfInterest:](<layerpointconverted(fromcapturedevicepoint_).md>) — Converts a point from the coordinate space of the capture device to the coordinate space of the layer.
- [- rectForMetadataOutputRectOfInterest:](<layerrectconverted(frommetadataoutputrect_).md>) — Converts a rectangle from metadata output coordinates to the coordinate space of the layer.
- [- metadataOutputRectOfInterestForRect:](<metadataoutputrectconverted(fromlayerrect_).md>) — Converts a rectangle from layer coordinates to the coordinate space of the metadata output.
- [- transformedMetadataObjectForMetadataObject:](<transformedmetadataobject(for_).md>) — Converts a metadata object’s visual properties to layer coordinates.

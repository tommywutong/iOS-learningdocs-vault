---
title: 'transformedMetadataObject(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturevideopreviewlayer/transformedmetadataobject(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/transformedmetadataobject(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer/transformedmetadataobject%28for%3A%29.json'
content_hash: 'sha256:af37bc85e4d22349'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md)

# transformedMetadataObject(for:)

<sub>Instance Method</sub>

Converts a metadata object’s visual properties to layer coordinates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func transformedMetadataObject(for metadataObject: AVMetadataObject) -> AVMetadataObject?
```

## Parameters

- `metadataObject` — The metadata object whose visual properties you want to convert. The metadata object must originate from the same [AVCaptureInput](../avcaptureinput.md) as the preview layer.

## Return Value

A metadata object with coordinates converted into layer coordinates, or `nil` if the  metadata object originates from an input source other than that of the preview layer.

## Discussion

The system provides the metadata object’s bounds as a rectangle where `{0,0}` represents the top-left of the picture area, and `{1,1}` represents the bottom-right on an unrotated image. Face metadata objects also provide [yawAngle](../avmetadatafaceobject/yawangle.md) and [rollAngle](../avmetadatafaceobject/rollangle.md) values with respect to an unrotated picture.

The conversion takes orientation, mirroring, layer bounds and video gravity into consideration.

## See Also

### Converting between coordinate spaces

- [- pointForCaptureDevicePointOfInterest:](<layerpointconverted(fromcapturedevicepoint_).md>) — Converts a point from the coordinate space of the capture device to the coordinate space of the layer.
- [- captureDevicePointOfInterestForPoint:](<capturedevicepointconverted(fromlayerpoint_).md>) — Converts a point from layer coordinates to the coordinate space of the capture device.
- [- rectForMetadataOutputRectOfInterest:](<layerrectconverted(frommetadataoutputrect_).md>) — Converts a rectangle from metadata output coordinates to the coordinate space of the layer.
- [- metadataOutputRectOfInterestForRect:](<metadataoutputrectconverted(fromlayerrect_).md>) — Converts a rectangle from layer coordinates to the coordinate space of the metadata output.

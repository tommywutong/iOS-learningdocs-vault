---
title: 'layerRectConverted(fromMetadataOutputRect:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturevideopreviewlayer/layerrectconverted(frommetadataoutputrect:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/layerrectconverted(frommetadataoutputrect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer/layerrectconverted%28frommetadataoutputrect%3A%29.json'
content_hash: 'sha256:22581940477d8e25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md)

# layerRectConverted(fromMetadataOutputRect:)

<sub>Instance Method</sub>

Converts a rectangle from metadata output coordinates to the coordinate space of the layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func layerRectConverted(fromMetadataOutputRect rectInMetadataOutputCoordinates: CGRect) -> CGRect
```

## Parameters

- `rectInMetadataOutputCoordinates` — A rectangle in the [AVCaptureMetadataOutput](../avcapturemetadataoutput.md) coordinate system.

## Return Value

A rectangle in the preview layer’s coordinate system.

## Discussion

A metadata capture output’s [rectOfInterest](../avcapturemetadataoutput/rectofinterest.md) a [CGRect](../../corefoundation/cgrect.md) value where `{0,0}` represents the top-left of the picture area, and `{1,1}` represents the bottom-right on an unrotated image.

The system takes the layer’s frame size and its [videoGravity](videogravity.md) into consideration when making the conversion.

## See Also

### Converting between coordinate spaces

- [- pointForCaptureDevicePointOfInterest:](<layerpointconverted(fromcapturedevicepoint_).md>) — Converts a point from the coordinate space of the capture device to the coordinate space of the layer.
- [- captureDevicePointOfInterestForPoint:](<capturedevicepointconverted(fromlayerpoint_).md>) — Converts a point from layer coordinates to the coordinate space of the capture device.
- [- metadataOutputRectOfInterestForRect:](<metadataoutputrectconverted(fromlayerrect_).md>) — Converts a rectangle from layer coordinates to the coordinate space of the metadata output.
- [- transformedMetadataObjectForMetadataObject:](<transformedmetadataobject(for_).md>) — Converts a metadata object’s visual properties to layer coordinates.

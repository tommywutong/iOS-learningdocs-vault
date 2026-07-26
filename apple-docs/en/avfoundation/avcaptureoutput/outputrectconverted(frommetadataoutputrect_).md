---
title: 'outputRectConverted(fromMetadataOutputRect:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureoutput/outputrectconverted(frommetadataoutputrect:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureoutput/outputrectconverted(frommetadataoutputrect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureoutput/outputrectconverted%28frommetadataoutputrect%3A%29.json'
content_hash: 'sha256:bed7fb036337d6e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureOutput](../avcaptureoutput.md)

# outputRectConverted(fromMetadataOutputRect:)

<sub>Instance Method</sub>

Converts a rectangle in the coordinate system used for metadata outputs to one in the capture output object’s coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func outputRectConverted(fromMetadataOutputRect rectInMetadataOutputCoordinates: CGRect) -> CGRect
```

## Parameters

- `rectInMetadataOutputCoordinates` — A rectangle in the [AVCaptureMetadataOutput](../avcapturemetadataoutput.md) coordinate system.

## Return Value

A rectangle in the [AVCaptureOutput](../avcaptureoutput.md) object’s coordinate system.

## Discussion

The rectangle of interest for an [AVCaptureMetadataOutput](../avcapturemetadataoutput.md) object is in a coordinate system extending from `{0,0}` in the top-left to `{1,1}` in the bottom-right, relative to the device’s natural orientation. A capture output object uses a pixel coordinate space which you may zoom, rotate, or mirror.

## See Also

### Converting between coordinate systems

- [- transformedMetadataObjectForMetadataObject:connection:](<transformedmetadataobject(for_connection_).md>) — Converts a metadata object’s visual properties to layer coordinates.
- [- metadataOutputRectOfInterestForRect:](<metadataoutputrectconverted(fromoutputrect_).md>) — Converts a rectangle in the capture output object’s coordinate system to one in the coordinate system used for metadata outputs.

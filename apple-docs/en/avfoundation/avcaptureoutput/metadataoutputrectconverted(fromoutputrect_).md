---
title: 'metadataOutputRectConverted(fromOutputRect:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptureoutput/metadataoutputrectconverted(fromoutputrect:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureoutput/metadataoutputrectconverted(fromoutputrect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureoutput/metadataoutputrectconverted%28fromoutputrect%3A%29.json'
content_hash: 'sha256:96774f678e878a25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureOutput](../avcaptureoutput.md)

# metadataOutputRectConverted(fromOutputRect:)

<sub>Instance Method</sub>

Converts a rectangle in the capture output object’s coordinate system to one in the coordinate system used for metadata outputs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func metadataOutputRectConverted(fromOutputRect rectInOutputCoordinates: CGRect) -> CGRect
```

## Parameters

- `rectInOutputCoordinates` — A rectangle in the [AVCaptureOutput](../avcaptureoutput.md) object’s coordinate system.

## Return Value

A rectangle in the [AVCaptureMetadataOutput](../avcapturemetadataoutput.md) coordinate system.

## Discussion

An [AVCaptureMetadataOutput](../avcapturemetadataoutput.md) object expresses its [rectOfInterest](../avcapturemetadataoutput/rectofinterest.md) as a [CGRect](../../corefoundation/cgrect.md) where 0,0 represents the top-left of the picture area, and 1,1 represents the bottom-right on an unrotated picture. This convenience method converts a rectangle in the coordinate space of the output to a rectangle of interest in the coordinate space of a metadata output whose capture device provides input to the output. The conversion takes orientation, mirroring, and scaling into consideration.

See [- transformedMetadataObjectForMetadataObject:connection:](<transformedmetadataobject(for_connection_).md>) for a full discussion of how the system applies orientation and mirroring to sample buffers passing through the output.

## See Also

### Converting between coordinate systems

- [- transformedMetadataObjectForMetadataObject:connection:](<transformedmetadataobject(for_connection_).md>) — Converts a metadata object’s visual properties to layer coordinates.
- [- rectForMetadataOutputRectOfInterest:](<outputrectconverted(frommetadataoutputrect_).md>) — Converts a rectangle in the coordinate system used for metadata outputs to one in the capture output object’s coordinate system.

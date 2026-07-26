---
title: availableMetadataObjectTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemetadataoutput/availablemetadataobjecttypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/availablemetadataobjecttypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemetadataoutput/availablemetadataobjecttypes.json'
content_hash: 'sha256:e15cf70c2b09cf78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMetadataOutput](../avcapturemetadataoutput.md)

# availableMetadataObjectTypes

<sub>Instance Property</sub>

An array of strings identifying the types of metadata objects that can be captured.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var availableMetadataObjectTypes: [AVMetadataObject.ObjectType] { get }
```

## Discussion

Each string in the array corresponds to a possible value in the [type](../avmetadataobject/type.md) property of the [AVMetadataObject](../avmetadataobject.md) objects reported by the receiver. The available types are dependent on the capabilities of the [Port](../avcaptureinput/port.md) to which the receiver’s connection is attached.

## See Also

### Configuring metadata capture

- [metadataObjectTypes](metadataobjecttypes.md) — An array of strings identifying the types of metadata objects  to process.
- [rectOfInterest](rectofinterest.md) — A rectangle of interest for limiting the search area for visual metadata.
- [requiredMetadataObjectTypesForCinematicVideoCapture](requiredmetadataobjecttypesforcinematicvideocapture.md) — The required metadata object types when Cinematic Video capture is enabled.

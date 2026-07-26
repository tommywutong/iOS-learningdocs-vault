---
title: requiredMetadataObjectTypesForCinematicVideoCapture
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemetadataoutput/requiredmetadataobjecttypesforcinematicvideocapture
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/requiredmetadataobjecttypesforcinematicvideocapture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemetadataoutput/requiredmetadataobjecttypesforcinematicvideocapture.json'
content_hash: 'sha256:f16aeb00f9620263'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMetadataOutput](../avcapturemetadataoutput.md)

# requiredMetadataObjectTypesForCinematicVideoCapture

<sub>Instance Property</sub>

The required metadata object types when Cinematic Video capture is enabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var requiredMetadataObjectTypesForCinematicVideoCapture: [AVMetadataObject.ObjectType] { get }
```

## Discussion

Since the Cinematic Video algorithm requires a particular set of metadata objects to function optimally, you must set your [metadataObjectTypes](metadataobjecttypes.md) property to this property’s returned value if you’ve set [cinematicVideoCaptureEnabled](../avcapturedeviceinput/iscinematicvideocaptureenabled.md) to `true` on the connected device input, otherwise an `NSInvalidArgumentException` is thrown.

## See Also

### Configuring metadata capture

- [availableMetadataObjectTypes](availablemetadataobjecttypes.md) — An array of strings identifying the types of metadata objects that can be captured.
- [metadataObjectTypes](metadataobjecttypes.md) — An array of strings identifying the types of metadata objects  to process.
- [rectOfInterest](rectofinterest.md) — A rectangle of interest for limiting the search area for visual metadata.

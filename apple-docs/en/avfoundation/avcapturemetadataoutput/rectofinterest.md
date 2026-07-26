---
title: rectOfInterest
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemetadataoutput/rectofinterest
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/rectofinterest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemetadataoutput/rectofinterest.json'
content_hash: 'sha256:9d210d55d2827b52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMetadataOutput](../avcapturemetadataoutput.md)

# rectOfInterest

<sub>Instance Property</sub>

A rectangle of interest for limiting the search area for visual metadata.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var rectOfInterest: CGRect { get set }
```

## Discussion

The value of this property is a [CGRect](../../corefoundation/cgrect.md) value that determines the object’s rectangle of interest for each frame of video.

The rectangle’s origin is top left and is relative to the coordinate space of the device providing the metadata.

Specifying a rectangle of interest may improve detection performance for certain types of metadata.  Metadata objects whose bounds do not intersect with the `rectOfInterest` will not be returned.

The default value of this property is a rectangle of `(0.0, 0.0, 1.0, 1.0)`.

## See Also

### Configuring metadata capture

- [availableMetadataObjectTypes](availablemetadataobjecttypes.md) — An array of strings identifying the types of metadata objects that can be captured.
- [metadataObjectTypes](metadataobjecttypes.md) — An array of strings identifying the types of metadata objects  to process.
- [requiredMetadataObjectTypesForCinematicVideoCapture](requiredmetadataobjecttypesforcinematicvideocapture.md) — The required metadata object types when Cinematic Video capture is enabled.

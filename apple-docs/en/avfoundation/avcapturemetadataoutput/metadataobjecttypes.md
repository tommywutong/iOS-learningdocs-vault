---
title: metadataObjectTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemetadataoutput/metadataobjecttypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/metadataobjecttypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemetadataoutput/metadataobjecttypes.json'
content_hash: 'sha256:c3f0ba26750f1086'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMetadataOutput](../avcapturemetadataoutput.md)

# metadataObjectTypes

<sub>Instance Property</sub>

An array of strings identifying the types of metadata objects  to process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var metadataObjectTypes: [AVMetadataObject.ObjectType]! { get set }
```

## Discussion

This property is used to filter the metadata objects reported by the receiver. Only metadata objects whose type matches one of the strings in this property are forwarded to the delegate’s [- captureOutput:didOutputMetadataObjects:fromConnection:](<../avcapturemetadataoutputobjectsdelegate/metadataoutput(__didoutput_from_).md>) method for processing.

When assigning a new array to this property, each of the type strings must be present in the array returned by the [availableMetadataObjectTypes](availablemetadataobjecttypes.md) property; otherwise, the receiver raises an[NSException](../../foundation/nsexception.md).

The default is an empty [NSArray](../../foundation/nsarray.md) object, and as a result, no metadata objects are forwarded to the delegate’s [- captureOutput:didOutputMetadataObjects:fromConnection:](<../avcapturemetadataoutputobjectsdelegate/metadataoutput(__didoutput_from_).md>) method. The same result can be achieved by setting the property to `nil`. This default behavior maximizes both performance and battery life.

> [!note] Note
> Applications linked prior to iOS 7.0 will pass [AVMetadataFaceObject](../avmetadatafaceobject.md) objects to the delegate by default, if supported by the device.

## See Also

### Configuring metadata capture

- [availableMetadataObjectTypes](availablemetadataobjecttypes.md) — An array of strings identifying the types of metadata objects that can be captured.
- [rectOfInterest](rectofinterest.md) — A rectangle of interest for limiting the search area for visual metadata.
- [requiredMetadataObjectTypesForCinematicVideoCapture](requiredmetadataobjecttypesforcinematicvideocapture.md) — The required metadata object types when Cinematic Video capture is enabled.

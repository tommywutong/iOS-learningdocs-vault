---
title: corners
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 9.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadatamachinereadablecodeobject/corners-8f6bv
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadatamachinereadablecodeobject/corners-8f6bv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadatamachinereadablecodeobject/corners-8f6bv.json'
content_hash: 'sha256:39c59d0d34267b44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataMachineReadableCodeObject](../avmetadatamachinereadablecodeobject.md)

# corners

<sub>Instance Property</sub>

The points defining the (x, 	y) locations of the corners.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly) NSArray<NSDictionary *> * corners;
```

## Discussion

The value of this property is an array of `CFDictionary` objects, each of which has been created from a `CGPoint` struct using the [dictionaryRepresentation](../../corefoundation/cgpoint/dictionaryrepresentation.md) function, representing the coordinates of the corners of the object with respect to the image in which it resides.

If the metadata originates from video, the points may be expressed as scalar values from `0` to `1`.

The points in the corners differ from the bounds rectangle in that bounds is axis aligned to orientation of the captured image, and the values of the corners reside within the bounds rectangle.

The points are arranged in counterclockwise order (clockwise if the code or image is mirrored), starting with the top left of the code in its canonical orientation.

## See Also

### Getting machine-readable code values

- [descriptor](descriptor.md) — A barcode description for use in Core Image.
- [stringValue](stringvalue.md) — Returns the error-corrected data decoded into a human-readable string.

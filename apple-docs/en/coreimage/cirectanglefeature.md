---
title: CIRectangleFeature
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirectanglefeature
source_url: 'https://developer.apple.com/documentation/coreimage/cirectanglefeature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirectanglefeature.json'
content_hash: 'sha256:f8b73c1885c078ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIRectangleFeature

<sub>Class</sub>

Information about a rectangular region detected in a still or video image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIRectangleFeature
```

## Overview

> [!note] Note
> In macOS 10.13, iOS 11, and tvOS 11 or later, the Vision framework replaces these classes for identifying and analyzing image features. See [VNDetectFaceRectanglesRequest](../vision/vndetectfacerectanglesrequest.md))

A detected rectangle feature is not necessarily rectangular in the plane of the image; rather, the feature identifies a shape that may be rectangular in space (for example a book on a desk) but which appears as a four-sided polygon in the image. The properties of a `CIRectangleFeature` object identify its four corners in image coordinates.

You can use rectangle feature detection together with the `CIPerspectiveCorrection` filter to transform the feature to a normal orientation.

To detect rectangles in an image or video, choose [CIDetectorTypeRectangle](cidetectortyperectangle.md) when initializing a [CIDetector](cidetector.md) object, and use the `CIDetectorAspectRatio` and `CIDetectorFocalLength` options to specify the approximate shape of rectangular features to search for. The detector returns at most one rectangle feature, the most prominent found in the image.

## Relationships

- **Inherits From**: [CIFeature](cifeature.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Locating a Detected Feature

- [bounds](cirectanglefeature/bounds-swift.property.md) — A rectangle indicating the position and extent of the feature in image coordinates.

### Identifying the Corners of a Detected Rectangle

- [bottomLeft](cirectanglefeature/bottomleft-swift.property.md) — The lower-left corner of the detected rectangle, in image coordinates.
- [bottomRight](cirectanglefeature/bottomright-swift.property.md) — The lower-right corner of the detected rectangle, in image coordinates.
- [topLeft](cirectanglefeature/topleft-swift.property.md) — The upper-left corner of the detected rectangle, in image coordinates.
- [topRight](cirectanglefeature/topright-swift.property.md) — The upper-right corner of the detected rectangle, in image coordinates.

## See Also

### Image Feature Detection

- [CIDetector](cidetector.md) — An image processor that identifies notable features, such as faces and barcodes, in a still image or video.
- [CIFeature](cifeature.md) — The abstract superclass for objects representing notable features detected in an image.
- [CIFaceFeature](cifacefeature.md) — Information about a face detected in a still or video image.
- [CITextFeature](citextfeature.md) — Information about a text that was detected in a still or video image.
- [CIQRCodeFeature](ciqrcodefeature.md) — Information about a Quick Response code detected in a still or video image.

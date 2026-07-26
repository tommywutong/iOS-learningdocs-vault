---
title: CITextFeature
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/citextfeature
source_url: 'https://developer.apple.com/documentation/coreimage/citextfeature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/citextfeature.json'
content_hash: 'sha256:2043add2742a4d5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CITextFeature

<sub>Class</sub>

Information about a text that was detected in a still or video image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CITextFeature
```

## Overview

> [!note] Note
> In macOS 10.13, iOS 11, and tvOS 11 or later, the Vision framework replaces these classes for identifying and analyzing image features. See [VNRecognizeTextRequest](../vision/vnrecognizetextrequest.md))

A detected text feature is not necessarily rectangular in the plane of the image; rather, the feature identifies a shape that may be rectangular in space (for example a text on a sign) but which appears as a four-sided polygon in the image. The properties of a `CITextFeature` object identify its four corners in image coordinates.

To detect text in an image or video, choose the [CIDetectorTypeText](cidetectortypetext.md) type when initializing a [CIDetector](cidetector.md) object, and use the `CIDetectorImageOrientation` option to specify the desired orientation for finding upright text.

## Relationships

- **Inherits From**: [CIFeature](cifeature.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Locating a Detected Feature

- [bounds](citextfeature/bounds.md) — A rectangle that indicates the position and extent of the text feature in image coordinates.

### Locating Features Within a Detected Region

- [subFeatures](citextfeature/subfeatures.md) — An array containing additional features detected within the feature.

### Identifying the Corners of a Detected Text Region

- [bottomLeft](citextfeature/bottomleft.md) — The image coordinate of the lower-left corner of the detected text.
- [bottomRight](citextfeature/bottomright.md) — The image coordinate of the lower-right corner of the detected text.
- [topLeft](citextfeature/topleft.md) — The image coordinate of the upper-left corner of the detected text.
- [topRight](citextfeature/topright.md) — The image coordinate of the upper-right corner of the detected text.

## See Also

### Image Feature Detection

- [CIDetector](cidetector.md) — An image processor that identifies notable features, such as faces and barcodes, in a still image or video.
- [CIFeature](cifeature.md) — The abstract superclass for objects representing notable features detected in an image.
- [CIFaceFeature](cifacefeature.md) — Information about a face detected in a still or video image.
- [CIRectangleFeature](cirectanglefeature.md) — Information about a rectangular region detected in a still or video image.
- [CIQRCodeFeature](ciqrcodefeature.md) — Information about a Quick Response code detected in a still or video image.

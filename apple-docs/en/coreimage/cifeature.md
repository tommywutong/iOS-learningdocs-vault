---
title: CIFeature
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifeature
source_url: 'https://developer.apple.com/documentation/coreimage/cifeature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifeature.json'
content_hash: 'sha256:da1c975460f4b2d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIFeature

<sub>Class</sub>

The abstract superclass for objects representing notable features detected in an image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIFeature
```

## Overview

> [!note] Note
> In macOS 10.13, iOS 11, and tvOS 11 or later, the Vision framework replaces these classes for identifying and analyzing image features. See [VNObservation](../vision/vnobservation.md))

A `CIFeature` object represents a portion of an image that a detector believes matches its criteria. Subclasses of CIFeature holds additional information specific to the detector that discovered the feature.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [CIFaceFeature](cifacefeature.md), [CIQRCodeFeature](ciqrcodefeature.md), [CIRectangleFeature](cirectanglefeature.md), [CITextFeature](citextfeature.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Feature Properties

- [bounds](cifeature/bounds.md) — The rectangle that holds discovered feature.
- [type](cifeature/type.md) — The type of feature that was discovered.

### Feature Types

- [CIFeatureTypeFace](cifeaturetypeface.md) — A Core Image feature type for person’s face.
- [CIFeatureTypeRectangle](cifeaturetyperectangle.md) — A Core Image feature type for rectangular object.
- [CIFeatureTypeQRCode](cifeaturetypeqrcode.md) — A Core Image feature type for QR code object.
- [CIFeatureTypeText](cifeaturetypetext.md) — A Core Image feature type for text.

## See Also

### Image Feature Detection

- [CIDetector](cidetector.md) — An image processor that identifies notable features, such as faces and barcodes, in a still image or video.
- [CIFaceFeature](cifacefeature.md) — Information about a face detected in a still or video image.
- [CIRectangleFeature](cirectanglefeature.md) — Information about a rectangular region detected in a still or video image.
- [CITextFeature](citextfeature.md) — Information about a text that was detected in a still or video image.
- [CIQRCodeFeature](ciqrcodefeature.md) — Information about a Quick Response code detected in a still or video image.

---
title: CIDetector
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidetector
source_url: 'https://developer.apple.com/documentation/coreimage/cidetector'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidetector.json'
content_hash: 'sha256:d316d26b0df2d8d5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIDetector

<sub>Class</sub>

An image processor that identifies notable features, such as faces and barcodes, in a still image or video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIDetector
```

## Overview

> [!note] Note
> In macOS 10.13, iOS 11, and tvOS 11 or later, the [Vision](../vision.md) framework replaces these classes for identifying and analyzing image features. See [VNRequest](../vision/vnrequest.md).

A `CIDetector` object uses image processing to search for and identify notable features (faces, rectangles, and barcodes) in a still image or video. Detected features are represented by [CIFeature](cifeature.md) objects that provide more information about each feature.

This class can maintain many state variables that can impact performance. So for best performance, reuse `CIDetector` instances instead of creating new ones.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Detector Object

- [+ detectorOfType:context:options:](<cidetector/init(oftype_context_options_).md>) — Creates and returns a configured detector.

### Using a Detector Object to Find Features

- [- featuresInImage:](<cidetector/features(in_).md>) — Searches for features in an image.
- [- featuresInImage:options:](<cidetector/features(in_options_).md>) — Searches for features in an image based on the specified image orientation.

### Constants

- [Detector Types](detector-types.md) — Strings used to declare the detector for which you are interested.
- [Detector Configuration Keys](detector-configuration-keys.md) — Keys used in the options dictionary to configure a detector.
- [Detector Accuracy Options](detector-accuracy-options.md) — Value options used to specify the desired accuracy of the detector.
- [Feature Detection Keys](feature-detection-keys.md) — Keys used in the options dictionary for [- featuresInImage:options:](<cidetector/features(in_options_).md>).

## See Also

### Image Feature Detection

- [CIFeature](cifeature.md) — The abstract superclass for objects representing notable features detected in an image.
- [CIFaceFeature](cifacefeature.md) — Information about a face detected in a still or video image.
- [CIRectangleFeature](cirectanglefeature.md) — Information about a rectangular region detected in a still or video image.
- [CITextFeature](citextfeature.md) — Information about a text that was detected in a still or video image.
- [CIQRCodeFeature](ciqrcodefeature.md) — Information about a Quick Response code detected in a still or video image.

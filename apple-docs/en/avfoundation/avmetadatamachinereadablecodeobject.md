---
title: AVMetadataMachineReadableCodeObject
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadatamachinereadablecodeobject
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadatamachinereadablecodeobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadatamachinereadablecodeobject.json'
content_hash: 'sha256:98e4ba35bae98637'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetadataMachineReadableCodeObject

<sub>Class</sub>

Barcode information detected by a metadata capture output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVMetadataMachineReadableCodeObject
```

## Overview

The `AVMetadataMachineReadableCodeObject` class is a concrete subclass of [AVMetadataObject](avmetadataobject.md) defining the features of a detected one-dimensional or two-dimensional barcode.

An `AVMetadataMachineReadableCodeObject` instance represents a single detected machine readable code in an image.  It’s an immutable object describing the features and payload of a barcode.

On supported platforms, the [AVCaptureMetadataOutput](avcapturemetadataoutput.md) class outputs arrays of detected machine readable code objects.

## Relationships

- **Inherits From**: [AVMetadataObject](avmetadataobject.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting machine-readable code values

- [corners](avmetadatamachinereadablecodeobject/corners-58qbe.md) — A Swift array of corner points.
- [descriptor](avmetadatamachinereadablecodeobject/descriptor.md) — A barcode description for use in Core Image.
- [stringValue](avmetadatamachinereadablecodeobject/stringvalue.md) — Returns the error-corrected data decoded into a human-readable string.

### Constants

- [Machine-readable object types](machine-readable-object-types.md) — Constants used to specify the type of barcode to scan.

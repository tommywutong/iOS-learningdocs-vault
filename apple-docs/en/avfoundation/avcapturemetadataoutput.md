---
title: AVCaptureMetadataOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemetadataoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemetadataoutput.json'
content_hash: 'sha256:68ae1aae3b6b351d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureMetadataOutput

<sub>Class</sub>

A capture output for processing timed metadata produced by a capture session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCaptureMetadataOutput
```

## Overview

An `AVCaptureMetadataOutput` object intercepts metadata objects emitted by its associated capture connection and forwards them to a delegate object for processing. You can use instances of this class to process specific types of metadata included with the input data. You use this class the way you do other output objects, typically by adding it as an output to an [AVCaptureSession](avcapturesession.md) object.

## Relationships

- **Inherits From**: [AVCaptureOutput](avcaptureoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating metadata output

- [- init](<avcapturemetadataoutput/init().md>) — Creates a new capture metadata output.

### Configuring metadata capture

- [availableMetadataObjectTypes](avcapturemetadataoutput/availablemetadataobjecttypes.md) — An array of strings identifying the types of metadata objects that can be captured.
- [metadataObjectTypes](avcapturemetadataoutput/metadataobjecttypes.md) — An array of strings identifying the types of metadata objects  to process.
- [rectOfInterest](avcapturemetadataoutput/rectofinterest.md) — A rectangle of interest for limiting the search area for visual metadata.
- [requiredMetadataObjectTypesForCinematicVideoCapture](avcapturemetadataoutput/requiredmetadataobjecttypesforcinematicvideocapture.md) — The required metadata object types when Cinematic Video capture is enabled.

### Receiving captured metadata objects

- [- setMetadataObjectsDelegate:queue:](<avcapturemetadataoutput/setmetadataobjectsdelegate(__queue_).md>) — Sets the delegate and dispatch queue to use handle callbacks.
- [metadataObjectsDelegate](avcapturemetadataoutput/metadataobjectsdelegate.md) — The delegate of the capture metadata output object.
- [metadataObjectsCallbackQueue](avcapturemetadataoutput/metadataobjectscallbackqueue.md) — The dispatch queue on which to execute the delegate’s methods.
- [AVCaptureMetadataOutputObjectsDelegate](avcapturemetadataoutputobjectsdelegate.md) — Methods for receiving metadata produced by a metadata capture output.

## See Also

### Metadata capture

- [AVCaptureMetadataInput](avcapturemetadatainput.md) — A capture input for providing timed metadata to a capture session.
- [AVMetadataObject](avmetadataobject.md) — The abstract superclass for objects provided by a metadata capture output.
- [Metadata types](metadata-types.md) — Inspect the supported metadata object types that the framework supports.

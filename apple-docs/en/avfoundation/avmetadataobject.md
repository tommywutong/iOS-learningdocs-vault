---
title: AVMetadataObject
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.10+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadataobject
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadataobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadataobject.json'
content_hash: 'sha256:30e03b04474a9806'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetadataObject

<sub>Class</sub>

The abstract superclass for objects provided by a metadata capture output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVMetadataObject
```

## Overview

The `AVMetadataObject` class is an abstract class that defines the basic properties associated with a piece of metadata. These attributes reflect information either about the metadata itself or the media from which the metadata originated. Subclasses are responsible for providing appropriate values for each of the relevant properties.

You shouldn’t subclass `AVMetadataObject` directly. Instead, you use one of the defined subclasses provided by the AVFoundation framework. Similarly, you don’t create instances of this class yourself but use an [AVCaptureMetadataOutput](avcapturemetadataoutput.md) object to retrieve them from the captured data.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVMetadataBodyObject](avmetadatabodyobject.md), [AVMetadataCatHeadObject](avmetadatacatheadobject.md), [AVMetadataDogHeadObject](avmetadatadogheadobject.md), [AVMetadataFaceObject](avmetadatafaceobject.md), [AVMetadataMachineReadableCodeObject](avmetadatamachinereadablecodeobject.md), [AVMetadataSalientObject](avmetadatasalientobject.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting the metadata

- [bounds](avmetadataobject/bounds.md) — The bounding rectangle associated with the metadata.
- [duration](avmetadataobject/duration.md) — The duration of the media associated with this metadata object.
- [time](avmetadataobject/time.md) — The media time value associated with the metadata object.
- [type](avmetadataobject/type.md) — The type of metadata that this object provides.
- [ObjectType](avmetadataobject/objecttype.md) — Constants that identify metadata object types.
- [fixedFocus](avmetadataobject/isfixedfocus.md) — A BOOL indicating whether this metadata object represents a fixed focus.
- [cinematicVideoFocusMode](avmetadataobject/cinematicvideofocusmode.md) — The current focus mode when an object is detected during a Cinematic Video recording.
- [groupID](avmetadataobject/groupid.md) — An identifier associated with a metadata object used to group it with other metadata objects belonging to a common parent.
- [objectID](avmetadataobject/objectid.md) — A unique identifier for each detected object type (face, body, hands, heads and salient objects) in a collection.

## See Also

### Metadata capture

- [AVCaptureMetadataInput](avcapturemetadatainput.md) — A capture input for providing timed metadata to a capture session.
- [AVCaptureMetadataOutput](avcapturemetadataoutput.md) — A capture output for processing timed metadata produced by a capture session.
- [Metadata types](metadata-types.md) — Inspect the supported metadata object types that the framework supports.

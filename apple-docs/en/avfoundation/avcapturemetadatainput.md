---
title: AVCaptureMetadataInput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemetadatainput
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemetadatainput.json'
content_hash: 'sha256:82053237e7207e53'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureMetadataInput

<sub>Class</sub>

A capture input for providing timed metadata to a capture session.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class AVCaptureMetadataInput
```

## Overview

This class provides input to an [AVCaptureSession](avcapturesession.md). An instance of [AVCaptureMetadataInput](avcapturemetadatainput.md) can present one and only one [Port](avcaptureinput/port.md) connected to an [AVCaptureMovieFileOutput](avcapturemoviefileoutput.md). Provide metadata through the input port by conforming to a [CMFormatDescription](../coremedia/cmformatdescription.md) and supplying [AVMetadataItem](avmetadataitem.md) objects in an [AVTimedMetadataGroup](avtimedmetadatagroup.md).

## Relationships

- **Inherits From**: [AVCaptureInput](avcaptureinput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating metadata input

- [- initWithFormatDescription:clock:](<avcapturemetadatainput/init(formatdescription_clock_).md>) — Creates capture metadata input to provide timed groups to a capture session.

### Providing metadata

- [- appendTimedMetadataGroup:error:](<avcapturemetadatainput/append(__).md>) — Provides metadata to the capture session.

## See Also

### Metadata capture

- [AVCaptureMetadataOutput](avcapturemetadataoutput.md) — A capture output for processing timed metadata produced by a capture session.
- [AVMetadataObject](avmetadataobject.md) — The abstract superclass for objects provided by a metadata capture output.
- [Metadata types](metadata-types.md) — Inspect the supported metadata object types that the framework supports.

---
title: 'metadataInputWithFormatDescription:clock:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturemetadatainput/metadatainputwithformatdescription:clock:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput/metadatainputwithformatdescription:clock:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemetadatainput/metadatainputwithformatdescription%3Aclock%3A.json'
content_hash: 'sha256:f9e60c02de56be95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMetadataInput](../avcapturemetadatainput.md)

# metadataInputWithFormatDescription:clock:

<sub>Type Method</sub>

Returns a metadata input instance that allows clients to provide timed metadata groups to a capture session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) metadataInputWithFormatDescription:(CMMetadataFormatDescriptionRef) desc clock:(CMClockRef) clock;
```

## Parameters

- `desc` — A [CMFormatDescription](../../coremedia/cmformatdescription.md) that defines the metadata to be supplied by the client. Throws [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) if `NULL` is passed.

- `clock` — A [CMClock](../../coremedia/cmclock.md) that provides the timebase for the supplied samples. Throws [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) if `NULL` is passed.

## See Also

### Creating metadata input

- [- initWithFormatDescription:clock:](<init(formatdescription_clock_).md>) — Creates capture metadata input to provide timed groups to a capture session.

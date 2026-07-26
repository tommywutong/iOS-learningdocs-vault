---
title: 'init(formatDescription:clock:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturemetadatainput/init(formatdescription:clock:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput/init(formatdescription:clock:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemetadatainput/init%28formatdescription%3Aclock%3A%29.json'
content_hash: 'sha256:39107afcfaf90a71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMetadataInput](../avcapturemetadatainput.md)

# init(formatDescription:clock:)

<sub>Initializer</sub>

Creates capture metadata input to provide timed groups to a capture session.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
init(formatDescription desc: CMMetadataFormatDescription, clock: CMClock)
```

## Parameters

- `desc` — A [CMFormatDescription](../../coremedia/cmformatdescription.md) that defines the metadata to be supplied by the client. Throws [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) if `NULL` is passed.

- `clock` — A [CMClock](../../coremedia/cmclock.md) that provides the timebase for the supplied samples. Throws [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) if `NULL` is passed.

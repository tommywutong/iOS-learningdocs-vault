---
title: metadataObjects
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesynchronizedmetadataobjectdata/metadataobjects
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesynchronizedmetadataobjectdata/metadataobjects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesynchronizedmetadataobjectdata/metadataobjects.json'
content_hash: 'sha256:21dbee4d5802def3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSynchronizedMetadataObjectData](../avcapturesynchronizedmetadataobjectdata.md)

# metadataObjects

<sub>Instance Property</sub>

The list of metadata objects captured at this synchronization timestamp.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var metadataObjects: [AVMetadataObject] { get }
```

## Discussion

> [!note] Note
> Because [AVMetadataObject](../avmetadataobject.md) is an abstract class, the objects in this array are always instances of a concrete subclass.

This array is equivalent to that provided by the [- captureOutput:didOutputMetadataObjects:fromConnection:](<../avcapturemetadataoutputobjectsdelegate/metadataoutput(__didoutput_from_).md>) delegate method when using a metadata capture output without a data output synchronizer.

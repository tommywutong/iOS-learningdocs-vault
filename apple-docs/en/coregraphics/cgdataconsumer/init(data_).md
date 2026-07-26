---
title: 'init(data:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgdataconsumer/init(data:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataconsumer/init(data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataconsumer/init%28data%3A%29.json'
content_hash: 'sha256:0351f179ea0e8c2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDataConsumer](../cgdataconsumer.md)

# init(data:)

<sub>Initializer</sub>

Creates a data consumer that writes to a CFData object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(data: CFMutableData)
```

## Parameters

- `data` — The CFData object to write to.

## Return Value

A new data consumer object. In Objective-C, you’re responsible for releasing this object using [CGDataConsumerRelease](../cgdataconsumerrelease.md).

## Discussion

You can use this function when you need to represent Core Graphics data as a [CFData](../../corefoundation/cfdata.md) type. For example, you might create a [CFData](../../corefoundation/cfdata.md) object that you then copy to the pasteboard.

## See Also

### Creating Data Consumers

- [CGDataConsumerCreate](<init(info_cbks_).md>) — Creates a data consumer that uses callback functions to write data.
- [CGDataConsumerCreateWithURL](<init(url_).md>) — Creates a data consumer that writes data to a location specified by a URL.
- [CGDataConsumerCallbacks](../cgdataconsumercallbacks.md) — A structure that contains pointers to callback functions that manage the copying of data for a data consumer.
- [CGDataConsumerPutBytesCallback](../cgdataconsumerputbytescallback.md) — Copies data from a Core Graphics-supplied buffer into a data consumer.
- [CGDataConsumerReleaseInfoCallback](../cgdataconsumerreleaseinfocallback.md) — Releases any private data or resources associated with the data consumer.

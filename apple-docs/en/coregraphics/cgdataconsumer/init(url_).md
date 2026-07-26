---
title: 'init(url:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgdataconsumer/init(url:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataconsumer/init(url:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataconsumer/init%28url%3A%29.json'
content_hash: 'sha256:8efd5f87b56bd779'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDataConsumer](../cgdataconsumer.md)

# init(url:)

<sub>Initializer</sub>

Creates a data consumer that writes data to a location specified by a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(url: CFURL)
```

## Parameters

- `url` — A CFURL object that specifies the data destination.

## Return Value

A new data consumer object. In Objective-C, you’re responsible for releasing this object using [CGDataConsumerRelease](../cgdataconsumerrelease.md).

## See Also

### Creating Data Consumers

- [CGDataConsumerCreate](<init(info_cbks_).md>) — Creates a data consumer that uses callback functions to write data.
- [CGDataConsumerCreateWithCFData](<init(data_).md>) — Creates a data consumer that writes to a CFData object.
- [CGDataConsumerCallbacks](../cgdataconsumercallbacks.md) — A structure that contains pointers to callback functions that manage the copying of data for a data consumer.
- [CGDataConsumerPutBytesCallback](../cgdataconsumerputbytescallback.md) — Copies data from a Core Graphics-supplied buffer into a data consumer.
- [CGDataConsumerReleaseInfoCallback](../cgdataconsumerreleaseinfocallback.md) — Releases any private data or resources associated with the data consumer.

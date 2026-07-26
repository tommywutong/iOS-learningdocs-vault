---
title: 'init(info:cbks:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgdataconsumer/init(info:cbks:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataconsumer/init(info:cbks:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataconsumer/init%28info%3Acbks%3A%29.json'
content_hash: 'sha256:49ce16e0705c742f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDataConsumer](../cgdataconsumer.md)

# init(info:cbks:)

<sub>Initializer</sub>

Creates a data consumer that uses callback functions to write data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(info: UnsafeMutableRawPointer?, cbks: UnsafePointer<CGDataConsumerCallbacks>)
```

## Parameters

- `info` — A pointer to data of any type or `NULL`. When the callback is called, Core Graphics passes this pointer as the `info` parameter.

- `cbks` — A pointer to a structure that specifies the callback functions you implement to copy data sent to the consumer and to handle the consumer’s basic memory management. For a complete description, see [CGDataConsumerCallbacks](../cgdataconsumercallbacks.md).

## Return Value

A new data consumer object. In Objective-C, you’re responsible for releasing this object using [CGDataConsumerRelease](../cgdataconsumerrelease.md).

## See Also

### Creating Data Consumers

- [CGDataConsumerCreateWithURL](<init(url_).md>) — Creates a data consumer that writes data to a location specified by a URL.
- [CGDataConsumerCreateWithCFData](<init(data_).md>) — Creates a data consumer that writes to a CFData object.
- [CGDataConsumerCallbacks](../cgdataconsumercallbacks.md) — A structure that contains pointers to callback functions that manage the copying of data for a data consumer.
- [CGDataConsumerPutBytesCallback](../cgdataconsumerputbytescallback.md) — Copies data from a Core Graphics-supplied buffer into a data consumer.
- [CGDataConsumerReleaseInfoCallback](../cgdataconsumerreleaseinfocallback.md) — Releases any private data or resources associated with the data consumer.

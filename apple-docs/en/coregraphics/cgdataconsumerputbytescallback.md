---
title: CGDataConsumerPutBytesCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataconsumerputbytescallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataconsumerputbytescallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataconsumerputbytescallback.json'
content_hash: 'sha256:5f7396c4c5ba1820'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDataConsumerPutBytesCallback

<sub>Type Alias</sub>

Copies data from a Core Graphics-supplied buffer into a data consumer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGDataConsumerPutBytesCallback = (UnsafeMutableRawPointer?, UnsafeRawPointer, Int) -> Int
```

## Parameters

- `info` — A generic pointer to private data shared among your callback functions. This is the pointer supplied to [CGDataConsumerCreate](<cgdataconsumer/init(info_cbks_).md>).

- `buffer` — The buffer from which you copy the specified number of bytes.

- `count` — The number of bytes to copy.

## Return Value

The number of bytes copied. If no more data can be written to the consumer, you should return `0`.

## Discussion

When Core Graphics is ready to send data to the consumer, your function is called. It should copy the specified number of bytes from `buffer` into some resource under your control—for example, a file.

For information on how to associate your callback function with a data consumer, see [CGDataConsumerCreate](<cgdataconsumer/init(info_cbks_).md>) and [CGDataConsumerCallbacks](cgdataconsumercallbacks.md).

## See Also

### Creating Data Consumers

- [CGDataConsumerCreate](<cgdataconsumer/init(info_cbks_).md>) — Creates a data consumer that uses callback functions to write data.
- [CGDataConsumerCreateWithURL](<cgdataconsumer/init(url_).md>) — Creates a data consumer that writes data to a location specified by a URL.
- [CGDataConsumerCreateWithCFData](<cgdataconsumer/init(data_).md>) — Creates a data consumer that writes to a CFData object.
- [CGDataConsumerCallbacks](cgdataconsumercallbacks.md) — A structure that contains pointers to callback functions that manage the copying of data for a data consumer.
- [CGDataConsumerReleaseInfoCallback](cgdataconsumerreleaseinfocallback.md) — Releases any private data or resources associated with the data consumer.

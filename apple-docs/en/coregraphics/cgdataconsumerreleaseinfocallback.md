---
title: CGDataConsumerReleaseInfoCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdataconsumerreleaseinfocallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdataconsumerreleaseinfocallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdataconsumerreleaseinfocallback.json'
content_hash: 'sha256:614c52d23a788f94'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDataConsumerReleaseInfoCallback

<sub>Type Alias</sub>

Releases any private data or resources associated with the data consumer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGDataConsumerReleaseInfoCallback = (UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `info` — A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [CGDataConsumerCreate](<cgdataconsumer/init(info_cbks_).md>).

## Discussion

When Core Graphics frees a data consumer that has an associated release function, the release function is called.

For information on how to associate your callback function with a data consumer, see [CGDataConsumerCreate](<cgdataconsumer/init(info_cbks_).md>) and [CGDataConsumerCallbacks](cgdataconsumercallbacks.md).

## See Also

### Creating Data Consumers

- [CGDataConsumerCreate](<cgdataconsumer/init(info_cbks_).md>) — Creates a data consumer that uses callback functions to write data.
- [CGDataConsumerCreateWithURL](<cgdataconsumer/init(url_).md>) — Creates a data consumer that writes data to a location specified by a URL.
- [CGDataConsumerCreateWithCFData](<cgdataconsumer/init(data_).md>) — Creates a data consumer that writes to a CFData object.
- [CGDataConsumerCallbacks](cgdataconsumercallbacks.md) — A structure that contains pointers to callback functions that manage the copying of data for a data consumer.
- [CGDataConsumerPutBytesCallback](cgdataconsumerputbytescallback.md) — Copies data from a Core Graphics-supplied buffer into a data consumer.

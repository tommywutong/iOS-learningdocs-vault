---
title: 'stream(_:handle:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/streamdelegate/stream(_:handle:)'
source_url: 'https://developer.apple.com/documentation/foundation/streamdelegate/stream(_:handle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/streamdelegate/stream%28_%3Ahandle%3A%29.json'
content_hash: 'sha256:0dfb6cbcfd03697d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [StreamDelegate](../streamdelegate.md)

# stream(_:handle:)

<sub>Instance Method</sub>

The delegate receives this message when a given event has occurred on a given stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func stream(_ aStream: Stream, handle eventCode: Stream.Event)
```

## Parameters

- `aStream` — The stream on which `streamEvent` occurred.

- `eventCode` — The stream event that occurred.

## Discussion

The delegate receives this message only if `theStream` is scheduled on a run loop. The message is sent on the stream object’s thread. The delegate should examine `streamEvent` to determine the appropriate action it should take.

## See Also

### Related Documentation

- [Stream Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Streams.html#//apple_ref/doc/uid/10000188i)

---
title: 'getStreamsTo(_:port:inputStream:outputStream:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.3+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/stream/getstreamsto(_:port:inputstream:outputstream:)'
source_url: 'https://developer.apple.com/documentation/foundation/stream/getstreamsto(_:port:inputstream:outputstream:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/getstreamsto%28_%3Aport%3Ainputstream%3Aoutputstream%3A%29.json'
content_hash: 'sha256:29b34603e61785fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Stream](../stream.md)

# getStreamsTo(_:port:inputStream:outputStream:)

<sub>Type Method</sub>

Creates and returns by reference an `NSInputStream` object and `NSOutputStream` object for a socket connection with a given host on a given port.

> [!warning] Deprecated
> Use nw_connection_t in Network framework instead

<sub>macOS</sub>

```swift
class func getStreamsTo(_ host: Host, port: Int, inputStream: AutoreleasingUnsafeMutablePointer<InputStream?>?, outputStream: AutoreleasingUnsafeMutablePointer<OutputStream?>?)
```

## Parameters

- `host` — The host to which to connect.

- `port` — The port to connect to on `host`.

- `inputStream` — Upon return, contains the input stream. If `nil` is passed, the stream object is not created.

- `outputStream` — Upon return, contains the output stream. If `nil` is passed, the stream object is not created.

## Discussion

If neither `port` nor `host` is properly specified, no socket connection is made.

## See Also

### Related Documentation

- [Stream Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Streams.html#//apple_ref/doc/uid/10000188i)

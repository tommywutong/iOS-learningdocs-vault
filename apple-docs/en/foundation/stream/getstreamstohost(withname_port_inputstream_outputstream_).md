---
title: 'getStreamsToHost(withName:port:inputStream:outputStream:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/stream/getstreamstohost(withname:port:inputstream:outputstream:)'
source_url: 'https://developer.apple.com/documentation/foundation/stream/getstreamstohost(withname:port:inputstream:outputstream:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/getstreamstohost%28withname%3Aport%3Ainputstream%3Aoutputstream%3A%29.json'
content_hash: 'sha256:ed1eff1d5a8eefa0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Stream](../stream.md)

# getStreamsToHost(withName:port:inputStream:outputStream:)

<sub>Type Method</sub>

Creates and returns by reference an `NSInputStream` object and `NSOutputStream` object for a socket connection with a given host on a given port.

> [!warning] Deprecated
> Use nw_connection_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func getStreamsToHost(withName hostname: String, port: Int, inputStream: AutoreleasingUnsafeMutablePointer<InputStream?>?, outputStream: AutoreleasingUnsafeMutablePointer<OutputStream?>?)
```

## Parameters

- `hostname` — The host to which to connect.

- `port` — The port to connect to on `host`.

- `inputStream` — Upon return, contains the input stream. If `nil` is passed, the stream object is not created.

- `outputStream` — Upon return, contains the output stream. If `nil` is passed, the stream object is not created.

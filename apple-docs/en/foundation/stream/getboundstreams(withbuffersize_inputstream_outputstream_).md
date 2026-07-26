---
title: 'getBoundStreams(withBufferSize:inputStream:outputStream:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/stream/getboundstreams(withbuffersize:inputstream:outputstream:)'
source_url: 'https://developer.apple.com/documentation/foundation/stream/getboundstreams(withbuffersize:inputstream:outputstream:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/getboundstreams%28withbuffersize%3Ainputstream%3Aoutputstream%3A%29.json'
content_hash: 'sha256:3f1d276c9bc1fc10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Stream](../stream.md)

# getBoundStreams(withBufferSize:inputStream:outputStream:)

<sub>Type Method</sub>

Creates and returns by reference a bound pair of input and output streams.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func getBoundStreams(withBufferSize bufferSize: Int, inputStream: AutoreleasingUnsafeMutablePointer<InputStream?>?, outputStream: AutoreleasingUnsafeMutablePointer<OutputStream?>?)
```

## Parameters

- `bufferSize` — The size of the buffer, in bytes, used to transfer data from `inputStream` to `outputStream`.

- `inputStream` — On return, contains an input stream.

- `outputStream` — On return, contains an output stream.

## Discussion

The created streams are bound to one another, such that any data written to `outputStream` is received by `inputStream`.

This is a convenience method for calling [CFStreamCreateBoundPair(_:_:_:_:)](<../../corefoundation/cfstreamcreateboundpair(________).md>) and bridging from the returned Core Foundation types.

## See Also

### Related Documentation

- [CFStreamCreateBoundPair(_:_:_:_:)](<../../corefoundation/cfstreamcreateboundpair(________).md>) — Creates a bound pair of read and write streams.

---
title: 'CFStreamCreateBoundPair(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstreamcreateboundpair(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreamcreateboundpair(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreamcreateboundpair%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4cff62ae69d96ecf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStreamCreateBoundPair(_:_:_:_:)

<sub>Function</sub>

Creates a bound pair of read and write streams.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStreamCreateBoundPair(_ alloc: CFAllocator!, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!, _ transferBufferSize: CFIndex)
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new objects. Pass [kCFAllocatorDefault](kcfallocatordefault.md) or `NULL` to use the current default allocator.

- `readStream` — On return, contains a readable stream. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

- `writeStream` — On return, contains a writable stream. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

- `transferBufferSize` — The size of the buffer, in bytes, used to transfer data from `readStream` to `writeStream`.

## Discussion

The created streams are bound to one another, such that any data written to `writeStream` is received by `readStream`.

## See Also

### Related Documentation

- [getBoundStreams(withBufferSize:inputStream:outputStream:)](<../foundation/stream/getboundstreams(withbuffersize_inputstream_outputstream_).md>) — Creates and returns by reference a bound pair of input and output streams.

### Creating Streams

- [CFStreamCreatePairWithPeerSocketSignature](<cfstreamcreatepairwithpeersocketsignature(________).md>) — Creates readable and writable streams connected to a socket. _(deprecated)_
- [CFStreamCreatePairWithSocketToHost](<cfstreamcreatepairwithsockettohost(__________).md>) — Creates readable and writable streams connected to a TCP/IP port of a particular host. _(deprecated)_
- [CFStreamCreatePairWithSocket](<cfstreamcreatepairwithsocket(________).md>) — Creates readable and writable streams connected to a socket. _(deprecated)_
- [CFStreamCreatePairWithSocketToCFHost(_:_:_:_:_:)](<../cfnetwork/cfstreamcreatepairwithsockettocfhost(__________).md>) — Creates readable and writable streams connected to a given `CFHost` object. _(deprecated)_
- [CFStreamCreatePairWithSocketToNetService(_:_:_:_:)](<../cfnetwork/cfstreamcreatepairwithsockettonetservice(________).md>) — Creates a pair of streams for a CFNetService. _(deprecated)_

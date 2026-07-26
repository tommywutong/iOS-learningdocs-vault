---
title: 'CFStreamCreatePairWithPeerSocketSignature(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfstreamcreatepairwithpeersocketsignature(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreamcreatepairwithpeersocketsignature(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreamcreatepairwithpeersocketsignature%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d99b88eb02c90be1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStreamCreatePairWithPeerSocketSignature(_:_:_:_:)

<sub>Function</sub>

Creates readable and writable streams connected to a socket.

> [!warning] Deprecated
> Use nw_connection_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStreamCreatePairWithPeerSocketSignature(_ alloc: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>!, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new objects. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `signature` — A [CFSocketSignature](cfsocketsignature.md) structure identifying the communication protocol and address to which the socket streams should connect.

- `readStream` — On return, a readable stream connected to the socket address in `signature`. If you pass `NULL`, this function will not create a readable stream. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

- `writeStream` — On return, a writable stream connected to the socket address in `signature`. If you pass `NULL`, this function will not create a writable stream. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The streams do not create a socket or connect to the remote host until you open one of the streams.

Most properties are shared by both streams. Setting a shared property for one stream automatically sets the property for the other.

## See Also

### Creating Streams

- [CFStreamCreatePairWithSocketToHost](<cfstreamcreatepairwithsockettohost(__________).md>) — Creates readable and writable streams connected to a TCP/IP port of a particular host. _(deprecated)_
- [CFStreamCreatePairWithSocket](<cfstreamcreatepairwithsocket(________).md>) — Creates readable and writable streams connected to a socket. _(deprecated)_
- [CFStreamCreateBoundPair](<cfstreamcreateboundpair(________).md>) — Creates a bound pair of read and write streams.
- [CFStreamCreatePairWithSocketToCFHost(_:_:_:_:_:)](<../cfnetwork/cfstreamcreatepairwithsockettocfhost(__________).md>) — Creates readable and writable streams connected to a given `CFHost` object. _(deprecated)_
- [CFStreamCreatePairWithSocketToNetService(_:_:_:_:)](<../cfnetwork/cfstreamcreatepairwithsockettonetservice(________).md>) — Creates a pair of streams for a CFNetService. _(deprecated)_

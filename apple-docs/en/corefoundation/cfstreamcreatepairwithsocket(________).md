---
title: 'CFStreamCreatePairWithSocket(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfstreamcreatepairwithsocket(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreamcreatepairwithsocket(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreamcreatepairwithsocket%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:28772c33988f6dfe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStreamCreatePairWithSocket(_:_:_:_:)

<sub>Function</sub>

Creates readable and writable streams connected to a socket.

> [!warning] Deprecated
> Use nw_connection_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStreamCreatePairWithSocket(_ alloc: CFAllocator!, _ sock: CFSocketNativeHandle, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new objects. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `sock` — The pre-existing (and already connected) socket which the socket streams should use. > [!important] Important > By default, your app is responsible for closing this socket after you close both streams. If you want CFNetwork to take ownership of the socket, set the [kCFStreamPropertyShouldCloseNativeSocket](kcfstreampropertyshouldclosenativesocket.md) property of the stream to [kCFBooleanTrue](kcfbooleantrue.md).

- `readStream` — Upon return, a readable stream connected to the socket address in `signature`. If you pass `NULL`, this function will not create a readable stream. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

- `writeStream` — Upon return, a writable stream connected to the socket address in `signature`. If you pass `NULL`, this function will not create a writable stream. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Most properties are shared by both streams. Setting a shared property for one stream automatically sets the property for the other.

## See Also

### Creating Streams

- [CFStreamCreatePairWithPeerSocketSignature](<cfstreamcreatepairwithpeersocketsignature(________).md>) — Creates readable and writable streams connected to a socket. _(deprecated)_
- [CFStreamCreatePairWithSocketToHost](<cfstreamcreatepairwithsockettohost(__________).md>) — Creates readable and writable streams connected to a TCP/IP port of a particular host. _(deprecated)_
- [CFStreamCreateBoundPair](<cfstreamcreateboundpair(________).md>) — Creates a bound pair of read and write streams.
- [CFStreamCreatePairWithSocketToCFHost(_:_:_:_:_:)](<../cfnetwork/cfstreamcreatepairwithsockettocfhost(__________).md>) — Creates readable and writable streams connected to a given `CFHost` object. _(deprecated)_
- [CFStreamCreatePairWithSocketToNetService(_:_:_:_:)](<../cfnetwork/cfstreamcreatepairwithsockettonetservice(________).md>) — Creates a pair of streams for a CFNetService. _(deprecated)_

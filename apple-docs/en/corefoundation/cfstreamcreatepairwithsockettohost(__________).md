---
title: 'CFStreamCreatePairWithSocketToHost(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfstreamcreatepairwithsockettohost(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreamcreatepairwithsockettohost(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreamcreatepairwithsockettohost%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0438f733d900b903'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStreamCreatePairWithSocketToHost(_:_:_:_:_:)

<sub>Function</sub>

Creates readable and writable streams connected to a TCP/IP port of a particular host.

> [!warning] Deprecated
> Use nw_connection_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStreamCreatePairWithSocketToHost(_ alloc: CFAllocator!, _ host: CFString!, _ port: UInt32, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the `CFReadStream` and `CFWriteStream` objects. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `host` — The hostname to which the socket streams should connect. The host can be specified using an IPv4 or IPv6 address or a fully qualified DNS hostname.

- `port` — The TCP port number to which the socket streams should connect.

- `readStream` — Upon return, a readable stream connected to the socket address in `port`. If you pass `NULL`, this function will not create a readable stream. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

- `writeStream` — Upon return, a writable stream connected to the socket address in `port`. If you pass `NULL`, this function will not create a writable stream. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The streams do not create a socket, resolve the hostname, or connect to the remote host until you open one of the streams.

Most properties are shared by both streams. Setting a shared property for one stream automatically sets the property for the other.

## See Also

### Creating Streams

- [CFStreamCreatePairWithPeerSocketSignature](<cfstreamcreatepairwithpeersocketsignature(________).md>) — Creates readable and writable streams connected to a socket. _(deprecated)_
- [CFStreamCreatePairWithSocket](<cfstreamcreatepairwithsocket(________).md>) — Creates readable and writable streams connected to a socket. _(deprecated)_
- [CFStreamCreateBoundPair](<cfstreamcreateboundpair(________).md>) — Creates a bound pair of read and write streams.
- [CFStreamCreatePairWithSocketToCFHost(_:_:_:_:_:)](<../cfnetwork/cfstreamcreatepairwithsockettocfhost(__________).md>) — Creates readable and writable streams connected to a given `CFHost` object. _(deprecated)_
- [CFStreamCreatePairWithSocketToNetService(_:_:_:_:)](<../cfnetwork/cfstreamcreatepairwithsockettonetservice(________).md>) — Creates a pair of streams for a CFNetService. _(deprecated)_

---
title: CFStream
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstream
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstream.json'
content_hash: 'sha256:6d9aaa2cced797b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStream

<sub>API Collection</sub>

## Overview

This document describes the generic `CFStream` functions, data types, and constants. See also [CFReadStream](cfreadstream.md) and [CFWriteStream](cfwritestream.md) for functions and constants specific to read and write streams respectively.

> [!note] Note
> When you use the `CFStream` API for networking, read and write operations on sockets can block. To prevent blocking:
>
> 1. Call [CFReadStreamSetClient](<cfreadstreamsetclient(________).md>) and [CFWriteStreamSetClient](<cfwritestreamsetclient(________).md>) to register to receive stream-related event notifications.
> 2. Call [CFReadStreamScheduleWithRunLoop](<cfreadstreamschedulewithrunloop(______).md>) and [CFWriteStreamScheduleWithRunLoop](<cfwritestreamschedulewithrunloop(______).md>) to schedule the stream on a run loop for receiving stream-related event notifications.
> 3. Call [CFReadStreamOpen](<cfreadstreamopen(__).md>) and [CFWriteStreamOpen](<cfwritestreamopen(__).md>) to open each stream.
> 4. Read only after receiving a [kCFStreamEventHasBytesAvailable](cfstreameventtype/hasbytesavailable.md) notification. Write only after receiving a [kCFStreamEventCanAcceptBytes](cfstreameventtype/canacceptbytes.md) notification.

## Topics

### Creating Streams

- [CFStreamCreatePairWithPeerSocketSignature](<cfstreamcreatepairwithpeersocketsignature(________).md>) — Creates readable and writable streams connected to a socket. _(deprecated)_
- [CFStreamCreatePairWithSocketToHost](<cfstreamcreatepairwithsockettohost(__________).md>) — Creates readable and writable streams connected to a TCP/IP port of a particular host. _(deprecated)_
- [CFStreamCreatePairWithSocket](<cfstreamcreatepairwithsocket(________).md>) — Creates readable and writable streams connected to a socket. _(deprecated)_
- [CFStreamCreateBoundPair](<cfstreamcreateboundpair(________).md>) — Creates a bound pair of read and write streams.
- [CFStreamCreatePairWithSocketToCFHost(_:_:_:_:_:)](<../cfnetwork/cfstreamcreatepairwithsockettocfhost(__________).md>) — Creates readable and writable streams connected to a given `CFHost` object. _(deprecated)_
- [CFStreamCreatePairWithSocketToNetService(_:_:_:_:)](<../cfnetwork/cfstreamcreatepairwithsockettonetservice(________).md>) — Creates a pair of streams for a CFNetService. _(deprecated)_

### Obtaining Errors

- [CFSocketStreamSOCKSGetError(_:)](<../cfnetwork/cfsocketstreamsocksgeterror(__).md>) — This function gets error codes in the `kCFStreamErrorDomainSOCKS` domain from the `CFStreamError` returned by a stream operation.
- [CFSocketStreamSOCKSGetErrorSubdomain(_:)](<../cfnetwork/cfsocketstreamsocksgeterrorsubdomain(__).md>) — Gets the error subdomain associated with errors in the `kCFStreamErrorDomainSOCKS` domain from the `CFStreamError` returned by a stream operation.

### Setting the Security Protocol

- [CFReadStreamSetProperty](<cfreadstreamsetproperty(______).md>) — Sets the value of a property for a stream.
- [CFWriteStreamSetProperty](<cfwritestreamsetproperty(______).md>) — Sets the value of a property for a stream.
- [CFStream Socket Security Level Constants](cfstream-socket-security-level-constants.md) — Constants for setting the security level of a socket stream.

### Data Types

- [CFStreamError](cfstreamerror.md) — The structure returned by [CFReadStreamGetError](<cfreadstreamgeterror(__).md>) and [CFWriteStreamGetError](<cfwritestreamgeterror(__).md>).
- [CFStreamClientContext](cfstreamclientcontext.md) — A structure that contains program-defined data and callbacks with which you can configure a stream’s client behavior.

### Constants

- [CFStreamStatus](cfstreamstatus.md) — Constants that describe the status of a stream.
- [CFStreamErrorDomain](cfstreamerrordomain.md) — Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [CFStream Error Domain Constants (CFHost)](cfstream-error-domain-constants-cfhost.md) — Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [Error Subdomains](error-subdomains.md) — Subdomains used to determine how to interpret an error in the `kCFStreamErrorDomainSOCKS` domain.
- [Secure Sockets (SOCKS) Errors](../cfnetwork/1518266-secure-sockets-socks-errors.md) — Error codes returned by the `kCFStreamErrorDomainSOCKS` error domain.
- [CFStreamEventType](cfstreameventtype.md) — Defines constants for stream-related events.
- [Stream Properties](stream-properties.md) — Stream property names that can be set or copied.
- [CFStream Property SSL Settings Constants](cfstream-property-ssl-settings-constants.md) — Constants for use in a `CFDictionary` object that is the value of the `kCFStreamPropertySSLSettings` stream property key.
- [CFStream Socket Security Level Constants](cfstream-socket-security-level-constants.md) — Constants for setting the security level of a socket stream.
- [CFStream SOCKS Proxy Key Constants](cfstream-socks-proxy-key-constants.md) — Constants for SOCKS Proxy `CFDictionary` keys.
- [Stream Service Types](stream-service-types.md) — String constants that specify the service type of a stream.

## See Also

### Related Documentation

- [Getting Started with Networking, Internet, and Web](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_NetworkingInternetWeb/_index.html#//apple_ref/doc/uid/TP40008807)
- [CFNetwork Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/CFNetwork/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001132)

### Reference

- [Core Foundation Structures](core-foundation-structures.md)
- [Core Foundation Enumerations](core-foundation-enumerations.md)
- [Core Foundation Constants](core-foundation-constants.md)
- [Core Foundation Functions](core-foundation-functions.md)
- [Core Foundation Data Types](core-foundation-data-types.md)
- [Core Foundation Macros](corefoundation-macros.md)

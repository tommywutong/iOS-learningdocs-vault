---
title: URLProtocolClient
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlprotocolclient
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocolclient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocolclient.json'
content_hash: 'sha256:642ce3494a31c5a6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLProtocolClient

<sub>Protocol</sub>

The interface used by [URLProtocol](urlprotocol.md) subclasses to communicate with the URL Loading System.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol URLProtocolClient : NSObjectProtocol, Sendable
```

## Overview

Don’t implement this protocol in your application. Instead, your [URLProtocol](urlprotocol.md) subclass calls methods of this protocol on its own [client](urlprotocol/client.md) property.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a response

- [- URLProtocol:didReceiveResponse:cacheStoragePolicy:](<urlprotocolclient/urlprotocol(__didreceive_cachestoragepolicy_).md>) — Tells the client that the protocol implementation has created a response object for the request.

### Handling redirects

- [- URLProtocol:wasRedirectedToRequest:redirectResponse:](<urlprotocolclient/urlprotocol(__wasredirectedto_redirectresponse_).md>) — Tells the client that the protocol implementation has been redirected.

### Working with cache data

- [- URLProtocol:cachedResponseIsValid:](<urlprotocolclient/urlprotocol(__cachedresponseisvalid_).md>) — Tells the client that a cached response is valid.

### Handling authentication challenges

- [- URLProtocol:didCancelAuthenticationChallenge:](<urlprotocolclient/urlprotocol(__didcancel_).md>) — Tells the client that an authentication challenge has been canceled.
- [- URLProtocol:didReceiveAuthenticationChallenge:](<urlprotocolclient/urlprotocol(__didreceive_).md>) — Tells the client that the URL Loading System received an authentication challenge.

### Indicating loading progress or failure

- [- URLProtocol:didFailWithError:](<urlprotocolclient/urlprotocol(__didfailwitherror_).md>) — Tells the client that the load request failed due to an error.
- [- URLProtocol:didLoadData:](<urlprotocolclient/urlprotocol(__didload_).md>) — Tells the client that the protocol implementation has loaded some data.
- [- URLProtocolDidFinishLoading:](<urlprotocolclient/urlprotocoldidfinishloading(__).md>) — Tells the client that the protocol implementation has finished loading.

## See Also

### Getting protocol attributes

- [cachedResponse](urlprotocol/cachedresponse.md) — The protocol’s cached response.
- [client](urlprotocol/client.md) — The object the protocol uses to communicate with the URL loading system.
- [request](urlprotocol/request.md) — The protocol’s request.
- [task](urlprotocol/task.md) — The protocol’s task.

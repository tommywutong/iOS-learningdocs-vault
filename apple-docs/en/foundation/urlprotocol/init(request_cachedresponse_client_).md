---
title: 'init(request:cachedResponse:client:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocol/init(request:cachedresponse:client:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocol/init(request:cachedresponse:client:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocol/init%28request%3Acachedresponse%3Aclient%3A%29.json'
content_hash: 'sha256:2b39cd14cbb9a09f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocol](../urlprotocol.md)

# init(request:cachedResponse:client:)

<sub>Initializer</sub>

Creates a URL protocol instance to handle the request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(request: URLRequest, cachedResponse: CachedURLResponse?, client: (any URLProtocolClient)?)
```

## Parameters

- `request` — The URL request for the URL protocol object. This request is retained.

- `cachedResponse` — A cached response for the request; it may be `nil` if there is no existing cached response for the request.

- `client` — An object that provides an implementation of the [URLProtocolClient](../urlprotocolclient.md) protocol that this instance uses to communicate with the URL Loading System. This client object is retained.

## Return Value

The initialized protocol object.

## Discussion

Subclasses should override this method to do any custom initialization. Don’t call this method explicitly. When you register your custom protocol class, the system will initialize instances of your protocol as needed.

This is the designated initializer for [URLProtocol](../urlprotocol.md).

## See Also

### Creating protocol objects

- [- initWithTask:cachedResponse:client:](<init(task_cachedresponse_client_).md>) — Creates a URL protocol instance to handle the task.

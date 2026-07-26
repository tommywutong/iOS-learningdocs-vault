---
title: 'init(task:cachedResponse:client:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocol/init(task:cachedresponse:client:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocol/init(task:cachedresponse:client:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocol/init%28task%3Acachedresponse%3Aclient%3A%29.json'
content_hash: 'sha256:98531464655fe330'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocol](../urlprotocol.md)

# init(task:cachedResponse:client:)

<sub>Initializer</sub>

Creates a URL protocol instance to handle the task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(task: URLSessionTask, cachedResponse: CachedURLResponse?, client: (any URLProtocolClient)?)
```

## Parameters

- `task` — A task containing a URL request to be performed by the protocol.

- `cachedResponse` — A cached response for the task; may be `nil` if there is no existing cached response for the task.

- `client` — An object that provides an implementation of the [URLProtocolClient](../urlprotocolclient.md) protocol that this instance uses to communicate with the URL loading system. This client object is retained.

## Return Value

The initialized protocol object.

## Discussion

Subclasses should override this method to do any custom initialization. Don’t call this method explicitly. When you register your custom protocol class, the system will initialize instances of your protocol as needed.

This initializer calls through to [- initWithRequest:cachedResponse:client:](<init(request_cachedresponse_client_).md>).

## See Also

### Creating protocol objects

- [- initWithRequest:cachedResponse:client:](<init(request_cachedresponse_client_).md>) — Creates a URL protocol instance to handle the request.

---
title: 'init(configuration:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/init(configuration:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/init(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/init%28configuration%3A%29.json'
content_hash: 'sha256:e1a0074690902251'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# init(configuration:)

<sub>Initializer</sub>

Creates a session with the specified session configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(configuration: URLSessionConfiguration)
```

## Parameters

- `configuration` — A configuration object that specifies certain behaviors, such as caching policies, timeouts, proxies, pipelining, TLS versions to support, cookie policies, credential storage, and so on. See [URLSessionConfiguration](../urlsessionconfiguration.md) for more information.

## Discussion

Calling this method is equivalent to calling [+ sessionWithConfiguration:delegate:delegateQueue:](<init(configuration_delegate_delegatequeue_).md>) with a `nil` delegate and queue.

## See Also

### Creating a session

- [+ sessionWithConfiguration:delegate:delegateQueue:](<init(configuration_delegate_delegatequeue_).md>) — Creates a session with the specified session configuration, delegate, and operation queue.
- [URLSessionConfiguration](../urlsessionconfiguration.md) — A configuration object that defines behavior and policies for a URL session.
- [configuration](configuration.md) — A copy of the configuration object for this session.

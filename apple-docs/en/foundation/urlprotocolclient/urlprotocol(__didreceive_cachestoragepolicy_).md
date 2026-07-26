---
title: 'urlProtocol(_:didReceive:cacheStoragePolicy:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocolclient/urlprotocol(_:didreceive:cachestoragepolicy:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocolclient/urlprotocol(_:didreceive:cachestoragepolicy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocolclient/urlprotocol%28_%3Adidreceive%3Acachestoragepolicy%3A%29.json'
content_hash: 'sha256:c7d07d06caea96fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocolClient](../urlprotocolclient.md)

# urlProtocol(_:didReceive:cacheStoragePolicy:)

<sub>Instance Method</sub>

Tells the client that the protocol implementation has created a response object for the request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func urlProtocol(_ protocol: URLProtocol, didReceive response: URLResponse, cacheStoragePolicy policy: URLCache.StoragePolicy)
```

## Parameters

- `protocol` — The URL protocol object sending the message.

- `response` — The newly available response object.

- `policy` — The cache storage policy for the response.

## Discussion

The implementation should use the provided cache storage policy to determine whether to store the response in a cache.

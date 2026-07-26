---
title: 'init(response:data:userInfo:storagePolicy:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/cachedurlresponse/init(response:data:userinfo:storagepolicy:)'
source_url: 'https://developer.apple.com/documentation/foundation/cachedurlresponse/init(response:data:userinfo:storagepolicy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/cachedurlresponse/init%28response%3Adata%3Auserinfo%3Astoragepolicy%3A%29.json'
content_hash: 'sha256:779a18221889d729'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [CachedURLResponse](../cachedurlresponse.md)

# init(response:data:userInfo:storagePolicy:)

<sub>Initializer</sub>

Creates a cached URL response with a given server response, data, user-info dictionary, and storage policy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(response: URLResponse, data: Data, userInfo: [AnyHashable : Any]? = nil, storagePolicy: URLCache.StoragePolicy)
```

## Parameters

- `response` — The response to cache.

- `data` — The data to cache.

- `userInfo` — An optional dictionary of user information. May be `nil`.

- `storagePolicy` — The storage policy for the cached response.

## Return Value

A cached URL response object, containing the response and data.

## See Also

### Creating a cached URL response

- [- initWithResponse:data:](<init(response_data_).md>) — Creates a cached URL response instance.

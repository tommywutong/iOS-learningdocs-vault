---
title: 'init(response:data:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/cachedurlresponse/init(response:data:)'
source_url: 'https://developer.apple.com/documentation/foundation/cachedurlresponse/init(response:data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/cachedurlresponse/init%28response%3Adata%3A%29.json'
content_hash: 'sha256:31af15418a3bd5af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [CachedURLResponse](../cachedurlresponse.md)

# init(response:data:)

<sub>Initializer</sub>

Creates a cached URL response instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(response: URLResponse, data: Data)
```

## Parameters

- `response` — The response to cache.

- `data` — The data to cache.

## Return Value

A cached URL response object, containing the response and data.

## Discussion

The cache storage policy is set to the default, [NSURLCacheStorageAllowed](../urlcache/storagepolicy/allowed.md), and the user info dictionary is set to `nil`.

## See Also

### Creating a cached URL response

- [- initWithResponse:data:userInfo:storagePolicy:](<init(response_data_userinfo_storagepolicy_).md>) — Creates a cached URL response with a given server response, data, user-info dictionary, and storage policy.

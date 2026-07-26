---
title: cachePolicy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutableurlrequest/cachepolicy
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableurlrequest/cachepolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableurlrequest/cachepolicy.json'
content_hash: 'sha256:41b5a95669ea2904'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableURLRequest](../nsmutableurlrequest.md)

# cachePolicy

<sub>Instance Property</sub>

The request’s cache policy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var cachePolicy: NSURLRequest.CachePolicy { get set }
```

## Discussion

This property is ignored for requests used to construct [URLSessionUploadTask](../urlsessionuploadtask.md) and [URLSessionDownloadTask](../urlsessiondownloadtask.md) objects, as caching is not supported by the URL Loading System for upload or download requests.

## See Also

### Working with a cache policy

- [CachePolicy](../nsurlrequest/cachepolicy-swift.enum.md) — The constants used to specify interaction with the cached responses.

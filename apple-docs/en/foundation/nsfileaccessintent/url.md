---
title: url
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileaccessintent/url
source_url: 'https://developer.apple.com/documentation/foundation/nsfileaccessintent/url'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileaccessintent/url.json'
content_hash: 'sha256:69685acd897b08a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileAccessIntent](../nsfileaccessintent.md)

# url

<sub>Instance Property</sub>

The current URL for the item managed by the file access intent instance. (read-only)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var url: URL { get }
```

## Discussion

Always use the URL returned by this property inside the accessor block of a file coordinator’s [- coordinateAccessWithIntents:queue:byAccessor:](<../nsfilecoordinator/coordinate(with_queue_byaccessor_).md>) method. This property’s value may be different from the original URL, because the item was either moved or renamed while the file coordinator waited for access.

## See Also

### Related Documentation

- [- coordinateAccessWithIntents:queue:byAccessor:](<../nsfilecoordinator/coordinate(with_queue_byaccessor_).md>) — Performs a number of coordinated-read or -write operations asynchronously.

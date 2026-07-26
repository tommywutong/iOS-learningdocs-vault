---
title: request
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurldownload/request
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownload/request'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownload/request.json'
content_hash: 'sha256:b0a97724871cc178'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownload](../nsurldownload.md)

# request

<sub>Instance Property</sub>

Returns the request that initiated the receiver’s download.

<sub>macOS</sub>

```swift
var request: URLRequest { get }
```

## Return Value

The URL request that initiated the receiver’s download.

## See Also

### Getting download properties

- [deletesFileUponFailure](deletesfileuponfailure.md) — Returns whether the receiver deletes partially downloaded files when a download stops prematurely.

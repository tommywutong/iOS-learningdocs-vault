---
title: 'addClient:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlhandle/addclient:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandle/addclient:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandle/addclient%3A.json'
content_hash: 'sha256:9fe905fc819e7e04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLHandle](../nsurlhandle.md)

# addClient:

<sub>Instance Method</sub>

Adds a client of the URL handle.

> [!warning] Deprecated
> Use [NSURLConnection](../nsurlconnection.md) or [NSURLDownload](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) addClient:(id<NSURLHandleClient>) client;
```

## Parameters

- `client` — An object conforming to the `NSURLHandleClient` protocol.

## See Also

### Managing clients

- [removeClient:](removeclient_.md) — Removes `client` as an `NSURLHandleClient` of the receiver. _(deprecated)_

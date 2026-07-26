---
title: 'removeClient:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlhandle/removeclient:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandle/removeclient:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandle/removeclient%3A.json'
content_hash: 'sha256:36923cfe820de2e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLHandle](../nsurlhandle.md)

# removeClient:

<sub>Instance Method</sub>

Removes `client` as an `NSURLHandleClient` of the receiver.

> [!warning] Deprecated
> Use [NSURLConnection](../nsurlconnection.md) or [NSURLDownload](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) removeClient:(id<NSURLHandleClient>) client;
```

## Parameters

- `client` — An object conforming to the `NSURLHandleClient` protocol.

## See Also

### Managing clients

- [addClient:](addclient_.md) — Adds a client of the URL handle. _(deprecated)_

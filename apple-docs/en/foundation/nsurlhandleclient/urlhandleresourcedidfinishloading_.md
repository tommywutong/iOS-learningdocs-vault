---
title: 'URLHandleResourceDidFinishLoading:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlhandleclient/urlhandleresourcedidfinishloading:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandleclient/urlhandleresourcedidfinishloading:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandleclient/urlhandleresourcedidfinishloading%3A.json'
content_hash: 'sha256:15f1755c30f32720'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLHandleClient](../nsurlhandleclient.md)

# URLHandleResourceDidFinishLoading:

<sub>Instance Method</sub>

Sent when an URL handle finishes loading resource data.

> [!warning] Deprecated
> Use [NSURLConnection](../nsurlconnection.md) or [NSURLDownload](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) URLHandleResourceDidFinishLoading:(NSURLHandle *) sender;
```

## Parameters

- `sender` — The URL handle sending the message.

## See Also

### Notification methods

- [URLHandleResourceDidBeginLoading:](urlhandleresourcedidbeginloading_.md) — Sent when an URL handle begins loading resource data. _(deprecated)_
- [URLHandleResourceDidCancelLoading:](urlhandleresourcedidcancelloading_.md) — Sent when an URL handle has canceled loading resource data in response to a programmatic request. _(deprecated)_
- [URLHandle:resourceDataDidBecomeAvailable:](urlhandle_resourcedatadidbecomeavailable_.md) — Sent periodically by an URL handle when new resource data becomes available. _(deprecated)_
- [URLHandle:resourceDidFailLoadingWithReason:](urlhandle_resourcedidfailloadingwithreason_.md) — Sent when the URL handle failed to load resource data for some reason other than being canceled. _(deprecated)_

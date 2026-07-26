---
title: 'URLHandle:resourceDataDidBecomeAvailable:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlhandleclient/urlhandle:resourcedatadidbecomeavailable:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandleclient/urlhandle:resourcedatadidbecomeavailable:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandleclient/urlhandle%3Aresourcedatadidbecomeavailable%3A.json'
content_hash: 'sha256:2ba2e1893b40626c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLHandleClient](../nsurlhandleclient.md)

# URLHandle:resourceDataDidBecomeAvailable:

<sub>Instance Method</sub>

Sent periodically by an URL handle when new resource data becomes available.

> [!warning] Deprecated
> Use [NSURLConnection](../nsurlconnection.md) or [NSURLDownload](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) URLHandle:(NSURLHandle *) sender resourceDataDidBecomeAvailable:(NSData *) newBytes;
```

## Parameters

- `sender` — The URL handle sending the message.

- `newBytes` — The newly available data.

## See Also

### Notification methods

- [URLHandleResourceDidBeginLoading:](urlhandleresourcedidbeginloading_.md) — Sent when an URL handle begins loading resource data. _(deprecated)_
- [URLHandleResourceDidCancelLoading:](urlhandleresourcedidcancelloading_.md) — Sent when an URL handle has canceled loading resource data in response to a programmatic request. _(deprecated)_
- [URLHandleResourceDidFinishLoading:](urlhandleresourcedidfinishloading_.md) — Sent when an URL handle finishes loading resource data. _(deprecated)_
- [URLHandle:resourceDidFailLoadingWithReason:](urlhandle_resourcedidfailloadingwithreason_.md) — Sent when the URL handle failed to load resource data for some reason other than being canceled. _(deprecated)_

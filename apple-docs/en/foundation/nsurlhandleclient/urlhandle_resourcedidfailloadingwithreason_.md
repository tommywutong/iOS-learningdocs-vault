---
title: 'URLHandle:resourceDidFailLoadingWithReason:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlhandleclient/urlhandle:resourcedidfailloadingwithreason:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandleclient/urlhandle:resourcedidfailloadingwithreason:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandleclient/urlhandle%3Aresourcedidfailloadingwithreason%3A.json'
content_hash: 'sha256:c5bd165918a4c496'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLHandleClient](../nsurlhandleclient.md)

# URLHandle:resourceDidFailLoadingWithReason:

<sub>Instance Method</sub>

Sent when the URL handle failed to load resource data for some reason other than being canceled.

> [!warning] Deprecated
> Use [NSURLConnection](../nsurlconnection.md) or [NSURLDownload](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) URLHandle:(NSURLHandle *) sender resourceDidFailLoadingWithReason:(NSString *) reason;
```

## Parameters

- `sender` — The URL handle sending the message.

- `reason` — A human-readable, localized string describing why the load failed.

## See Also

### Notification methods

- [URLHandleResourceDidBeginLoading:](urlhandleresourcedidbeginloading_.md) — Sent when an URL handle begins loading resource data. _(deprecated)_
- [URLHandleResourceDidCancelLoading:](urlhandleresourcedidcancelloading_.md) — Sent when an URL handle has canceled loading resource data in response to a programmatic request. _(deprecated)_
- [URLHandleResourceDidFinishLoading:](urlhandleresourcedidfinishloading_.md) — Sent when an URL handle finishes loading resource data. _(deprecated)_
- [URLHandle:resourceDataDidBecomeAvailable:](urlhandle_resourcedatadidbecomeavailable_.md) — Sent periodically by an URL handle when new resource data becomes available. _(deprecated)_

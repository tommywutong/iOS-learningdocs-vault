---
title: NSURLHandleClient
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsurlhandleclient
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandleclient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandleclient.json'
content_hash: 'sha256:5876c9a0c80832c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLHandleClient

<sub>Protocol</sub>

The interface implemented by URL handle clients.

<sub>Mac Catalyst, macOS</sub>

```objc
@protocol NSURLHandleClient
```

## Overview

[NSURLHandleClient](nsurlhandleclient.md) is deprecated in macOS 10.4 and later. Applications that are intended for deployment in macOS 10.3 or later should use [NSURLConnection](nsurlconnection.md) or [NSURLDownload](nsurldownload.md) instead; see [URL Loading System](url-loading-system.md).

## Topics

### Notification methods

- [URLHandleResourceDidBeginLoading:](nsurlhandleclient/urlhandleresourcedidbeginloading_.md) — Sent when an URL handle begins loading resource data. _(deprecated)_
- [URLHandleResourceDidCancelLoading:](nsurlhandleclient/urlhandleresourcedidcancelloading_.md) — Sent when an URL handle has canceled loading resource data in response to a programmatic request. _(deprecated)_
- [URLHandleResourceDidFinishLoading:](nsurlhandleclient/urlhandleresourcedidfinishloading_.md) — Sent when an URL handle finishes loading resource data. _(deprecated)_
- [URLHandle:resourceDataDidBecomeAvailable:](nsurlhandleclient/urlhandle_resourcedatadidbecomeavailable_.md) — Sent periodically by an URL handle when new resource data becomes available. _(deprecated)_
- [URLHandle:resourceDidFailLoadingWithReason:](nsurlhandleclient/urlhandle_resourcedidfailloadingwithreason_.md) — Sent when the URL handle failed to load resource data for some reason other than being canceled. _(deprecated)_

## See Also

### URL Handle

- [NSURLHandle](nsurlhandle.md) — An object that accesses and manages resource data indicated by a URL.

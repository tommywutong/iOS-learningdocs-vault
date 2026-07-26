---
title: 'cachedHandleForURL:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlhandle/cachedhandleforurl:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandle/cachedhandleforurl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandle/cachedhandleforurl%3A.json'
content_hash: 'sha256:54a15fd6db5c463f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLHandle](../nsurlhandle.md)

# cachedHandleForURL:

<sub>Type Method</sub>

Returns the URL handle from the cache that has serviced the specified URL or another identical URL.

> [!warning] Deprecated
> Use [NSURLConnection](../nsurlconnection.md) or [NSURLDownload](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

<sub>Mac Catalyst, macOS</sub>

```objc
+ (NSURLHandle *) cachedHandleForURL:(NSURL *) anURL;
```

## Parameters

- `anURL` — The URL whose cached URL handle is desired.

## Return Value

The URL handle from the cache that has serviced `aURL` or another identical URL. Returns `nil` if there is no such handle.

## Discussion

Subclasses of `NSURLHandle` must override this method.

## See Also

### Constructing NSURLHandles

- [initWithURL:cached:](initwithurl_cached_.md) — Initializes a newly created URL handle with the specified URL. _(deprecated)_

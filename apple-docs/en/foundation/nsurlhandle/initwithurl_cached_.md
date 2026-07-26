---
title: 'initWithURL:cached:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlhandle/initwithurl:cached:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandle/initwithurl:cached:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandle/initwithurl%3Acached%3A.json'
content_hash: 'sha256:f4ec94d1b1c54256'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLHandle](../nsurlhandle.md)

# initWithURL:cached:

<sub>Instance Method</sub>

Initializes a newly created URL handle with the specified URL.

> [!warning] Deprecated
> Use [NSURLConnection](../nsurlconnection.md) or [NSURLDownload](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

<sub>Mac Catalyst, macOS</sub>

```objc
- (id) initWithURL:(NSURL *) anURL cached:(BOOL) willCache;
```

## Parameters

- `anURL` — The URL for the new handle.

- `willCache` — [true](../../swift/true.md) if the URL handle should cache its data and respond to requests from equivalent URLs for the cached data, [false](../../swift/false.md) otherwise.

## Discussion

Subclasses of `NSURLHandle` must override this method.

## See Also

### Constructing NSURLHandles

- [cachedHandleForURL:](cachedhandleforurl_.md) — Returns the URL handle from the cache that has serviced the specified URL or another identical URL. _(deprecated)_

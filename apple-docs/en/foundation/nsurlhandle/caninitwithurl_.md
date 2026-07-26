---
title: 'canInitWithURL:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlhandle/caninitwithurl:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandle/caninitwithurl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandle/caninitwithurl%3A.json'
content_hash: 'sha256:b641fb72e93d928c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLHandle](../nsurlhandle.md)

# canInitWithURL:

<sub>Type Method</sub>

Returns whether a URL handle can be initialized with a given URL.

> [!warning] Deprecated
> Use [NSURLConnection](../nsurlconnection.md) or [NSURLDownload](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

<sub>Mac Catalyst, macOS</sub>

```objc
+ (BOOL) canInitWithURL:(NSURL *) anURL;
```

## Parameters

- `anURL` — The URL in question.

## Return Value

[true](../../swift/true.md) if a URL handle can be initialized with `aURL`, [false](../../swift/false.md) otherwise.

## Discussion

Subclasses of `NSURLHandle` must override this method to identify which URLs they can service.

## See Also

### Managing subclasses

- [URLHandleClassForURL:](urlhandleclassforurl_.md) — Returns the class of the URL handle that will be used for a specified URL. _(deprecated)_
- [registerURLHandleClass:](registerurlhandleclass_.md) — Registers a subclass of `NSURLHandle` as an available subclass for handling URLs _(deprecated)_

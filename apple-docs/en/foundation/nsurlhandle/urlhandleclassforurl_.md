---
title: 'URLHandleClassForURL:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlhandle/urlhandleclassforurl:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandle/urlhandleclassforurl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandle/urlhandleclassforurl%3A.json'
content_hash: 'sha256:b3948ffa01c459bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLHandle](../nsurlhandle.md)

# URLHandleClassForURL:

<sub>Type Method</sub>

Returns the class of the URL handle that will be used for a specified URL.

> [!warning] Deprecated
> Use [NSURLConnection](../nsurlconnection.md) or [NSURLDownload](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

<sub>Mac Catalyst, macOS</sub>

```objc
+ (Class) URLHandleClassForURL:(NSURL *) anURL;
```

## Parameters

- `anURL` — The URL in question.

## Return Value

The class of the URL handle that will be used for `aURL`.

## Discussion

Subclasses of `NSURLHandle` must be registered via the [registerURLHandleClass:](registerurlhandleclass_.md) method. The subclass is determined by asking the list of registered subclasses if it [canInitWithURL:](caninitwithurl_.md); the first class to respond [true](../../swift/true.md) is selected.

## See Also

### Managing subclasses

- [canInitWithURL:](caninitwithurl_.md) — Returns whether a URL handle can be initialized with a given URL. _(deprecated)_
- [registerURLHandleClass:](registerurlhandleclass_.md) — Registers a subclass of `NSURLHandle` as an available subclass for handling URLs _(deprecated)_

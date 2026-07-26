---
title: 'registerURLHandleClass:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（10.4 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurlhandle/registerurlhandleclass:'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlhandle/registerurlhandleclass:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlhandle/registerurlhandleclass%3A.json'
content_hash: 'sha256:ba88abdf73180001'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLHandle](../nsurlhandle.md)

# registerURLHandleClass:

<sub>Type Method</sub>

Registers a subclass of `NSURLHandle` as an available subclass for handling URLs

> [!warning] Deprecated
> Use [NSURLConnection](../nsurlconnection.md) or [NSURLDownload](../nsurldownload.md) instead; see [URL Loading System](../url-loading-system.md).

<sub>Mac Catalyst, macOS</sub>

```objc
+ (void) registerURLHandleClass:(Class) anURLHandleSubclass;
```

## Parameters

- `anURLHandleSubclass` — The new subclass to register as an available subclass.

## See Also

### Managing subclasses

- [URLHandleClassForURL:](urlhandleclassforurl_.md) — Returns the class of the URL handle that will be used for a specified URL. _(deprecated)_
- [canInitWithURL:](caninitwithurl_.md) — Returns whether a URL handle can be initialized with a given URL. _(deprecated)_

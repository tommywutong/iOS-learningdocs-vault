---
title: flushHostCache
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nshost/flushhostcache
source_url: 'https://developer.apple.com/documentation/foundation/nshost/flushhostcache'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshost/flushhostcache.json'
content_hash: 'sha256:3d076c9084f29688'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Host](../host.md)

# flushHostCache

<sub>Type Method</sub>

Releases the cache of existing `NSHost` objects so subsequent requests for `NSHost` objects create new ones.

> [!warning] Deprecated
> `NSHost` does not implement caching in macOS 10.6 and later.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (void) flushHostCache;
```

## Discussion

`NSHost` objects that were retained before this method was invoked remain valid.

## See Also

### Managing the Host Cache

- [isHostCacheEnabled](ishostcacheenabled.md) — Indicates whether caching is turned on or off. _(deprecated)_
- [setHostCacheEnabled:](sethostcacheenabled_.md) — Specifies whether the receiver is to cache instances as it creates them to avoid creating duplicate instances. _(deprecated)_

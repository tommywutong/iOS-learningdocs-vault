---
title: isHostCacheEnabled
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nshost/ishostcacheenabled
source_url: 'https://developer.apple.com/documentation/foundation/nshost/ishostcacheenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshost/ishostcacheenabled.json'
content_hash: 'sha256:38d591a14b3e15c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Host](../host.md)

# isHostCacheEnabled

<sub>Type Method</sub>

Indicates whether caching is turned on or off.

> [!warning] Deprecated
> `NSHost` does not implement caching in macOS 10.6 and later.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (BOOL) isHostCacheEnabled;
```

## Return Value

[true](../../swift/true.md) when caching is turned on; [false](../../swift/false.md) otherwise.

## See Also

### Managing the Host Cache

- [setHostCacheEnabled:](sethostcacheenabled_.md) — Specifies whether the receiver is to cache instances as it creates them to avoid creating duplicate instances. _(deprecated)_
- [flushHostCache](flushhostcache.md) — Releases the cache of existing `NSHost` objects so subsequent requests for `NSHost` objects create new ones. _(deprecated)_

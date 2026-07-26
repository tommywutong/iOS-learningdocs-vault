---
title: 'setHostCacheEnabled:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nshost/sethostcacheenabled:'
source_url: 'https://developer.apple.com/documentation/foundation/nshost/sethostcacheenabled:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshost/sethostcacheenabled%3A.json'
content_hash: 'sha256:9354bcf79bb2ab64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Host](../host.md)

# setHostCacheEnabled:

<sub>Type Method</sub>

Specifies whether the receiver is to cache instances as it creates them to avoid creating duplicate instances.

> [!warning] Deprecated
> `NSHost` does not implement caching in macOS 10.6 and later.

<sub>Mac Catalyst, macOS</sub>

```objc
+ (void) setHostCacheEnabled:(BOOL) flag;
```

## Parameters

- `flag` — [true](../../swift/true.md) to turn on caching. [false](../../swift/false.md) to turn of caching.

## Discussion

This method doesn’t flush the cache. If you turn caching off and then back on, new requests for hosts use what was in the cache at the time caching was turned off. However, `NSHost` objects created while caching is turned off aren’t entered into the cache.

## See Also

### Managing the Host Cache

- [isHostCacheEnabled](ishostcacheenabled.md) — Indicates whether caching is turned on or off. _(deprecated)_
- [flushHostCache](flushhostcache.md) — Releases the cache of existing `NSHost` objects so subsequent requests for `NSHost` objects create new ones. _(deprecated)_

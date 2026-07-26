---
title: URLCache.StoragePolicy.allowed
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcache/storagepolicy/allowed
source_url: 'https://developer.apple.com/documentation/foundation/urlcache/storagepolicy/allowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcache/storagepolicy/allowed.json'
content_hash: 'sha256:0c134709864b2b89'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLCache](../../urlcache.md) · [StoragePolicy](../storagepolicy.md)

# URLCache.StoragePolicy.allowed

<sub>Case</sub>

Storage in [URLCache](../../urlcache.md) is allowed without restriction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case allowed
```

## Discussion

> [!important] Important
> iOS prior to version 5 ignores this cache policy, and instead treats it as [NSURLCacheStorageAllowedInMemoryOnly](allowedinmemoryonly.md).

## See Also

### Policies

- [NSURLCacheStorageAllowedInMemoryOnly](allowedinmemoryonly.md) — Storage in [URLCache](../../urlcache.md) is allowed; however storage should be restricted to memory only.
- [NSURLCacheStorageNotAllowed](notallowed.md) — Storage in [URLCache](../../urlcache.md) is not allowed in any fashion, either in memory or on disk.

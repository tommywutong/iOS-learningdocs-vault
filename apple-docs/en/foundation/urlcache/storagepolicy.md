---
title: URLCache.StoragePolicy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcache/storagepolicy
source_url: 'https://developer.apple.com/documentation/foundation/urlcache/storagepolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcache/storagepolicy.json'
content_hash: 'sha256:2ea1594980f60092'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLCache](../urlcache.md)

# URLCache.StoragePolicy

<sub>Enumeration</sub>

These constants specify the caching strategy used by an [CachedURLResponse](../cachedurlresponse.md) object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum StoragePolicy
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Policies

- [NSURLCacheStorageAllowed](storagepolicy/allowed.md) — Storage in [URLCache](../urlcache.md) is allowed without restriction.
- [NSURLCacheStorageAllowedInMemoryOnly](storagepolicy/allowedinmemoryonly.md) — Storage in [URLCache](../urlcache.md) is allowed; however storage should be restricted to memory only.
- [NSURLCacheStorageNotAllowed](storagepolicy/notallowed.md) — Storage in [URLCache](../urlcache.md) is not allowed in any fashion, either in memory or on disk.

### Initializers

- [init(rawValue:)](<storagepolicy/init(rawvalue_).md>)

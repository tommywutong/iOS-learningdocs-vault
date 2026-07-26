---
title: NSURLRequest.CachePolicy
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/cachepolicy-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/cachepolicy-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/cachepolicy-swift.enum.json'
content_hash: 'sha256:c67d89d2ac63aa0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# NSURLRequest.CachePolicy

<sub>Enumeration</sub>

The constants used to specify interaction with the cached responses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CachePolicy
```

## Overview

The default policy is [NSURLRequestUseProtocolCachePolicy](cachepolicy-swift.enum/useprotocolcachepolicy.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Policies

- [NSURLRequestUseProtocolCachePolicy](cachepolicy-swift.enum/useprotocolcachepolicy.md) — Use the caching logic defined in the protocol implementation, if any, for a particular URL load request.
- [NSURLRequestReloadIgnoringLocalCacheData](cachepolicy-swift.enum/reloadignoringlocalcachedata.md) — The URL load should be loaded only from the originating source.
- [NSURLRequestReloadIgnoringLocalAndRemoteCacheData](cachepolicy-swift.enum/reloadignoringlocalandremotecachedata.md) — Ignore local cache data, and instruct proxies and other intermediates to disregard their caches so far as the protocol allows.
- [NSURLRequestReloadIgnoringCacheData](cachepolicy-swift.enum/reloadignoringcachedata.md) — Replaced by [NSURLRequestReloadIgnoringLocalCacheData](cachepolicy-swift.enum/reloadignoringlocalcachedata.md).
- [NSURLRequestReturnCacheDataElseLoad](cachepolicy-swift.enum/returncachedataelseload.md) — Use existing cache data, regardless or age or expiration date, loading from originating source only if there is no cached data.
- [NSURLRequestReturnCacheDataDontLoad](cachepolicy-swift.enum/returncachedatadontload.md) — Use existing cache data, regardless or age or expiration date, and fail if no cached data is available.
- [NSURLRequestReloadRevalidatingCacheData](cachepolicy-swift.enum/reloadrevalidatingcachedata.md) — Use cache data if the origin source can validate it; otherwise, load from the origin.

### Initializers

- [init(rawValue:)](<cachepolicy-swift.enum/init(rawvalue_).md>)

## See Also

### Working with a cache policy

- [cachePolicy](../nsmutableurlrequest/cachepolicy.md) — The request’s cache policy.

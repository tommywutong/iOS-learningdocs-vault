---
title: NSURLRequest.CachePolicy.reloadIgnoringLocalAndRemoteCacheData
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlrequest/cachepolicy-swift.enum/reloadignoringlocalandremotecachedata
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/cachepolicy-swift.enum/reloadignoringlocalandremotecachedata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/cachepolicy-swift.enum/reloadignoringlocalandremotecachedata.json'
content_hash: 'sha256:949ed0add9b7f40a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSURLRequest](../../nsurlrequest.md) · [CachePolicy](../cachepolicy-swift.enum.md)

# NSURLRequest.CachePolicy.reloadIgnoringLocalAndRemoteCacheData

<sub>Case</sub>

Ignore local cache data, and instruct proxies and other intermediates to disregard their caches so far as the protocol allows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case reloadIgnoringLocalAndRemoteCacheData
```

## Discussion

> [!important] Important
> Versions earlier than macOS 10.15, iOS 13, watchOS 6, and tvOS 13 don’t implement this constant.

## See Also

### Policies

- [NSURLRequestUseProtocolCachePolicy](useprotocolcachepolicy.md) — Use the caching logic defined in the protocol implementation, if any, for a particular URL load request.
- [NSURLRequestReloadIgnoringLocalCacheData](reloadignoringlocalcachedata.md) — The URL load should be loaded only from the originating source.
- [NSURLRequestReloadIgnoringCacheData](reloadignoringcachedata.md) — Replaced by [NSURLRequestReloadIgnoringLocalCacheData](reloadignoringlocalcachedata.md).
- [NSURLRequestReturnCacheDataElseLoad](returncachedataelseload.md) — Use existing cache data, regardless or age or expiration date, loading from originating source only if there is no cached data.
- [NSURLRequestReturnCacheDataDontLoad](returncachedatadontload.md) — Use existing cache data, regardless or age or expiration date, and fail if no cached data is available.
- [NSURLRequestReloadRevalidatingCacheData](reloadrevalidatingcachedata.md) — Use cache data if the origin source can validate it; otherwise, load from the origin.

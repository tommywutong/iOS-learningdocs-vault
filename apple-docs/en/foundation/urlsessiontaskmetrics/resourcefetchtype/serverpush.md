---
title: URLSessionTaskMetrics.ResourceFetchType.serverPush
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+（18.4 起废弃）, iPadOS 10.0+（18.4 起废弃）, Mac Catalyst 13.1+（18.4 起废弃）, macOS 10.12+（15.4 起废弃）, tvOS 10.0+（18.4 起废弃）, visionOS 1.0+（2.4 起废弃）, watchOS 3.0+（11.4 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlsessiontaskmetrics/resourcefetchtype/serverpush
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontaskmetrics/resourcefetchtype/serverpush'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontaskmetrics/resourcefetchtype/serverpush.json'
content_hash: 'sha256:1ee635beb95cf873'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLSessionTaskMetrics](../../urlsessiontaskmetrics.md) · [ResourceFetchType](../resourcefetchtype.md)

# URLSessionTaskMetrics.ResourceFetchType.serverPush

<sub>Case</sub>

The resource was pushed by the server to the client.

> [!warning] Deprecated
> Server push is no longer supported as of iOS 17 and aligned releases

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case serverPush
```

## See Also

### Fetch types

- [NSURLSessionTaskMetricsResourceFetchTypeUnknown](unknown.md) — The manner in which the resource was fetched could not be determined.
- [NSURLSessionTaskMetricsResourceFetchTypeNetworkLoad](networkload.md) — The resource was loaded over the network.
- [NSURLSessionTaskMetricsResourceFetchTypeLocalCache](localcache.md) — The resource was retrieved from the local storage.

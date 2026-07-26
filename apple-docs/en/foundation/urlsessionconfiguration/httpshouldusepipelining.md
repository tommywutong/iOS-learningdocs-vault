---
title: httpShouldUsePipelining
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（18.4 起废弃）, iPadOS 7.0+（18.4 起废弃）, Mac Catalyst 13.1+（18.4 起废弃）, macOS 10.9+（15.4 起废弃）, tvOS 9.0+（18.4 起废弃）, visionOS 1.0+（2.4 起废弃）, watchOS 2.0+（11.4 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlsessionconfiguration/httpshouldusepipelining
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/httpshouldusepipelining'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/httpshouldusepipelining.json'
content_hash: 'sha256:5a53912577c93d93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# httpShouldUsePipelining

<sub>Instance Property</sub>

A Boolean value that determines whether the session should use HTTP pipelining.

> [!warning] Deprecated
> Only supported in the classic loader, please adopt HTTP/2 and HTTP/3 instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpShouldUsePipelining: Bool { get set }
```

## Discussion

This property determines whether tasks within sessions based on this configuration should use HTTP pipelining. You can also enable pipelining on a per-task basis by creating the task with an [NSURLRequest](../nsurlrequest.md) object.

The default value is [false](../../swift/false.md).

## See Also

### Setting HTTP policy and proxy properties

- [HTTPMaximumConnectionsPerHost](httpmaximumconnectionsperhost.md) — The maximum number of simultaneous connections to make to a given host.
- [proxyConfigurations](proxyconfigurations.md) — An array of proxy configuration objects containing information about the proxies to use within this session.
- [connectionProxyDictionary](connectionproxydictionary.md) — A dictionary containing information about the proxy to use within this session.

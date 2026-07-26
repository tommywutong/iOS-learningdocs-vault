---
title: connectionProxyDictionary
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/connectionproxydictionary
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/connectionproxydictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/connectionproxydictionary.json'
content_hash: 'sha256:fe38c7f304f99ae0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# connectionProxyDictionary

<sub>Instance Property</sub>

A dictionary containing information about the proxy to use within this session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var connectionProxyDictionary: [AnyHashable : Any]? { get set }
```

## Discussion

This property controls which proxy tasks within sessions based on this configuration use when connecting to remote hosts.

Prefer using [proxyConfigurations](proxyconfigurations.md), which supports secure proxy and relay types.

The default value is `NULL`, which means that tasks use the default system settings.

See `Global Proxy Configuration` for more information about these dictionaries.

## See Also

### Setting HTTP policy and proxy properties

- [HTTPMaximumConnectionsPerHost](httpmaximumconnectionsperhost.md) — The maximum number of simultaneous connections to make to a given host.
- [HTTPShouldUsePipelining](httpshouldusepipelining.md) — A Boolean value that determines whether the session should use HTTP pipelining. _(deprecated)_
- [proxyConfigurations](proxyconfigurations.md) — An array of proxy configuration objects containing information about the proxies to use within this session.

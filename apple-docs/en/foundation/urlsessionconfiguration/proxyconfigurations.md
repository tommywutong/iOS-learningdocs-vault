---
title: proxyConfigurations
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionconfiguration/proxyconfigurations
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionconfiguration/proxyconfigurations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionconfiguration/proxyconfigurations.json'
content_hash: 'sha256:b452cf810fe6ed31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionConfiguration](../urlsessionconfiguration.md)

# proxyConfigurations

<sub>Instance Property</sub>

An array of proxy configuration objects containing information about the proxies to use within this session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var proxyConfigurations: [ProxyConfiguration] { get set }
```

## Discussion

This property controls which proxy tasks within sessions based on this configuration use when connecting to remote hosts.

The default value is the empty array, which means that tasks use the default system settings.

## See Also

### Setting HTTP policy and proxy properties

- [HTTPMaximumConnectionsPerHost](httpmaximumconnectionsperhost.md) — The maximum number of simultaneous connections to make to a given host.
- [HTTPShouldUsePipelining](httpshouldusepipelining.md) — A Boolean value that determines whether the session should use HTTP pipelining. _(deprecated)_
- [connectionProxyDictionary](connectionproxydictionary.md) — A dictionary containing information about the proxy to use within this session.

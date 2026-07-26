---
title: 'noProxiesPreferred(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparametersprovider/noproxiespreferred(_:)-ostv'
source_url: 'https://developer.apple.com/documentation/network/nwparametersprovider/noproxiespreferred(_:)-ostv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparametersprovider/noproxiespreferred%28_%3A%29-ostv.json'
content_hash: 'sha256:b8dc9b24ad92ac59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParametersProvider](../nwparametersprovider.md)

# noProxiesPreferred(_:)

<sub>Instance Method</sub>

Prefer not using proxies when making connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func noProxiesPreferred(_ noProxies: Bool) -> Self
```

## Parameters

- `noProxies` — True if connections should not use proxies, false otherwise.

## Discussion

Attempt connections without using proxies, only using any configured proxies if the connection cannot otherwise be completed.

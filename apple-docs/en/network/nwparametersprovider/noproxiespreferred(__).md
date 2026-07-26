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
doc_path: '/documentation/network/nwparametersprovider/noproxiespreferred(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwparametersprovider/noproxiespreferred(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparametersprovider/noproxiespreferred%28_%3A%29.json'
content_hash: 'sha256:edfff95812781299'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParametersProvider](../nwparametersprovider.md)

# noProxiesPreferred(_:)

<sub>Instance Method</sub>

Prefer not using proxies when making connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func noProxiesPreferred(_ preferred: Bool) -> Self
```

## Discussion

Attempt connections without using proxies, only using any configured proxies if the connection cannot otherwise be completed.

## Default Implementations

### NWParametersProvider Implementations

- [noProxiesPreferred(_:)](<noproxiespreferred(__)-ostv.md>) — Prefer not using proxies when making connections.

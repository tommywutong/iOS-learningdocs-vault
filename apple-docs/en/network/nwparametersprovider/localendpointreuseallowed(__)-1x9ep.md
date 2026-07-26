---
title: 'localEndpointReuseAllowed(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparametersprovider/localendpointreuseallowed(_:)-1x9ep'
source_url: 'https://developer.apple.com/documentation/network/nwparametersprovider/localendpointreuseallowed(_:)-1x9ep'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparametersprovider/localendpointreuseallowed%28_%3A%29-1x9ep.json'
content_hash: 'sha256:9a8c5308317dfe18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParametersProvider](../nwparametersprovider.md)

# localEndpointReuseAllowed(_:)

<sub>Instance Method</sub>

Allow local endpoint reuse.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localEndpointReuseAllowed(_ allowed: Bool) -> Self
```

## Parameters

- `allowed` — True if allowed, false otherwise.

## Discussion

Allow multiple connections to use the same local address and port (`SO_REUSEADDR` and `SO_REUSEPORT`).

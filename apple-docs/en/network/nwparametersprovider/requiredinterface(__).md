---
title: 'requiredInterface(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparametersprovider/requiredinterface(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwparametersprovider/requiredinterface(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparametersprovider/requiredinterface%28_%3A%29.json'
content_hash: 'sha256:e11d00bff4f76583'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParametersProvider](../nwparametersprovider.md)

# requiredInterface(_:)

<sub>Instance Method</sub>

Require an interface when connecting, listening, and browsing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func requiredInterface(_ interface: NWInterface) -> Self
```

## Parameters

- `interface` — The interface to require.

## Discussion

Connections will fail if this interface is not available.

## Default Implementations

### NWParametersProvider Implementations

- [requiredInterface(_:)](<requiredinterface(__)-tfqe.md>) — Require an interface when connecting, listening, and browsing.

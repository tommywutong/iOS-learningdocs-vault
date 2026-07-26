---
title: 'localEndpoint(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparametersprovider/localendpoint(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwparametersprovider/localendpoint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparametersprovider/localendpoint%28_%3A%29.json'
content_hash: 'sha256:c6a529345ed1e8df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParametersProvider](../nwparametersprovider.md)

# localEndpoint(_:)

<sub>Instance Method</sub>

Specify a specific endpoint to use as the local endpoint.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localEndpoint(_ endpoint: NWEndpoint?) -> Self
```

## Parameters

- `endpoint` — The local endpoint to require, or `nil` if none.

## Discussion

For connections, this will be used to initiate traffic; for listeners, this will be used for receiving incoming connections.

## Default Implementations

### NWParametersProvider Implementations

- [localEndpoint(_:)](<localendpoint(__)-64i45.md>) — Specify a specific endpoint to use as the local endpoint.

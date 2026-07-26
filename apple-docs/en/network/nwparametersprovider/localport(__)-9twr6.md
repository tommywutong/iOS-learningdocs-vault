---
title: 'localPort(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparametersprovider/localport(_:)-9twr6'
source_url: 'https://developer.apple.com/documentation/network/nwparametersprovider/localport(_:)-9twr6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparametersprovider/localport%28_%3A%29-9twr6.json'
content_hash: 'sha256:e884608ba2f34138'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParametersProvider](../nwparametersprovider.md)

# localPort(_:)

<sub>Instance Method</sub>

Specify a specific port to use as the local endpoint, letting the system select the address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localPort(_ port: NWEndpoint.Port) -> Self
```

## Parameters

- `port` — The local port to require. Force a specific local port to be used.

## Discussion

For connections, this will be used to initiate traffic; for listeners, this will be used for receiving incoming connections.

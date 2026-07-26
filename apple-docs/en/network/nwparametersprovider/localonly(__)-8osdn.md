---
title: 'localOnly(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparametersprovider/localonly(_:)-8osdn'
source_url: 'https://developer.apple.com/documentation/network/nwparametersprovider/localonly(_:)-8osdn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparametersprovider/localonly%28_%3A%29-8osdn.json'
content_hash: 'sha256:eb3ea27ecc4d1739'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParametersProvider](../nwparametersprovider.md)

# localOnly(_:)

<sub>Instance Method</sub>

Limit inbound connections to peers attached to the local link.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func localOnly(_ local: Bool) -> Self
```

## Parameters

- `local` — True if limited to local peers, false otherwise.

## Discussion

Listeners will only advertise services on the local link and will only accept connections from the local link.

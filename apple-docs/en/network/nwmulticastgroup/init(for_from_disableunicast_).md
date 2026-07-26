---
title: 'init(for:from:disableUnicast:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwmulticastgroup/init(for:from:disableunicast:)'
source_url: 'https://developer.apple.com/documentation/network/nwmulticastgroup/init(for:from:disableunicast:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwmulticastgroup/init%28for%3Afrom%3Adisableunicast%3A%29.json'
content_hash: 'sha256:af7fa7358db1b3ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWMulticastGroup](../nwmulticastgroup.md)

# init(for:from:disableUnicast:)

<sub>Initializer</sub>

Initializes a multicast group with a set of multicast addresses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(for groupAddresses: [NWEndpoint], from: NWEndpoint? = nil, disableUnicast: Bool = false) throws
```

## Parameters

- `groupAddresses` — A set of multicast address endpoints you specify to define the IP multicast groups to join. The port indicates which local port the connection group will use to receive messages.

- `from` — An optional address endpoint used to filter received multicast packets.

- `disableUnicast` — A Boolean that specifies whether the connection group rejects unicast traffic.

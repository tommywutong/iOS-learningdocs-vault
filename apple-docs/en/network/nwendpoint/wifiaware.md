---
title: wifiAware
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.4+, iPadOS 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwendpoint/wifiaware
source_url: 'https://developer.apple.com/documentation/network/nwendpoint/wifiaware'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwendpoint/wifiaware.json'
content_hash: 'sha256:62dc583034d54ac1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEndpoint](../nwendpoint.md)

# wifiAware

<sub>Instance Property</sub>

Get an `WAEndpoint` that can connect to this `NWEndpoint`’s remote device over Wi-Fi Aware, or `nil` if the `NWEndpoint` is not compatible with Wi-Fi Aware.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var wifiAware: WAEndpoint? { get }
```

## Return Value

A new endpoint that can be used to connect over Wi-Fi Aware, or `nil` if it not compatible with Wi-Fi Aware.

## Discussion

The returned endpoint can be used to connect to a remote `NetworkListener` that accepts additional Wi-Fi Aware connections without publishing a service, via  `WiFiAware/WAPublisherListener/Action/addingConnections(from:)`

The returned endpoint will use Wi-Fi Aware as a transport.

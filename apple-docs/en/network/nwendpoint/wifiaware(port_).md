---
title: 'wifiAware(port:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.4+, iPadOS 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwendpoint/wifiaware(port:)'
source_url: 'https://developer.apple.com/documentation/network/nwendpoint/wifiaware(port:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwendpoint/wifiaware%28port%3A%29.json'
content_hash: 'sha256:1c8b141b01bad398'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEndpoint](../nwendpoint.md)

# wifiAware(port:)

<sub>Instance Method</sub>

Get an `WAEndpoint` that can connect to this `NWEndpoint`’s remote device over Wi-Fi Aware on the specified port, or `nil` if the `NWEndpoint` is not compatible with Wi-Fi Aware.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func wifiAware(port: NWEndpoint.Port) -> WAEndpoint?
```

## Parameters

- `port` — The port to use for this endpoint.

## Return Value

A new endpoint that can be used to connect over Wi-Fi Aware, or `nil` if it not compatible with Wi-Fi Aware.

## Discussion

The returned endpoint can be used to connect to a remote `NetworkListener` that accepts additional Wi-Fi Aware connections without publishing a service, via  `WiFiAware/WAPublisherListener/Action/addingConnections(from:)`

The returned endpoint will use Wi-Fi Aware as a transport.

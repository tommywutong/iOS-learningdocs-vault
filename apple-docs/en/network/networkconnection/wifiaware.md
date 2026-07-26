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
doc_path: /documentation/network/networkconnection/wifiaware
source_url: 'https://developer.apple.com/documentation/network/networkconnection/wifiaware'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkconnection/wifiaware.json'
content_hash: 'sha256:523235711a1e3be1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkConnection](../networkconnection.md)

# wifiAware

<sub>Instance Property</sub>

Get the current connection information for Wi-Fi Aware if the connection is over Wi-Fi Aware, `nil` if it’s not over Wi-Fi Aware.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
final var wifiAware: WAConnection<ApplicationProtocol>? { get }
```

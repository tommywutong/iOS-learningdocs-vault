---
title: wifiAware
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwpath/wifiaware
source_url: 'https://developer.apple.com/documentation/network/nwpath/wifiaware'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpath/wifiaware.json'
content_hash: 'sha256:5c5ec93602192a2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWPath](../nwpath.md)

# wifiAware

<sub>Instance Property</sub>

Current status and performance information for Wi-Fi Aware, or `nil` if this path is not over Wi-Fi Aware.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var wifiAware: WAPath? { get async throws }
```

## Discussion

> [!danger] Throws
> An error if the path could not be retrieved, or if the App does not have access to Wi-Fi Aware.

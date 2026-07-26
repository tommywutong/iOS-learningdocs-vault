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
doc_path: /documentation/network/nwparameters/wifiaware
source_url: 'https://developer.apple.com/documentation/network/nwparameters/wifiaware'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/wifiaware.json'
content_hash: 'sha256:eec495794211a8e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# wifiAware

<sub>Instance Property</sub>

Get and set Wi-Fi Aware specific connection parameters.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
final var wifiAware: WAParameters { get set }
```

## Discussion

If no Wi-Fi Aware specific properties were previously set, the `WAParameters/defaults` are assumed.

The following code is an example of creating the `NWParameters`, setting, and getting the WiFi Aware parameters.

```swift
// Create NWParameters
var networkParameters = NWParameters()

// Set Wi-Fi Aware Parameters
networkParameters.wifiAware = .defaults

// Get Wi-Fi Aware Parameters
let wifiAwareParameters = networkParameters.wifiAware
```

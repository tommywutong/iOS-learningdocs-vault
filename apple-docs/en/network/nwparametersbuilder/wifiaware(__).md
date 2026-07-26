---
title: 'wifiAware(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparametersbuilder/wifiaware(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwparametersbuilder/wifiaware(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparametersbuilder/wifiaware%28_%3A%29.json'
content_hash: 'sha256:3fe53d0bc0ea2f3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParametersBuilder](../nwparametersbuilder.md)

# wifiAware(_:)

<sub>Instance Method</sub>

Configure Wi-Fi Aware properties on an `NetworkConnection`

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func wifiAware(_ configurator: (inout WAParameters) -> Void) -> NWParametersBuilder<Top, repeat each P>
```

## Parameters

- `configurator` — The function that will apply the desired `WAParameters` to the network parameters.

## Return Value

The updated parameters, with the configured Wi-Fi Aware parameters applied.

## Discussion

If not previously set, parameters will have `WAParameters/defaults` applied initially.

Example:

```swift
let connection = NetworkConnection(to: endpoint, using: .parameters {
	UDP()
}.wifiAware {
	$0 = .defaults
}
```

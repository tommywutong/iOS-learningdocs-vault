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
doc_path: '/documentation/network/nwparameters/wifiaware(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwparameters/wifiaware(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/wifiaware%28_%3A%29.json'
content_hash: 'sha256:2fb233610b37a75a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# wifiAware(_:)

<sub>Instance Method</sub>

Configure Wi-Fi Aware properties on an `NWParameters` object.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
final func wifiAware(_ configurator: (inout WAParameters) -> Void) -> Self
```

## Parameters

- `configurator` — The function that will apply the desired `WAParameters` to the network parameters.

## Return Value

The updated parameters, with the configured Wi-Fi Aware parameters applied.

## Discussion

If not previously set, parameters will have `WAParameters/defaults` applied initially.

Example:

```swift
// Create NWParameters & apply wifiAware parameters
let networkParameters = NWParameters().wifiAware {
	$0 = .defaults
}
```

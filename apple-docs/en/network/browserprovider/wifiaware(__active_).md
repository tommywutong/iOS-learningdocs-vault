---
title: 'wifiAware(_:active:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/browserprovider/wifiaware(_:active:)'
source_url: 'https://developer.apple.com/documentation/network/browserprovider/wifiaware(_:active:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/browserprovider/wifiaware%28_%3Aactive%3A%29.json'
content_hash: 'sha256:4f6520dea1af3a35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [BrowserProvider](../browserprovider.md)

# wifiAware(_:active:)

<sub>Type Method</sub>

Setup a `NetworkBrowser` to subscribe to Wi-Fi Aware services on selected, paired devices.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static func wifiAware(_ action: WASubscriberBrowser.Action, active requestedDuration: Duration? = nil) -> Self
```

## Parameters

- `action` — The specific Wi-Fi Aware operation to perform, and the service & devices to perform it on.

- `requestedDuration` — Optional duration requested to keep the `NetworkBrowser` subscribing. The default value of `nil` instructs the system to stay active for long enough to guarantee the action completes with all nearby target devices.

## Return Value

A new `BrowserProvider` containing the `.wifiAware()` instruction that will configure a `NetworkBrowser` as a Wi-Fi Aware subscriber.

## Discussion

Example:

```swift
NetworkBrowser(for: .wifiAware(.connecting(to:.selected(devices), from:service)) )
```

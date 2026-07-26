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
doc_path: '/documentation/network/listenerprovider/wifiaware(_:active:)'
source_url: 'https://developer.apple.com/documentation/network/listenerprovider/wifiaware(_:active:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/listenerprovider/wifiaware%28_%3Aactive%3A%29.json'
content_hash: 'sha256:25d17e67ad2e385e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [ListenerProvider](../listenerprovider.md)

# wifiAware(_:active:)

<sub>Type Method</sub>

Sets a network listener to publish Wi-Fi Aware services to the selected paired devices.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static func wifiAware(_ action: WAPublisherListener.Action, active requestedDuration: Duration? = nil) -> Self
```

## Parameters

- `action` — The specific Wi-Fi Aware operation to perform, and the service & devices to perform it on.

- `requestedDuration` — Optional duration requested to keep the `NetworkListener` publishing. The default value of `nil` instructs the system to stay active for long enough to guarantee the action completes with all nearby target devices.

## Return Value

A new `ListenerProvider` containing the `.wifiAware()` instruction that will configure a `NetworkListener` as a Wi-Fi Aware publisher.

## Discussion

The code below is an example of how to set the `NetworkListener`:

```swift
NetworkListener(for: .wifiAware(.connecting(to:service, from:.selected(devices))) )
```

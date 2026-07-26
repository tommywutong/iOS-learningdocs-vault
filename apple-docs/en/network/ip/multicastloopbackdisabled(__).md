---
title: 'multicastLoopbackDisabled(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/ip/multicastloopbackdisabled(_:)'
source_url: 'https://developer.apple.com/documentation/network/ip/multicastloopbackdisabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ip/multicastloopbackdisabled%28_%3A%29.json'
content_hash: 'sha256:e273305b15c2cc03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IP](../ip.md)

# multicastLoopbackDisabled(_:)

<sub>Instance Method</sub>

Specify if multicast packets should be looped back for local delivery.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func multicastLoopbackDisabled(_ disableMulticastLoopback: Bool) -> IP
```

## Parameters

- `disableMulticastLoopback` — True to disable multicast loopback, false otherwise.

## Discussion

By default, a multicast packet sent to a group to which the sending host itself belongs will be looped back for local delivery. `disableMulticastLoopback` disables this behavior and, if set, multicast packets will not be looped back to the sender.

> [!note] Note
> Only applies to multicast packets.

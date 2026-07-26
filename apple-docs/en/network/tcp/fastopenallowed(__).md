---
title: 'fastOpenAllowed(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tcp/fastopenallowed(_:)'
source_url: 'https://developer.apple.com/documentation/network/tcp/fastopenallowed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tcp/fastopenallowed%28_%3A%29.json'
content_hash: 'sha256:718647f2977c2954'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TCP](../tcp.md)

# fastOpenAllowed(_:)

<sub>Instance Method</sub>

Configure TCP to enable TCP Fast Open (TFO).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fastOpenAllowed(_ allowed: Bool) -> TCP
```

## Parameters

- `allowed` — True to allow TFO, false otherwise.

## Discussion

This may take effect even when TCP is not the top-level protocol in the protocol stack. For example, if TLS is running over TCP, the Client Hello message may be sent as fast open data.

If TCP is the top-level protocol in the stack (the one the application directly interacts with), TFO will be disabled unless the application indicated that it will provide its own fast open data by calling NWParameters.allowFastOpen.

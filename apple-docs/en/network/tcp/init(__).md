---
title: 'init(_:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/tcp/init(_:)'
source_url: 'https://developer.apple.com/documentation/network/tcp/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tcp/init%28_%3A%29.json'
content_hash: 'sha256:a2e87506a3c8240c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TCP](../tcp.md)

# init(_:)

<sub>Initializer</sub>

Create an instance of TCP.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(@ProtocolStackBuilder<IP> _ builder: () -> IP)
```

## Parameters

- `builder` — The protocol stack below TCP. Defaults to `IP()`.

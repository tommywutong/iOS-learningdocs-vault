---
title: 'init(for:using:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networklistener/init(for:using:)-2hkg'
source_url: 'https://developer.apple.com/documentation/network/networklistener/init(for:using:)-2hkg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networklistener/init%28for%3Ausing%3A%29-2hkg.json'
content_hash: 'sha256:f0c5a348fab00f7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkListener](../networklistener.md)

# init(for:using:)

<sub>Initializer</sub>

Create a listener that advertises a service with a protocol stack to use for listening.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(for provider: (any ListenerProvider)? = nil, @ProtocolStackBuilder<ApplicationProtocol> using builder: () -> ApplicationProtocol) throws
```

## Parameters

- `provider` — The listener provider to use for advertising the service.

- `builder` — The protocol stack to use for incoming connections.

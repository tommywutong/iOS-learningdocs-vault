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
doc_path: '/documentation/network/networklistener/init(for:using:)-2vh87'
source_url: 'https://developer.apple.com/documentation/network/networklistener/init(for:using:)-2vh87'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networklistener/init%28for%3Ausing%3A%29-2vh87.json'
content_hash: 'sha256:21bc962294b40236'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkListener](../networklistener.md)

# init(for:using:)

<sub>Initializer</sub>

Create a listener that advertises a service with a protocol stack and parameters to use for listening.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(for provider: (any ListenerProvider)? = nil, using builder: NWParametersBuilder<ApplicationProtocol>) throws
```

## Parameters

- `provider` — The listener provider to use for advertising the service.

- `builder` — The builder to use for constructing the protocol stack and parameters.

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
doc_path: '/documentation/network/networkbrowser/init(for:using:)'
source_url: 'https://developer.apple.com/documentation/network/networkbrowser/init(for:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkbrowser/init%28for%3Ausing%3A%29.json'
content_hash: 'sha256:d0410a4b874c3271'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkBrowser](../networkbrowser.md)

# init(for:using:)

<sub>Initializer</sub>

Create a browser that will browse for the service specified by a BrowserProvider, with parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(for provider: Provider, using parameters: NWParameters? = nil)
```

## Parameters

- `provider` — A BrowserProvider that describes the kind of service to browse for, the browse descriptor, and parameter configuration.

- `parameters` — The parameters that will be used while browsing.

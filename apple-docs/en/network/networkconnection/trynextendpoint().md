---
title: tryNextEndpoint()
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkconnection/trynextendpoint()
source_url: 'https://developer.apple.com/documentation/network/networkconnection/trynextendpoint()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkconnection/trynextendpoint%28%29.json'
content_hash: 'sha256:b7f63146b4eb8d9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkConnection](../networkconnection.md)

# tryNextEndpoint()

<sub>Instance Method</sub>

Cancel the currently connected endpoint, causing the connection to fall through to the next endpoint if available, or to go to the waiting state if no more endpoints are available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func tryNextEndpoint()
```

---
title: 'run(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkbrowser/run(_:)-wqyo'
source_url: 'https://developer.apple.com/documentation/network/networkbrowser/run(_:)-wqyo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkbrowser/run%28_%3A%29-wqyo.json'
content_hash: 'sha256:e3a5baa140448675'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkBrowser](../networkbrowser.md)

# run(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func run<Return>(_ handler: @escaping @isolated(any) @Sendable ([Provider.Endpoint]) async throws -> NetworkBrowser<Provider>.RunResult<Return>) async throws -> Return
```

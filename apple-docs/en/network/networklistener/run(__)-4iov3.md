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
doc_path: '/documentation/network/networklistener/run(_:)-4iov3'
source_url: 'https://developer.apple.com/documentation/network/networklistener/run(_:)-4iov3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networklistener/run%28_%3A%29-4iov3.json'
content_hash: 'sha256:14c7e1d3241f1a8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkListener](../networklistener.md)

# run(_:)

<sub>Instance Method</sub>

Run the listener and receive incoming connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func run(_ handler: @escaping @isolated(any) @Sendable (NetworkConnection<ApplicationProtocol>) async throws -> Void) async throws
```

## Parameters

- `handler` — A handler to receive incoming connections.

## Discussion

When the listener state moves to ready, the listener is registered with the system and can receive incoming connections.

`run()` should only be called once on a listener, and multiple calls to `run()` will throw an exception.

The closure inherits the isolation domain of the caller.

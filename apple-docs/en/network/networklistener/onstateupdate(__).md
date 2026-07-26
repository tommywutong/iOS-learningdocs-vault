---
title: 'onStateUpdate(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networklistener/onstateupdate(_:)'
source_url: 'https://developer.apple.com/documentation/network/networklistener/onstateupdate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networklistener/onstateupdate%28_%3A%29.json'
content_hash: 'sha256:0035575c67be9bf2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkListener](../networklistener.md)

# onStateUpdate(_:)

<sub>Instance Method</sub>

Set a closure to be called when the listener’s state changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult final func onStateUpdate(_ handler: @escaping @isolated(any) @Sendable (NetworkListener<ApplicationProtocol>, NetworkListener<ApplicationProtocol>.State) -> Void) -> Self
```

## Parameters

- `handler` — A handler to be called with state updates.

## Discussion

The closure may be called multiple times until the listener is cancelled.

The closure inherits the isolation domain of the caller.

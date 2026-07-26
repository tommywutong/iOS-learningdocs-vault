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
doc_path: '/documentation/network/networkbrowser/onstateupdate(_:)'
source_url: 'https://developer.apple.com/documentation/network/networkbrowser/onstateupdate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkbrowser/onstateupdate%28_%3A%29.json'
content_hash: 'sha256:4eaa40c1e467d6cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkBrowser](../networkbrowser.md)

# onStateUpdate(_:)

<sub>Instance Method</sub>

Set a closure to be called when the browser’s state changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult final func onStateUpdate(_ handler: @escaping @isolated(any) @Sendable (NetworkBrowser<Provider>, NetworkBrowser<Provider>.State) -> Void) -> Self
```

## Discussion

The closure may be called multiple times until the browser is cancelled.

The closure inherits the isolation domain of the caller.

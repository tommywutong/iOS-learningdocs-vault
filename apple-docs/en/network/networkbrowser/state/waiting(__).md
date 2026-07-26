---
title: 'NetworkBrowser.State.waiting(_:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkbrowser/state/waiting(_:)'
source_url: 'https://developer.apple.com/documentation/network/networkbrowser/state/waiting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkbrowser/state/waiting%28_%3A%29.json'
content_hash: 'sha256:a0f7063f76326170'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NetworkBrowser](../../networkbrowser.md) · [State](../state.md)

# NetworkBrowser.State.waiting(_:)

<sub>Case</sub>

The browser is waiting for connectivity. Results will not be delivered until the browser moves into the ready state. A browser can move from the ready state into the waiting state. The associated error indicates why the browser is unable to browse.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case waiting(NWError)
```

---
title: NetworkBrowser.State
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkbrowser/state
source_url: 'https://developer.apple.com/documentation/network/networkbrowser/state'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkbrowser/state.json'
content_hash: 'sha256:8be435fa24af367b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkBrowser](../networkbrowser.md)

# NetworkBrowser.State

<sub>Enumeration</sub>

Possible states for the browser to be in.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum State
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [NetworkBrowser.State.cancelled](state/cancelled.md) — The browser has been cancelled. Do not call `start()` on the browser to restart it. Instead, create a new browser.
- [NetworkBrowser.State.failed(_:)](<state/failed(__).md>) — The browser has irrecoverably failed. Do not call `start()` on the browser to restart it. Instead, `cancel()` the browser and create a new browser.
- [NetworkBrowser.State.ready](state/ready.md) — The browser is active and will monitor services on the network. Set the `browseResultsChangedHandler` to get updates for these services.
- [NetworkBrowser.State.setup](state/setup.md) — The browser has been created but not started. Set any relevant callback handlers on the browser before calling `start()`.
- [NetworkBrowser.State.waiting(_:)](<state/waiting(__).md>) — The browser is waiting for connectivity. Results will not be delivered until the browser moves into the ready state. A browser can move from the ready state into the waiting state. The associated error indicates why the browser is unable to browse.

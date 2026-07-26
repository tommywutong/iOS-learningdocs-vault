---
title: NWBrowser.State
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwbrowser/state-swift.enum
source_url: 'https://developer.apple.com/documentation/network/nwbrowser/state-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwbrowser/state-swift.enum.json'
content_hash: 'sha256:5515b961f9a5b08c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWBrowser](../nwbrowser.md)

# NWBrowser.State

<sub>Enumeration</sub>

States indicating whether a browser is able to discover services.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum State
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### States

- [NWBrowser.State.setup](state-swift.enum/setup.md) — The browser has been initialized but not started.
- [NWBrowser.State.ready](state-swift.enum/ready.md) — The browser is registered for discovering services.
- [NWBrowser.State.failed(_:)](<state-swift.enum/failed(__).md>) — The browser has encountered a fatal error.
- [NWBrowser.State.cancelled](state-swift.enum/cancelled.md) — The browser has been canceled.

### Enumeration Cases

- [NWBrowser.State.waiting(_:)](<state-swift.enum/waiting(__).md>)

## See Also

### Managing Browsers

- [stateUpdateHandler](stateupdatehandler.md) — A handler that receives browser state updates.
- [state](state-swift.property.md) — The current state of the browser.
- [cancel()](<cancel().md>) — Stops browsing for services.

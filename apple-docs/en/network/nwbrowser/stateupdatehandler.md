---
title: stateUpdateHandler
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwbrowser/stateupdatehandler
source_url: 'https://developer.apple.com/documentation/network/nwbrowser/stateupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwbrowser/stateupdatehandler.json'
content_hash: 'sha256:ae0638bb0609513c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWBrowser](../nwbrowser.md)

# stateUpdateHandler

<sub>Instance Property</sub>

A handler that receives browser state updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final var stateUpdateHandler: (@Sendable (NWBrowser.State) -> Void)? { get set }
```

## See Also

### Managing Browsers

- [State](state-swift.enum.md) — States indicating whether a browser is able to discover services.
- [state](state-swift.property.md) — The current state of the browser.
- [cancel()](<cancel().md>) — Stops browsing for services.

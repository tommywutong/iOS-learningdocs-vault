---
title: state
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwbrowser/state-swift.property
source_url: 'https://developer.apple.com/documentation/network/nwbrowser/state-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwbrowser/state-swift.property.json'
content_hash: 'sha256:76352b6c736fc01d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWBrowser](../nwbrowser.md)

# state

<sub>Instance Property</sub>

The current state of the browser.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var state: NWBrowser.State { get }
```

## See Also

### Managing Browsers

- [stateUpdateHandler](stateupdatehandler.md) — A handler that receives browser state updates.
- [State](state-swift.enum.md) — States indicating whether a browser is able to discover services.
- [cancel()](<cancel().md>) — Stops browsing for services.

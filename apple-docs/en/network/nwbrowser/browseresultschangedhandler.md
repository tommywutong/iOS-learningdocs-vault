---
title: browseResultsChangedHandler
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwbrowser/browseresultschangedhandler
source_url: 'https://developer.apple.com/documentation/network/nwbrowser/browseresultschangedhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwbrowser/browseresultschangedhandler.json'
content_hash: 'sha256:6cfa6b69f05aa4b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWBrowser](../nwbrowser.md)

# browseResultsChangedHandler

<sub>Instance Property</sub>

A handler that delivers updates about discovered services.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final var browseResultsChangedHandler: (@Sendable (Set<NWBrowser.Result>, Set<NWBrowser.Result.Change>) -> Void)? { get set }
```

## See Also

### Browsing for Services

- [init(for:using:)](<init(for_using_).md>) — Initializes a browser with a type of service to discover.
- [Descriptor](descriptor-swift.enum.md) — A service description used to discover Bonjour services.
- [start(queue:)](<start(queue_).md>) — Starts browsing for services, and sets the queue on which all browser events will be delivered.
- [Result](result.md) — A set of discovered services and changes from the last result.
- [browseResults](browseresults.md) — The list of discovered services.

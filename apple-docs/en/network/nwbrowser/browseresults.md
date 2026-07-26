---
title: browseResults
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwbrowser/browseresults
source_url: 'https://developer.apple.com/documentation/network/nwbrowser/browseresults'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwbrowser/browseresults.json'
content_hash: 'sha256:c7563f9953c595dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWBrowser](../nwbrowser.md)

# browseResults

<sub>Instance Property</sub>

The list of discovered services.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var browseResults: Set<NWBrowser.Result> { get }
```

## See Also

### Browsing for Services

- [init(for:using:)](<init(for_using_).md>) — Initializes a browser with a type of service to discover.
- [Descriptor](descriptor-swift.enum.md) — A service description used to discover Bonjour services.
- [start(queue:)](<start(queue_).md>) — Starts browsing for services, and sets the queue on which all browser events will be delivered.
- [browseResultsChangedHandler](browseresultschangedhandler.md) — A handler that delivers updates about discovered services.
- [Result](result.md) — A set of discovered services and changes from the last result.

---
title: 'init(for:using:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwbrowser/init(for:using:)'
source_url: 'https://developer.apple.com/documentation/network/nwbrowser/init(for:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwbrowser/init%28for%3Ausing%3A%29.json'
content_hash: 'sha256:f44f0daefd4deb6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWBrowser](../nwbrowser.md)

# init(for:using:)

<sub>Initializer</sub>

Initializes a browser with a type of service to discover.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(for descriptor: NWBrowser.Descriptor, using parameters: NWParameters)
```

## See Also

### Browsing for Services

- [Descriptor](descriptor-swift.enum.md) — A service description used to discover Bonjour services.
- [start(queue:)](<start(queue_).md>) — Starts browsing for services, and sets the queue on which all browser events will be delivered.
- [browseResultsChangedHandler](browseresultschangedhandler.md) — A handler that delivers updates about discovered services.
- [Result](result.md) — A set of discovered services and changes from the last result.
- [browseResults](browseresults.md) — The list of discovered services.

---
title: 'start(queue:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwbrowser/start(queue:)'
source_url: 'https://developer.apple.com/documentation/network/nwbrowser/start(queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwbrowser/start%28queue%3A%29.json'
content_hash: 'sha256:85780be66138418d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWBrowser](../nwbrowser.md)

# start(queue:)

<sub>Instance Method</sub>

Starts browsing for services, and sets the queue on which all browser events will be delivered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func start(queue: DispatchQueue)
```

## See Also

### Browsing for Services

- [init(for:using:)](<init(for_using_).md>) — Initializes a browser with a type of service to discover.
- [Descriptor](descriptor-swift.enum.md) — A service description used to discover Bonjour services.
- [browseResultsChangedHandler](browseresultschangedhandler.md) — A handler that delivers updates about discovered services.
- [Result](result.md) — A set of discovered services and changes from the last result.
- [browseResults](browseresults.md) — The list of discovered services.

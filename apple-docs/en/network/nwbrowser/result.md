---
title: NWBrowser.Result
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwbrowser/result
source_url: 'https://developer.apple.com/documentation/network/nwbrowser/result'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwbrowser/result.json'
content_hash: 'sha256:7202d2e8e507852d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWBrowser](../nwbrowser.md)

# NWBrowser.Result

<sub>Structure</sub>

A set of discovered services and changes from the last result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Result
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Evaluating Browser Results

- [endpoint](result/endpoint.md) — The discovered service endpoint.
- [interfaces](result/interfaces.md) — The list of interfaces on which the service was discovered.
- [metadata](result/metadata-swift.property.md) — The metadata associated with the discovered service, such as the TXT record.
- [Metadata](result/metadata-swift.enum.md) — Values associated with discovered services, such as TXT records.
- [NWTXTRecord](../nwtxtrecord.md) — A dictionary representing a TXT record in a DNS packet.

### Comparing Results

- [Change](result/change.md) — Ways in which discovered services can change between specific results.

## See Also

### Browsing for Services

- [init(for:using:)](<init(for_using_).md>) — Initializes a browser with a type of service to discover.
- [Descriptor](descriptor-swift.enum.md) — A service description used to discover Bonjour services.
- [start(queue:)](<start(queue_).md>) — Starts browsing for services, and sets the queue on which all browser events will be delivered.
- [browseResultsChangedHandler](browseresultschangedhandler.md) — A handler that delivers updates about discovered services.
- [browseResults](browseresults.md) — The list of discovered services.

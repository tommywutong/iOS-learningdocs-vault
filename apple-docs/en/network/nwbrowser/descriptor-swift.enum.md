---
title: NWBrowser.Descriptor
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwbrowser/descriptor-swift.enum
source_url: 'https://developer.apple.com/documentation/network/nwbrowser/descriptor-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwbrowser/descriptor-swift.enum.json'
content_hash: 'sha256:b10c9f7b7a509e39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWBrowser](../nwbrowser.md)

# NWBrowser.Descriptor

<sub>Enumeration</sub>

A service description used to discover Bonjour services.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Descriptor
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Descriptor Types

- [NWBrowser.Descriptor.bonjour(type:domain:)](<descriptor-swift.enum/bonjour(type_domain_).md>) — A service descriptor used to discover a Bonjour service.
- [NWBrowser.Descriptor.bonjourWithTXTRecord(type:domain:)](<descriptor-swift.enum/bonjourwithtxtrecord(type_domain_).md>) — A service descriptor used to discover a Bonjour service with associated TXT records.

### Enumeration Cases

- [NWBrowser.Descriptor.applicationService(name:)](<descriptor-swift.enum/applicationservice(name_).md>) — Returns a browser descriptor for application services.

## See Also

### Browsing for Services

- [init(for:using:)](<init(for_using_).md>) — Initializes a browser with a type of service to discover.
- [start(queue:)](<start(queue_).md>) — Starts browsing for services, and sets the queue on which all browser events will be delivered.
- [browseResultsChangedHandler](browseresultschangedhandler.md) — A handler that delivers updates about discovered services.
- [Result](result.md) — A set of discovered services and changes from the last result.
- [browseResults](browseresults.md) — The list of discovered services.

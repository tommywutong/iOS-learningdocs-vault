---
title: NWBrowser.Result.Metadata
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwbrowser/result/metadata-swift.enum
source_url: 'https://developer.apple.com/documentation/network/nwbrowser/result/metadata-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwbrowser/result/metadata-swift.enum.json'
content_hash: 'sha256:e79fc7a4aca8af2c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWBrowser](../../nwbrowser.md) · [Result](../result.md)

# NWBrowser.Result.Metadata

<sub>Enumeration</sub>

Values associated with discovered services, such as TXT records.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Metadata
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../../../swift/customdebugstringconvertible.md), [Equatable](../../../swift/equatable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Metadata Types

- [NWBrowser.Result.Metadata.bonjour(_:)](<metadata-swift.enum/bonjour(__).md>) — A TXT record associated with a discovered service.
- [NWBrowser.Result.Metadata.none](metadata-swift.enum/none.md) — A value indicating that no associated data was discovered on a service.

## See Also

### Evaluating Browser Results

- [endpoint](endpoint.md) — The discovered service endpoint.
- [interfaces](interfaces.md) — The list of interfaces on which the service was discovered.
- [metadata](metadata-swift.property.md) — The metadata associated with the discovered service, such as the TXT record.
- [NWTXTRecord](../../nwtxtrecord.md) — A dictionary representing a TXT record in a DNS packet.

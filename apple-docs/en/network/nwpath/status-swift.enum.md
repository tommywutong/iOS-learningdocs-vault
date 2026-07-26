---
title: NWPath.Status
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwpath/status-swift.enum
source_url: 'https://developer.apple.com/documentation/network/nwpath/status-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpath/status-swift.enum.json'
content_hash: 'sha256:5edb9c1296b17d72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWPath](../nwpath.md)

# NWPath.Status

<sub>Enumeration</sub>

Status values indicating whether a path can be used by connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Status
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Status Values

- [NWPath.Status.unsatisfied](status-swift.enum/unsatisfied.md) — The path is not available for use.
- [NWPath.Status.satisfied](status-swift.enum/satisfied.md) — The path is available to establish connections and send data.
- [NWPath.Status.requiresConnection](status-swift.enum/requiresconnection.md) — The path is not currently available, but establishing a new connection may activate the path.

## See Also

### Checking Path Availability

- [status](status-swift.property.md) — A status indicating whether a path can be used by connections.

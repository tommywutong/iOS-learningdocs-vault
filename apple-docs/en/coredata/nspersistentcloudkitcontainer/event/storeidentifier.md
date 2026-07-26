---
title: storeIdentifier
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcloudkitcontainer/event/storeidentifier
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/event/storeidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainer/event/storeidentifier.json'
content_hash: 'sha256:0739d7088c0f5422'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Data](../../../coredata.md) · [NSPersistentCloudKitContainer](../../nspersistentcloudkitcontainer.md) · [Event](../event.md)

# storeIdentifier

<sub>Instance Property</sub>

The associated store identifier in the container for the event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var storeIdentifier: String { get }
```

## See Also

### Inspecting Event Properties

- [type](type.md) — The type of event, either setup, import, or export.
- [identifier](identifier.md) — A unique identifier for the event in a container.
- [succeeded](succeeded.md) — A Boolean value that indicates whether the operation the event represents is successful.
- [startDate](startdate.md) — The start date of the operation that the event represents.
- [endDate](enddate.md) — The end date of the operation that the event represents.
- [error](error.md) — An error that indicates why an operation fails.

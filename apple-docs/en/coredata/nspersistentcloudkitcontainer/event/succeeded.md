---
title: succeeded
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcloudkitcontainer/event/succeeded
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/event/succeeded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainer/event/succeeded.json'
content_hash: 'sha256:8f3974c3b08b1f95'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Data](../../../coredata.md) · [NSPersistentCloudKitContainer](../../nspersistentcloudkitcontainer.md) · [Event](../event.md)

# succeeded

<sub>Instance Property</sub>

A Boolean value that indicates whether the operation the event represents is successful.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var succeeded: Bool { get }
```

## See Also

### Inspecting Event Properties

- [type](type.md) — The type of event, either setup, import, or export.
- [identifier](identifier.md) — A unique identifier for the event in a container.
- [storeIdentifier](storeidentifier.md) — The associated store identifier in the container for the event.
- [startDate](startdate.md) — The start date of the operation that the event represents.
- [endDate](enddate.md) — The end date of the operation that the event represents.
- [error](error.md) — An error that indicates why an operation fails.

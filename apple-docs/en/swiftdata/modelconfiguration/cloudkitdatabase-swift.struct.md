---
title: ModelConfiguration.CloudKitDatabase
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelconfiguration/cloudkitdatabase-swift.struct
source_url: 'https://developer.apple.com/documentation/swiftdata/modelconfiguration/cloudkitdatabase-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelconfiguration/cloudkitdatabase-swift.struct.json'
content_hash: 'sha256:d75519830032d362'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelConfiguration](../modelconfiguration.md)

# ModelConfiguration.CloudKitDatabase

<sub>Structure</sub>

A type that describes the options for detecting a CloudKit database.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CloudKitDatabase
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting discovery options

- [automatic](cloudkitdatabase-swift.struct/automatic.md) — Enables managed CloudKit sync using the primary ubiquity container from the app’s entitlements.
- [private(_:)](<cloudkitdatabase-swift.struct/private(__).md>) — Enables managed CloudKit sync using the specified ubiquity container.
- [none](cloudkitdatabase-swift.struct/none.md) — Disables managed CloudKit sync.

## See Also

### Sharing and syncing the model store

- [cloudKitContainerIdentifier](cloudkitcontaineridentifier.md) — The identifier of the configuration’s CloudKit database container.
- [cloudKitDatabase](cloudkitdatabase-swift.property.md) — The option to use when detecting the container of the preferred CloudKit database.
- [groupAppContainerIdentifier](groupappcontaineridentifier.md) — The identifier of the configuration’s app group container.
- [groupContainer](groupcontainer-swift.property.md) — The option to use when detecting the preferred app group container.
- [GroupContainer](groupcontainer-swift.struct.md) — A type that describes the options for detecting an app group container.

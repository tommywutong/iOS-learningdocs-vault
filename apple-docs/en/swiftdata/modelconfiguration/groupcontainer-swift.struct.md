---
title: ModelConfiguration.GroupContainer
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelconfiguration/groupcontainer-swift.struct
source_url: 'https://developer.apple.com/documentation/swiftdata/modelconfiguration/groupcontainer-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelconfiguration/groupcontainer-swift.struct.json'
content_hash: 'sha256:589dfdfd4a6ac612'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelConfiguration](../modelconfiguration.md)

# ModelConfiguration.GroupContainer

<sub>Structure</sub>

A type that describes the options for detecting an app group container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct GroupContainer
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting discovery options

- [automatic](groupcontainer-swift.struct/automatic.md) — Tells SwiftData to use the app’s primary group container as the root location for the persistent storage.
- [identifier(_:)](<groupcontainer-swift.struct/identifier(__).md>) — Tells SwiftData to use the specified group container as the root location for the app’s persistent storage.
- [none](groupcontainer-swift.struct/none.md) — Prevents SwiftData from using a group container as the root location for the app’s persistent storage.

## See Also

### Sharing and syncing the model store

- [cloudKitContainerIdentifier](cloudkitcontaineridentifier.md) — The identifier of the configuration’s CloudKit database container.
- [cloudKitDatabase](cloudkitdatabase-swift.property.md) — The option to use when detecting the container of the preferred CloudKit database.
- [CloudKitDatabase](cloudkitdatabase-swift.struct.md) — A type that describes the options for detecting a CloudKit database.
- [groupAppContainerIdentifier](groupappcontaineridentifier.md) — The identifier of the configuration’s app group container.
- [groupContainer](groupcontainer-swift.property.md) — The option to use when detecting the preferred app group container.

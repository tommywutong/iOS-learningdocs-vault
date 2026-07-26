---
title: NSPersistentCloudKitContainerOptions
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcloudkitcontaineroptions
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontaineroptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontaineroptions.json'
content_hash: 'sha256:3f4edb33b30bbec9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentCloudKitContainerOptions

<sub>Class</sub>

An object that customizes how a store description aligns with a CloudKit database.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPersistentCloudKitContainerOptions
```

## Overview

Use [NSPersistentCloudKitContainerOptions](nspersistentcloudkitcontaineroptions.md) to customize the behavior of an [NSPersistentCloudKitContainer](nspersistentcloudkitcontainer.md) or to create additional store descriptions that sync to other containers.

For more information about setting up multiple stores, see [Setting Up Core Data with CloudKit](setting-up-core-data-with-cloudkit.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating Container Options

- [- initWithContainerIdentifier:](<nspersistentcloudkitcontaineroptions/init(containeridentifier_).md>) — Initializes container options using the given CloudKit container identifier.
- [containerIdentifier](nspersistentcloudkitcontaineroptions/containeridentifier.md) — The identifier of the CloudKit container associated with a given store description.
- [databaseScope](nspersistentcloudkitcontaineroptions/databasescope-4c72t.md) — The database scope — public, private, or shared — to use for a specified store in a persistent CloudKit container.

## See Also

### CloudKit mirroring

- [Mirroring a Core Data store with CloudKit](mirroring-a-core-data-store-with-cloudkit.md) — Back user interfaces with a local replica of a CloudKit private database.
- [Synchronizing a local store to the cloud](synchronizing-a-local-store-to-the-cloud.md) — Share data between a user’s devices and other iCloud users.
- [NSPersistentCloudKitContainer](nspersistentcloudkitcontainer.md) — A container that encapsulates the Core Data stack in your app, and mirrors select persistent stores to a CloudKit private database.
- [Sharing Core Data objects between iCloud users](sharing-core-data-objects-between-icloud-users.md) — Use Core Data and CloudKit to synchronize data between devices of an iCloud user and share data between different iCloud users.

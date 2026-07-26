---
title: NSPersistentCloudKitContainer
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcloudkitcontainer
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainer.json'
content_hash: 'sha256:76331eca00370977'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentCloudKitContainer

<sub>Class</sub>

A container that encapsulates the Core Data stack in your app, and mirrors select persistent stores to a CloudKit private database.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPersistentCloudKitContainer
```

## Overview

[NSPersistentCloudKitContainer](nspersistentcloudkitcontainer.md) is a subclass of [NSPersistentContainer](nspersistentcontainer.md) capable of managing both CloudKit-backed and noncloud stores.

By default, [NSPersistentCloudKitContainer](nspersistentcloudkitcontainer.md) contains a single store description, which Core Data assigns to the first CloudKit container identifier in an app’s entitlements. Use [NSPersistentCloudKitContainerOptions](nspersistentcloudkitcontaineroptions.md) to customize this behavior or create additional store descriptions with backing by different containers.

For more information about setting up multiple stores, see [Setting Up Core Data with CloudKit](setting-up-core-data-with-cloudkit.md).

## Relationships

- **Inherits From**: [NSPersistentContainer](nspersistentcontainer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Checking Permissions

- [- canUpdateRecordForManagedObjectWithID:](<nspersistentcloudkitcontainer/canupdaterecord(formanagedobjectwith_).md>) — Returns a Boolean value that indicates whether the user can modify the managed object’s underlying CloudKit record.
- [- canDeleteRecordForManagedObjectWithID:](<nspersistentcloudkitcontainer/candeleterecord(formanagedobjectwith_).md>) — Returns a Boolean value that indicates whether the user can delete the managed object’s underlying CloudKit record.
- [- canModifyManagedObjectsInStore:](<nspersistentcloudkitcontainer/canmodifymanagedobjects(in_).md>) — Returns a Boolean value that indicates whether the user can modify the specified persistent store.

### Sharing Objects

- [Accepting Share Invitations in a SwiftUI App](accepting-share-invitations-in-a-swiftui-app.md) — Adapt your app to use UIKit’s application and scene delegates so it can process CloudKit share invitations.

### Promoting Your Schema

- [- initializeCloudKitSchemaWithOptions:error:](<nspersistentcloudkitcontainer/initializecloudkitschema(options_).md>) — Creates the CloudKit schema for all stores in the container that manage a CloudKit database.
- [NSPersistentCloudKitContainerSchemaInitializationOptions](nspersistentcloudkitcontainerschemainitializationoptions.md) — Options that control the behavior when promoting the container’s schema to CloudKit.

### Monitoring Container Events

- [Event](nspersistentcloudkitcontainer/event.md) — An object that represents activity in a persistent CloudKit container.
- [EventType](nspersistentcloudkitcontainer/eventtype.md) — The type of event in a persistent CloudKit container, either setup, import, or export.
- [NSPersistentCloudKitContainerEventRequest](nspersistentcloudkitcontainereventrequest.md) — A request to fetch setup, import, or export events in a persistent CloudKit container.
- [NSPersistentCloudKitContainerEventResult](nspersistentcloudkitcontainereventresult.md) — The result of a request to fetch persistent CloudKit container events.
- [NSPersistentCloudKitContainerEventChangedNotification](nspersistentcloudkitcontainer/eventchangednotification.md) — A notification that contains details about an event in a persistent CloudKit container.
- [NSPersistentCloudKitContainerEventUserInfoKey](nspersistentcloudkitcontainer/eventnotificationuserinfokey.md) — The user info dictionary key for the persistent CloudKit container event.

### Structures

- [EventChangedMessage](nspersistentcloudkitcontainer/eventchangedmessage.md) — Posted when a CloudKit event occurs on the CloudKit private serial queue.

## See Also

### CloudKit mirroring

- [Mirroring a Core Data store with CloudKit](mirroring-a-core-data-store-with-cloudkit.md) — Back user interfaces with a local replica of a CloudKit private database.
- [Synchronizing a local store to the cloud](synchronizing-a-local-store-to-the-cloud.md) — Share data between a user’s devices and other iCloud users.
- [NSPersistentCloudKitContainerOptions](nspersistentcloudkitcontaineroptions.md) — An object that customizes how a store description aligns with a CloudKit database.
- [Sharing Core Data objects between iCloud users](sharing-core-data-objects-between-icloud-users.md) — Use Core Data and CloudKit to synchronize data between devices of an iCloud user and share data between different iCloud users.

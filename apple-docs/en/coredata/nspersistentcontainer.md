---
title: NSPersistentContainer
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcontainer
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcontainer.json'
content_hash: 'sha256:fa285b2678a8331f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentContainer

<sub>Class</sub>

A container that encapsulates the Core Data stack in your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPersistentContainer
```

## Overview

NSPersistentContainer simplifies the creation and management of the Core Data stack by handling the creation of the managed object model ([NSManagedObjectModel](nsmanagedobjectmodel.md)), persistent store coordinator ([NSPersistentStoreCoordinator](nspersistentstorecoordinator.md)), and the managed object context ([NSManagedObjectContext](nsmanagedobjectcontext.md)).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSPersistentCloudKitContainer](nspersistentcloudkitcontainer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Container

- [- initWithName:](<nspersistentcontainer/init(name_).md>) — Creates a container with the specified name.
- [- initWithName:managedObjectModel:](<nspersistentcontainer/init(name_managedobjectmodel_).md>) — Create a container with the specified name and managed object model.

### Getting the Container’s Configuration

- [managedObjectModel](nspersistentcontainer/managedobjectmodel.md) — The container’s managed object model.
- [name](nspersistentcontainer/name.md) — The container’s name.
- [persistentStoreCoordinator](nspersistentcontainer/persistentstorecoordinator.md) — The container’s persistent store coordinator.

### Accessing the Default Directory

- [defaultDirectoryURL](nspersistentcontainer/defaultdirectoryurl-swift.type.property.md) — The location of the directory that contains the persistent stores.
- [+ defaultDirectoryURL](<nspersistentcontainer/defaultdirectoryurl().md>) — Returns the location of the directory that contains the persistent stores.

### Managing Persistent Stores

- [persistentStoreDescriptions](nspersistentcontainer/persistentstoredescriptions.md) — The descriptions of the container’s persistent stores.
- [- loadPersistentStoresWithCompletionHandler:](<nspersistentcontainer/loadpersistentstores(completionhandler_).md>) — Loads the persistent stores.

### Acquiring Contexts

- [- newBackgroundContext](<nspersistentcontainer/newbackgroundcontext().md>) — Returns a new managed object context that executes on a private queue.
- [viewContext](nspersistentcontainer/viewcontext.md) — The main queue’s managed object context.

### Performing Background Tasks

- [- performBackgroundTask:](<nspersistentcontainer/performbackgroundtask(__)-39sch.md>) — Executes a closure on a private queue using an ephemeral managed object context.
- [performBackgroundTask(_:)](<nspersistentcontainer/performbackgroundtask(__)-25nok.md>)

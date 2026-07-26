---
title: NSStagedMigrationManager
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsstagedmigrationmanager
source_url: 'https://developer.apple.com/documentation/coredata/nsstagedmigrationmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsstagedmigrationmanager.json'
content_hash: 'sha256:060fcfb387f02a0b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSStagedMigrationManager

<sub>Class</sub>

An object that handles the migration event loop and provides access to the migrating persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSStagedMigrationManager
```

## Overview

A staged migration manager contains the individual stages of a migration and applies those stages, in the order you specify, when that migration runs. The manager handles the migration’s event loop, and provides access to the migrating store through its [container](nsstagedmigrationmanager/container.md) property. Stages can be custom, which enables you to perform tasks immediately before and after a stage runs, or lightweight, which supplements custom stages with those that Core Data can invoke automatically because they’re already compatible with lightweight migrations.

Use [NSPersistentStoreStagedMigrationManagerOptionKey](nspersistentstorestagedmigrationmanageroptionkey.md) to include an instance of [NSStagedMigrationManager](nsstagedmigrationmanager.md) in your persistent store’s options dictionary, as the following example shows:

```swift
// Create a migration manager with the required stages.
let manager = NSStagedMigrationManager(stages)

let options = [
    // Enable lightweight migrations for this store.
    NSMigratePersistentStoresAutomaticallyOption: true,
    NSInferMappingModelAutomaticallyOption: true
    // Specify the migration manager to use with this store.
    NSPersistentStoreStagedMigrationManagerOptionKey: manager 
]

// Add the store to the persistent store coordinator.        
let store = coordinator.addPersistentStore(
    type: .sqlite,
    at: storeURL,
    options: options
)
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a migration manager

- [init(_:)](<nsstagedmigrationmanager/init(__).md>) — Creates a migration manager with the specified stages.

### Accessing the persistent container

- [container](nsstagedmigrationmanager/container.md) — The container that provides access to the migrating persistent store.

### Accessing the stages

- [stages](nsstagedmigrationmanager/stages.md) — The migration stages.

## See Also

### Migration staging

- [NSPersistentStoreStagedMigrationManagerOptionKey](nspersistentstorestagedmigrationmanageroptionkey.md) — The key for specifying your staged migration manager.

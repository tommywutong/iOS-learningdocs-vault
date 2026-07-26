---
title: NSCoreDataCoreSpotlightDelegate
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nscoredatacorespotlightdelegate
source_url: 'https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscoredatacorespotlightdelegate.json'
content_hash: 'sha256:c6e75bb06ef47e51'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSCoreDataCoreSpotlightDelegate

<sub>Class</sub>

A set of methods that enable integration with Core Spotlight.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class NSCoreDataCoreSpotlightDelegate
```

## Overview

> [!note] Note
> Core Spotlight integration is only available for persistent stores that have a store type of [sqlite](nspersistentstore/storetype/sqlite.md), and which use persistent history tracking. For more information, see [Consuming relevant store changes](consuming-relevant-store-changes.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Core Spotlight Delegate

- [- initForStoreWithDescription:coordinator:](<nscoredatacorespotlightdelegate/init(forstorewith_coordinator_).md>) — Creates a Core Spotlight delegate with the specified store description and coordinator.
- [- initForStoreWithDescription:model:](<nscoredatacorespotlightdelegate/init(forstorewith_model_).md>) — Creates a Core Spotlight delegate with the specified store description and managed object model. _(deprecated)_

### Configuring the Index

- [indexingEnabled](nscoredatacorespotlightdelegate/isindexingenabled.md) — A Boolean value that indicates whether Core Data is currently updating the Core Spotlight index with the persistent store’s entities.
- [- domainIdentifier](<nscoredatacorespotlightdelegate/domainidentifier().md>) — Returns the domain identifier.
- [- indexName](<nscoredatacorespotlightdelegate/indexname().md>) — Returns the index’s name.

### Managing the Index

- [- attributeSetForObject:](<nscoredatacorespotlightdelegate/attributeset(for_).md>) — Returns the searchable attributes for the specified managed object.
- [- deleteSpotlightIndexWithCompletionHandler:](<nscoredatacorespotlightdelegate/deletespotlightindex(completionhandler_).md>) — Deletes all searchable items from the configured index.
- [- startSpotlightIndexing](<nscoredatacorespotlightdelegate/startspotlightindexing().md>) — Starts the indexing of the store’s entities.
- [- stopSpotlightIndexing](<nscoredatacorespotlightdelegate/stopspotlightindexing().md>) — Stops the indexing of the store’s entities.

### Updating the Index

- [indexDidUpdateNotification](nscoredatacorespotlightdelegate/indexdidupdatenotification.md) — The notification the delegate posts after Spotlight updates the index.
- [- searchableIndex:reindexAllSearchableItemsWithAcknowledgementHandler:](<nscoredatacorespotlightdelegate/searchableindex(__reindexallsearchableitemswithacknowledgementhandler_).md>) — Reindexes all searchable items and clears any local state.
- [- searchableIndex:reindexSearchableItemsWithIdentifiers:acknowledgementHandler:](<nscoredatacorespotlightdelegate/searchableindex(__reindexsearchableitemswithidentifiers_acknowledgementhandler_).md>) — Reindexes the searchable items for the specified identifiers.

### Structures

- [IndexDidUpdateMessage](nscoredatacorespotlightdelegate/indexdidupdatemessage.md) — Posted when the Core Spotlight index is updated on a private queue.

### Initializers

- [init(forStoreWithDescription:coordinator:)](<nscoredatacorespotlightdelegate/init(forstorewithdescription_coordinator_).md>)
- [init(forStoreWithDescription:model:)](<nscoredatacorespotlightdelegate/init(forstorewithdescription_model_).md>) _(deprecated)_

## See Also

### Integrating with Spotlight

- [NSCoreDataCoreSpotlightExporter](nscoredatacorespotlightexporter.md) — The key you use to specify your Core Spotlight delegate.
- [Spotlight record keys](spotlight-record-keys.md) — The keys for the values that exist in Spotlight’s external record files.
- [Showcase App Data in Spotlight](showcase-app-data-in-spotlight.md) — Index app data so users can find it by using Spotlight search.

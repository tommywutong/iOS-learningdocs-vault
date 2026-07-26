---
title: Spotlight record keys
framework: Core Data
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/spotlight-record-keys
source_url: 'https://developer.apple.com/documentation/coredata/spotlight-record-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/spotlight-record-keys.json'
content_hash: 'sha256:766be3419e9c9ab1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md) · [Core Data stack](core-data-stack.md) · [NSPersistentStoreCoordinator](nspersistentstorecoordinator.md)

# Spotlight record keys

<sub>API Collection</sub>

The keys for the values that exist in Spotlight’s external record files.

## Topics

### Constants

- [NSEntityNameInPathKey](nsentitynameinpathkey.md) — Dictionary key for the entity name extracted from an external record file. _(deprecated)_
- [NSStoreUUIDInPathKey](nsstoreuuidinpathkey.md) — Dictionary key for the store UUID extracted from an external record file. _(deprecated)_
- [NSStorePathKey](nsstorepathkey.md) — Dictionary key for the store path (an instance of `NSURL`) extracted from an external record file. _(deprecated)_
- [NSModelPathKey](nsmodelpathkey.md) — Dictionary key for the managed object model path (an instance of `NSURL`) extracted from an external record file. _(deprecated)_
- [NSObjectURIKey](nsobjecturikey.md) — Dictionary key for the object URI extracted from an external record file. _(deprecated)_

## See Also

### Integrating with Spotlight

- [NSCoreDataCoreSpotlightExporter](nscoredatacorespotlightexporter.md) — The key you use to specify your Core Spotlight delegate.
- [NSCoreDataCoreSpotlightDelegate](nscoredatacorespotlightdelegate.md) — A set of methods that enable integration with Core Spotlight.
- [Showcase App Data in Spotlight](showcase-app-data-in-spotlight.md) — Index app data so users can find it by using Spotlight search.

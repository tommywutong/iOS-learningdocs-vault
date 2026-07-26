---
title: NSPersistentStoreRequestType
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstorerequesttype
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorerequesttype.json'
content_hash: 'sha256:1c8303425f0a0bc7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreRequestType

<sub>Enumeration</sub>

Constants that specify the types of fetch requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSPersistentStoreRequestType
```

## Overview

[requestType](nspersistentstorerequest/requesttype.md) uses these constants.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [NSFetchRequestType](nspersistentstorerequesttype/fetchrequesttype.md) — Specifies that the request returns managed objects.
- [NSSaveRequestType](nspersistentstorerequesttype/saverequesttype.md) — Specifies that the request saves managed objects.
- [NSBatchInsertRequestType](nspersistentstorerequesttype/batchinsertrequesttype.md) — A request that inserts data into a persistent store using a batch of managed objects or dictionaries.
- [NSBatchUpdateRequestType](nspersistentstorerequesttype/batchupdaterequesttype.md) — A request that updates data for multiple managed objects in a persistent store.
- [NSBatchDeleteRequestType](nspersistentstorerequesttype/batchdeleterequesttype.md) — A request that deletes data for multiple managed objects from a persistent store.

### Initializers

- [init(rawValue:)](<nspersistentstorerequesttype/init(rawvalue_).md>)

## See Also

### Configuring a Request

- [affectedStores](nspersistentstorerequest/affectedstores.md) — The stores the request should be sent to.
- [requestType](nspersistentstorerequest/requesttype.md) — The type of the fetch request.

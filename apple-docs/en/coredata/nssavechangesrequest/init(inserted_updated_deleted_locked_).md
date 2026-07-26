---
title: 'init(inserted:updated:deleted:locked:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nssavechangesrequest/init(inserted:updated:deleted:locked:)'
source_url: 'https://developer.apple.com/documentation/coredata/nssavechangesrequest/init(inserted:updated:deleted:locked:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nssavechangesrequest/init%28inserted%3Aupdated%3Adeleted%3Alocked%3A%29.json'
content_hash: 'sha256:3f0581c9da8ff8e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSSaveChangesRequest](../nssavechangesrequest.md)

# init(inserted:updated:deleted:locked:)

<sub>Initializer</sub>

Initializes a save changes request with collections of given changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(inserted insertedObjects: Set<NSManagedObject>?, updated updatedObjects: Set<NSManagedObject>?, deleted deletedObjects: Set<NSManagedObject>?, locked lockedObjects: Set<NSManagedObject>?)
```

## Parameters

- `insertedObjects` — Objects that were inserted into the calling context.

- `updatedObjects` — Objects that were updated in the calling context.

- `deletedObjects` — Objects that were deleted in the calling context.

- `lockedObjects` — Objects that were flagged for optimistic locking on the calling context.

## Return Value

A save changes request initialized with the given changes.

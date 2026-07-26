---
title: NSManagedObjectID
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectid
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectid.json'
content_hash: 'sha256:ad4861802943e0d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSManagedObjectID

<sub>Class</sub>

A compact, universal identifier for a managed object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSManagedObjectID
```

## Overview

This identifier forms the basis for uniquing in the Core Data Framework. A managed object ID uniquely identifies the same managed object both between managed object contexts in a single application, and in multiple applications (as in distributed systems). Identifiers contain the information needed to exactly describe an object in a persistent store (like the primary key in the database), although the detailed information is not exposed. The framework completely encapsulates the “external” information and presents a clean object oriented interface.

Object IDs can be transformed into a URI representation which can be archived and recreated later to refer back to a given object (using [- managedObjectIDForURIRepresentation:](<nspersistentstorecoordinator/managedobjectid(forurirepresentation_).md>) (`NSPersistentStoreCoordinator`) and [- objectWithID:](<nsmanagedobjectcontext/object(with_).md>) (`NSManagedObjectContext`). For example, the last selected group in an application could be stored in the user defaults through the group object’s ID. You can also use object ID URI representations to store “weak” relationships across persistent stores (where no hard join is possible).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSFetchRequestResult](nsfetchrequestresult.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting Managed Object ID Information

- [entity](nsmanagedobjectid/entity.md) — The entity description associated with the object ID.
- [temporaryID](nsmanagedobjectid/istemporaryid.md) — A Boolean value that indicates whether the object ID is temporary.
- [persistentStore](nsmanagedobjectid/persistentstore.md) — The persistent store that fetched the object for the object ID.
- [- URIRepresentation](<nsmanagedobjectid/urirepresentation().md>) — Returns a URI that provides an archiveable reference to the object for the object ID.

## See Also

### Object Management

- [NSManagedObjectContext](nsmanagedobjectcontext.md) — An object space to manipulate and track changes to managed objects.
- [NSManagedObject](nsmanagedobject.md) — The base class that all Core Data model objects inherit from.

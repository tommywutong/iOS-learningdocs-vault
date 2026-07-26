---
title: hasPersistentChangedValues
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/haspersistentchangedvalues
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/haspersistentchangedvalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/haspersistentchangedvalues.json'
content_hash: 'sha256:0929b934697529a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# hasPersistentChangedValues

<sub>Instance Property</sub>

A Boolean value that indicates whether the managed object has persistent changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hasPersistentChangedValues: Bool { get }
```

## See Also

### Getting State Information

- [managedObjectContext](managedobjectcontext.md) — The managed object context with which the managed object is registered.
- [hasChanges](haschanges.md) — A Boolean value that indicates whether the managed object has been inserted, has been deleted, or has unsaved changes.
- [inserted](isinserted.md) — A Boolean value that indicates whether the managed object has been inserted in a managed object context.
- [updated](isupdated.md) — A Boolean value that indicates whether the managed object has unsaved changes.
- [deleted](isdeleted.md) — A Boolean value that indicates whether the managed object will be deleted during the next save.
- [fault](isfault.md) — A Boolean value that indicates whether the managed object is a fault.
- [faultingState](faultingstate.md) — The faulting state of the managed object.
- [- hasFaultForRelationshipNamed:](<hasfault(forrelationshipnamed_).md>) — Returns a Boolean value that indicates whether the relationship for a given key is a fault.

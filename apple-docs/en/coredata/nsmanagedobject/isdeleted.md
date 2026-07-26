---
title: isDeleted
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/isdeleted
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/isdeleted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/isdeleted.json'
content_hash: 'sha256:1ce0bec280b17de0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# isDeleted

<sub>Instance Property</sub>

A Boolean value that indicates whether the managed object will be deleted during the next save.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isDeleted: Bool { get }
```

## Discussion

[true](../../swift/true.md) if Core Data will ask the persistent store to delete the object during the next save operation, otherwise [false](../../swift/false.md). It may return [false](../../swift/false.md) at other times, particularly after the object has been deleted. The immediacy with which it will stop returning [true](../../swift/true.md) depends on where the object is in the process of being deleted.

If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

### Getting State Information

- [managedObjectContext](managedobjectcontext.md) — The managed object context with which the managed object is registered.
- [hasChanges](haschanges.md) — A Boolean value that indicates whether the managed object has been inserted, has been deleted, or has unsaved changes.
- [inserted](isinserted.md) — A Boolean value that indicates whether the managed object has been inserted in a managed object context.
- [updated](isupdated.md) — A Boolean value that indicates whether the managed object has unsaved changes.
- [fault](isfault.md) — A Boolean value that indicates whether the managed object is a fault.
- [faultingState](faultingstate.md) — The faulting state of the managed object.
- [- hasFaultForRelationshipNamed:](<hasfault(forrelationshipnamed_).md>) — Returns a Boolean value that indicates whether the relationship for a given key is a fault.
- [hasPersistentChangedValues](haspersistentchangedvalues.md) — A Boolean value that indicates whether the managed object has persistent changes.

---
title: isUpdated
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/isupdated
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/isupdated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/isupdated.json'
content_hash: 'sha256:6b1c11f1a45b9e3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# isUpdated

<sub>Instance Property</sub>

A Boolean value that indicates whether the managed object has unsaved changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isUpdated: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the receiver has unsaved changes, otherwise [false](../../swift/false.md). The receiver has unsaved changes if it has been updated since its managed object context was last saved.

If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

### Getting State Information

- [managedObjectContext](managedobjectcontext.md) — The managed object context with which the managed object is registered.
- [hasChanges](haschanges.md) — A Boolean value that indicates whether the managed object has been inserted, has been deleted, or has unsaved changes.
- [inserted](isinserted.md) — A Boolean value that indicates whether the managed object has been inserted in a managed object context.
- [deleted](isdeleted.md) — A Boolean value that indicates whether the managed object will be deleted during the next save.
- [fault](isfault.md) — A Boolean value that indicates whether the managed object is a fault.
- [faultingState](faultingstate.md) — The faulting state of the managed object.
- [- hasFaultForRelationshipNamed:](<hasfault(forrelationshipnamed_).md>) — Returns a Boolean value that indicates whether the relationship for a given key is a fault.
- [hasPersistentChangedValues](haspersistentchangedvalues.md) — A Boolean value that indicates whether the managed object has persistent changes.

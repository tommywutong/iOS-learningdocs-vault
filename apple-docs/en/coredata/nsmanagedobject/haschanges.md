---
title: hasChanges
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/haschanges
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/haschanges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/haschanges.json'
content_hash: 'sha256:91c7ac95b7e89203'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# hasChanges

<sub>Instance Property</sub>

A Boolean value that indicates whether the managed object has been inserted, has been deleted, or has unsaved changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hasChanges: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the receiver has been inserted, has been deleted, or has unsaved changes, otherwise [false](../../swift/false.md). The result is the equivalent of OR-ing the values of [inserted](isinserted.md), [deleted](isdeleted.md), and [updated](isupdated.md).

## See Also

### Getting State Information

- [managedObjectContext](managedobjectcontext.md) — The managed object context with which the managed object is registered.
- [inserted](isinserted.md) — A Boolean value that indicates whether the managed object has been inserted in a managed object context.
- [updated](isupdated.md) — A Boolean value that indicates whether the managed object has unsaved changes.
- [deleted](isdeleted.md) — A Boolean value that indicates whether the managed object will be deleted during the next save.
- [fault](isfault.md) — A Boolean value that indicates whether the managed object is a fault.
- [faultingState](faultingstate.md) — The faulting state of the managed object.
- [- hasFaultForRelationshipNamed:](<hasfault(forrelationshipnamed_).md>) — Returns a Boolean value that indicates whether the relationship for a given key is a fault.
- [hasPersistentChangedValues](haspersistentchangedvalues.md) — A Boolean value that indicates whether the managed object has persistent changes.

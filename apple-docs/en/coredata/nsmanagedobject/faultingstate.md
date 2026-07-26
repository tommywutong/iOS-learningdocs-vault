---
title: faultingState
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/faultingstate
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/faultingstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/faultingstate.json'
content_hash: 'sha256:3c41b8dc828b5b7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# faultingState

<sub>Instance Property</sub>

The faulting state of the managed object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var faultingState: Int { get }
```

## Return Value

`0` if the object is fully initialized as a managed object and not transitioning to or from another state, otherwise some other value.

## Discussion

`0` if the object is fully initialized as a managed object and not transitioning to or from another state, otherwise some other value. This property allows you to determine if an object is in a transitional phase when receiving a key-value observing change notification.

## See Also

### Getting State Information

- [managedObjectContext](managedobjectcontext.md) — The managed object context with which the managed object is registered.
- [hasChanges](haschanges.md) — A Boolean value that indicates whether the managed object has been inserted, has been deleted, or has unsaved changes.
- [inserted](isinserted.md) — A Boolean value that indicates whether the managed object has been inserted in a managed object context.
- [updated](isupdated.md) — A Boolean value that indicates whether the managed object has unsaved changes.
- [deleted](isdeleted.md) — A Boolean value that indicates whether the managed object will be deleted during the next save.
- [fault](isfault.md) — A Boolean value that indicates whether the managed object is a fault.
- [- hasFaultForRelationshipNamed:](<hasfault(forrelationshipnamed_).md>) — Returns a Boolean value that indicates whether the relationship for a given key is a fault.
- [hasPersistentChangedValues](haspersistentchangedvalues.md) — A Boolean value that indicates whether the managed object has persistent changes.

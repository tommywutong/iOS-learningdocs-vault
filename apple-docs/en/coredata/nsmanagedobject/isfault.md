---
title: isFault
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/isfault
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/isfault'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/isfault.json'
content_hash: 'sha256:7b4f9a41e935b98a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# isFault

<sub>Instance Property</sub>

A Boolean value that indicates whether the managed object is a fault.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isFault: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the receiver is a fault, otherwise [false](../../swift/false.md). Knowing whether an object is a fault is useful in many situations when computations are optional. It can also be used to avoid growing the object graph unnecessarily (which may improve performance as it can avoid time-consuming fetches from data stores).

If this property is [false](../../swift/false.md), then the receiver’s data must be in memory. However, if this property is  [true](../../swift/true.md), it does _not_ mean that the data is not in memory. The data may be in memory, or it may not, depending on many factors influencing caching.

If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

### Getting State Information

- [managedObjectContext](managedobjectcontext.md) — The managed object context with which the managed object is registered.
- [hasChanges](haschanges.md) — A Boolean value that indicates whether the managed object has been inserted, has been deleted, or has unsaved changes.
- [inserted](isinserted.md) — A Boolean value that indicates whether the managed object has been inserted in a managed object context.
- [updated](isupdated.md) — A Boolean value that indicates whether the managed object has unsaved changes.
- [deleted](isdeleted.md) — A Boolean value that indicates whether the managed object will be deleted during the next save.
- [faultingState](faultingstate.md) — The faulting state of the managed object.
- [- hasFaultForRelationshipNamed:](<hasfault(forrelationshipnamed_).md>) — Returns a Boolean value that indicates whether the relationship for a given key is a fault.
- [hasPersistentChangedValues](haspersistentchangedvalues.md) — A Boolean value that indicates whether the managed object has persistent changes.

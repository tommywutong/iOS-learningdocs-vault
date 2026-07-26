---
title: 'hasFault(forRelationshipNamed:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobject/hasfault(forrelationshipnamed:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/hasfault(forrelationshipnamed:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/hasfault%28forrelationshipnamed%3A%29.json'
content_hash: 'sha256:c6f22c0f2a2b29b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# hasFault(forRelationshipNamed:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the relationship for a given key is a fault.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hasFault(forRelationshipNamed key: String) -> Bool
```

## Parameters

- `key` — The name of one of the receiver’s relationships.

## Return Value

[true](../../swift/true.md) if the relationship for `key` is a fault; otherwise, [false](../../swift/false.md).

## Discussion

If the specified relationship is a fault, calling this method does not result in the fault firing.

## See Also

### Getting State Information

- [managedObjectContext](managedobjectcontext.md) — The managed object context with which the managed object is registered.
- [hasChanges](haschanges.md) — A Boolean value that indicates whether the managed object has been inserted, has been deleted, or has unsaved changes.
- [inserted](isinserted.md) — A Boolean value that indicates whether the managed object has been inserted in a managed object context.
- [updated](isupdated.md) — A Boolean value that indicates whether the managed object has unsaved changes.
- [deleted](isdeleted.md) — A Boolean value that indicates whether the managed object will be deleted during the next save.
- [fault](isfault.md) — A Boolean value that indicates whether the managed object is a fault.
- [faultingState](faultingstate.md) — The faulting state of the managed object.
- [hasPersistentChangedValues](haspersistentchangedvalues.md) — A Boolean value that indicates whether the managed object has persistent changes.

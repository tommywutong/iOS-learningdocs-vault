---
title: 'willChangeValue(forKey:withSetMutation:using:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobject/willchangevalue(forkey:withsetmutation:using:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/willchangevalue(forkey:withsetmutation:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/willchangevalue%28forkey%3Awithsetmutation%3Ausing%3A%29.json'
content_hash: 'sha256:377fc8ce403b24d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# willChangeValue(forKey:withSetMutation:using:)

<sub>Instance Method</sub>

Provides an opportunity to respond when a change is about to be made to a specified to-many relationship.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func willChangeValue(forKey inKey: String, withSetMutation inMutationKind: NSKeyValueSetMutationKind, using inObjects: Set<AnyHashable>)
```

## Parameters

- `inKey` — The name of a property that is a to-many relationship

- `inMutationKind` — The type of change that will be made.

- `inObjects` — The objects that were involved in the change (see [NSKeyValueSetMutationKind](../../foundation/nskeyvaluesetmutationkind.md)).

## Discussion

For more details, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

You must not override this method.

## See Also

### Supporting Key-Value Observing

- [- didAccessValueForKey:](<didaccessvalue(forkey_).md>) — Provides support for key-value observing access notification.
- [- observationInfo](<observationinfo().md>) — Returns the observation info of the managed object.
- [- setObservationInfo:](<setobservationinfo(__).md>) — Sets the observation info of the managed object.
- [- willAccessValueForKey:](<willaccessvalue(forkey_).md>) — Provides support for key-value observing access notification.
- [- didChangeValueForKey:](<didchangevalue(forkey_).md>) — Provides an opportunity to respond when a value of a given property has changed.
- [- didChangeValueForKey:withSetMutation:usingObjects:](<didchangevalue(forkey_withsetmutation_using_).md>) — Provides an opportunity to respond when a change was made to a specified to-many relationship.
- [- willChangeValueForKey:](<willchangevalue(forkey_).md>) — Provides an opportunity to respond when a value of a given property is about to change.

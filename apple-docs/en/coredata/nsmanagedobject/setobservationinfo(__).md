---
title: 'setObservationInfo(_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobject/setobservationinfo(_:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/setobservationinfo(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/setobservationinfo%28_%3A%29.json'
content_hash: 'sha256:e8c1e10077200582'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# setObservationInfo(_:)

<sub>Instance Method</sub>

Sets the observation info of the managed object.

<sub>Mac Catalyst, macOS</sub>

```swift
func setObservationInfo(_ inObservationInfo: UnsafeMutableRawPointer?)
```

## Parameters

- `inObservationInfo` — The new observation info for the receiver.

## Discussion

For more about observation information, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

### Supporting Key-Value Observing

- [- didAccessValueForKey:](<didaccessvalue(forkey_).md>) — Provides support for key-value observing access notification.
- [- observationInfo](<observationinfo().md>) — Returns the observation info of the managed object.
- [- willAccessValueForKey:](<willaccessvalue(forkey_).md>) — Provides support for key-value observing access notification.
- [- didChangeValueForKey:](<didchangevalue(forkey_).md>) — Provides an opportunity to respond when a value of a given property has changed.
- [- didChangeValueForKey:withSetMutation:usingObjects:](<didchangevalue(forkey_withsetmutation_using_).md>) — Provides an opportunity to respond when a change was made to a specified to-many relationship.
- [- willChangeValueForKey:](<willchangevalue(forkey_).md>) — Provides an opportunity to respond when a value of a given property is about to change.
- [- willChangeValueForKey:withSetMutation:usingObjects:](<willchangevalue(forkey_withsetmutation_using_).md>) — Provides an opportunity to respond when a change is about to be made to a specified to-many relationship.

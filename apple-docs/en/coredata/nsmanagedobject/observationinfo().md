---
title: observationInfo()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobject/observationinfo()
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/observationinfo()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/observationinfo%28%29.json'
content_hash: 'sha256:da3c97c811573b8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# observationInfo()

<sub>Instance Method</sub>

Returns the observation info of the managed object.

<sub>Mac Catalyst, macOS</sub>

```swift
func observationInfo() -> UnsafeMutableRawPointer?
```

## Return Value

The observation info of the receiver.

## Discussion

For more about key-value observation, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

> [!important] Important
> You must not override this method.

## See Also

### Supporting Key-Value Observing

- [- didAccessValueForKey:](<didaccessvalue(forkey_).md>) — Provides support for key-value observing access notification.
- [- setObservationInfo:](<setobservationinfo(__).md>) — Sets the observation info of the managed object.
- [- willAccessValueForKey:](<willaccessvalue(forkey_).md>) — Provides support for key-value observing access notification.
- [- didChangeValueForKey:](<didchangevalue(forkey_).md>) — Provides an opportunity to respond when a value of a given property has changed.
- [- didChangeValueForKey:withSetMutation:usingObjects:](<didchangevalue(forkey_withsetmutation_using_).md>) — Provides an opportunity to respond when a change was made to a specified to-many relationship.
- [- willChangeValueForKey:](<willchangevalue(forkey_).md>) — Provides an opportunity to respond when a value of a given property is about to change.
- [- willChangeValueForKey:withSetMutation:usingObjects:](<willchangevalue(forkey_withsetmutation_using_).md>) — Provides an opportunity to respond when a change is about to be made to a specified to-many relationship.

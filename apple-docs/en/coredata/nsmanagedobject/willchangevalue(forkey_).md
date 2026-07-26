---
title: 'willChangeValue(forKey:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobject/willchangevalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/willchangevalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/willchangevalue%28forkey%3A%29.json'
content_hash: 'sha256:42c68fa85b3a09a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# willChangeValue(forKey:)

<sub>Instance Method</sub>

Provides an opportunity to respond when a value of a given property is about to change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func willChangeValue(forKey key: String)
```

## Parameters

- `key` — The name of the property that will change.

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
- [- willChangeValueForKey:withSetMutation:usingObjects:](<willchangevalue(forkey_withsetmutation_using_).md>) — Provides an opportunity to respond when a change is about to be made to a specified to-many relationship.

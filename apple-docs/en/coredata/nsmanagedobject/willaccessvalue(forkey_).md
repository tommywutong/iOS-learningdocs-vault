---
title: 'willAccessValue(forKey:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobject/willaccessvalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/willaccessvalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/willaccessvalue%28forkey%3A%29.json'
content_hash: 'sha256:fd3b57fa00075891'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# willAccessValue(forKey:)

<sub>Instance Method</sub>

Provides support for key-value observing access notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func willAccessValue(forKey key: String?)
```

## Parameters

- `key` — The name of one of the receiver’s properties.

## Discussion

See [- didAccessValueForKey:](<didaccessvalue(forkey_).md>) for more details. You can invoke this method with the `key` value of `nil` to ensure that a fault has been fired, as illustrated by the following example.

```objc
[aManagedObject willAccessValueForKey:nil];
```

## See Also

### Supporting Key-Value Observing

- [- didAccessValueForKey:](<didaccessvalue(forkey_).md>) — Provides support for key-value observing access notification.
- [- observationInfo](<observationinfo().md>) — Returns the observation info of the managed object.
- [- setObservationInfo:](<setobservationinfo(__).md>) — Sets the observation info of the managed object.
- [- didChangeValueForKey:](<didchangevalue(forkey_).md>) — Provides an opportunity to respond when a value of a given property has changed.
- [- didChangeValueForKey:withSetMutation:usingObjects:](<didchangevalue(forkey_withsetmutation_using_).md>) — Provides an opportunity to respond when a change was made to a specified to-many relationship.
- [- willChangeValueForKey:](<willchangevalue(forkey_).md>) — Provides an opportunity to respond when a value of a given property is about to change.
- [- willChangeValueForKey:withSetMutation:usingObjects:](<willchangevalue(forkey_withsetmutation_using_).md>) — Provides an opportunity to respond when a change is about to be made to a specified to-many relationship.

---
title: 'didAccessValue(forKey:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobject/didaccessvalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobject/didaccessvalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobject/didaccessvalue%28forkey%3A%29.json'
content_hash: 'sha256:19641755ca4a84e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObject](../nsmanagedobject.md)

# didAccessValue(forKey:)

<sub>Instance Method</sub>

Provides support for key-value observing access notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func didAccessValue(forKey key: String?)
```

## Parameters

- `key` — The name of one of the receiver’s properties.

## Discussion

Together with [- willAccessValueForKey:](<willaccessvalue(forkey_).md>), this method is used to fire faults, to maintain inverse relationships, and so on. Each read access must be wrapped in this method pair (in the same way that each write access must be wrapped in the `willChangeValueForKey:`/`didChangeValueForKey:` method pair). In the default implementation of `NSManagedObject` these methods are invoked for you automatically. If, say, you create a custom subclass that uses explicit instance variables, you must invoke them yourself, as in the following example.

```objc
- (NSString *)firstName
{
    [self willAccessValueForKey:@"firstName"];
    NSString *rtn = firstName;
    [self didAccessValueForKey:@"firstName"];
    return rtn;
}
```

## See Also

### Supporting Key-Value Observing

- [- observationInfo](<observationinfo().md>) — Returns the observation info of the managed object.
- [- setObservationInfo:](<setobservationinfo(__).md>) — Sets the observation info of the managed object.
- [- willAccessValueForKey:](<willaccessvalue(forkey_).md>) — Provides support for key-value observing access notification.
- [- didChangeValueForKey:](<didchangevalue(forkey_).md>) — Provides an opportunity to respond when a value of a given property has changed.
- [- didChangeValueForKey:withSetMutation:usingObjects:](<didchangevalue(forkey_withsetmutation_using_).md>) — Provides an opportunity to respond when a change was made to a specified to-many relationship.
- [- willChangeValueForKey:](<willchangevalue(forkey_).md>) — Provides an opportunity to respond when a value of a given property is about to change.
- [- willChangeValueForKey:withSetMutation:usingObjects:](<willchangevalue(forkey_withsetmutation_using_).md>) — Provides an opportunity to respond when a change is about to be made to a specified to-many relationship.

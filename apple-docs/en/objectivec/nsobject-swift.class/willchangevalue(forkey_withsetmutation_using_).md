---
title: 'willChangeValue(forKey:withSetMutation:using:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/willchangevalue(forkey:withsetmutation:using:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/willchangevalue(forkey:withsetmutation:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/willchangevalue%28forkey%3Awithsetmutation%3Ausing%3A%29.json'
content_hash: 'sha256:d7484ccd01d43ef5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# willChangeValue(forKey:withSetMutation:using:)

<sub>Instance Method</sub>

Informs the observed object that the specified change is about to be made to a specified unordered to-many relationship.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)
```

## Parameters

- `key` — The name of a property that is an unordered to-many relationship

- `mutationKind` — The type of change that will be made.

- `objects` — The objects that are involved in the change (see [NSKeyValueSetMutationKind](../../foundation/nskeyvaluesetmutationkind.md)).

## Discussion

Use this method when implementing key-value observer compliance manually.

> [!important] Important
> After the values have been changed, a corresponding [- didChangeValueForKey:withSetMutation:usingObjects:](<didchangevalue(forkey_withsetmutation_using_).md>) must be invoked with the same parameters.

### Special Considerations

You rarely need to override this method in subclasses, but if you do, be sure to call `super`.

## See Also

### Notifying Observers of Changes

- [- willChangeValueForKey:](<willchangevalue(forkey_).md>) — Informs the observed object that the value of a given property is about to change.
- [- didChangeValueForKey:](<didchangevalue(forkey_).md>) — Informs the observed object that the value of a given property has changed.
- [- willChange:valuesAtIndexes:forKey:](<willchange(__valuesat_forkey_).md>) — Informs the observed object that the specified change is about to be executed at given indexes for a specified ordered to-many relationship.
- [- didChange:valuesAtIndexes:forKey:](<didchange(__valuesat_forkey_).md>) — Informs the observed object that the specified change has occurred on the indexes for a specified ordered to-many relationship.
- [- didChangeValueForKey:withSetMutation:usingObjects:](<didchangevalue(forkey_withsetmutation_using_).md>) — Informs the observed object that the specified change was made to a specified unordered to-many relationship.

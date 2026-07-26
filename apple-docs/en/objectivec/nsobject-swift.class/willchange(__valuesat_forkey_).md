---
title: 'willChange(_:valuesAt:forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/willchange(_:valuesat:forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/willchange(_:valuesat:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/willchange%28_%3Avaluesat%3Aforkey%3A%29.json'
content_hash: 'sha256:429a25e40b75bc63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# willChange(_:valuesAt:forKey:)

<sub>Instance Method</sub>

Informs the observed object that the specified change is about to be executed at given indexes for a specified ordered to-many relationship.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)
```

## Parameters

- `changeKind` — The type of change that is about to be made.

- `indexes` — The indexes of the to-many relationship that will be affected by the change.

- `key` — The name of a property that is an ordered to-many relationship.

## Discussion

Use this method when implementing key-value-observing compliance manually.

> [!important] Important
> After the values have been changed, a corresponding [- didChange:valuesAtIndexes:forKey:](<didchange(__valuesat_forkey_).md>) must be invoked with the same parameters.

### Special Considerations

You rarely need to override this method in subclasses, but if you do, be sure to call `super`.

## See Also

### Notifying Observers of Changes

- [- willChangeValueForKey:](<willchangevalue(forkey_).md>) — Informs the observed object that the value of a given property is about to change.
- [- didChangeValueForKey:](<didchangevalue(forkey_).md>) — Informs the observed object that the value of a given property has changed.
- [- didChange:valuesAtIndexes:forKey:](<didchange(__valuesat_forkey_).md>) — Informs the observed object that the specified change has occurred on the indexes for a specified ordered to-many relationship.
- [- willChangeValueForKey:withSetMutation:usingObjects:](<willchangevalue(forkey_withsetmutation_using_).md>) — Informs the observed object that the specified change is about to be made to a specified unordered to-many relationship.
- [- didChangeValueForKey:withSetMutation:usingObjects:](<didchangevalue(forkey_withsetmutation_using_).md>) — Informs the observed object that the specified change was made to a specified unordered to-many relationship.

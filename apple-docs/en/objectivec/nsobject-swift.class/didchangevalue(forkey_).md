---
title: 'didChangeValue(forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/didchangevalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/didchangevalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/didchangevalue%28forkey%3A%29.json'
content_hash: 'sha256:5f70925a9980106e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# didChangeValue(forKey:)

<sub>Instance Method</sub>

Informs the observed object that the value of a given property has changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func didChangeValue(forKey key: String)
```

## Parameters

- `key` — The name of the property that changed.

## Discussion

Use this method when implementing key-value observer compliance manually to inform the observed object that the value at `key` has just changed. Calls to this method are always paired with a matching call to [- willChangeValueForKey:](<willchangevalue(forkey_).md>).

### Special Considerations

You rarely need to override this method in subclasses, but if you do, be sure to call `super`.

## See Also

### Notifying Observers of Changes

- [- willChangeValueForKey:](<willchangevalue(forkey_).md>) — Informs the observed object that the value of a given property is about to change.
- [- willChange:valuesAtIndexes:forKey:](<willchange(__valuesat_forkey_).md>) — Informs the observed object that the specified change is about to be executed at given indexes for a specified ordered to-many relationship.
- [- didChange:valuesAtIndexes:forKey:](<didchange(__valuesat_forkey_).md>) — Informs the observed object that the specified change has occurred on the indexes for a specified ordered to-many relationship.
- [- willChangeValueForKey:withSetMutation:usingObjects:](<willchangevalue(forkey_withsetmutation_using_).md>) — Informs the observed object that the specified change is about to be made to a specified unordered to-many relationship.
- [- didChangeValueForKey:withSetMutation:usingObjects:](<didchangevalue(forkey_withsetmutation_using_).md>) — Informs the observed object that the specified change was made to a specified unordered to-many relationship.

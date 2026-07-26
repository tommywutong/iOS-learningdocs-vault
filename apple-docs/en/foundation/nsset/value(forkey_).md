---
title: 'value(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/value(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/value(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/value%28forkey%3A%29.json'
content_hash: 'sha256:39bae099123812c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# value(forKey:)

<sub>Instance Method</sub>

Return a set containing the results of invoking `valueForKey:` on each of the receiving set’s members.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value(forKey key: String) -> Any
```

## Parameters

- `key` — The name of one of the properties of the receiving set’s members.

## Return Value

A set containing the results of invoking `valueForKey:` (with the argument `key`) on each of the receiving set’s members.

## Discussion

The returned set might not have the same number of members as the receiving set. The returned set will not contain any elements corresponding to instances of `valueForKey:` returning `nil` (note that this is in contrast with `NSArray`’s implementation, which may put `NSNull` values in the arrays it returns).

## See Also

### Comparing Sets

- [- isSubsetOfSet:](<issubset(of_).md>) — Returns a Boolean value that indicates whether every object in the receiving set is also present in another given set.
- [- intersectsSet:](<intersects(__).md>) — Returns a Boolean value that indicates whether at least one object in the receiving set is also present in another given set.
- [- isEqualToSet:](<isequal(to_).md>) — Compares the receiving set to another set.
- [- setValue:forKey:](<setvalue(__forkey_).md>) — Invokes `setValue:forKey:` on each of the set’s members.

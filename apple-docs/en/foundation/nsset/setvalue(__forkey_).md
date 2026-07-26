---
title: 'setValue(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/setvalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/setvalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/setvalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:306fd18185153bfc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# setValue(_:forKey:)

<sub>Instance Method</sub>

Invokes `setValue:forKey:` on each of the set’s members.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue(_ value: Any?, forKey key: String)
```

## Parameters

- `value` — The value for the property identified by `key`.

- `key` — The name of one of the properties of the set’s members.

## See Also

### Comparing Sets

- [- isSubsetOfSet:](<issubset(of_).md>) — Returns a Boolean value that indicates whether every object in the receiving set is also present in another given set.
- [- intersectsSet:](<intersects(__).md>) — Returns a Boolean value that indicates whether at least one object in the receiving set is also present in another given set.
- [- isEqualToSet:](<isequal(to_).md>) — Compares the receiving set to another set.
- [- valueForKey:](<value(forkey_).md>) — Return a set containing the results of invoking `valueForKey:` on each of the receiving set’s members.

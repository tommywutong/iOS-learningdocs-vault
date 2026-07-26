---
title: 'contains(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/contains(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/contains%28_%3A%29.json'
content_hash: 'sha256:2694048a5729cb3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether a given object is present in the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ anObject: Any) -> Bool
```

## Parameters

- `anObject` — An object to look for in the set.

## Return Value

[true](../../swift/true.md) if `anObject` is present in the set, otherwise [false](../../swift/false.md).

## Discussion

Each element of the set is checked for equality with `anObject` until a match is found or the end of the set is reached.  Objects are considered equal if [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>) returns [true](../../swift/true.md).

## See Also

### Accessing Set Members

- [allObjects](allobjects.md) — An array containing the set’s members, or an empty array if the set has no members.
- [- anyObject](<anyobject().md>) — Returns one of the objects in the set, or `nil` if the set contains no objects.
- [- filteredSetUsingPredicate:](<filtered(using_).md>) — Evaluates a given predicate against each object in the receiving set and returns a new set containing the objects for which the predicate returns true.
- [- member:](<member(__).md>) — Determines whether a given object is present in the set, and returns that object if it is.
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each object in the set.
- [- enumerateObjectsUsingBlock:](<enumerateobjects(__).md>) — Executes a given block using each object in the set.
- [- enumerateObjectsWithOptions:usingBlock:](<enumerateobjects(options_using_).md>) — Executes a given block using each object in the set, using the specified enumeration options.
- [- objectsPassingTest:](<objects(passingtest_).md>) — Returns a set of objects that pass a test in a given block.
- [- objectsWithOptions:passingTest:](<objects(options_passingtest_).md>) — Returns a set of objects that pass a test in a given block, using the specified enumeration options.

---
title: 'member(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/member(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/member(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/member%28_%3A%29.json'
content_hash: 'sha256:438f4795143fb308'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# member(_:)

<sub>Instance Method</sub>

Determines whether a given object is present in the set, and returns that object if it is.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func member(_ object: Any) -> Any?
```

## Parameters

- `object` — An object to look for in the set.

## Return Value

Returns an object equal to `object` if it’s present in the set, otherwise `nil`.

## Discussion

Each element of the set is checked for equality with `object` until a match is found or the end of the set is reached.  Objects are considered equal if [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>) returns [true](../../swift/true.md).

## See Also

### Accessing Set Members

- [allObjects](allobjects.md) — An array containing the set’s members, or an empty array if the set has no members.
- [- anyObject](<anyobject().md>) — Returns one of the objects in the set, or `nil` if the set contains no objects.
- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the set.
- [- filteredSetUsingPredicate:](<filtered(using_).md>) — Evaluates a given predicate against each object in the receiving set and returns a new set containing the objects for which the predicate returns true.
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each object in the set.
- [- enumerateObjectsUsingBlock:](<enumerateobjects(__).md>) — Executes a given block using each object in the set.
- [- enumerateObjectsWithOptions:usingBlock:](<enumerateobjects(options_using_).md>) — Executes a given block using each object in the set, using the specified enumeration options.
- [- objectsPassingTest:](<objects(passingtest_).md>) — Returns a set of objects that pass a test in a given block.
- [- objectsWithOptions:passingTest:](<objects(options_passingtest_).md>) — Returns a set of objects that pass a test in a given block, using the specified enumeration options.

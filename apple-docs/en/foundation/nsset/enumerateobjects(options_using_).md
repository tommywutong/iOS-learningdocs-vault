---
title: 'enumerateObjects(options:using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/enumerateobjects(options:using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/enumerateobjects(options:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/enumerateobjects%28options%3Ausing%3A%29.json'
content_hash: 'sha256:32ca85dedd33b2a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# enumerateObjects(options:using:)

<sub>Instance Method</sub>

Executes a given block using each object in the set, using the specified enumeration options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateObjects(options opts: NSEnumerationOptions = [], using block: (Any, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `opts` — A bitmask that specifies the options for the enumeration.

- `block` — The block to apply to elements in the set. The block takes two arguments: - **obj** — The element in the set. - **stop** — A reference to a Boolean value. The block can set the value to [true](../../swift/true.md) to stop further processing of the set. The `stop` argument is an out-only argument. You should only ever set this Boolean to [true](../../swift/true.md) within the block.

## See Also

### Accessing Set Members

- [allObjects](allobjects.md) — An array containing the set’s members, or an empty array if the set has no members.
- [- anyObject](<anyobject().md>) — Returns one of the objects in the set, or `nil` if the set contains no objects.
- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the set.
- [- filteredSetUsingPredicate:](<filtered(using_).md>) — Evaluates a given predicate against each object in the receiving set and returns a new set containing the objects for which the predicate returns true.
- [- member:](<member(__).md>) — Determines whether a given object is present in the set, and returns that object if it is.
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each object in the set.
- [- enumerateObjectsUsingBlock:](<enumerateobjects(__).md>) — Executes a given block using each object in the set.
- [- objectsPassingTest:](<objects(passingtest_).md>) — Returns a set of objects that pass a test in a given block.
- [- objectsWithOptions:passingTest:](<objects(options_passingtest_).md>) — Returns a set of objects that pass a test in a given block, using the specified enumeration options.

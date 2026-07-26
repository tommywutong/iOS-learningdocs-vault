---
title: 'filtered(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/filtered(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/filtered(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/filtered%28using%3A%29.json'
content_hash: 'sha256:e0b10f789acf214f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# filtered(using:)

<sub>Instance Method</sub>

Evaluates a given predicate against each object in the receiving set and returns a new set containing the objects for which the predicate returns true.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func filtered(using predicate: NSPredicate) -> Set<AnyHashable>
```

## Parameters

- `predicate` — A predicate.

## Return Value

A new set containing the objects in the receiving set for which `predicate` returns true.

## Discussion

The following example illustrates the use of this method.

```objc
NSSet *sourceSet =
    [NSSet setWithObjects:@"One", @"Two", @"Three", @"Four", nil];
NSPredicate *predicate =
    [NSPredicate predicateWithFormat:@"SELF beginswith 'T'"];
NSSet *filteredSet =
    [sourceSet filteredSetUsingPredicate:predicate];
// filteredSet contains (Two, Three)
```

## See Also

### Accessing Set Members

- [allObjects](allobjects.md) — An array containing the set’s members, or an empty array if the set has no members.
- [- anyObject](<anyobject().md>) — Returns one of the objects in the set, or `nil` if the set contains no objects.
- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the set.
- [- member:](<member(__).md>) — Determines whether a given object is present in the set, and returns that object if it is.
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each object in the set.
- [- enumerateObjectsUsingBlock:](<enumerateobjects(__).md>) — Executes a given block using each object in the set.
- [- enumerateObjectsWithOptions:usingBlock:](<enumerateobjects(options_using_).md>) — Executes a given block using each object in the set, using the specified enumeration options.
- [- objectsPassingTest:](<objects(passingtest_).md>) — Returns a set of objects that pass a test in a given block.
- [- objectsWithOptions:passingTest:](<objects(options_passingtest_).md>) — Returns a set of objects that pass a test in a given block, using the specified enumeration options.

---
title: objectEnumerator()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsset/objectenumerator()
source_url: 'https://developer.apple.com/documentation/foundation/nsset/objectenumerator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/objectenumerator%28%29.json'
content_hash: 'sha256:2150569b84d3f50c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# objectEnumerator()

<sub>Instance Method</sub>

Returns an enumerator object that lets you access each object in the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objectEnumerator() -> NSEnumerator
```

## Return Value

An enumerator object that lets you access each object in the set.

## Discussion

The following code fragment illustrates how you can use this method.

```objc
NSEnumerator *enumerator = [mySet objectEnumerator];
id value;
 
while ((value = [enumerator nextObject])) {
    /* code that acts on the set’s values */
}
```

When this method is used with mutable subclasses of `NSSet`, your code shouldn’t modify the set during enumeration. If you intend to modify the set, use the [allObjects](allobjects.md) method to create a “snapshot” of the set’s members. Enumerate the snapshot, but make your modifications to the original set.

### Special Considerations

It is more efficient to use the fast enumeration protocol (see [NSFastEnumeration](../nsfastenumeration.md)). Fast enumeration is available in macOS 10.5 and later and iOS 2.0 and later.

## See Also

### Related Documentation

- [- nextObject](<../nsenumerator/nextobject().md>) — Returns the next object from the collection being enumerated.

### Accessing Set Members

- [allObjects](allobjects.md) — An array containing the set’s members, or an empty array if the set has no members.
- [- anyObject](<anyobject().md>) — Returns one of the objects in the set, or `nil` if the set contains no objects.
- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the set.
- [- filteredSetUsingPredicate:](<filtered(using_).md>) — Evaluates a given predicate against each object in the receiving set and returns a new set containing the objects for which the predicate returns true.
- [- member:](<member(__).md>) — Determines whether a given object is present in the set, and returns that object if it is.
- [- enumerateObjectsUsingBlock:](<enumerateobjects(__).md>) — Executes a given block using each object in the set.
- [- enumerateObjectsWithOptions:usingBlock:](<enumerateobjects(options_using_).md>) — Executes a given block using each object in the set, using the specified enumeration options.
- [- objectsPassingTest:](<objects(passingtest_).md>) — Returns a set of objects that pass a test in a given block.
- [- objectsWithOptions:passingTest:](<objects(options_passingtest_).md>) — Returns a set of objects that pass a test in a given block, using the specified enumeration options.

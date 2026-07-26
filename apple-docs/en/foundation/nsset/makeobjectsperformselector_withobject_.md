---
title: 'makeObjectsPerformSelector:withObject:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/makeobjectsperformselector:withobject:'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/makeobjectsperformselector:withobject:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/makeobjectsperformselector%3Awithobject%3A.json'
content_hash: 'sha256:83cfe956e6ab5710'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# makeObjectsPerformSelector:withObject:

<sub>Instance Method</sub>

Sends a message specified by a given selector to each object in the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) makeObjectsPerformSelector:(SEL) aSelector withObject:(id) argument;
```

## Parameters

- `aSelector` — A selector that specifies the message to send to the set’s members. The method must take a single argument of type `id`. The method should not, as a side effect, modify the set. The value must not be `NULL`.

- `argument` — The object to pass as an argument to the method specified by `aSelector`.

## Discussion

The message specified by `aSelector` is sent, with `argument` as the argument, once to each member of the set. This method raises an `NSInvalidArgumentException` if `aSelector` is `NULL`.

## See Also

### Accessing Set Members

- [allObjects](allobjects.md) — An array containing the set’s members, or an empty array if the set has no members.
- [- anyObject](<anyobject().md>) — Returns one of the objects in the set, or `nil` if the set contains no objects.
- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether a given object is present in the set.
- [- filteredSetUsingPredicate:](<filtered(using_).md>) — Evaluates a given predicate against each object in the receiving set and returns a new set containing the objects for which the predicate returns true.
- [makeObjectsPerformSelector:](makeobjectsperformselector_.md) — Sends a message specified by a given selector to each object in the set.
- [- member:](<member(__).md>) — Determines whether a given object is present in the set, and returns that object if it is.
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each object in the set.
- [- enumerateObjectsUsingBlock:](<enumerateobjects(__).md>) — Executes a given block using each object in the set.
- [- enumerateObjectsWithOptions:usingBlock:](<enumerateobjects(options_using_).md>) — Executes a given block using each object in the set, using the specified enumeration options.
- [- objectsPassingTest:](<objects(passingtest_).md>) — Returns a set of objects that pass a test in a given block.
- [- objectsWithOptions:passingTest:](<objects(options_passingtest_).md>) — Returns a set of objects that pass a test in a given block, using the specified enumeration options.

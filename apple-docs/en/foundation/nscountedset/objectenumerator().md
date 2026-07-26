---
title: objectEnumerator()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscountedset/objectenumerator()
source_url: 'https://developer.apple.com/documentation/foundation/nscountedset/objectenumerator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscountedset/objectenumerator%28%29.json'
content_hash: 'sha256:31d1ba4b998e9985'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCountedSet](../nscountedset.md)

# objectEnumerator()

<sub>Instance Method</sub>

Returns an enumerator object that lets you access each object in the set once, independent of its count.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objectEnumerator() -> NSEnumerator
```

## Return Value

An enumerator object that lets you access each object in the set once, independent of its count.

## Discussion

If you add a given object to the counted set multiple times, an enumeration of the set will produce that object only once.

You shouldn’t modify the set during enumeration. If you intend to modify the set, use the [allObjects](../nsset/allobjects.md) method to create a “snapshot,” then enumerate the snapshot and modify the original set.

## See Also

### Related Documentation

- [- nextObject](<../nsenumerator/nextobject().md>) — Returns the next object from the collection being enumerated.

### Examining a Counted Set

- [- countForObject:](<count(for_).md>) — Returns the count associated with a given object in the set.

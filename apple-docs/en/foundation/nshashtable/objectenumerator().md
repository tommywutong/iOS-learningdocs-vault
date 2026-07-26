---
title: objectEnumerator()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nshashtable/objectenumerator()
source_url: 'https://developer.apple.com/documentation/foundation/nshashtable/objectenumerator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtable/objectenumerator%28%29.json'
content_hash: 'sha256:6a0a6b4a6e0a38e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSHashTable](../nshashtable.md)

# objectEnumerator()

<sub>Instance Method</sub>

Returns an enumerator object that lets you access each object in the hash table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objectEnumerator() -> NSEnumerator
```

## Return Value

An enumerator object that lets you access each object in the hash table.

## Discussion

The following code fragment illustrates how you can use this method.

```objc
NSEnumerator *enumerator = [myHashTable objectEnumerator];
id value;
 
while ((value = [enumerator nextObject])) {
    /* code that acts on the hash table's values */
}
```

### Special Considerations

It is more efficient to use the fast enumeration protocol (see [NSFastEnumeration](../nsfastenumeration.md)).

## See Also

### Accessing Content

- [anyObject](anyobject.md) — One of the objects in the hash table.
- [allObjects](allobjects.md) — The hash table’s members.
- [setRepresentation](setrepresentation.md) — A set that contains the hash table’s members.
- [count](count.md) — The number of elements in the hash table.
- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether the hash table contains a given object.
- [- member:](<member(__).md>) — Determines whether the hash table contains a given object, and returns that object if it is present

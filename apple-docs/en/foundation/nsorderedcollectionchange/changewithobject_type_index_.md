---
title: 'changeWithObject:type:index:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedcollectionchange/changewithobject:type:index:'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedcollectionchange/changewithobject:type:index:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedcollectionchange/changewithobject%3Atype%3Aindex%3A.json'
content_hash: 'sha256:87018d6a55d2f9a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedCollectionChange](../nsorderedcollectionchange.md)

# changeWithObject:type:index:

<sub>Type Method</sub>

Creates an change object that represents inserting or removing an object from an ordered collection at a specific index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSOrderedCollectionChange<id> *) changeWithObject:(ObjectType) anObject type:(NSCollectionChangeType) type index:(NSUInteger) index;
```

## Parameters

- `anObject` — An object to be removed or inserted by the change.

- `type` — The type of change

- `index` — The index location within an ordered collection where the change applies.

## Return Value

An object that represents an indexed change to an ordered collection and references the object to be inserted or removed.

## See Also

### Creating a Change

- [- initWithObject:type:index:](<init(object_type_index_).md>) — Creates a change object that represents inserting or removing an object from an ordered collection at a specific index.
- [- initWithObject:type:index:associatedIndex:](<init(object_type_index_associatedindex_).md>) — Creates a change object that represents inserting, removing, or moving an object from an ordered collection at a specific index.
- [changeWithObject:type:index:associatedIndex:](changewithobject_type_index_associatedindex_.md) — Creates an change object that represents inserting or removing an object from an ordered collection at a specific index, matched with an associated location that infers a move within the collection.

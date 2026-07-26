---
title: RangeReplaceableCollection Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/contiguousarray/rangereplaceablecollection-implementations
source_url: 'https://developer.apple.com/documentation/swift/contiguousarray/rangereplaceablecollection-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/contiguousarray/rangereplaceablecollection-implementations.json'
content_hash: 'sha256:b9da4a4759154696'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md) · [ContiguousArray](../contiguousarray.md)

# RangeReplaceableCollection Implementations

<sub>API Collection</sub>

## Topics

### Operators

- [+(_:_:)](<+(____)-1rz1t.md>) — Creates a new collection by concatenating the elements of a collection and a sequence.
- [+(_:_:)](<+(____)-3ntif.md>) — Creates a new collection by concatenating the elements of a sequence and a collection.
- [+(_:_:)](<+(____)-5igl.md>) — Creates a new collection by concatenating the elements of two collections.
- [+=(_:_:)](<+=(____).md>) — Appends the elements of a sequence to a range-replaceable collection.

### Initializers

- [init()](<init().md>) — Creates a new, empty array.
- [init(_:)](<init(__)-19zub.md>) — Creates a new instance of a collection containing the elements of a sequence.
- [init(repeating:count:)](<init(repeating_count_).md>) — Creates a new array containing the specified number of a single, repeated value.
- [init(repeating:count:)](<init(repeating_count_)-47x84.md>) — Creates a new collection containing the specified number of a single, repeated value.

### Instance Methods

- [append(_:)](<append(__).md>) — Adds a new element at the end of the array.
- [append(_:)](<append(__)-4na3g.md>) — Adds an element to the end of the collection.
- [append(contentsOf:)](<append(contentsof_).md>) — Adds the elements of a sequence to the end of the array.
- [append(contentsOf:)](<append(contentsof_)-66qjk.md>) — Adds the elements of a sequence or collection to the end of this collection.
- [applying(_:)](<applying(__).md>) — Applies the given difference to this collection.
- [filter(_:)](<filter(__)-1km0c.md>) — Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
- [insert(_:at:)](<insert(__at_)-81ye7.md>) — Inserts a new element into the collection at the specified position.
- [insert(contentsOf:at:)](<insert(contentsof_at_).md>) — Inserts the elements of a sequence into the collection at the specified position.
- [popLast()](<poplast().md>) — Removes and returns the last element of the collection.
- [remove(at:)](<remove(at_)-6yx8z.md>) — Removes and returns the element at the specified position.
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — Removes all elements from the array.
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_)-2onkd.md>) — Removes all elements from the collection.
- [removeAll(where:)](<removeall(where_)-3or72.md>) — Removes all the elements that satisfy the given predicate.
- [removeAll(where:)](<removeall(where_)-44y75.md>) — Removes all the elements that satisfy the given predicate.
- [removeFirst()](<removefirst().md>) — Removes and returns the first element of the collection.
- [removeFirst(_:)](<removefirst(__).md>) — Removes the specified number of elements from the beginning of the collection.
- [removeLast()](<removelast().md>) — Removes and returns the last element of the collection.
- [removeLast(_:)](<removelast(__).md>) — Removes the specified number of elements from the end of the collection.
- [removeSubrange(_:)](<removesubrange(__)-3k98x.md>) — Removes the elements in the specified subrange from the collection.
- [removeSubrange(_:)](<removesubrange(__)-8cd5m.md>) — Removes the elements in the specified subrange from the collection.
- [removeSubranges(_:)](<removesubranges(__)-147en.md>) — Removes the elements at the given indices.
- [replaceSubrange(_:with:)](<replacesubrange(__with_).md>) — Replaces a range of elements with the elements in the specified collection.
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-4iomk.md>) — Replaces the specified subrange of elements with the given collection.
- [replaceSubrange(_:with:)](<replacesubrange(__with_)-95xhb.md>) — Replaces the specified subrange of elements with the given collection. _(deprecated)_
- [reserveCapacity(_:)](<reservecapacity(__)-4601w.md>) — Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.

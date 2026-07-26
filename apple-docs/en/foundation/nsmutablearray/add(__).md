---
title: 'add(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/add(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/add(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/add%28_%3A%29.json'
content_hash: 'sha256:83abc695e0a5346d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# add(_:)

<sub>Instance Method</sub>

Inserts a given object at the end of the array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func add(_ anObject: Any)
```

## Parameters

- `anObject` — The object to add to the end of the array’s content. This value must not be `nil`. > [!important] Important > Raises an `NSInvalidArgumentException` if `anObject` is `nil`.

## See Also

### Related Documentation

- [- removeObject:](<remove(__).md>) — Removes all occurrences in the array of a given object.
- [- setArray:](<setarray(__).md>) — Sets the receiving array’s elements to those in another given array.

### Adding Objects

- [- addObjectsFromArray:](<addobjects(from_).md>) — Adds the objects contained in another given array to the end of the receiving array’s content.
- [- insertObject:atIndex:](<insert(__at_)-5dbx5.md>) — Inserts a given object into the array’s contents at a given index.
- [- insertObjects:atIndexes:](<insert(__at_)-73pln.md>) — Inserts the objects in the provided array into the receiving array at the specified indexes.

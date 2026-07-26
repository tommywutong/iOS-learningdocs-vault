---
title: 'initWithObjects:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/initwithobjects:'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/initwithobjects:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/initwithobjects%3A.json'
content_hash: 'sha256:5d03dcd8fdce5e27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# initWithObjects:

<sub>Instance Method</sub>

Initializes a newly allocated array by placing in it the objects in the argument list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithObjects:(ObjectType) firstObj;
```

## Parameters

- `firstObj` — The first object for the array.

## Return Value

An array initialized to include the objects in the argument list. The returned object might be different than the original receiver.

## Discussion

Pass comma-separated list of trailing variadic arguments as additional objects, ending with `nil`.

After an immutable array has been initialized in this way, it can’t be modified.

This method is a designated initializer.

## See Also

### Related Documentation

- [arrayWithObjects:](arraywithobjects_.md) — Creates and returns an array containing the objects in the argument list.

### Initializing an Array

- [- init](<init().md>) — Initializes a newly allocated array.
- [- initWithArray:](<init(array_)-o72h.md>) — Initializes a newly allocated array by placing in it the objects contained in a given array.
- [- initWithArray:copyItems:](<init(array_copyitems_).md>) — Initializes a newly allocated array using `anArray` as the source of data objects for the array.
- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes a newly allocated array with the contents of the file specified by a given path. _(deprecated)_
- [- initWithObjects:count:](<init(objects_count_)-5odxv.md>) — Initializes a newly allocated array to include a given number of objects from a given C array.

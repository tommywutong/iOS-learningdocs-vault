---
title: 'init(objects:count:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/init(objects:count:)-5odxv'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/init(objects:count:)-5odxv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/init%28objects%3Acount%3A%29-5odxv.json'
content_hash: 'sha256:8d118dd4bef86591'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# init(objects:count:)

<sub>Initializer</sub>

Initializes a newly allocated array to include a given number of objects from a given C array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(objects: UnsafePointer<AnyObject>?, count cnt: Int)
```

## Parameters

- `objects` — A C array of objects.

- `cnt` — The number of values from the `objects` C array to include in the new array. This number will be the count of the new array—it must not be negative or greater than the number of elements in `objects`.

## Return Value

A newly allocated array including the first `count` objects from `objects`. The returned object might be different than the original receiver.

## Discussion

Elements are added to the new array in the same order they appear in `objects`, up to but not including index `count`.

After an immutable array has been initialized in this way, it can’t be modified.

This method is a designated initializer.

## See Also

### Initializing an Array

- [- init](<init().md>) — Initializes a newly allocated array.
- [- initWithArray:](<init(array_)-o72h.md>) — Initializes a newly allocated array by placing in it the objects contained in a given array.
- [- initWithArray:copyItems:](<init(array_copyitems_).md>) — Initializes a newly allocated array using `anArray` as the source of data objects for the array.
- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes a newly allocated array with the contents of the file specified by a given path. _(deprecated)_

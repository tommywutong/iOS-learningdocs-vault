---
title: init()
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsarray/init()
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/init%28%29.json'
content_hash: 'sha256:5e16bb59895422ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# init()

<sub>Initializer</sub>

Initializes a newly allocated array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Return Value

An array.

## Discussion

After an immutable array has been initialized in this way, it cannot be modified.

This method is a designated initializer.

## See Also

### Initializing an Array

- [- initWithArray:](<init(array_)-o72h.md>) — Initializes a newly allocated array by placing in it the objects contained in a given array.
- [- initWithArray:copyItems:](<init(array_copyitems_).md>) — Initializes a newly allocated array using `anArray` as the source of data objects for the array.
- [- initWithContentsOfFile:](<init(contentsoffile_).md>) — Initializes a newly allocated array with the contents of the file specified by a given path. _(deprecated)_
- [- initWithObjects:count:](<init(objects_count_)-5odxv.md>) — Initializes a newly allocated array to include a given number of objects from a given C array.

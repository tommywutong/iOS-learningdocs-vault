---
title: 'arrayWithCapacity:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/arraywithcapacity:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/arraywithcapacity:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/arraywithcapacity%3A.json'
content_hash: 'sha256:189c69ffed7b72c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# arrayWithCapacity:

<sub>Type Method</sub>

Creates and returns an `NSMutableArray` object with enough allocated memory to initially hold a given number of objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) arrayWithCapacity:(NSUInteger) numItems;
```

## Parameters

- `numItems` — The initial capacity of the new array.

## Return Value

A new `NSMutableArray` object with enough allocated memory to hold `numItems` objects.

## Discussion

Mutable arrays expand as needed; `numItems` simply establishes the object’s initial capacity.

## See Also

### Related Documentation

- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
- [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)

### Creating and Initializing a Mutable Array

- [arrayWithContentsOfFile:](arraywithcontentsoffile_.md) — Creates and returns a mutable array containing the contents of the file specified by the given path.
- [- init](<init().md>) — Initializes a newly allocated array.
- [- initWithCapacity:](<init(capacity_).md>) — Returns an array, initialized with enough memory to initially hold a given number of objects.
- [initWithContentsOfFile:](initwithcontentsoffile_.md) — Initializes a newly allocated mutable array with the contents of the file specified by a given path
- [initWithContentsOfURL:](initwithcontentsofurl_.md) — Initialized a newly allocated mutable array with the contents of the location specified by a given URL.

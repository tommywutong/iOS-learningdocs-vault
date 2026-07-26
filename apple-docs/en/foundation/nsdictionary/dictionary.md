---
title: dictionary
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdictionary/dictionary
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/dictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/dictionary.json'
content_hash: 'sha256:a5c6748b4f4b4881'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDictionary](../nsdictionary.md)

# dictionary

<sub>Type Method</sub>

Creates an empty dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dictionary;
```

## Return Value

A new empty dictionary.

## Discussion

This method is declared primarily for use with mutable subclasses of [NSDictionary](../nsdictionary.md).

If you don’t want a temporary object, you can also create an empty dictionary using `alloc` and [- init](<init().md>).

## See Also

### Related Documentation

- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
- [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i)

### Creating an Empty Dictionary

- [- init](<init().md>) — Initializes a newly allocated dictionary.

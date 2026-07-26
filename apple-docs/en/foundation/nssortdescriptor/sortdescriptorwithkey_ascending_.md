---
title: 'sortDescriptorWithKey:ascending:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nssortdescriptor/sortdescriptorwithkey:ascending:'
source_url: 'https://developer.apple.com/documentation/foundation/nssortdescriptor/sortdescriptorwithkey:ascending:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssortdescriptor/sortdescriptorwithkey%3Aascending%3A.json'
content_hash: 'sha256:146ca6f90cb5db9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSortDescriptor](../nssortdescriptor.md)

# sortDescriptorWithKey:ascending:

<sub>Type Method</sub>

Creates and returns a sort descriptor with the specified key path and ordering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) sortDescriptorWithKey:(NSString *) key ascending:(BOOL) ascending;
```

## Parameters

- `key` — The key path to use when performing a comparison. For information about key paths, see [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i).

- `ascending` — [true](../../swift/true.md) if the receiver specifies sorting in ascending order, otherwise [false](../../swift/false.md).

## Return Value

A sort descriptor initialized with the specified key path and sort order, and the default comparison selector ([compare](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/ci_gslang_ext.html#//apple_ref/doc/uid/TP40004397-CH206-BCIECEBI)).

## See Also

### Related Documentation

- [Sort Descriptor Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SortDescriptors/SortDescriptors.html#//apple_ref/doc/uid/10000174i)

### Creating a Sort Descriptor

- [- initWithKey:ascending:](<init(key_ascending_).md>) — Creates a sort descriptor with a specified string key path and sort order.
- [sortDescriptorWithKey:ascending:selector:](sortdescriptorwithkey_ascending_selector_.md) — Creates a sort descriptor with the specified key path, ordering, and comparison selector.
- [- initWithKey:ascending:selector:](<init(key_ascending_selector_).md>) — Creates a sort descriptor with a specified string key path, ordering, and comparison selector.
- [sortDescriptorWithKey:ascending:comparator:](sortdescriptorwithkey_ascending_comparator_.md) — Creates and returns a sort descriptor initialized with the specified key path and ordering, and a comparator block.
- [- initWithKey:ascending:comparator:](<init(key_ascending_comparator_).md>) — Creates a sort descriptor with a specified string key path and ordering, and a comparator block.
- [- initWithCoder:](<init(coder_).md>) — Creates a sort descriptor by decoding from the coder you specify.

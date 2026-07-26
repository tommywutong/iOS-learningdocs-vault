---
title: 'sortDescriptorWithKey:ascending:selector:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nssortdescriptor/sortdescriptorwithkey:ascending:selector:'
source_url: 'https://developer.apple.com/documentation/foundation/nssortdescriptor/sortdescriptorwithkey:ascending:selector:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssortdescriptor/sortdescriptorwithkey%3Aascending%3Aselector%3A.json'
content_hash: 'sha256:8043789f3627f23a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSortDescriptor](../nssortdescriptor.md)

# sortDescriptorWithKey:ascending:selector:

<sub>Type Method</sub>

Creates a sort descriptor with the specified key path, ordering, and comparison selector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) sortDescriptorWithKey:(NSString *) key ascending:(BOOL) ascending selector:(SEL) selector;
```

## Parameters

- `key` — The key path for performing a comparison. For information about key paths, see [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i).

- `ascending` — [true](../../swift/true.md) if the receiver specifies sorting in ascending order; otherwise, [false](../../swift/false.md).

- `selector` — The method to use when comparing the properties of objects, for example [- localizedStandardCompare:](<../nsstring/localizedstandardcompare(__).md>). The selector must specify a method implemented by the value of the property identified by the key path. The selector used for the comparison is passed a single parameter, the object to compare against, and it returns the appropriate [ComparisonResult](../comparisonresult.md) constant.

## Return Value

A sort descriptor that initializes with the specified key path, sort order, and comparison selector.

## See Also

### Creating a Sort Descriptor

- [sortDescriptorWithKey:ascending:](sortdescriptorwithkey_ascending_.md) — Creates and returns a sort descriptor with the specified key path and ordering.
- [- initWithKey:ascending:](<init(key_ascending_).md>) — Creates a sort descriptor with a specified string key path and sort order.
- [- initWithKey:ascending:selector:](<init(key_ascending_selector_).md>) — Creates a sort descriptor with a specified string key path, ordering, and comparison selector.
- [sortDescriptorWithKey:ascending:comparator:](sortdescriptorwithkey_ascending_comparator_.md) — Creates and returns a sort descriptor initialized with the specified key path and ordering, and a comparator block.
- [- initWithKey:ascending:comparator:](<init(key_ascending_comparator_).md>) — Creates a sort descriptor with a specified string key path and ordering, and a comparator block.
- [- initWithCoder:](<init(coder_).md>) — Creates a sort descriptor by decoding from the coder you specify.

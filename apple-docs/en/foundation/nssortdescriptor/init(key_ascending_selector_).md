---
title: 'init(key:ascending:selector:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nssortdescriptor/init(key:ascending:selector:)'
source_url: 'https://developer.apple.com/documentation/foundation/nssortdescriptor/init(key:ascending:selector:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssortdescriptor/init%28key%3Aascending%3Aselector%3A%29.json'
content_hash: 'sha256:0b79b099d9f8b308'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSortDescriptor](../nssortdescriptor.md)

# init(key:ascending:selector:)

<sub>Initializer</sub>

Creates a sort descriptor with a specified string key path, ordering, and comparison selector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(key: String?, ascending: Bool, selector: Selector?)
```

## Parameters

- `key` — The key path for performing a comparison. For information about key paths, see [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i).

- `ascending` — [true](../../swift/true.md) if the receiver specifies sorting in ascending order; otherwise, [false](../../swift/false.md).

- `selector` — The method to use when comparing the properties of objects, such as [- localizedStandardCompare:](<../nsstring/localizedstandardcompare(__).md>). The selector must specify a method that you implement according to the value of the property that the key path identifies. Pass the selector a single parameter, the object to compare against, and it returns the appropriate [ComparisonResult](../comparisonresult.md) constant.

## Return Value

A sort descriptor that initializes with the specified key path, sort order, and comparison selector.

## See Also

### Creating a Sort Descriptor

- [- initWithKey:ascending:](<init(key_ascending_).md>) — Creates a sort descriptor with a specified string key path and sort order.
- [init(keyPath:ascending:)](<init(keypath_ascending_).md>) — Creates a sort descriptor with a specified key path and ordering.
- [- initWithKey:ascending:comparator:](<init(key_ascending_comparator_).md>) — Creates a sort descriptor with a specified string key path and ordering, and a comparator block.
- [init(keyPath:ascending:comparator:)](<init(keypath_ascending_comparator_).md>) — Creates a sort descriptor with a specified key path and ordering, and a comparator block.
- [- initWithCoder:](<init(coder_).md>) — Creates a sort descriptor by decoding from the coder you specify.
- [init(_:)](<init(__)-7qf91.md>) — Creates a sort descriptor using a sort descriptor you specify. _(deprecated)_

---
title: 'stringWithCapacity:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablestring/stringwithcapacity:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablestring/stringwithcapacity:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablestring/stringwithcapacity%3A.json'
content_hash: 'sha256:594c33c77b45218b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableString](../nsmutablestring.md)

# stringWithCapacity:

<sub>Type Method</sub>

Returns an empty `NSMutableString` object with initial storage for a given number of characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSMutableString *) stringWithCapacity:(NSUInteger) capacity;
```

## Parameters

- `capacity` — The number of characters the string is expected to initially contain.

## Return Value

An empty `NSMutableString` object with initial storage for `capacity` characters.

## Discussion

The number of characters indicated by `capacity` is simply a hint to increase the efficiency of data storage. The value does _not_ limit the length of the string.

## See Also

### Related Documentation

- [String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i)

### Creating and Initializing a Mutable String

- [- initWithCapacity:](<init(capacity_).md>) — Returns an `NSMutableString` object initialized with initial storage for a given number of characters,

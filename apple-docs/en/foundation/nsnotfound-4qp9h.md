---
title: NSNotFound
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotfound-4qp9h
source_url: 'https://developer.apple.com/documentation/foundation/nsnotfound-4qp9h'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotfound-4qp9h.json'
content_hash: 'sha256:f902d3a8029c2625'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSNotFound

<sub>Global Variable</sub>

A value indicating that a requested item couldn’t be found or doesn’t exist.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSNotFound: Int { get }
```

## Discussion

`NSNotFound` is typically used by various methods and functions that search for items in serial data and return indices, such as characters in a string object or `id` objects in an `NSArray` object.

### Special Considerations

Prior to OS X v10.5, `NSNotFound` was defined as `0x7fffffff`. For 32-bit systems, this was effectively the same as `NSIntegerMax`. To support 64-bit environments, `NSNotFound` is now formally defined as `NSIntegerMax`. This means, however, that the value is different in 32-bit and 64-bit environments. You should therefore not save the value directly in files or archives. Moreover, sending the value between 32-bit and 64-bit processes via Distributed Objects will not get you `NSNotFound` on the other side. This applies to any Cocoa methods invoked over Distributed Objects and which might return `NSNotFound`, such as the `indexOfObject:` method of `NSArray` (if sent to a proxy for an array).

## See Also

### Special Semantic Values

- [NSNull](nsnull.md) — A singleton object used to represent null values in collection objects that don’t allow `nil` values.
- [NSNotFound](nsnotfound-9t5v2.md)

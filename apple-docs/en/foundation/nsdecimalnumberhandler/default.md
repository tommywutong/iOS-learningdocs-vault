---
title: default
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdecimalnumberhandler/default
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumberhandler/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumberhandler/default.json'
content_hash: 'sha256:c2603250ea8ed658'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumberHandler](../nsdecimalnumberhandler.md)

# default

<sub>Type Property</sub>

Returns the default instance of `NSDecimalNumberHandler`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var `default`: NSDecimalNumberHandler { get }
```

## Return Value

The default instance of `NSDecimalNumberHandler`.

## Discussion

This default decimal number handler rounds to the closest possible return value. It assumes your need for precision does not exceed 38 significant digits, and it raises an exception when its `NSDecimalNumber` object tries to divide by `0` or when its `NSDecimalNumber` object produces a number too big or too small to be represented.

## See Also

### Related Documentation

- [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i)

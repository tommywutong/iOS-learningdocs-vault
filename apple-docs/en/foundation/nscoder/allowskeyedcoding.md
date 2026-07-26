---
title: allowsKeyedCoding
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscoder/allowskeyedcoding
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/allowskeyedcoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/allowskeyedcoding.json'
content_hash: 'sha256:06dbb20d6d366514'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# allowsKeyedCoding

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver supports keyed coding of objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsKeyedCoding: Bool { get }
```

## Discussion

[false](../../swift/false.md) by default. Concrete subclasses that support keyed coding, such as `NSKeyedArchiver`, need to override this property to return [true](../../swift/true.md).

## See Also

### Related Documentation

- [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)

### Inspecting a Coder

- [- containsValueForKey:](<containsvalue(forkey_).md>) — Returns a Boolean value that indicates whether an encoded value is available for a string.
- [decodingFailurePolicy](decodingfailurepolicy-swift.property.md) — The action the coder should take when decoding fails.
- [DecodingFailurePolicy](decodingfailurepolicy-swift.enum.md) — Policies describing the action the coder should take when encountering decode failures.

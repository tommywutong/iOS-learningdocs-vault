---
title: decodingFailurePolicy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscoder/decodingfailurepolicy-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodingfailurepolicy-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodingfailurepolicy-swift.property.json'
content_hash: 'sha256:a2a68784694efc18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodingFailurePolicy

<sub>Instance Property</sub>

The action the coder should take when decoding fails.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var decodingFailurePolicy: NSCoder.DecodingFailurePolicy { get }
```

## Discussion

A decode call can fail for the following reasons:

- The keyed archive data is corrupt or missing.
- A type mismatch occurs, such as expecting a class by calling [decodeObject(of:forKey:)](<decodeobject(of_forkey_)-7tmft.md>) but encountering a numeric type instead. This also occurs when [- decodeIntegerForKey:](<decodeinteger(forkey_).md>) encounters a value encoded as floating-point, or vice versa.
- A secure coding violation occurs. This happens when you attempt to decode an object that doesn’t conform to [NSSecureCoding](../nssecurecoding.md). This also happens when the encoded type doesn’t match any of the types passed to [decodeObject(of:forKey:)](<decodeobject(of_forkey_)-roif.md>).

## See Also

### Inspecting a Coder

- [allowsKeyedCoding](allowskeyedcoding.md) — A Boolean value that indicates whether the receiver supports keyed coding of objects.
- [- containsValueForKey:](<containsvalue(forkey_).md>) — Returns a Boolean value that indicates whether an encoded value is available for a string.
- [DecodingFailurePolicy](decodingfailurepolicy-swift.enum.md) — Policies describing the action the coder should take when encountering decode failures.

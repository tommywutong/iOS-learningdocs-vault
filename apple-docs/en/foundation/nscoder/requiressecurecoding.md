---
title: requiresSecureCoding
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscoder/requiressecurecoding
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/requiressecurecoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/requiressecurecoding.json'
content_hash: 'sha256:8da6987c70afc268'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# requiresSecureCoding

<sub>Instance Property</sub>

Indicates whether the archiver requires all archived classes to resist object substitution attacks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var requiresSecureCoding: Bool { get }
```

## Discussion

[true](../../swift/true.md) if this coder requires secure coding; [false](../../swift/false.md) otherwise.

Secure coders check a set of allowed classes before decoding objects, and all objects must implement the [NSSecureCoding](../nssecurecoding.md) protocol.

## See Also

### Related Documentation

- [allowsKeyedCoding](allowskeyedcoding.md) — A Boolean value that indicates whether the receiver supports keyed coding of objects.

### Secure Coding

- [allowedClasses](allowedclasses.md) — The set of coded classes allowed for secure coding.

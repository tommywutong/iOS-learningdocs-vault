---
title: allowedClasses
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscoder/allowedclasses
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/allowedclasses'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/allowedclasses.json'
content_hash: 'sha256:8549be7685b7ee0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# allowedClasses

<sub>Instance Property</sub>

The set of coded classes allowed for secure coding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowedClasses: Set<AnyHashable>? { get }
```

## Discussion

Secure coders check this set of allowed classes before decoding objects, and all objects must implement the [NSSecureCoding](../nssecurecoding.md) protocol.

## See Also

### Secure Coding

- [requiresSecureCoding](requiressecurecoding.md) — Indicates whether the archiver requires all archived classes to resist object substitution attacks.

---
title: opaquePersonality
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerfunctions/options/opaquepersonality
source_url: 'https://developer.apple.com/documentation/foundation/nspointerfunctions/options/opaquepersonality'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerfunctions/options/opaquepersonality.json'
content_hash: 'sha256:853e6b20ef66c0d2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSPointerFunctions](../../nspointerfunctions.md) · [Options](../options.md)

# opaquePersonality

<sub>Type Property</sub>

Use shifted pointer for the hash value and direct comparison to determine equality.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var opaquePersonality: NSPointerFunctions.Options { get }
```

## See Also

### Personality Options

- [NSPointerFunctionsCStringPersonality](cstringpersonality.md) — Use a string hash and `strcmp`; C-string ‘`%s`’ style description.
- [NSPointerFunctionsIntegerPersonality](integerpersonality.md) — Use unshifted value as hash and equality.
- [NSPointerFunctionsObjectPersonality](objectpersonality.md) — Use `hash` and `isEqual` methods for hashing and equality comparisons, use the `description` method for a description.
- [NSPointerFunctionsObjectPointerPersonality](objectpointerpersonality.md) — Use shifted pointer for the hash value and direct comparison to determine equality; use the `description` method for a description.
- [NSPointerFunctionsStructPersonality](structpersonality.md) — Use a memory hash and `memcmp` (using a size function that you must set—see [sizeFunction](../sizefunction.md)).
- [NSMapTableObjectPointerPersonality](../../nsmaptableobjectpointerpersonality.md) — Equivalent to [NSPointerFunctionsObjectPointerPersonality](objectpointerpersonality.md).

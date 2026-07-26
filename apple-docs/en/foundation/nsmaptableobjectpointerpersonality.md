---
title: NSMapTableObjectPointerPersonality
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmaptableobjectpointerpersonality
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptableobjectpointerpersonality'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptableobjectpointerpersonality.json'
content_hash: 'sha256:0ad1ac3f14dc28e7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMapTableObjectPointerPersonality

<sub>Global Variable</sub>

Equivalent to [NSPointerFunctionsObjectPointerPersonality](nspointerfunctions/options/objectpointerpersonality.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSMapTableObjectPointerPersonality: NSPointerFunctions.Options { get }
```

## See Also

### Personality Options

- [NSPointerFunctionsCStringPersonality](nspointerfunctions/options/cstringpersonality.md) — Use a string hash and `strcmp`; C-string ‘`%s`’ style description.
- [NSPointerFunctionsIntegerPersonality](nspointerfunctions/options/integerpersonality.md) — Use unshifted value as hash and equality.
- [NSPointerFunctionsObjectPersonality](nspointerfunctions/options/objectpersonality.md) — Use `hash` and `isEqual` methods for hashing and equality comparisons, use the `description` method for a description.
- [NSPointerFunctionsObjectPointerPersonality](nspointerfunctions/options/objectpointerpersonality.md) — Use shifted pointer for the hash value and direct comparison to determine equality; use the `description` method for a description.
- [NSPointerFunctionsOpaquePersonality](nspointerfunctions/options/opaquepersonality.md) — Use shifted pointer for the hash value and direct comparison to determine equality.
- [NSPointerFunctionsStructPersonality](nspointerfunctions/options/structpersonality.md) — Use a memory hash and `memcmp` (using a size function that you must set—see [sizeFunction](nspointerfunctions/sizefunction.md)).

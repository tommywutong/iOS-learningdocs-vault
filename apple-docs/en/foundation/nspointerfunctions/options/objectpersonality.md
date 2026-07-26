---
title: objectPersonality
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerfunctions/options/objectpersonality
source_url: 'https://developer.apple.com/documentation/foundation/nspointerfunctions/options/objectpersonality'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerfunctions/options/objectpersonality.json'
content_hash: 'sha256:504729c5024dfccd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSPointerFunctions](../../nspointerfunctions.md) · [Options](../options.md)

# objectPersonality

<sub>Type Property</sub>

Use `hash` and `isEqual` methods for hashing and equality comparisons, use the `description` method for a description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var objectPersonality: NSPointerFunctions.Options { get }
```

## Discussion

This is the default personality value.

As a special case, if you do not use garbage collection and specify this value in conjunction with [NSPointerFunctionsStrongMemory](strongmemory.md) then the `NSPointerFunctions` object uses `retain` and `release`.

## See Also

### Personality Options

- [NSPointerFunctionsCStringPersonality](cstringpersonality.md) — Use a string hash and `strcmp`; C-string ‘`%s`’ style description.
- [NSPointerFunctionsIntegerPersonality](integerpersonality.md) — Use unshifted value as hash and equality.
- [NSPointerFunctionsObjectPointerPersonality](objectpointerpersonality.md) — Use shifted pointer for the hash value and direct comparison to determine equality; use the `description` method for a description.
- [NSPointerFunctionsOpaquePersonality](opaquepersonality.md) — Use shifted pointer for the hash value and direct comparison to determine equality.
- [NSPointerFunctionsStructPersonality](structpersonality.md) — Use a memory hash and `memcmp` (using a size function that you must set—see [sizeFunction](../sizefunction.md)).
- [NSMapTableObjectPointerPersonality](../../nsmaptableobjectpointerpersonality.md) — Equivalent to [NSPointerFunctionsObjectPointerPersonality](objectpointerpersonality.md).

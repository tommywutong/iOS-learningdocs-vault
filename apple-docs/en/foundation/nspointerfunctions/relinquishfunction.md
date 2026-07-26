---
title: relinquishFunction
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerfunctions/relinquishfunction
source_url: 'https://developer.apple.com/documentation/foundation/nspointerfunctions/relinquishfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerfunctions/relinquishfunction.json'
content_hash: 'sha256:87aa1f0695da76ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerFunctions](../nspointerfunctions.md)

# relinquishFunction

<sub>Instance Property</sub>

The function used to relinquish memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var relinquishFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> Void)? { get set }
```

## Discussion

This specifies the function to use when an item is removed from a table or pointer array.

## See Also

### Memory Configuration

- [acquireFunction](acquirefunction.md) — The function used to acquire memory.
- [usesStrongWriteBarrier](usesstrongwritebarrier.md) — Specifies whether, in a garbage collected environment, pointers should be assigned using a strong write barrier. _(deprecated)_
- [usesWeakReadAndWriteBarriers](usesweakreadandwritebarriers.md) — Specifies whether, in a garbage collected environment, pointers should use weak read and write barriers. _(deprecated)_

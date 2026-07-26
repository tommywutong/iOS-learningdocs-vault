---
title: usesStrongWriteBarrier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（10.0 起废弃）, iPadOS 2.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.12 起废弃）, tvOS 9.0+（10.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nspointerfunctions/usesstrongwritebarrier
source_url: 'https://developer.apple.com/documentation/foundation/nspointerfunctions/usesstrongwritebarrier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerfunctions/usesstrongwritebarrier.json'
content_hash: 'sha256:5978b054f64caa69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerFunctions](../nspointerfunctions.md)

# usesStrongWriteBarrier

<sub>Instance Property</sub>

Specifies whether, in a garbage collected environment, pointers should be assigned using a strong write barrier.

> [!warning] Deprecated
> Garbage collection no longer supported

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var usesStrongWriteBarrier: Bool { get set }
```

## Discussion

If you use garbage collection, read and write barrier functions must be used when pointers are from memory scanned by the collector.

## See Also

### Memory Configuration

- [acquireFunction](acquirefunction.md) — The function used to acquire memory.
- [relinquishFunction](relinquishfunction.md) — The function used to relinquish memory.
- [usesWeakReadAndWriteBarriers](usesweakreadandwritebarriers.md) — Specifies whether, in a garbage collected environment, pointers should use weak read and write barriers. _(deprecated)_

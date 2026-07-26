---
title: acquireFunction
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerfunctions/acquirefunction
source_url: 'https://developer.apple.com/documentation/foundation/nspointerfunctions/acquirefunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerfunctions/acquirefunction.json'
content_hash: 'sha256:f789bd58fab895c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerFunctions](../nspointerfunctions.md)

# acquireFunction

<sub>Instance Property</sub>

The function used to acquire memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var acquireFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?, ObjCBool) -> UnsafeMutableRawPointer)? { get set }
```

## Discussion

This specifies the function to use for copy-in operations.

## See Also

### Memory Configuration

- [relinquishFunction](relinquishfunction.md) — The function used to relinquish memory.
- [usesStrongWriteBarrier](usesstrongwritebarrier.md) — Specifies whether, in a garbage collected environment, pointers should be assigned using a strong write barrier. _(deprecated)_
- [usesWeakReadAndWriteBarriers](usesweakreadandwritebarriers.md) — Specifies whether, in a garbage collected environment, pointers should use weak read and write barriers. _(deprecated)_

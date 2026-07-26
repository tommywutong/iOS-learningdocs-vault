---
title: inferMoves
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsorderedcollectiondifferencecalculationoptions/infermoves
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedcollectiondifferencecalculationoptions/infermoves'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedcollectiondifferencecalculationoptions/infermoves.json'
content_hash: 'sha256:85a571c4ead964f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedCollectionDifferenceCalculationOptions](../nsorderedcollectiondifferencecalculationoptions.md)

# inferMoves

<sub>Type Property</sub>

An option that identifies insertions or removals as moves.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var inferMoves: NSOrderedCollectionDifferenceCalculationOptions { get }
```

## Discussion

When you use the option to infer moves, the difference calculation adds an associated index to change objects to indicate the original positions of the objects.

## See Also

### Difference Calculation Options

- [NSOrderedCollectionDifferenceCalculationOmitInsertedObjects](omitinsertedobjects.md) — An option that indicates that the difference should omit references to the insertions.
- [NSOrderedCollectionDifferenceCalculationOmitRemovedObjects](omitremovedobjects.md) — An option that indicates that the difference should omit references to the removals.

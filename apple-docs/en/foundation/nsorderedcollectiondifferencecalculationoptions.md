---
title: NSOrderedCollectionDifferenceCalculationOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsorderedcollectiondifferencecalculationoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedcollectiondifferencecalculationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedcollectiondifferencecalculationoptions.json'
content_hash: 'sha256:dc3021fe99ff41b7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSOrderedCollectionDifferenceCalculationOptions

<sub>Structure</sub>

Constants that specify the options to use when creating an ordered collection difference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSOrderedCollectionDifferenceCalculationOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Creating Difference Calculation Options

- [init(rawValue:)](<nsorderedcollectiondifferencecalculationoptions/init(rawvalue_).md>) — Creates a set of difference calculation options.

### Difference Calculation Options

- [NSOrderedCollectionDifferenceCalculationInferMoves](nsorderedcollectiondifferencecalculationoptions/infermoves.md) — An option that identifies insertions or removals as moves.
- [NSOrderedCollectionDifferenceCalculationOmitInsertedObjects](nsorderedcollectiondifferencecalculationoptions/omitinsertedobjects.md) — An option that indicates that the difference should omit references to the insertions.
- [NSOrderedCollectionDifferenceCalculationOmitRemovedObjects](nsorderedcollectiondifferencecalculationoptions/omitremovedobjects.md) — An option that indicates that the difference should omit references to the removals.

## See Also

### Comparing with Another Array

- [NSOrderedCollectionDifference](nsorderedcollectiondifference.md) — An object representing the difference between two ordered collections.

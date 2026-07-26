---
title: 'differenceFromArray:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/differencefromarray:'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/differencefromarray:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/differencefromarray%3A.json'
content_hash: 'sha256:6250c59e1ac42392'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# differenceFromArray:

<sub>Instance Method</sub>

Compares two arrays to create a difference object that represents the changes between them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSOrderedCollectionDifference<id> *) differenceFromArray:(NSArray<id> *) other;
```

## Discussion

The difference method creates the difference object by comparing objects within the arrays with the `isEqual:` method.

The following example computes the difference between two arrays:

```objc
NSArray *original = @[@"1", @"2"];
NSArray *modified = @[@"1", @"2", @"3"];

NSOrderedCollectionDifference *diff = [modified differenceFromArray:original];
// diff.hasChanges == TRUE
// diff.insertions.count == 1
// diff.removals.count == 0
```

## See Also

### Comparing with Another Array

- [differenceFromArray:withOptions:](differencefromarray_withoptions_.md) — Compares two arrays, with options, to create a difference object that represents the changes between them.
- [differenceFromArray:withOptions:usingEquivalenceTest:](differencefromarray_withoptions_usingequivalencetest_.md) — Compares two arrays, using the provided block and with options, to create a difference object that represents the changes between them.
- [NSOrderedCollectionDifference](../nsorderedcollectiondifference.md) — An object representing the difference between two ordered collections.
- [NSOrderedCollectionDifferenceCalculationOptions](../nsorderedcollectiondifferencecalculationoptions.md) — Constants that specify the options to use when creating an ordered collection difference.

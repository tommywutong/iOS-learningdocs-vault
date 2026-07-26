---
title: 'differenceFromOrderedSet:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/differencefromorderedset:'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/differencefromorderedset:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/differencefromorderedset%3A.json'
content_hash: 'sha256:84a093afff00e1bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# differenceFromOrderedSet:

<sub>Instance Method</sub>

Compares two ordered sets to create a difference object that represents the changes between them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSOrderedCollectionDifference<id> *) differenceFromOrderedSet:(NSOrderedSet<id> *) other;
```

## Discussion

The difference method creates the difference object by comparing objects within the ordered sets with the `isEqual:` method.

The following example computes the difference between two ordered sets:

```objc
NSOrderedSet *original = [NSOrderedSet orderedSetWithObjects:@"1", @"2", nil];
NSOrderedSet *modified = [NSOrderedSet orderedSetWithObjects:@"1", @"2", @"3", nil];

NSOrderedCollectionDifference *diff = [modified differenceFromOrderedSet:original];
NSLog(@"diff is: %@", diff.debugDescription);
// diff.hasChanges == true
// diff.insertions.count == 1
// diff.removals.count == 0
```

## See Also

### Comparing with Another Set

- [differenceFromOrderedSet:withOptions:](differencefromorderedset_withoptions_.md) — Compares two ordered sets, with options, to create a difference object that represents the changes between them.
- [differenceFromOrderedSet:withOptions:usingEquivalenceTest:](differencefromorderedset_withoptions_usingequivalencetest_.md) — Compares two ordered sets, using the provided block and with options, to create a difference object that represents the changes between them.
- [NSOrderedCollectionDifference](../nsorderedcollectiondifference.md) — An object representing the difference between two ordered collections.
- [NSOrderedCollectionDifferenceCalculationOptions](../nsorderedcollectiondifferencecalculationoptions.md) — Constants that specify the options to use when creating an ordered collection difference.

---
title: inverse()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsorderedcollectiondifference/inverse()
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedcollectiondifference/inverse()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedcollectiondifference/inverse%28%29.json'
content_hash: 'sha256:3e6cd6859cd4802e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedCollectionDifference](../nsorderedcollectiondifference.md)

# inverse()

<sub>Instance Method</sub>

Calculate the difference between two objects in the reverse direction of comparison.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func inverse() -> Self
```

## Return Value

A copy of the receiver with all removals changed to insertions (and vice versa).

## Discussion

Applying a difference to an ordered collection and then applying the inverse difference results in the original ordered collection:

```objc
NSArray *original = @[@"1", @"2"];
NSArray *modified = [original arrayByAddingObject:@"3"];

NSOrderedCollectionDifference *diff = [modified differenceFromArray:original];

NSArray *updated = [original arrayByApplyingDifference:diff];
// updated == [@"1", @"2", @"3"] == modified

NSOrderedCollectionDifference *inverse = [diff inverseDifference];

updated = [updated arrayByApplyingDifference:inverse];
// updated == [@"1", @"2"] == original
```

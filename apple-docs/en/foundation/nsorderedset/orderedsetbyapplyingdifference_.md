---
title: 'orderedSetByApplyingDifference:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/orderedsetbyapplyingdifference:'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/orderedsetbyapplyingdifference:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/orderedsetbyapplyingdifference%3A.json'
content_hash: 'sha256:34e59ce39b3685e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# orderedSetByApplyingDifference:

<sub>Instance Method</sub>

Creates a new ordered set by applying a difference object to an existing ordered set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSOrderedSet<id> *) orderedSetByApplyingDifference:(NSOrderedCollectionDifference<id> *) difference;
```

## Discussion

The following example computes the difference between two ordered sets, then applies the difference to create an ordered set that duplicates the original:

```objc
NSOrderedSet *original = [NSOrderedSet orderedSetWithObjects:@"1", @"2", nil];
NSOrderedSet *modified = [NSOrderedSet orderedSetWithObjects:@"1", @"2", @"3", nil];

NSOrderedCollectionDifference *diff = [modified differenceFromOrderedSet:original];
// diff.hasChanges == true
// diff.insertions.count == 1
// diff.removals.count == 0

NSOrderedSet *updated = [original orderedSetByApplyingDifference:diff];
// updated == [@"1", @"2", @"3"]

```

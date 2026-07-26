---
title: 'arrayByApplyingDifference:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/arraybyapplyingdifference:'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/arraybyapplyingdifference:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/arraybyapplyingdifference%3A.json'
content_hash: 'sha256:3c7cf03f06afb570'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# arrayByApplyingDifference:

<sub>Instance Method</sub>

Creates a new array by applying a difference object to an existing array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSArray<id> *) arrayByApplyingDifference:(NSOrderedCollectionDifference<id> *) difference;
```

## Discussion

The following example computes the difference between two arrays, then applies the difference to create an array that duplicates the original:

```objc
NSArray *original = @[@"1", @"2"];
NSArray *modified = @[@"1", @"2", @"3"];

NSOrderedCollectionDifference *diff = [modified differenceFromArray:original];
// diff.hasChanges == true
// diff.insertions.count == 
// diff.removals.count == 0

NSArray *updated = [original arrayByApplyingDifference:diff];
// updated == [@"1", @"2", @"3"]

```

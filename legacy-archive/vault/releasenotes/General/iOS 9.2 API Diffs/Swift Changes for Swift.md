---
title: iOS 9.2 API Diffs
apple_id: TP40016605
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS92APIDiffs/Swift/Swift.html
archived_at: '2026-07-18T02:57:12.907347Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.2 API Diffs](iOS%209.1%20to%20iOS%209.2%20API%20Differences.md)


# Swift Changes for Swift

### Swift

Added BidirectionalIndexType.predecessor() -> SelfAdded CollectionType.countAdded CollectionType.dropLast(_: Int) -> Self.SubSequenceAdded CollectionType.firstAdded CollectionType.isEmptyAdded CollectionType.prefixThrough(_: Self.Index) -> Self.SubSequenceAdded CollectionType.prefixUpTo(_: Self.Index) -> Self.SubSequenceAdded CollectionType.startIndexAdded CollectionType.suffix(_: Int) -> Self.SubSequenceAdded CollectionType.suffixFrom(_: Self.Index) -> Self.SubSequenceAdded ForwardIndexType.advancedBy(_: Self.Distance) -> SelfAdded ForwardIndexType.advancedBy(_: Self.Distance, limit: Self) -> SelfAdded ForwardIndexType.distanceTo(_: Self) -> Self.DistanceAdded RandomAccessIndexType.advancedBy(_: Self.Distance, limit: Self) -> SelfAdded RangeReplaceableCollectionType.append(_: Self.Generator.Element)Added RangeReplaceableCollectionType.appendContentsOf<S : SequenceType where S.Generator.Element == Generator.Element>(_: S)Added RangeReplaceableCollectionType.insert(_: Self.Generator.Element, atIndex: Self.Index)Added RangeReplaceableCollectionType.removeAll(keepCapacity: Bool)Added RangeReplaceableCollectionType.removeAtIndex(_: Self.Index) -> Self.Generator.ElementAdded RangeReplaceableCollectionType.removeFirst() -> Self.Generator.ElementAdded RangeReplaceableCollectionType.removeFirst(_: Int)Added RangeReplaceableCollectionType.removeRange(_: Range<Self.Index>)Added RangeReplaceableCollectionType.reserveCapacity(_: Self.Index.Distance)Added SequenceType.filter(_: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.Generator.Element]Added SequenceType.filter(_: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.Generator.Element]Added SequenceType.forEach(_: (Self.Generator.Element) throws -> ()) rethrowsAdded SequenceType.generate() -> Self.GeneratorAdded SequenceType.map<T>(_: (Self.Generator.Element) throws -> T) rethrows -> [T]Added SequenceType.map<T>(_: (Self.Generator.Element) throws -> T) rethrows -> [T]Added SequenceType.underestimateCount() -> IntAdded SequenceType.underestimateCount() -> Int

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

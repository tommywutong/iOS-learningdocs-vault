---
title: NSMutableIndexSet
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutableindexset
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableindexset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableindexset.json'
content_hash: 'sha256:a4bafe217cedbef6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMutableIndexSet

<sub>Class</sub>

A mutable collection of unique integer values that represent indexes in another collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMutableIndexSet
```

## Overview

In Swift, this type bridges to [IndexSet](indexset.md); use [NSMutableIndexSet](nsmutableindexset.md) when you need reference semantics or other Foundation-specific behavior.

The [NSMutableIndexSet](nsmutableindexset.md) class represents a mutable collection of unique unsigned integers, known as _indexes_ because of the way they are used. This collection is referred to as a _mutable index set_. The inclusive range of valid indexes is `0...(NSNotFound - 1)`; trying to use indexes outside this range is invalid.

The values in a mutable index set are always sorted, so the order in which values are added is irrelevant.

Do not subclass the [NSMutableIndexSet](nsmutableindexset.md) class.

> [!important] Important
> The Swift overlay to the Foundation framework provides the [IndexSet](indexset.md) structure, which bridges to the [NSMutableIndexSet](nsmutableindexset.md) class and its immutable superclass, [NSIndexSet](nsindexset.md). For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

## Relationships

- **Inherits From**: [NSIndexSet](nsindexset.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Adding Indexes

- [- addIndex:](<nsmutableindexset/add(__)-6dtkj.md>) — Adds an index  to the receiver.
- [- addIndexes:](<nsmutableindexset/add(__)-6zmti.md>) — Adds the indexes in an index set to the receiver.
- [- addIndexesInRange:](<nsmutableindexset/add(in_).md>) — Adds the indexes in an index range to the receiver.

### Removing Indexes

- [- removeIndex:](<nsmutableindexset/remove(__)-5li0r.md>) — Removes an index from the receiver.
- [- removeIndexes:](<nsmutableindexset/remove(__)-196u2.md>) — Removes the indexes in an index set from the receiver.
- [- removeAllIndexes](<nsmutableindexset/removeallindexes().md>) — Removes the receiver’s indexes.
- [- removeIndexesInRange:](<nsmutableindexset/remove(in_).md>) — Removes the indexes in an index range from the receiver.

### Shifting Index Groups

- [- shiftIndexesStartingAtIndex:by:](<nsmutableindexset/shiftindexesstarting(at_by_).md>) — Shifts a group of indexes to the left or the right within the receiver.

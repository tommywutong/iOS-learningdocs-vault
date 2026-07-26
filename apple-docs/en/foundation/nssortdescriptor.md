---
title: NSSortDescriptor
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nssortdescriptor
source_url: 'https://developer.apple.com/documentation/foundation/nssortdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssortdescriptor.json'
content_hash: 'sha256:9e4e11b2f70207d1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSortDescriptor

<sub>Class</sub>

An immutable description of how to order a collection of objects according to a property common to all the objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSSortDescriptor
```

## Overview

You construct instances of [NSSortDescriptor](nssortdescriptor.md) by specifying the key path of the property to compare and the order of the sort (ascending or descending). Optionally, you can also specify a selector to use to perform the comparison, which allows you to specify other comparison selectors, such as [- localizedStandardCompare:](<nsstring/localizedstandardcompare(__).md>) and [- localizedCaseInsensitiveCompare:](<nsstring/localizedcaseinsensitivecompare(__).md>). Sorting raises an exception if the objects don’t respond to the sort descriptor’s comparison selector.

You can use sort descriptors for the following:

- Sorting an array (an instance of [NSArray](nsarray.md) or [NSMutableArray](nsmutablearray.md) — see [- sortedArrayUsingDescriptors:](<nsarray/sortedarray(using_)-82wi1.md>) and [- sortUsingDescriptors:](<nsmutablearray/sort(using_)-4eh07.md>))
- Comparing two objects directly (see [- compareObject:toObject:](<nssortdescriptor/compare(__to_).md>))
- Specifying the order of objects that return from a Core Data fetch request (see [sortDescriptors](../coredata/nsfetchrequest/sortdescriptors.md))

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Creating a Sort Descriptor

- [- initWithKey:ascending:](<nssortdescriptor/init(key_ascending_).md>) — Creates a sort descriptor with a specified string key path and sort order.
- [- initWithKey:ascending:selector:](<nssortdescriptor/init(key_ascending_selector_).md>) — Creates a sort descriptor with a specified string key path, ordering, and comparison selector.
- [init(keyPath:ascending:)](<nssortdescriptor/init(keypath_ascending_).md>) — Creates a sort descriptor with a specified key path and ordering.
- [- initWithKey:ascending:comparator:](<nssortdescriptor/init(key_ascending_comparator_).md>) — Creates a sort descriptor with a specified string key path and ordering, and a comparator block.
- [init(keyPath:ascending:comparator:)](<nssortdescriptor/init(keypath_ascending_comparator_).md>) — Creates a sort descriptor with a specified key path and ordering, and a comparator block.
- [- initWithCoder:](<nssortdescriptor/init(coder_).md>) — Creates a sort descriptor by decoding from the coder you specify.
- [init(_:)](<nssortdescriptor/init(__)-7qf91.md>) — Creates a sort descriptor using a sort descriptor you specify. _(deprecated)_

### Getting Information About a Sort Descriptor

- [ascending](nssortdescriptor/ascending.md) — A Boolean value that indicates whether the receiver specifies sorting in ascending order.
- [key](nssortdescriptor/key.md) — The key that specifies the property to compare during sorting.
- [keyPath](nssortdescriptor/keypath.md) — The key path that specifies the property to compare during sorting.
- [selector](nssortdescriptor/selector.md) — The selector for comparing objects.
- [comparator](nssortdescriptor/comparator.md) — The comparator for the sort descriptor.

### Using Sort Descriptors

- [- compareObject:toObject:](<nssortdescriptor/compare(__to_).md>) — Returns a comparison result value that indicates the sort order of two objects.
- [reversedSortDescriptor](nssortdescriptor/reversedsortdescriptor.md) — Returns a sort descriptor that reverses the sort order.
- [- allowEvaluation](<nssortdescriptor/allowevaluation().md>) — Forces a securely decoded sort descriptor to allow evaluation.

### Initializers

- [init(_:)](<nssortdescriptor/init(__)-527yl.md>) — Creates an `NSSortDescriptor` representing the same sort as the given `SortDescriptor`.

## See Also

### Sorting

- [ComparisonResult](comparisonresult.md) — Constants that indicate sort order.
- [SortDescriptor](sortdescriptor.md) — A serializable description of how to sort numerics and strings.
- [SortComparator](sortcomparator.md) — A comparison algorithm for a specified type.
- [ComparableComparator](comparablecomparator.md) — A comparator that compares types according to their conformance to the comparable protocol.
- [KeyPathComparator](keypathcomparator.md) — A comparator that uses another sort comparator to provide the comparison of values at a key path.
- [SortOrder](sortorder.md) — The orderings that you can perform sorts with.

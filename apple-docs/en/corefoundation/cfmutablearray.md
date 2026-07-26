---
title: CFMutableArray
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmutablearray
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmutablearray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmutablearray.json'
content_hash: 'sha256:f19b7526e456a859'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMutableArray

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFMutableArray
```

## Overview

CFMutableArray manages dynamic arrays. The basic interface for managing arrays is provided by [CFArray](cfarray.md). CFMutableArray adds functions to modify the contents of an array.

You create a mutable array object using either the [CFArrayCreateMutable](<cfarraycreatemutable(______).md>) or [CFArrayCreateMutableCopy](<cfarraycreatemutablecopy(______).md>) function.

CFMutableArray provides several functions for changing the contents of an array, for example the [CFArrayAppendValue](<cfarrayappendvalue(____).md>) and [CFArrayInsertValueAtIndex](<cfarrayinsertvalueatindex(______).md>) functions add values to an array and [CFArrayRemoveValueAtIndex](<cfarrayremovevalueatindex(____).md>) removes values from an array. You can also reorder the contents of an array using [CFArrayExchangeValuesAtIndices](<cfarrayexchangevaluesatindices(______).md>) and [CFArraySortValues](<cfarraysortvalues(________).md>).

CFMutableArray is “toll-free bridged” with its Cocoa Foundation counterpart, [NSMutableArray](../foundation/nsmutablearray.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSMutableArray *` parameter, you can pass in a `CFMutableArrayRef`, and in a function where you see a `CFMutableArrayRef` parameter, you can pass in an NSMutableArray instance. This fact also applies to concrete subclasses of NSMutableArray. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Inherits From**: [CFArray](cfarray.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### CFMutableArray Miscellaneous Functions

- [CFArrayAppendArray](<cfarrayappendarray(______).md>) — Adds the values from one array to another array.
- [CFArrayAppendValue](<cfarrayappendvalue(____).md>) — Adds a value to an array giving it the new largest index.
- [CFArrayCreateMutable](<cfarraycreatemutable(______).md>) — Creates a new empty mutable array.
- [CFArrayCreateMutableCopy](<cfarraycreatemutablecopy(______).md>) — Creates a new mutable array with the values from another array.
- [CFArrayExchangeValuesAtIndices](<cfarrayexchangevaluesatindices(______).md>) — Exchanges the values at two indices of an array.
- [CFArrayInsertValueAtIndex](<cfarrayinsertvalueatindex(______).md>) — Inserts a value into an array at a given index.
- [CFArrayRemoveAllValues](<cfarrayremoveallvalues(__).md>) — Removes all the values from an array, making it empty.
- [CFArrayRemoveValueAtIndex](<cfarrayremovevalueatindex(____).md>) — Removes the value at a given index from an array.
- [CFArrayReplaceValues](<cfarrayreplacevalues(________).md>) — Replaces a range of values in an array.
- [CFArraySetValueAtIndex](<cfarraysetvalueatindex(______).md>) — Changes the value at a given index in an array.
- [CFArraySortValues](<cfarraysortvalues(________).md>) — Sorts the values in an array using a given comparison function.

## See Also

### Related Documentation

- [Collections Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html#//apple_ref/doc/uid/10000124i)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)

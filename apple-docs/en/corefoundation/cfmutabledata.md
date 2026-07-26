---
title: CFMutableData
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmutabledata
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmutabledata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmutabledata.json'
content_hash: 'sha256:1f4daa502589798d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMutableData

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFMutableData
```

## Overview

CFMutableData manages dynamic binary data. The basic interface for managing binary data is provided by [CFData](cfdata.md). CFMutableData adds functions to modify the contents of a binary data object.

You create a mutable data object using either the [CFDataCreateMutable](<cfdatacreatemutable(____).md>) or [CFDataCreateMutableCopy](<cfdatacreatemutablecopy(______).md>) function.

Bytes are added to a data object with the [CFDataAppendBytes](<cfdataappendbytes(______).md>) function. Bytes are removed from a data object with the [CFDataDeleteBytes](<cfdatadeletebytes(____).md>) function.

> [!important] Important
> Many of the CFMutableData functions take a [CFIndex](cfindex.md) `length` or `capacity` argument. You must not pass a negative number for such values—this may introduce a security risk.

CFMutableData is “toll-free bridged” with its Cocoa Foundation counterpart, [NSMutableData](../foundation/nsmutabledata.md). What this means is that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. In other words, in a method where you see an `NSMutableData *` parameter, you can pass in a `CFMutableDataRef`, and in a function where you see a `CFMutableDataRef` parameter, you can pass in an `NSMutableData` instance. This also applies to concrete subclasses of `NSMutableData`. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Inherits From**: [CFData](cfdata.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Mutable Data Object

- [CFDataCreateMutable](<cfdatacreatemutable(____).md>) — Creates an empty CFMutableData object.
- [CFDataCreateMutableCopy](<cfdatacreatemutablecopy(______).md>) — Creates a CFMutableData object by copying another CFData object.

### Accessing Data

- [CFDataGetMutableBytePtr](<cfdatagetmutablebyteptr(__).md>) — Returns a pointer to a mutable byte buffer of a CFMutableData object.

### Modifying a Mutable Data Object

- [CFDataAppendBytes](<cfdataappendbytes(______).md>) — Appends the bytes from a byte buffer to the contents of a CFData object.
- [CFDataDeleteBytes](<cfdatadeletebytes(____).md>) — Deletes the bytes in a CFMutableData object within a specified range.
- [CFDataReplaceBytes](<cfdatareplacebytes(________).md>) — Replaces those bytes in a CFMutableData object that fall within a specified range with other bytes.
- [CFDataIncreaseLength](<cfdataincreaselength(____).md>) — Increases the length of a CFMutableData object’s internal byte buffer, zero-filling the extension to the buffer.
- [CFDataSetLength](<cfdatasetlength(____).md>) — Resets the length of a CFMutableData object’s internal byte buffer.

## See Also

### Related Documentation

- [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [Binary Data Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBinaryData/CFBinaryData.html#//apple_ref/doc/uid/10000144i)

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

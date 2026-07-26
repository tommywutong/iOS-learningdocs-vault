---
title: CFNumber
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfnumber
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumber.json'
content_hash: 'sha256:1eaadb4b4d2386d8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumber

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFNumber
```

## Overview

CFNumber encapsulates C scalar (numeric) types. It provides functions for setting and accessing the value as any basic C type. It also provides a compare function to determine the ordering of two CFNumber objects. CFNumber objects are used to wrap numerical values for use in Core Foundation property lists and collections.

CFNumber objects are not intended as a replacement for C scalar values and should not be used in APIs or implementations where scalar values are more appropriate and efficient.

> [!note] Note
> In order to improve performance, some commonly-used numbers (such as `0` and `1`) are uniqued. You should not expect that allocating multiple CFNumber instances will necessarily result in distinct objects.

CFNumber is “toll-free bridged” with its Cocoa Foundation counterpart, [NSNumber](../foundation/nsnumber.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSNumber *` parameter, you can pass in a `CFNumberRef`, and in a function where you see a `CFNumberRef` parameter, you can pass in an NSNumber instance. This fact also applies to concrete subclasses of NSNumber. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Number

- [CFNumberCreate](<cfnumbercreate(______).md>) — Creates a CFNumber object using a specified value.

### Getting Information About Numbers

- [CFNumberGetByteSize](<cfnumbergetbytesize(__).md>) — Returns the number of bytes used by a CFNumber object to store its value.
- [CFNumberGetType](<cfnumbergettype(__).md>) — Returns the type used by a CFNumber object to store its value.
- [CFNumberGetValue](<cfnumbergetvalue(______).md>) — Obtains the value of a CFNumber object cast to a specified type.
- [CFNumberIsFloatType](<cfnumberisfloattype(__).md>) — Determines whether a CFNumber object contains a value stored as one of the defined floating point types.

### Comparing Numbers

- [CFNumberCompare](<cfnumbercompare(______).md>) — Compares two CFNumber objects and returns a comparison result.

### Getting the CFNumber Type ID

- [CFNumberGetTypeID](<cfnumbergettypeid().md>) — Returns the type identifier for the CFNumber opaque type.

### Constants

- [CFNumberType](cfnumbertype.md) — Flags used by CFNumber to indicate the data type of a value.
- [Predefined Values](predefined-values.md) — CFNumber provides some predefined number values.

## See Also

### Related Documentation

- [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)

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

---
title: CFData
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdata
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdata.json'
content_hash: 'sha256:b11fe4c6397a11ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFData

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFData
```

## Overview

CFData and its derived mutable type, [CFMutableData](cfmutabledata.md), provide support for data objects, object-oriented wrappers for byte buffers. Data objects let simple allocated buffers (that is, data with no embedded pointers) take on the behavior of Core Foundation objects. CFData creates static data objects, and CFMutableData creates dynamic data objects. Data objects are typically used for raw data storage.

You use the [CFDataCreate](<cfdatacreate(______).md>) and [CFDataCreateCopy](<cfdatacreatecopy(____).md>) functions to create static data objects. These functions make a new copy of the supplied data. To create a data object that uses the supplied buffer instead of making a separate copy, use the [CFDataCreateWithBytesNoCopy](<cfdatacreatewithbytesnocopy(________).md>) function. You use the [CFDataGetBytes](<cfdatagetbytes(______).md>) function to retrieve the bytes and the [CFDataGetLength](<cfdatagetlength(__).md>) function to get the length of the bytes.

CFData is “toll-free bridged” with its Cocoa Foundation counterpart, [NSData](../foundation/nsdata.md). What this means is that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. In other words, in a method where you see an `NSData *` parameter, you can pass in a `CFDataRef`, and in a function where you see a `CFDataRef` parameter, you can pass in an `NSData` instance. This also applies to concrete subclasses of `NSData`. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Inherited By**: [CFMutableData](cfmutabledata.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a CFData Object

- [CFDataCreate](<cfdatacreate(______).md>) — Creates an immutable CFData object using data copied from a specified byte buffer.
- [CFDataCreateCopy](<cfdatacreatecopy(____).md>) — Creates an immutable copy of a CFData object.
- [CFDataCreateWithBytesNoCopy](<cfdatacreatewithbytesnocopy(________).md>) — Creates an immutable CFData object from an external (client-owned) byte buffer.

### Examining a CFData Object

- [CFDataGetBytePtr](<cfdatagetbyteptr(__).md>) — Returns a read-only pointer to the bytes of a CFData object.
- [CFDataGetBytes](<cfdatagetbytes(______).md>) — Copies the byte contents of a CFData object to an external buffer.
- [CFDataGetLength](<cfdatagetlength(__).md>) — Returns the number of bytes contained by a CFData object.
- [CFDataFind](<cfdatafind(________).md>) — Finds and returns the range within a data object of the first occurrence of the given data, within a given range, subject to any given options.

### Getting the CFData Type ID

- [CFDataGetTypeID](<cfdatagettypeid().md>) — Returns the type identifier for the CFData opaque type.

### Data Types

- [CFDataSearchFlags](cfdatasearchflags.md) — A [CFOptionFlags](cfoptionflags.md) type for specifying options for searching.

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
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
- [CFFileDescriptor](cffiledescriptor.md)

---
title: CFMutableCharacterSet
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmutablecharacterset
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmutablecharacterset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmutablecharacterset.json'
content_hash: 'sha256:8a4d383e2c537b46'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMutableCharacterSet

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFMutableCharacterSet
```

## Overview

CFMutableCharacterSet manages dynamic character sets. The basic interface for managing character sets is provided by [CFCharacterSet](cfcharacterset.md). CFMutableCharacterSet adds functions to modify the contents of a character set.

You create a mutable character set object using either the [CFCharacterSetCreateMutable](<cfcharactersetcreatemutable(__).md>) or [CFCharacterSetCreateMutableCopy](<cfcharactersetcreatemutablecopy(____).md>) function.

CFMutableCharacterSet is “toll-free bridged” with its Cocoa Foundation counterpart, [NSMutableCharacterSet](../foundation/nsmutablecharacterset.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSMutableCharacterSet *` parameter, you can pass in a `CFMutableCharacterSetRef`, and in a function where you see a `CFMutableCharacterSetRef` parameter, you can pass in an NSMutableCharacterSet instance. This capability also applies to concrete subclasses of NSMutableCharacterSet. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Inherits From**: [CFCharacterSet](cfcharacterset.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Mutable Character Set

- [CFCharacterSetCreateMutable](<cfcharactersetcreatemutable(__).md>) — Creates a new empty mutable character set.
- [CFCharacterSetCreateMutableCopy](<cfcharactersetcreatemutablecopy(____).md>) — Creates a new mutable character set with the values from another character set.

### Adding Characters

- [CFCharacterSetAddCharactersInRange](<cfcharactersetaddcharactersinrange(____).md>) — Adds a given range to a character set.
- [CFCharacterSetAddCharactersInString](<cfcharactersetaddcharactersinstring(____).md>) — Adds the characters in a given string to a character set.

### Removing Characters

- [CFCharacterSetRemoveCharactersInRange](<cfcharactersetremovecharactersinrange(____).md>) — Removes a given range of Unicode characters from a character set.
- [CFCharacterSetRemoveCharactersInString](<cfcharactersetremovecharactersinstring(____).md>) — Removes the characters in a given string from a character set.

### Logical Operations

- [CFCharacterSetIntersect](<cfcharactersetintersect(____).md>) — Forms an intersection of two character sets.
- [CFCharacterSetInvert](<cfcharactersetinvert(__).md>) — Inverts the content of a given character set.
- [CFCharacterSetUnion](<cfcharactersetunion(____).md>) — Forms the union of two character sets.

## See Also

### Related Documentation

- [String Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i)

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

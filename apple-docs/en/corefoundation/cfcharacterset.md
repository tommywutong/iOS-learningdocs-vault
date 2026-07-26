---
title: CFCharacterSet
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfcharacterset
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharacterset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharacterset.json'
content_hash: 'sha256:0dd3f5204b572d0b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSet

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFCharacterSet
```

## Overview

A CFCharacterSet object represents a set of Unicode compliant characters. CFString uses CFCharacterSet objects to group characters together for searching operations, so that they can find any of a particular set of characters during a search. The two opaque types, CFCharacterSet and [CFMutableCharacterSet](cfmutablecharacterset.md), define the interface for static and dynamic character sets, respectively. The objects you create using these opaque types are referred to as character set objects (and when no confusion will result, merely as character sets).

CFCharacterSet’s principal function, [CFCharacterSetIsCharacterMember](<cfcharactersetischaractermember(____).md>), provides the basis for all other functions in its interface. You create a character set using one of the `CFCharacterSetCreate...` functions. You may also use any one of the predefined character sets using the [CFCharacterSetGetPredefined](<cfcharactersetgetpredefined(__).md>) function.

CFCharacterSet is “toll-free bridged” with its Cocoa Foundation counterpart, [NSCharacterSet](../foundation/nscharacterset.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSCharacterSet *` parameter, you can pass in a `CFCharacterSetRef`, and in a function where you see a `CFCharacterSetRef` parameter, you can pass in an NSCharacterSet instance. This capability also applies to concrete subclasses of NSCharacterSet. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Inherited By**: [CFMutableCharacterSet](cfmutablecharacterset.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Character Sets

- [CFCharacterSetCreateCopy](<cfcharactersetcreatecopy(____).md>) — Creates a new character set with the values from a given character set.
- [CFCharacterSetCreateInvertedSet](<cfcharactersetcreateinvertedset(____).md>) — Creates a new immutable character set that is the invert of the specified character set.
- [CFCharacterSetCreateWithCharactersInRange](<cfcharactersetcreatewithcharactersinrange(____).md>) — Creates a new character set with the values from the given range of Unicode characters.
- [CFCharacterSetCreateWithCharactersInString](<cfcharactersetcreatewithcharactersinstring(____).md>) — Creates a new character set with the values in the given string.
- [CFCharacterSetCreateWithBitmapRepresentation](<cfcharactersetcreatewithbitmaprepresentation(____).md>) — Creates a new immutable character set with the bitmap representation specified by given data.

### Getting Predefined Character Sets

- [CFCharacterSetGetPredefined](<cfcharactersetgetpredefined(__).md>) — Returns a predefined character set.

### Querying Character Sets

- [CFCharacterSetCreateBitmapRepresentation](<cfcharactersetcreatebitmaprepresentation(____).md>) — Creates a new immutable data with the bitmap representation from the given character set.
- [CFCharacterSetHasMemberInPlane](<cfcharactersethasmemberinplane(____).md>) — Reports whether or not a character set contains at least one member character in the specified plane.
- [CFCharacterSetIsCharacterMember](<cfcharactersetischaractermember(____).md>) — Reports whether or not a given Unicode character is in a character set.
- [CFCharacterSetIsLongCharacterMember](<cfcharactersetislongcharactermember(____).md>) — Reports whether or not a given UTF-32 character is in a character set.
- [CFCharacterSetIsSupersetOfSet](<cfcharactersetissupersetofset(____).md>) — Reports whether or not a character set is a superset of another set.

### Getting the Character Set Type Identifier

- [CFCharacterSetGetTypeID](<cfcharactersetgettypeid().md>) — Returns the type identifier of the CFCharacterSet opaque type.

### Data Types

- [CFCharacterSetPredefinedSet](cfcharactersetpredefinedset.md) — Defines a predefined character set.

### Constants

- [Predefined CFCharacterSet Selector Values](predefined_cfcharacterset_selector_values.md) — Identifiers for the available predefined CFCharacterSet objects.

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
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
- [CFFileDescriptor](cffiledescriptor.md)

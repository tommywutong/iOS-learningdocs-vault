---
title: CFMutableAttributedString
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmutableattributedstring
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmutableattributedstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmutableattributedstring.json'
content_hash: 'sha256:593b52e21384e281'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMutableAttributedString

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFMutableAttributedString
```

## Overview

Instances of CFMutableAttributedString manage mutable character strings and associated sets of attributes (for example, font and kerning information) that apply to individual characters or ranges of characters in the string. CFAttributedString as defined in CoreFoundation provides the basic container functionality, while higher levels provide definitions for standard attributes, their values, and additional behaviors involving these. CFMutableAttributedString represents a mutable string—use CFAttributedString to create and manage an attributed string that cannot be changed after it has been created.

CFMutableAttributedString is not a “subclass” of CFMutableString; that is, it does not respond to CFMutableString (or CFString) function calls. CFAttributedString conceptually contains a CFMutableString to which it applies attributes. This protects you from ambiguities caused by the semantic differences between simple and attributed string. Functions defined for CFAttributedString can be applied to a CFMutableAttributedString object.

Attributes are identified by key/value pairs stored in CFDictionary objects. Keys must be CFString objects, while the corresponding values are CFType objects of an appropriate type. See the attribute constants in NSAttributedString Application Kit Additions Reference for standard attribute names in macOS and NSAttributedString UIKit Additions Reference on iOS.

> [!important] Important
> Attribute dictionaries set for an attributed string must always be created with kCFCopyStringDictionaryKeyCallbacks for their dictionary key callbacks and kCFTypeDictionaryValueCallBacks for their value callbacks; otherwise it’s an error.

When you modify the contents of a mutable attributed string, it may have to do a lot of work to ensure it is internally consistent, and to coalesce runs of identical attributes. You can call [CFAttributedStringBeginEditing](<cfattributedstringbeginediting(__).md>) and [CFAttributedStringEndEditing](<cfattributedstringendediting(__).md>) around a set of related mutation calls that don’t require the string to be in consistent state in between, and thereby reduce the amount of work necessary. These calls can be nested.

CFMutableAttributedString is “toll-free bridged” with its Foundation counterpart, NSMutableAttributedString. This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSMutableAttributedString *` parameter, you can pass in an object of type `CFMutableAttributedStringRef`, and in a function where you see a `CFMutableAttributedStringRef` parameter, you can pass in an `NSMutableAttributedString` instance. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

There is not always a 1:1 mapping between `NSMutableAttributedString`‘s methods and CFMutableAttributedString’s functions. For example, to perform an operation equivalent to `NSMutableAttributedString`’s [append(_:)](<../foundation/nsmutableattributedstring/append(__).md>) method on a CFMutableAttributedString object, you can use [CFAttributedStringReplaceAttributedString](<cfattributedstringreplaceattributedstring(______).md>) and specify `CFRangeMake(CFAttributedStringGetLength(attrStr), 0)` as the range. Alternatively you can cast the CFMutableAttributedString object to an `NSMutableAttributedString` object and send the `appendAttributedString:` message.

## Relationships

- **Inherits From**: [CFAttributedString](cfattributedstring.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a CFMutableAttributedString

- [CFAttributedStringCreateMutable](<cfattributedstringcreatemutable(____).md>) — Creates a mutable attributed string.
- [CFAttributedStringCreateMutableCopy](<cfattributedstringcreatemutablecopy(______).md>) — Creates a mutable copy of an attributed string.

### Modifying a CFMutableAttributedString

- [CFAttributedStringBeginEditing](<cfattributedstringbeginediting(__).md>) — Defers internal consistency-checking and coalescing for a mutable attributed string.
- [CFAttributedStringEndEditing](<cfattributedstringendediting(__).md>) — Re-enables internal consistency-checking and coalescing for a mutable attributed string.
- [CFAttributedStringGetMutableString](<cfattributedstringgetmutablestring(__).md>) — Gets as a mutable string the string for an attributed string.
- [CFAttributedStringRemoveAttribute](<cfattributedstringremoveattribute(______).md>) — Removes the value of a single attribute over a specified range.
- [CFAttributedStringReplaceString](<cfattributedstringreplacestring(______).md>) — Modifies the string of an attributed string.
- [CFAttributedStringReplaceAttributedString](<cfattributedstringreplaceattributedstring(______).md>) — Replaces the attributed substring over a range with another attributed string.
- [CFAttributedStringSetAttribute](<cfattributedstringsetattribute(________).md>) — Sets the value of a single attribute over the specified range.
- [CFAttributedStringSetAttributes](<cfattributedstringsetattributes(________).md>) — Sets the value of attributes of a mutable attributed string over a specified range.

## See Also

### Related Documentation

- [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [String Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i)
- [Data Formatting Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDataFormatting/Articles/CFDataFormatting.html#//apple_ref/doc/uid/10000176i)

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

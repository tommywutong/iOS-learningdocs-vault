---
title: CFAttributedString
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfattributedstring
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstring.json'
content_hash: 'sha256:3cdc3214048263ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedString

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFAttributedString
```

## Overview

Instances of CFAttributedString manage character strings and associated sets of attributes (for example, font and kerning information) that apply to individual characters or ranges of characters in the string. CFAttributedString as defined in Core Foundation provides the basic container functionality, while higher levels provide definitions for standard attributes, their values, and additional behaviors involving these. CFAttributedString represents an immutable string—use [CFMutableAttributedString](cfmutableattributedstring.md) to create and manage an attributed string that can be changed after it has been created.

CFAttributedString is not a “subclass” of CFString; that is, it does not respond to CFString function calls. CFAttributedString conceptually contains a CFString to which it applies attributes. This protects you from ambiguities caused by the semantic differences between simple and attributed string.

Attributes are identified by key/value pairs stored in CFDictionary objects. Keys must be CFString objects, while the corresponding values are CFType objects of an appropriate type. See the attribute constants in NSAttributedString Application Kit Additions Reference or NSAttributedString UIKit Additions Reference for standard attribute names.

> [!important] Important
> Attribute dictionaries set for an attributed string must always be created with [kCFCopyStringDictionaryKeyCallBacks](kcfcopystringdictionarykeycallbacks.md) for their dictionary key callbacks and [kCFTypeDictionaryValueCallBacks](kcftypedictionaryvaluecallbacks.md) for their value callbacks; otherwise it’s an error.

CFAttributedString is “toll-free bridged” with its Foundation counterpart, [NSAttributedString](../foundation/nsattributedstring.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSAttributedString *` parameter, you can pass in a `CFAttributedStringRef`, and in a function where you see a `CFAttributedStringRef` parameter, you can pass in an [NSAttributedString](../foundation/nsattributedstring.md) instance. This also applies to concrete subclasses of [NSAttributedString](../foundation/nsattributedstring.md). See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Inherited By**: [CFMutableAttributedString](cfmutableattributedstring.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a CFAttributedString

- [CFAttributedStringCreate](<cfattributedstringcreate(______).md>) — Creates an attributed string with specified string and attributes.
- [CFAttributedStringCreateCopy](<cfattributedstringcreatecopy(____).md>) — Creates an immutable copy of an attributed string.
- [CFAttributedStringCreateWithSubstring](<cfattributedstringcreatewithsubstring(______).md>) — Creates a sub-attributed string from the specified range.
- [CFAttributedStringGetLength](<cfattributedstringgetlength(__).md>) — Returns the length of the attributed string in characters.
- [CFAttributedStringGetString](<cfattributedstringgetstring(__).md>) — Returns the string for an attributed string.

### Accessing Attributes

- [CFAttributedStringGetAttribute](<cfattributedstringgetattribute(________).md>) — Returns the value of a given attribute of an attributed string at a specified location.
- [CFAttributedStringGetAttributes](<cfattributedstringgetattributes(______).md>) — Returns the attributes of an attributed string at a specified location.
- [CFAttributedStringGetAttributeAndLongestEffectiveRange](<cfattributedstringgetattributeandlongesteffectiverange(__________).md>) — Returns the value of a given attribute of an attributed string at a specified location.
- [CFAttributedStringGetAttributesAndLongestEffectiveRange](<cfattributedstringgetattributesandlongesteffectiverange(________).md>) — Returns the attributes of an attributed string at a specified location.

### Getting Attributed String Properties

- [CFAttributedStringGetTypeID](<cfattributedstringgettypeid().md>) — Returns the type identifier for the CFAttributedString opaque type.

## See Also

### Related Documentation

- [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [String Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i)
- [Data Formatting Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDataFormatting/Articles/CFDataFormatting.html#//apple_ref/doc/uid/10000176i)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
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
- [CFFileDescriptor](cffiledescriptor.md)

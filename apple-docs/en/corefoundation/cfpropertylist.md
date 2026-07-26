---
title: CFPropertyList
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfpropertylist
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpropertylist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpropertylist.json'
content_hash: 'sha256:c65ef113e5236bc0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPropertyList

<sub>Type Alias</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFPropertyList = CFTypeRef
```

## Overview

CFPropertyList provides functions that convert property list objects to and from several serialized formats such as XML. The [CFPropertyList](cfpropertylist.md) type that denotes CFPropertyList objects is an abstract type for property list objects. Depending on the contents of the XML data used to create the property list, `CFPropertyListRef` can be any of the property list objects: CFData, CFString, CFArray, CFDictionary, CFDate, CFBoolean, and CFNumber. Note that if you use a property list to generate XML, the keys of any dictionaries in the property list must be CFString objects.

It is important to understand that CFPropertyList provides an abstraction for all the property list types—you can think of CFPropertyList in object-oriented terms as being the superclass of CFString, CFNumber, CFDictionary, and so on. When a Core Foundation function returns a `CFPropertyListRef`, it means that the value may be any of the property list types. For example, [CFPreferencesCopyAppValue](<cfpreferencescopyappvalue(____).md>) returns a `CFPropertyListRef`. This means that the value returned can be a CFString object, a CFNumber object, a CFDictionary object, and so on again. You can use [CFGetTypeID](<cfgettypeid(__).md>) to determine what type of object a property list value is.

You use one of the `CFPropertyListCreate...` functions to create a property list object given an existing property list object, raw XML data (as in a file), or a stream. You can also convert a property list object to XML using the [CFPropertyListCreateXMLData](<cfpropertylistcreatexmldata(____).md>) function. You use the [CFPropertyListWriteToStream](<cfpropertylistwritetostream(________).md>) function to write a property list to an output stream, and validate a property list object using the [CFPropertyListIsValid](<cfpropertylistisvalid(____).md>) function. CFPropertyList properly takes care of endian issues—a property list (whether represented by a stream, XML, or a CFData object) created on a PowerPC-based Macintosh is correctly interpreted on an Intel-based Macintosh, and vice versa.

For code examples illustrating how to read and write property list files, see [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i) and in particular [Saving and Restoring Property Lists](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/Articles/Saving.html#//apple_ref/doc/uid/20001175).

## Topics

### Creating a Property List

- [CFPropertyListCreateWithData](<cfpropertylistcreatewithdata(__________).md>) — Creates a property list from a given CFData object.
- [CFPropertyListCreateWithStream](<cfpropertylistcreatewithstream(____________).md>) — Create and return a property list with a CFReadStream input.
- [CFPropertyListCreateDeepCopy](<cfpropertylistcreatedeepcopy(______).md>) — Recursively creates a copy of a given property list.
- [CFPropertyListCreateFromXMLData](<cfpropertylistcreatefromxmldata(________).md>) — Creates a property list using the specified XML or binary property list data. _(deprecated)_
- [CFPropertyListCreateFromStream](<cfpropertylistcreatefromstream(____________).md>) — Creates a property list using data from a stream. _(deprecated)_

### Exporting a Property List

- [CFPropertyListCreateData](<cfpropertylistcreatedata(__________).md>) — Returns a CFData object containing a serialized representation of a given property list in a specified format.
- [CFPropertyListWrite](<cfpropertylistwrite(__________).md>) — Write the bytes of a serialized property list out to a stream.
- [CFPropertyListCreateXMLData](<cfpropertylistcreatexmldata(____).md>) — Creates an XML representation of the specified property list. _(deprecated)_
- [CFPropertyListWriteToStream](<cfpropertylistwritetostream(________).md>) — Writes the bytes of a property list serialization out to a stream. _(deprecated)_

### Validating a Property List

- [CFPropertyListIsValid](<cfpropertylistisvalid(____).md>) — Determines if a property list is valid.

### Data Types

- [CFPropertyListMutabilityOptions](cfpropertylistmutabilityoptions.md) — Type for flags that determine the degree of mutability of newly created property lists.

### Constants

- [CFPropertyListFormat](cfpropertylistformat.md) — Specifies the format of a property list.
- [Property List Mutability Options](property_list_mutability_options.md) — Option flags that determine the degree of mutability of newly created property lists.
- [Reading and Writing Error Codes](1429999-reading-and-writing-error-codes.md) — Error codes for property list reading and writing functions such as [CFPropertyListCreateWithData](<cfpropertylistcreatewithdata(__________).md>).

## See Also

### Related Documentation

- [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [XML Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFXML/CFXML.html#//apple_ref/doc/uid/10000138i)

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

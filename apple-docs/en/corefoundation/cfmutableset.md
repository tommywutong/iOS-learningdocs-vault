---
title: CFMutableSet
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmutableset
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmutableset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmutableset.json'
content_hash: 'sha256:3b680bdbdd906f8e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMutableSet

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFMutableSet
```

## Overview

CFMutableSet manages dynamic sets. The basic interface for managing sets is provided by [CFSet](cfset.md). CFMutableSet adds functions to modify the contents of a set.

You create a mutable set object using either the [CFSetCreateMutable](<cfsetcreatemutable(______).md>) or [CFSetCreateMutableCopy](<cfsetcreatemutablecopy(______).md>) function.

CFMutableSet provides several functions for adding and removing values from a set. The [CFSetAddValue](<cfsetaddvalue(____).md>) function adds a value to a set and [CFSetRemoveValue](<cfsetremovevalue(____).md>) removes a value from a set.

CFMutableSet is “toll-free bridged” with its Cocoa Foundation counterpart, [NSMutableSet](../foundation/nsmutableset.md). What this means is that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. This means that in a method where you see an `NSMutableSet *` parameter, you can pass in a `CFMutableSetRef`, and in a function where you see a `CFMutableSetRef` parameter, you can pass in an NSMutableSet instance. This also applies to concrete subclasses of NSMutableSet. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Inherits From**: [CFSet](cfset.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### CFMutableSet Miscellaneous Functions

- [CFSetAddValue](<cfsetaddvalue(____).md>) — Adds a value to a CFMutableSet object.
- [CFSetCreateMutable](<cfsetcreatemutable(______).md>) — Creates an empty CFMutableSet object.
- [CFSetCreateMutableCopy](<cfsetcreatemutablecopy(______).md>) — Creates a new mutable set with the values from another set.
- [CFSetRemoveAllValues](<cfsetremoveallvalues(__).md>) — Removes all values from a CFMutableSet object.
- [CFSetRemoveValue](<cfsetremovevalue(____).md>) — Removes a value from a CFMutableSet object.
- [CFSetReplaceValue](<cfsetreplacevalue(____).md>) — Replaces a value in a CFMutableSet object.
- [CFSetSetValue](<cfsetsetvalue(____).md>) — Sets a value in a CFMutableSet object.

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

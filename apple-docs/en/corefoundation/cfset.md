---
title: CFSet
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfset
source_url: 'https://developer.apple.com/documentation/corefoundation/cfset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfset.json'
content_hash: 'sha256:02cd3e0c217cc4b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSet

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFSet
```

## Overview

CFSet and its derived mutable type, [CFMutableSet](cfmutableset.md), provide support for the mathematical concept of a set. A set, both in its mathematical sense and in the implementation of CFSet, is an unordered collection of distinct elements. CFSet creates static sets and CFMutableSet creates dynamic sets.

Use bags or sets as an alternative to arrays when the order of elements isn’t important and performance in testing whether a value is contained in the collection is a consideration—while arrays are ordered, testing for membership is slower than with bags or sets. Use bags over sets if you want to allow duplicate values in your collections.

You create a static set object using either the [CFSetCreate](<cfsetcreate(________).md>) or [CFSetCreateCopy](<cfsetcreatecopy(____).md>) function. These functions return a set containing the values you pass in as arguments. (Note that sets can’t contain `NULL` pointers; in most cases, though, you can use the [kCFNull](kcfnull.md) constant instead.) Values are not copied but retained using the retain callback provided when the set was created. Similarly, when a value is removed from a set, it is released using the release callback.

CFSet provides functions for querying the values of a set. The [CFSetGetCount](<cfsetgetcount(__).md>) returns the number of values in a set, the [CFSetContainsValue](<cfsetcontainsvalue(____).md>) function checks if a value is in a set, and [CFSetGetValues](<cfsetgetvalues(____).md>) returns a C array containing all the values in a set.

CFSet is “toll-free bridged” with its Cocoa Foundation counterpart, [NSSet](../foundation/nsset.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSSet *` parameter, you can pass in a `CFSetRef`, and in a function where you see a `CFSetRef` parameter, you can pass in an NSSet instance. This also applies to concrete subclasses of NSSet. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Inherited By**: [CFMutableSet](cfmutableset.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Sets

- [CFSetCreate](<cfsetcreate(________).md>) — Creates an immutable CFSet object containing supplied values.
- [CFSetCreateCopy](<cfsetcreatecopy(____).md>) — Creates an immutable set containing the values of an existing set.

### Examining a Set

- [CFSetContainsValue](<cfsetcontainsvalue(____).md>) — Returns a Boolean that indicates whether a set contains a given value.
- [CFSetGetCount](<cfsetgetcount(__).md>) — Returns the number of values currently in a set.
- [CFSetGetCountOfValue](<cfsetgetcountofvalue(____).md>) — Returns the number of values in a set that match a given value.
- [CFSetGetValue](<cfsetgetvalue(____).md>) — Obtains a specified value from a set.
- [CFSetGetValueIfPresent](<cfsetgetvalueifpresent(______).md>) — Reports whether or not a value is in a set, and if it exists returns the value indirectly.
- [CFSetGetValues](<cfsetgetvalues(____).md>) — Obtains all values in a set.

### Applying a Function to Set Members

- [CFSetApplyFunction](<cfsetapplyfunction(______).md>) — Calls a function once for each value in a set.

### Getting the CFSet Type ID

- [CFSetGetTypeID](<cfsetgettypeid().md>) — Returns the type identifier for the CFSet type.

### Callbacks

- [CFSetApplierFunction](cfsetapplierfunction.md) — Prototype of a callback function that may be applied to every value in a set.
- [CFSetCopyDescriptionCallBack](cfsetcopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value in a set.
- [CFSetEqualCallBack](cfsetequalcallback.md) — Prototype of a callback function used to determine if two values in a set are equal.
- [CFSetHashCallBack](cfsethashcallback.md) — Prototype of a callback function called to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [CFSetReleaseCallBack](cfsetreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from a set.
- [CFSetRetainCallBack](cfsetretaincallback.md) — Prototype of a callback function used to retain a value being added to a set.

### Data Types

- [CFSetCallBacks](cfsetcallbacks.md) — This structure contains the callbacks used to retain, release, describe, and compare the values of a CFSet object.

### Constants

- [Predefined Callback Structures](cfset-predefined-callback-structures.md) — CFSet provides some predefined callbacks for your convenience.

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

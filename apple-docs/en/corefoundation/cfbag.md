---
title: CFBag
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbag
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbag.json'
content_hash: 'sha256:a924f5b7e36a8ba3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBag

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFBag
```

## Overview

CFBag and its derived mutable type, [CFMutableBag](cfmutablebag.md), manage non-sequential collections of values called bags in which there can be duplicate values. CFBag creates static bags and CFMutableBag creates dynamic bags.

Use bags or sets as an alternative to arrays when the order of elements isn’t important and performance in testing whether a value is contained in the collection is a consideration—while arrays are ordered, testing for membership is slower than with bags or sets. Use bags over sets if you want to allow duplicate values in your collections.

You create a static bag object using either the [CFBagCreate](<cfbagcreate(________).md>) or [CFBagCreateCopy](<cfbagcreatecopy(____).md>) function. These functions return a bag containing the values you pass in as arguments. (Note that bags can’t contain `NULL` pointers; in most cases, though, you can use the kCFNull constant instead.) Values are not copied but retained using the retain callback provided when the bag was created. Similarly, when a value is removed from a bag, it is released using the release callback.

CFBag provides functions for querying the values of a bag. The [CFBagGetCount](<cfbaggetcount(__).md>) returns the number of values in a bag, the [CFBagContainsValue](<cfbagcontainsvalue(____).md>) function checks if a value is in a bag, and [CFBagGetValues](<cfbaggetvalues(____).md>) returns a C array containing all the values in a bag.

The [CFBagApplyFunction](<cfbagapplyfunction(______).md>) function lets you apply a function to all values in a bag.

## Relationships

- **Inherited By**: [CFMutableBag](cfmutablebag.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Bag

- [CFBagCreate](<cfbagcreate(________).md>) — Creates an immutable bag containing specified values.
- [CFBagCreateCopy](<cfbagcreatecopy(____).md>) — Creates an immutable bag with the values of another bag.

### Examining a Bag

- [CFBagContainsValue](<cfbagcontainsvalue(____).md>) — Reports whether or not a value is in a bag.
- [CFBagGetCount](<cfbaggetcount(__).md>) — Returns the number of values currently in a bag.
- [CFBagGetCountOfValue](<cfbaggetcountofvalue(____).md>) — Returns the number of times a value occurs in a bag.
- [CFBagGetValue](<cfbaggetvalue(____).md>) — Returns a requested value from a bag.
- [CFBagGetValueIfPresent](<cfbaggetvalueifpresent(______).md>) — Reports whether or not a value is in a bag, and returns that value indirectly if it exists.
- [CFBagGetValues](<cfbaggetvalues(____).md>) — Fills a buffer with values from a bag.

### Applying a Function to the Contents of a Bag

- [CFBagApplyFunction](<cfbagapplyfunction(______).md>) — Calls a function once for each value in a bag.

### Getting the CFBag Type ID

- [CFBagGetTypeID](<cfbaggettypeid().md>) — Returns the type identifier for the CFBag opaque type.

### Callbacks

- [CFBagApplierFunction](cfbagapplierfunction.md) — Prototype of a callback function that may be applied to every value in a bag.
- [CFBagCopyDescriptionCallBack](cfbagcopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value in a bag.
- [CFBagEqualCallBack](cfbagequalcallback.md) — Prototype of a callback function used to determine if two values in a bag are equal.
- [CFBagHashCallBack](cfbaghashcallback.md) — Prototype of a callback function invoked to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [CFBagReleaseCallBack](cfbagreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from a bag.
- [CFBagRetainCallBack](cfbagretaincallback.md) — Prototype of a callback function used to retain a value being added to a bag.

### Data Types

- [CFBagCallBacks](cfbagcallbacks.md) — This structure contains the callbacks used to retain, release, describe, and compare the values of a CFBag object.

### Constants

- [Predefined Callback Structures](cfbag-predefined-callback-structures.md) — CFBag provides some predefined callbacks for your convenience.

## See Also

### Related Documentation

- [Collections Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html#//apple_ref/doc/uid/10000124i)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
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

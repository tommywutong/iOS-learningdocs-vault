---
title: CFArray
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfarray
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarray.json'
content_hash: 'sha256:2abfc023045fcb15'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArray

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFArray
```

## Overview

CFArray and its derived mutable type, [CFMutableArray](cfmutablearray.md), manage ordered collections of values called arrays. CFArray creates static arrays and CFMutableArray creates dynamic arrays.

You create a static array object using either the [CFArrayCreate](<cfarraycreate(________).md>) or [CFArrayCreateCopy](<cfarraycreatecopy(____).md>) function. These functions return an array containing the values you pass in as arguments. (Note that arrays can’t contain `NULL` pointers; in most cases, though, you can use the [kCFNull](kcfnull.md) constant instead.) Values are not copied but retained using the retain callback provided when an array was created. Similarly, when a value is removed from an array, it is released using the release callback.

CFArray’s two primitive functions [CFArrayGetCount](<cfarraygetcount(__).md>) and [CFArrayGetValueAtIndex](<cfarraygetvalueatindex(____).md>) provide the basis for all other functions in its interface. The [CFArrayGetCount](<cfarraygetcount(__).md>) function returns the number of elements in an array; [CFArrayGetValueAtIndex](<cfarraygetvalueatindex(____).md>) gives you access to an array’s elements by index, with index values starting at 0.

A number of CFArray functions allow you to operate over a range of values in an array, for example [CFArrayApplyFunction](<cfarrayapplyfunction(________).md>) lets you apply a function to values in an array, and [CFArrayBSearchValues](<cfarraybsearchvalues(__________).md>) searches an array for the value that matches its parameter. Recall that a range is defined as `{start, length}`, therefore to operate over the entire array the range you supply should be `{0, N}` (where `N` is the count of the array).

CFArray is “toll-free bridged” with its Cocoa Foundation counterpart, [NSArray](../foundation/nsarray.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSArray *` parameter, you can pass in a `CFArrayRef`, and in a function where you see a `CFArrayRef` parameter, you can pass in an NSArray instance. This also applies to concrete subclasses of NSArray. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Inherited By**: [CFMutableArray](cfmutablearray.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating an Array

- [CFArrayCreate](<cfarraycreate(________).md>) — Creates a new immutable array with the given values.
- [CFArrayCreateCopy](<cfarraycreatecopy(____).md>) — Creates a new immutable array with the values from another array.

### Examining an Array

- [CFArrayBSearchValues](<cfarraybsearchvalues(__________).md>) — Searches an array for a value using a binary search algorithm.
- [CFArrayContainsValue](<cfarraycontainsvalue(______).md>) — Reports whether or not a value is in an array.
- [CFArrayGetCount](<cfarraygetcount(__).md>) — Returns the number of values currently in an array.
- [CFArrayGetCountOfValue](<cfarraygetcountofvalue(______).md>) — Counts the number of times a given value occurs in an array.
- [CFArrayGetFirstIndexOfValue](<cfarraygetfirstindexofvalue(______).md>) — Searches an array forward for a value.
- [CFArrayGetLastIndexOfValue](<cfarraygetlastindexofvalue(______).md>) — Searches an array backward for a value.
- [CFArrayGetValues](<cfarraygetvalues(______).md>) — Fills a buffer with values from an array.
- [CFArrayGetValueAtIndex](<cfarraygetvalueatindex(____).md>) — Retrieves a value at a given index.

### Applying a Function to Elements

- [CFArrayApplyFunction](<cfarrayapplyfunction(________).md>) — Calls a function once for each element in range in an array.

### Getting the CFArray Type ID

- [CFArrayGetTypeID](<cfarraygettypeid().md>) — Returns the type identifier for the CFArray opaque type.

### Callbacks

- [CFArrayApplierFunction](cfarrayapplierfunction.md) — Prototype of a callback function that may be applied to every value in an array.
- [CFArrayCopyDescriptionCallBack](cfarraycopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value in an array.
- [CFArrayEqualCallBack](cfarrayequalcallback.md) — Prototype of a callback function used to determine if two values in an array are equal.
- [CFArrayReleaseCallBack](cfarrayreleasecallback.md) — Prototype of a callback function used to release a value before it’s removed from an array.
- [CFArrayRetainCallBack](cfarrayretaincallback.md) — Prototype of a callback function used to retain a value being added to an array.

### Data Types

- [CFArrayCallBacks](cfarraycallbacks.md) — Structure containing the callbacks of a CFArray.

### Constants

- [Predefined Callback Structures](predefined-callback-structures.md) — CFArray provides a predefined callback structure appropriate for use when the values in a CFArray are all CFType-derived objects.

## See Also

### Related Documentation

- [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [Collections Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html#//apple_ref/doc/uid/10000124i)

### Opaque Types

- [CFAllocator](cfallocator.md)
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
- [CFFileDescriptor](cffiledescriptor.md)

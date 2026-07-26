---
title: CFDictionary
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdictionary
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionary.json'
content_hash: 'sha256:470ab28643905dda'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDictionary

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFDictionary
```

## Overview

CFDictionary and its derived mutable type, [CFMutableDictionary](cfmutabledictionary.md), manage associations of key-value pairs. CFDictionary creates static dictionaries where you set the key-value pairs when first creating a dictionary and cannot modify them afterward; CFMutableDictionary creates dynamic dictionaries where you can add or delete key-value pairs at any time, and the dictionary automatically allocates memory as needed.

A key-value pair within a dictionary is called an entry. Each entry consists of one object that represents the key and a second object that is that key’s value. Within a dictionary, the keys are unique. That is, no two keys in a single dictionary are equal (as determined by the equal callback). Internally, a dictionary uses a hash table to organize its storage and to provide rapid access to a value given the corresponding key.

Keys for a CFDictionary may be of any C type, however note that if you want to convert a CFPropertyList to XML, any dictionary’s keys must be CFString objects.

You create static dictionaries using either the [CFDictionaryCreate](<cfdictionarycreate(____________).md>) or [CFDictionaryCreateCopy](<cfdictionarycreatecopy(____).md>) function. Key-value pairs are passed as parameters to [CFDictionaryCreate](<cfdictionarycreate(____________).md>). When adding key-value pairs to a dictionary, the keys and values are not copied—they are retained so they are not invalidated before the dictionary is deallocated.

CFDictionary provides functions for querying the values of a dictionary. The function [CFDictionaryGetCount](<cfdictionarygetcount(__).md>) returns the number of key-value pairs in a dictionary; the [CFDictionaryContainsValue](<cfdictionarycontainsvalue(____).md>) function checks if a value is in a dictionary; and [CFDictionaryGetKeysAndValues](<cfdictionarygetkeysandvalues(______).md>) returns a C array containing all the values and a C array containing all the keys in a dictionary.

The [CFDictionaryApplyFunction](<cfdictionaryapplyfunction(______).md>) function lets you apply a function to all key-value pairs in a dictionary.

CFDictionary is “toll-free bridged” with its Cocoa Foundation counterpart, [NSDictionary](../foundation/nsdictionary.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSDictionary *` parameter, you can pass in a `CFDictionaryRef`, and in a function where you see a `CFDictionaryRef` parameter, you can pass in an NSDictionary instance. This also applies to concrete subclasses of NSDictionary. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Inherited By**: [CFMutableDictionary](cfmutabledictionary.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a dictionary

- [CFDictionaryCreate](<cfdictionarycreate(____________).md>) — Creates an immutable dictionary containing the specified key-value pairs.
- [CFDictionaryCreateCopy](<cfdictionarycreatecopy(____).md>) — Creates and returns a new immutable dictionary with the key-value pairs of another dictionary.

### Examining a dictionary

- [CFDictionaryContainsKey](<cfdictionarycontainskey(____).md>) — Returns a Boolean value that indicates whether a given key is in a dictionary.
- [CFDictionaryContainsValue](<cfdictionarycontainsvalue(____).md>) — Returns a Boolean value that indicates whether a given value is in a dictionary.
- [CFDictionaryGetCount](<cfdictionarygetcount(__).md>) — Returns the number of key-value pairs in a dictionary.
- [CFDictionaryGetCountOfKey](<cfdictionarygetcountofkey(____).md>) — Returns the number of times a key occurs in a dictionary.
- [CFDictionaryGetCountOfValue](<cfdictionarygetcountofvalue(____).md>) — Counts the number of times a given value occurs in the dictionary.
- [CFDictionaryGetKeysAndValues](<cfdictionarygetkeysandvalues(______).md>) — Fills two buffers with the keys and values from a dictionary.
- [CFDictionaryGetValue](<cfdictionarygetvalue(____).md>) — Returns the value associated with a given key.
- [CFDictionaryGetValueIfPresent](<cfdictionarygetvalueifpresent(______).md>) — Returns a Boolean value that indicates whether a given value for a given key is in a dictionary, and returns that value indirectly if it exists.

### Applying a function to a dictionary

- [CFDictionaryApplyFunction](<cfdictionaryapplyfunction(______).md>) — Calls a function once for each key-value pair in a dictionary.

### Getting the CFDictionary type ID

- [CFDictionaryGetTypeID](<cfdictionarygettypeid().md>) — Returns the type identifier for the CFDictionary opaque type.

### Callbacks

- [CFDictionaryApplierFunction](cfdictionaryapplierfunction.md) — Prototype of a callback function that may be applied to every key-value pair in a dictionary.
- [CFDictionaryCopyDescriptionCallBack](cfdictionarycopydescriptioncallback.md) — Prototype of a callback function used to get a description of a value or key in a dictionary.
- [CFDictionaryEqualCallBack](cfdictionaryequalcallback.md) — Prototype of a callback function used to determine if two values or keys in a dictionary are equal.
- [CFDictionaryHashCallBack](cfdictionaryhashcallback.md) — Prototype of a callback function invoked to compute a hash code for a key. Hash codes are used when key-value pairs are accessed, added, or removed from a collection.
- [CFDictionaryReleaseCallBack](cfdictionaryreleasecallback.md) — Prototype of a callback function used to release a key-value pair before it’s removed from a dictionary.
- [CFDictionaryRetainCallBack](cfdictionaryretaincallback.md) — Prototype of a callback function used to retain a value or key being added to a dictionary.

### Data Types

- [CFDictionaryKeyCallBacks](cfdictionarykeycallbacks.md) — This structure contains the callbacks used to retain, release, describe, and compare the keys in a dictionary.
- [CFDictionaryValueCallBacks](cfdictionaryvaluecallbacks.md) — This structure contains the callbacks used to retain, release, describe, and compare the values in a dictionary.

### Constants

- [Predefined Callback Structures](cfdictionary-predefined-callback-structures.md) — CFDictionary provides some predefined callbacks for your convenience.

## See Also

### Related Documentation

- [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
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
- [CFError](cferror.md)
- [CFFileDescriptor](cffiledescriptor.md)

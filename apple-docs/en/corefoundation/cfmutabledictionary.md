---
title: CFMutableDictionary
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmutabledictionary
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmutabledictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmutabledictionary.json'
content_hash: 'sha256:309b29f43e5de990'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMutableDictionary

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFMutableDictionary
```

## Overview

CFMutableDictionary manages dynamic dictionaries. The basic interface for managing dictionaries is provided by [CFDictionary](cfdictionary.md). CFMutableDictionary adds functions to modify the contents of a dictionary.

You create a mutable dictionary object using either the [CFDictionaryCreateMutable](<cfdictionarycreatemutable(________).md>) or [CFDictionaryCreateMutableCopy](<cfdictionarycreatemutablecopy(______).md>) function. You can add key-value pairs using the [CFDictionaryAddValue](<cfdictionaryaddvalue(______).md>) and [CFDictionarySetValue](<cfdictionarysetvalue(______).md>) functions. When adding key-value pairs to a dictionary, the keys and values are not copied—they are retained so they are not invalidated before the dictionary is deallocated. You can remove key-value pairs using the [CFDictionaryRemoveValue](<cfdictionaryremovevalue(____).md>) function. When removing key-value pairs from a dictionary, the keys and values are released.

CFMutableDictionary is “toll-free bridged” with its Cocoa Foundation counterpart, [NSMutableDictionary](../foundation/nsmutabledictionary.md). What this means is that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. This means that in a method where you see an `NSMutableDictionary *` parameter, you can pass in a `CFMutableDictionaryRef`, and in a function where you see a `CFMutableDictionaryRef` parameter, you can pass in an NSMutableDictionary instance. This also applies to concrete subclasses of NSMutableDictionary. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Inherits From**: [CFDictionary](cfdictionary.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Mutable Dictionary

- [CFDictionaryCreateMutable](<cfdictionarycreatemutable(________).md>) — Creates a new mutable dictionary.
- [CFDictionaryCreateMutableCopy](<cfdictionarycreatemutablecopy(______).md>) — Creates a new mutable dictionary with the key-value pairs from another dictionary.

### Modifying a Dictionary

- [CFDictionaryAddValue](<cfdictionaryaddvalue(______).md>) — Adds a key-value pair to a dictionary if the specified key is not already present.
- [CFDictionaryRemoveAllValues](<cfdictionaryremoveallvalues(__).md>) — Removes all the key-value pairs from a dictionary, making it empty.
- [CFDictionaryRemoveValue](<cfdictionaryremovevalue(____).md>) — Removes a key-value pair.
- [CFDictionaryReplaceValue](<cfdictionaryreplacevalue(______).md>) — Replaces a value corresponding to a given key.
- [CFDictionarySetValue](<cfdictionarysetvalue(______).md>) — Sets the value corresponding to a given key.

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
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)

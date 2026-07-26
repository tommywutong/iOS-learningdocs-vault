---
title: CFBitVector
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfbitvector
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbitvector'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbitvector.json'
content_hash: 'sha256:2a716473b290a25f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBitVector

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFBitVector
```

## Overview

CFBitVector and its derived mutable type, [CFMutableBitVector](cfmutablebitvector.md), manage ordered collections of bit values, which are either `0` or `1`. CFBitVector creates static bit vectors and CFMutableBitVector creates dynamic bit vectors.

## Relationships

- **Inherited By**: [CFMutableBitVector](cfmutablebitvector.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Bit Vector

- [CFBitVectorCreate](<cfbitvectorcreate(______).md>) — Creates an immutable bit vector from a block of memory.
- [CFBitVectorCreateCopy](<cfbitvectorcreatecopy(____).md>) — Creates an immutable bit vector that is a copy of another bit vector.

### Getting Information About a Bit Vector

- [CFBitVectorContainsBit](<cfbitvectorcontainsbit(______).md>) — Returns whether a bit vector contains a particular bit value.
- [CFBitVectorGetBitAtIndex](<cfbitvectorgetbitatindex(____).md>) — Returns the bit value at a given index in a bit vector.
- [CFBitVectorGetBits](<cfbitvectorgetbits(______).md>) — Returns the bit values in a range of indices in a bit vector.
- [CFBitVectorGetCount](<cfbitvectorgetcount(__).md>) — Returns the number of bit values in a bit vector.
- [CFBitVectorGetCountOfBit](<cfbitvectorgetcountofbit(______).md>) — Counts the number of times a certain bit value occurs within a range of bits in a bit vector.
- [CFBitVectorGetFirstIndexOfBit](<cfbitvectorgetfirstindexofbit(______).md>) — Locates the first occurrence of a certain bit value within a range of bits in a bit vector.
- [CFBitVectorGetLastIndexOfBit](<cfbitvectorgetlastindexofbit(______).md>) — Locates the last occurrence of a certain bit value within a range of bits in a bit vector.

### Getting the CFBitVector Type ID

- [CFBitVectorGetTypeID](<cfbitvectorgettypeid().md>) — Returns the type identifier for the CFBitVector opaque type.

### Data Types

- [CFBit](cfbit.md) — A binary value of either `0` or `1`.

## See Also

### Related Documentation

- [Collections Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html#//apple_ref/doc/uid/10000124i)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
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

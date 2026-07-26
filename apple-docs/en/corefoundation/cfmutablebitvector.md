---
title: CFMutableBitVector
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfmutablebitvector
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmutablebitvector'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmutablebitvector.json'
content_hash: 'sha256:024b53b125c1719c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMutableBitVector

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFMutableBitVector
```

## Overview

CFMutableBitVector objects manage dynamic bit vectors. The basic interface for managing bit vectors is provided by [CFBitVector](cfbitvector.md). CFMutableBitVector adds functions to modify the contents of a bit vector.

You create a mutable bit vector object using either the [CFBitVectorCreateMutable](<cfbitvectorcreatemutable(____).md>) or [CFBitVectorCreateMutableCopy](<cfbitvectorcreatemutablecopy(______).md>) function. You add to and remove from a bit vector by altering the size of the bit vector with the [CFBitVectorSetCount](<cfbitvectorsetcount(____).md>) function

## Relationships

- **Inherits From**: [CFBitVector](cfbitvector.md)

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a CFMutableBitVector Object

- [CFBitVectorCreateMutable](<cfbitvectorcreatemutable(____).md>) — Creates a mutable bit vector.
- [CFBitVectorCreateMutableCopy](<cfbitvectorcreatemutablecopy(______).md>) — Creates a new mutable bit vector from a pre-existing bit vector.

### Modifying a Bit Vector

- [CFBitVectorFlipBitAtIndex](<cfbitvectorflipbitatindex(____).md>) — Flips a bit value in a bit vector.
- [CFBitVectorFlipBits](<cfbitvectorflipbits(____).md>) — Flips a range of bit values in a bit vector.
- [CFBitVectorSetAllBits](<cfbitvectorsetallbits(____).md>) — Sets all bits in a bit vector to a particular value.
- [CFBitVectorSetBitAtIndex](<cfbitvectorsetbitatindex(______).md>) — Sets the value of a particular bit in a bit vector.
- [CFBitVectorSetBits](<cfbitvectorsetbits(______).md>) — Sets a range of bits in a bit vector to a particular value.
- [CFBitVectorSetCount](<cfbitvectorsetcount(____).md>) — Changes the size of a mutable bit vector.

## See Also

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

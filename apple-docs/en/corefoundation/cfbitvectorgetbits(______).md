---
title: 'CFBitVectorGetBits(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbitvectorgetbits(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbitvectorgetbits(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbitvectorgetbits%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:217f77876880f775'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBitVectorGetBits(_:_:_:)

<sub>Function</sub>

Returns the bit values in a range of indices in a bit vector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBitVectorGetBits(_ bv: CFBitVector!, _ range: CFRange, _ bytes: UnsafeMutablePointer<UInt8>!)
```

## Parameters

- `bv` — The bit vector to examine.

- `range` — The range of bit values to return.

- `bytes` — On return, contains the requested bit values from `bv`. This argument must point to enough memory to hold the number of bits requested. The requested bits are left-aligned with the first requested bit stored in the left-most, or most-significant, bit of the byte stream.

## See Also

### Getting Information About a Bit Vector

- [CFBitVectorContainsBit](<cfbitvectorcontainsbit(______).md>) — Returns whether a bit vector contains a particular bit value.
- [CFBitVectorGetBitAtIndex](<cfbitvectorgetbitatindex(____).md>) — Returns the bit value at a given index in a bit vector.
- [CFBitVectorGetCount](<cfbitvectorgetcount(__).md>) — Returns the number of bit values in a bit vector.
- [CFBitVectorGetCountOfBit](<cfbitvectorgetcountofbit(______).md>) — Counts the number of times a certain bit value occurs within a range of bits in a bit vector.
- [CFBitVectorGetFirstIndexOfBit](<cfbitvectorgetfirstindexofbit(______).md>) — Locates the first occurrence of a certain bit value within a range of bits in a bit vector.
- [CFBitVectorGetLastIndexOfBit](<cfbitvectorgetlastindexofbit(______).md>) — Locates the last occurrence of a certain bit value within a range of bits in a bit vector.

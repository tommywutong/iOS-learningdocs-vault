---
title: 'CFBitVectorGetFirstIndexOfBit(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbitvectorgetfirstindexofbit(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbitvectorgetfirstindexofbit(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbitvectorgetfirstindexofbit%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ddc7cd524c4b6fcc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBitVectorGetFirstIndexOfBit(_:_:_:)

<sub>Function</sub>

Locates the first occurrence of a certain bit value within a range of bits in a bit vector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBitVectorGetFirstIndexOfBit(_ bv: CFBitVector!, _ range: CFRange, _ value: CFBit) -> CFIndex
```

## Parameters

- `bv` — The bit vector to examine.

- `range` — The range of bits in `bv` to search.

- `value` — The bit value for which to search.

## Return Value

The index of the first occurrence of `value` in the specified range of `bv`, or `kCFNotFound` if `value` is not present.

## See Also

### Getting Information About a Bit Vector

- [CFBitVectorContainsBit](<cfbitvectorcontainsbit(______).md>) — Returns whether a bit vector contains a particular bit value.
- [CFBitVectorGetBitAtIndex](<cfbitvectorgetbitatindex(____).md>) — Returns the bit value at a given index in a bit vector.
- [CFBitVectorGetBits](<cfbitvectorgetbits(______).md>) — Returns the bit values in a range of indices in a bit vector.
- [CFBitVectorGetCount](<cfbitvectorgetcount(__).md>) — Returns the number of bit values in a bit vector.
- [CFBitVectorGetCountOfBit](<cfbitvectorgetcountofbit(______).md>) — Counts the number of times a certain bit value occurs within a range of bits in a bit vector.
- [CFBitVectorGetLastIndexOfBit](<cfbitvectorgetlastindexofbit(______).md>) — Locates the last occurrence of a certain bit value within a range of bits in a bit vector.

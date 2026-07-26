---
title: 'CFBitVectorContainsBit(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbitvectorcontainsbit(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbitvectorcontainsbit(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbitvectorcontainsbit%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0b37f2b73c193556'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBitVectorContainsBit(_:_:_:)

<sub>Function</sub>

Returns whether a bit vector contains a particular bit value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBitVectorContainsBit(_ bv: CFBitVector!, _ range: CFRange, _ value: CFBit) -> Bool
```

## Parameters

- `bv` — The bit vector to search.

- `range` — The range of bits in `bv` to search.

- `value` — The bit value for which to search.

## Return Value

`true` if the specified range of bits in `bv` contains `value`, otherwise `false`.

## See Also

### Getting Information About a Bit Vector

- [CFBitVectorGetBitAtIndex](<cfbitvectorgetbitatindex(____).md>) — Returns the bit value at a given index in a bit vector.
- [CFBitVectorGetBits](<cfbitvectorgetbits(______).md>) — Returns the bit values in a range of indices in a bit vector.
- [CFBitVectorGetCount](<cfbitvectorgetcount(__).md>) — Returns the number of bit values in a bit vector.
- [CFBitVectorGetCountOfBit](<cfbitvectorgetcountofbit(______).md>) — Counts the number of times a certain bit value occurs within a range of bits in a bit vector.
- [CFBitVectorGetFirstIndexOfBit](<cfbitvectorgetfirstindexofbit(______).md>) — Locates the first occurrence of a certain bit value within a range of bits in a bit vector.
- [CFBitVectorGetLastIndexOfBit](<cfbitvectorgetlastindexofbit(______).md>) — Locates the last occurrence of a certain bit value within a range of bits in a bit vector.

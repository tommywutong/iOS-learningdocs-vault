---
title: 'CFBitVectorGetCount(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbitvectorgetcount(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbitvectorgetcount(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbitvectorgetcount%28_%3A%29.json'
content_hash: 'sha256:10dda2ac94362955'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBitVectorGetCount(_:)

<sub>Function</sub>

Returns the number of bit values in a bit vector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBitVectorGetCount(_ bv: CFBitVector!) -> CFIndex
```

## Parameters

- `bv` — The bit vector to examine.

## Return Value

The current size of `bv`.

## See Also

### Getting Information About a Bit Vector

- [CFBitVectorContainsBit](<cfbitvectorcontainsbit(______).md>) — Returns whether a bit vector contains a particular bit value.
- [CFBitVectorGetBitAtIndex](<cfbitvectorgetbitatindex(____).md>) — Returns the bit value at a given index in a bit vector.
- [CFBitVectorGetBits](<cfbitvectorgetbits(______).md>) — Returns the bit values in a range of indices in a bit vector.
- [CFBitVectorGetCountOfBit](<cfbitvectorgetcountofbit(______).md>) — Counts the number of times a certain bit value occurs within a range of bits in a bit vector.
- [CFBitVectorGetFirstIndexOfBit](<cfbitvectorgetfirstindexofbit(______).md>) — Locates the first occurrence of a certain bit value within a range of bits in a bit vector.
- [CFBitVectorGetLastIndexOfBit](<cfbitvectorgetlastindexofbit(______).md>) — Locates the last occurrence of a certain bit value within a range of bits in a bit vector.

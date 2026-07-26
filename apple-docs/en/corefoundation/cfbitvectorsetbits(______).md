---
title: 'CFBitVectorSetBits(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbitvectorsetbits(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbitvectorsetbits(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbitvectorsetbits%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4dbdeb117f2726c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBitVectorSetBits(_:_:_:)

<sub>Function</sub>

Sets a range of bits in a bit vector to a particular value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBitVectorSetBits(_ bv: CFMutableBitVector!, _ range: CFRange, _ value: CFBit)
```

## Parameters

- `bv` — The bit vector to modify.

- `range` — The range of bits to set. The range must not exceed `0…N-1`, where `N` is the count of the vector.

- `value` — The bit value to which to set the range of bits.

## See Also

### Related Documentation

- [CFBitVectorGetCount](<cfbitvectorgetcount(__).md>) — Returns the number of bit values in a bit vector.

### Modifying a Bit Vector

- [CFBitVectorFlipBitAtIndex](<cfbitvectorflipbitatindex(____).md>) — Flips a bit value in a bit vector.
- [CFBitVectorFlipBits](<cfbitvectorflipbits(____).md>) — Flips a range of bit values in a bit vector.
- [CFBitVectorSetAllBits](<cfbitvectorsetallbits(____).md>) — Sets all bits in a bit vector to a particular value.
- [CFBitVectorSetBitAtIndex](<cfbitvectorsetbitatindex(______).md>) — Sets the value of a particular bit in a bit vector.
- [CFBitVectorSetCount](<cfbitvectorsetcount(____).md>) — Changes the size of a mutable bit vector.

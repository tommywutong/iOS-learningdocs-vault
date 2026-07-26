---
title: 'CFBitVectorFlipBitAtIndex(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbitvectorflipbitatindex(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbitvectorflipbitatindex(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbitvectorflipbitatindex%28_%3A_%3A%29.json'
content_hash: 'sha256:52248e1fa6756716'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBitVectorFlipBitAtIndex(_:_:)

<sub>Function</sub>

Flips a bit value in a bit vector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBitVectorFlipBitAtIndex(_ bv: CFMutableBitVector!, _ idx: CFIndex)
```

## Parameters

- `bv` — The bit vector to modify.

- `idx` — The index of the bit value to flip. The index must be in the range `0…N-1`, where `N` is the count of the vector.

## See Also

### Related Documentation

- [CFBitVectorGetCount](<cfbitvectorgetcount(__).md>) — Returns the number of bit values in a bit vector.

### Modifying a Bit Vector

- [CFBitVectorFlipBits](<cfbitvectorflipbits(____).md>) — Flips a range of bit values in a bit vector.
- [CFBitVectorSetAllBits](<cfbitvectorsetallbits(____).md>) — Sets all bits in a bit vector to a particular value.
- [CFBitVectorSetBitAtIndex](<cfbitvectorsetbitatindex(______).md>) — Sets the value of a particular bit in a bit vector.
- [CFBitVectorSetBits](<cfbitvectorsetbits(______).md>) — Sets a range of bits in a bit vector to a particular value.
- [CFBitVectorSetCount](<cfbitvectorsetcount(____).md>) — Changes the size of a mutable bit vector.

---
title: 'CFBitVectorSetCount(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbitvectorsetcount(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbitvectorsetcount(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbitvectorsetcount%28_%3A_%3A%29.json'
content_hash: 'sha256:782785a30dc5f839'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBitVectorSetCount(_:_:)

<sub>Function</sub>

Changes the size of a mutable bit vector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBitVectorSetCount(_ bv: CFMutableBitVector!, _ count: CFIndex)
```

## Parameters

- `bv` — The bit vector to modify.

- `count` — The new size for `bv`. If `count` is greater than the current size of `bv`, the additional bit values are set to `0`.

## Discussion

If `bv` was created with a fixed capacity, you cannot increase its size beyond that capacity.

## See Also

### Related Documentation

- [CFBitVectorCreateMutable](<cfbitvectorcreatemutable(____).md>) — Creates a mutable bit vector.
- [CFBitVectorCreateMutableCopy](<cfbitvectorcreatemutablecopy(______).md>) — Creates a new mutable bit vector from a pre-existing bit vector.
- [CFBitVectorGetCount](<cfbitvectorgetcount(__).md>) — Returns the number of bit values in a bit vector.

### Modifying a Bit Vector

- [CFBitVectorFlipBitAtIndex](<cfbitvectorflipbitatindex(____).md>) — Flips a bit value in a bit vector.
- [CFBitVectorFlipBits](<cfbitvectorflipbits(____).md>) — Flips a range of bit values in a bit vector.
- [CFBitVectorSetAllBits](<cfbitvectorsetallbits(____).md>) — Sets all bits in a bit vector to a particular value.
- [CFBitVectorSetBitAtIndex](<cfbitvectorsetbitatindex(______).md>) — Sets the value of a particular bit in a bit vector.
- [CFBitVectorSetBits](<cfbitvectorsetbits(______).md>) — Sets a range of bits in a bit vector to a particular value.

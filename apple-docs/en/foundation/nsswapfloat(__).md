---
title: 'NSSwapFloat(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsswapfloat(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsswapfloat(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsswapfloat%28_%3A%29.json'
content_hash: 'sha256:f326f7a2214b7630'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSwapFloat(_:)

<sub>Function</sub>

Swaps the bytes of a number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSSwapFloat(_ x: NSSwappedFloat) -> NSSwappedFloat
```

## Discussion

Swaps the bytes of `x` and returns the resulting value. Bytes are swapped from each low-order position to the corresponding high-order position and vice versa. For example, if the bytes of `x` are numbered from 1 to 4, this function swaps bytes 1 and 4, and bytes 2 and 3.

## See Also

### Related Documentation

- [NSSwapLong](<nsswaplong(__).md>) — Swaps the bytes of a number.
- [NSSwapDouble](<nsswapdouble(__).md>) — Swaps the bytes of a number.

### Functions

- [NSConvertHostDoubleToSwapped](<nsconverthostdoubletoswapped(__).md>) — Performs a type conversion.
- [NSConvertHostFloatToSwapped](<nsconverthostfloattoswapped(__).md>) — Performs a type conversion.
- [NSConvertSwappedDoubleToHost](<nsconvertswappeddoubletohost(__).md>) — Performs a type conversion.
- [NSConvertSwappedFloatToHost](<nsconvertswappedfloattohost(__).md>) — Performs a type conversion.
- [NSHostByteOrder](<nshostbyteorder().md>) — Returns the endian format.
- [NSSwapBigDoubleToHost](<nsswapbigdoubletohost(__).md>) — Swaps the bytes of a number.
- [NSSwapBigFloatToHost](<nsswapbigfloattohost(__).md>) — Swaps the bytes of a number.
- [NSSwapBigIntToHost](<nsswapbiginttohost(__).md>) — Swaps the bytes of a number.
- [NSSwapBigLongLongToHost](<nsswapbiglonglongtohost(__).md>) — Swaps the bytes of a number.
- [NSSwapBigLongToHost](<nsswapbiglongtohost(__).md>) — Swaps the bytes of a number.
- [NSSwapBigShortToHost](<nsswapbigshorttohost(__).md>) — Swaps the bytes of a number.
- [NSSwapDouble](<nsswapdouble(__).md>) — Swaps the bytes of a number.
- [NSSwapHostDoubleToBig](<nsswaphostdoubletobig(__).md>) — Swaps the bytes of a number.
- [NSSwapHostDoubleToLittle](<nsswaphostdoubletolittle(__).md>) — Swaps the bytes of a number.
- [NSSwapHostFloatToBig](<nsswaphostfloattobig(__).md>) — Swaps the bytes of a number.

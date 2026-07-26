---
title: 'NSSwapLittleLongToHost(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsswaplittlelongtohost(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsswaplittlelongtohost(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsswaplittlelongtohost%28_%3A%29.json'
content_hash: 'sha256:3371eb72e5962a9f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSwapLittleLongToHost(_:)

<sub>Function</sub>

Swaps the bytes of a number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSSwapLittleLongToHost(_ x: UInt) -> UInt
```

## Discussion

Converts the little-endian formatted value in `x` to the current endian format and returns the resulting value. If it is necessary to swap the bytes of x, this function calls [NSSwapLong](<nsswaplong(__).md>) to perform the swap.

## See Also

### Related Documentation

- [NSSwapLong](<nsswaplong(__).md>) — Swaps the bytes of a number.
- [NSSwapHostLongToLittle](<nsswaphostlongtolittle(__).md>) — Swaps the bytes of a number.
- [NSSwapBigLongToHost](<nsswapbiglongtohost(__).md>) — Swaps the bytes of a number.

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
- [NSSwapFloat](<nsswapfloat(__).md>) — Swaps the bytes of a number.
- [NSSwapHostDoubleToBig](<nsswaphostdoubletobig(__).md>) — Swaps the bytes of a number.
- [NSSwapHostDoubleToLittle](<nsswaphostdoubletolittle(__).md>) — Swaps the bytes of a number.

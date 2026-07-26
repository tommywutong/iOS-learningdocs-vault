---
title: 'NSSwapBigLongLongToHost(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsswapbiglonglongtohost(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsswapbiglonglongtohost(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsswapbiglonglongtohost%28_%3A%29.json'
content_hash: 'sha256:8ee9b5a93088d548'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSwapBigLongLongToHost(_:)

<sub>Function</sub>

Swaps the bytes of a number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSSwapBigLongLongToHost(_ x: UInt64) -> UInt64
```

## Discussion

Converts the big-endian value in `x` to the current endian format and returns the resulting value. If it is necessary to swap the bytes of `x`, this function calls [NSSwapLongLong](<nsswaplonglong(__).md>) to perform the swap.

## See Also

### Related Documentation

- [NSSwapLittleLongLongToHost](<nsswaplittlelonglongtohost(__).md>) — Swaps the bytes of a number.
- [NSSwapHostLongLongToBig](<nsswaphostlonglongtobig(__).md>) — Swaps the bytes of a number.

### Functions

- [NSConvertHostDoubleToSwapped](<nsconverthostdoubletoswapped(__).md>) — Performs a type conversion.
- [NSConvertHostFloatToSwapped](<nsconverthostfloattoswapped(__).md>) — Performs a type conversion.
- [NSConvertSwappedDoubleToHost](<nsconvertswappeddoubletohost(__).md>) — Performs a type conversion.
- [NSConvertSwappedFloatToHost](<nsconvertswappedfloattohost(__).md>) — Performs a type conversion.
- [NSHostByteOrder](<nshostbyteorder().md>) — Returns the endian format.
- [NSSwapBigDoubleToHost](<nsswapbigdoubletohost(__).md>) — Swaps the bytes of a number.
- [NSSwapBigFloatToHost](<nsswapbigfloattohost(__).md>) — Swaps the bytes of a number.
- [NSSwapBigIntToHost](<nsswapbiginttohost(__).md>) — Swaps the bytes of a number.
- [NSSwapBigLongToHost](<nsswapbiglongtohost(__).md>) — Swaps the bytes of a number.
- [NSSwapBigShortToHost](<nsswapbigshorttohost(__).md>) — Swaps the bytes of a number.
- [NSSwapDouble](<nsswapdouble(__).md>) — Swaps the bytes of a number.
- [NSSwapFloat](<nsswapfloat(__).md>) — Swaps the bytes of a number.
- [NSSwapHostDoubleToBig](<nsswaphostdoubletobig(__).md>) — Swaps the bytes of a number.
- [NSSwapHostDoubleToLittle](<nsswaphostdoubletolittle(__).md>) — Swaps the bytes of a number.
- [NSSwapHostFloatToBig](<nsswaphostfloattobig(__).md>) — Swaps the bytes of a number.

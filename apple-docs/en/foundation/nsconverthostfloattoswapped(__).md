---
title: 'NSConvertHostFloatToSwapped(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsconverthostfloattoswapped(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsconverthostfloattoswapped(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconverthostfloattoswapped%28_%3A%29.json'
content_hash: 'sha256:67175c8251f7e959'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSConvertHostFloatToSwapped(_:)

<sub>Function</sub>

Performs a type conversion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSConvertHostFloatToSwapped(_ x: Float) -> NSSwappedFloat
```

## Discussion

Converts the float value in `x` to a value whose bytes can be swapped. This function does not actually swap the bytes of `x`. You should not need to call this function directly.

## See Also

### Related Documentation

- [NSSwapHostFloatToBig](<nsswaphostfloattobig(__).md>) — Swaps the bytes of a number.
- [NSSwapHostFloatToLittle](<nsswaphostfloattolittle(__).md>) — Swaps the bytes of a number.

### Functions

- [NSConvertHostDoubleToSwapped](<nsconverthostdoubletoswapped(__).md>) — Performs a type conversion.
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
- [NSSwapHostFloatToBig](<nsswaphostfloattobig(__).md>) — Swaps the bytes of a number.

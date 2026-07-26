---
title: ulp
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/ulp
source_url: 'https://developer.apple.com/documentation/swift/float16/ulp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/ulp.json'
content_hash: 'sha256:cc46f38744774692'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# ulp

<sub>Instance Property</sub>

The unit in the last place of this value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var ulp: Float16 { get }
```

## Discussion

This is the unit of the least significant digit in this value’s significand. For most numbers `x`, this is the difference between `x` and the next greater (in magnitude) representable number. There are some edge cases to be aware of:

- If `x` is not a finite number, then `x.ulp` is NaN.
- If `x` is very small in magnitude, then `x.ulp` may be a subnormal number. If a type does not support subnormals, `x.ulp` may be rounded to zero.
- `greatestFiniteMagnitude.ulp` is a finite number, even though the next greater representable value is `infinity`.

See also the `ulpOfOne` static property.

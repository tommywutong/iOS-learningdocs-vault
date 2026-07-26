---
title: 'value(at:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/civector/value(at:)'
source_url: 'https://developer.apple.com/documentation/coreimage/civector/value(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/civector/value%28at%3A%29.json'
content_hash: 'sha256:d16dd5eaf0cdfcaa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIVector](../civector.md)

# value(at:)

<sub>Instance Method</sub>

Returns a value from a specific position in the vector.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func value(at index: Int) -> CGFloat
```

## Parameters

- `index` — The position in the vector of the value that you want to retrieve.

## Return Value

The value retrieved from the vector or `0` if the position is undefined.

## Discussion

The numbering of elements in a vector begins with zero.

## See Also

### Getting Values From a Vector

- [count](count.md) — The number of items in the vector.
- [X](x.md) — The value located in the first position in the vector.
- [Y](y.md) — The value located in the second position in the vector.
- [Z](z.md) — The value located in the third position in the vector.
- [W](w.md) — The value located in the forth position in the vector.
- [stringRepresentation](stringrepresentation.md) — Returns a formatted string with all the values of a `CIVector`.
- [CGAffineTransformValue](cgaffinetransformvalue.md) — Returns the values in the vector as a `CGAffineTransformValue` structure.
- [CGPointValue](cgpointvalue.md) — Returns the values in the vector as a `CGPoint` structure.
- [CGRectValue](cgrectvalue.md) — Returns the values in the vector as a `CGRect` structure.

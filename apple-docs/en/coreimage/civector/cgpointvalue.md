---
title: cgPointValue
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/civector/cgpointvalue
source_url: 'https://developer.apple.com/documentation/coreimage/civector/cgpointvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/civector/cgpointvalue.json'
content_hash: 'sha256:3d46e6c1f04cb020'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIVector](../civector.md)

# cgPointValue

<sub>Instance Property</sub>

Returns the values in the vector as a `CGPoint` structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var cgPointValue: CGPoint { get }
```

## Return Value

Reading this property returns a `CGPoint` structure from the `X` and `Y` values from the vector.

## See Also

### Getting Values From a Vector

- [- valueAtIndex:](<value(at_).md>) — Returns a value from a specific position in the vector.
- [count](count.md) — The number of items in the vector.
- [X](x.md) — The value located in the first position in the vector.
- [Y](y.md) — The value located in the second position in the vector.
- [Z](z.md) — The value located in the third position in the vector.
- [W](w.md) — The value located in the forth position in the vector.
- [stringRepresentation](stringrepresentation.md) — Returns a formatted string with all the values of a `CIVector`.
- [CGAffineTransformValue](cgaffinetransformvalue.md) — Returns the values in the vector as a `CGAffineTransformValue` structure.
- [CGRectValue](cgrectvalue.md) — Returns the values in the vector as a `CGRect` structure.

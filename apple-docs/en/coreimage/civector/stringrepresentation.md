---
title: stringRepresentation
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/civector/stringrepresentation
source_url: 'https://developer.apple.com/documentation/coreimage/civector/stringrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/civector/stringrepresentation.json'
content_hash: 'sha256:b258479c9ac2c3ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIVector](../civector.md)

# stringRepresentation

<sub>Instance Property</sub>

Returns a formatted string with all the values of a `CIVector`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var stringRepresentation: String { get }
```

## Discussion

Some example string representations of vectors:

| `CIVector` | `stringRepresentation` |
|---|---|
| `[CIVector vectorWithX:1.0 Y:0.5 Z:0.3]` | `"[1.0 0.5 0.3]"` |
| `[CIVector vectorWithX:10.0 Y:23.0]` | `"[10.0 23.0]"` |

To create a [CIVector](../civector.md) object from a string representation, use the [vectorWithString:](vectorwithstring_.md) method.

## See Also

### Getting Values From a Vector

- [- valueAtIndex:](<value(at_).md>) — Returns a value from a specific position in the vector.
- [count](count.md) — The number of items in the vector.
- [X](x.md) — The value located in the first position in the vector.
- [Y](y.md) — The value located in the second position in the vector.
- [Z](z.md) — The value located in the third position in the vector.
- [W](w.md) — The value located in the forth position in the vector.
- [CGAffineTransformValue](cgaffinetransformvalue.md) — Returns the values in the vector as a `CGAffineTransformValue` structure.
- [CGPointValue](cgpointvalue.md) — Returns the values in the vector as a `CGPoint` structure.
- [CGRectValue](cgrectvalue.md) — Returns the values in the vector as a `CGRect` structure.

---
title: cgAffineTransformValue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsvalue/cgaffinetransformvalue
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/cgaffinetransformvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/cgaffinetransformvalue.json'
content_hash: 'sha256:2917fdb02c1d45a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# cgAffineTransformValue

<sub>Instance Property</sub>

Returns the CoreGraphics affine transform representation of the value.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var cgAffineTransformValue: CGAffineTransform { get }
```

## Return Value

The CoreGraphics affine transform representation of the value.

## See Also

### Related Documentation

- [CGAffineTransform](../../coregraphics/cgaffinetransform.md) — An affine transformation matrix for use in drawing 2D graphics.

### Working with CoreGraphics Geometry Values

- [+ valueWithCGPoint:](<init(cgpoint_).md>) — Creates a new value object containing the specified CoreGraphics point structure.
- [+ valueWithCGVector:](<init(cgvector_).md>) — Creates a new value object containing the specified CoreGraphics vector structure.
- [+ valueWithCGSize:](<init(cgsize_).md>) — Creates a new value object containing the specified CoreGraphics size structure.
- [+ valueWithCGRect:](<init(cgrect_).md>) — Creates a new value object containing the specified CoreGraphics rectangle structure.
- [+ valueWithCGAffineTransform:](<init(cgaffinetransform_).md>) — Creates a new value object containing the specified CoreGraphics affine transform structure.
- [CGPointValue](cgpointvalue.md) — Returns the CoreGraphics point structure representation of the value.
- [CGVectorValue](cgvectorvalue.md) — Returns the CoreGraphics vector structure representation of the value.
- [CGSizeValue](cgsizevalue.md) — Returns the CoreGraphics size structure representation of the value.
- [CGRectValue](cgrectvalue.md) — Returns the CoreGraphics rectangle structure representation of the value.

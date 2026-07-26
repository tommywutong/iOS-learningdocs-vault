---
title: cgVectorValue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsvalue/cgvectorvalue
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/cgvectorvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/cgvectorvalue.json'
content_hash: 'sha256:540941408c3c8c8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# cgVectorValue

<sub>Instance Property</sub>

Returns the CoreGraphics vector structure representation of the value.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var cgVectorValue: CGVector { get }
```

## Return Value

The CoreGraphics vector structure representation of the value.

## See Also

### Related Documentation

- [CGVector](../../corefoundation/cgvector.md) — A structure that contains a two-dimensional vector.

### Working with CoreGraphics Geometry Values

- [+ valueWithCGPoint:](<init(cgpoint_).md>) — Creates a new value object containing the specified CoreGraphics point structure.
- [+ valueWithCGVector:](<init(cgvector_).md>) — Creates a new value object containing the specified CoreGraphics vector structure.
- [+ valueWithCGSize:](<init(cgsize_).md>) — Creates a new value object containing the specified CoreGraphics size structure.
- [+ valueWithCGRect:](<init(cgrect_).md>) — Creates a new value object containing the specified CoreGraphics rectangle structure.
- [+ valueWithCGAffineTransform:](<init(cgaffinetransform_).md>) — Creates a new value object containing the specified CoreGraphics affine transform structure.
- [CGPointValue](cgpointvalue.md) — Returns the CoreGraphics point structure representation of the value.
- [CGSizeValue](cgsizevalue.md) — Returns the CoreGraphics size structure representation of the value.
- [CGRectValue](cgrectvalue.md) — Returns the CoreGraphics rectangle structure representation of the value.
- [CGAffineTransformValue](cgaffinetransformvalue.md) — Returns the CoreGraphics affine transform representation of the value.

---
title: cgSizeValue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsvalue/cgsizevalue
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/cgsizevalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/cgsizevalue.json'
content_hash: 'sha256:1bf247aa39af91bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# cgSizeValue

<sub>Instance Property</sub>

Returns the CoreGraphics size structure representation of the value.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var cgSizeValue: CGSize { get }
```

## Return Value

The CoreGraphics size structure representation of the value.

## See Also

### Related Documentation

- [CGSize](../../corefoundation/cgsize.md) — A structure that contains width and height values.

### Working with CoreGraphics Geometry Values

- [+ valueWithCGPoint:](<init(cgpoint_).md>) — Creates a new value object containing the specified CoreGraphics point structure.
- [+ valueWithCGVector:](<init(cgvector_).md>) — Creates a new value object containing the specified CoreGraphics vector structure.
- [+ valueWithCGSize:](<init(cgsize_).md>) — Creates a new value object containing the specified CoreGraphics size structure.
- [+ valueWithCGRect:](<init(cgrect_).md>) — Creates a new value object containing the specified CoreGraphics rectangle structure.
- [+ valueWithCGAffineTransform:](<init(cgaffinetransform_).md>) — Creates a new value object containing the specified CoreGraphics affine transform structure.
- [CGPointValue](cgpointvalue.md) — Returns the CoreGraphics point structure representation of the value.
- [CGVectorValue](cgvectorvalue.md) — Returns the CoreGraphics vector structure representation of the value.
- [CGRectValue](cgrectvalue.md) — Returns the CoreGraphics rectangle structure representation of the value.
- [CGAffineTransformValue](cgaffinetransformvalue.md) — Returns the CoreGraphics affine transform representation of the value.

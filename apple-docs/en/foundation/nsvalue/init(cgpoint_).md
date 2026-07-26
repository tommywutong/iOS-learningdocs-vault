---
title: 'init(CGPoint:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/init(cgpoint:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/init(cgpoint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/init%28cgpoint%3A%29.json'
content_hash: 'sha256:36ab7d3103feab07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# init(CGPoint:)

<sub>Initializer</sub>

Creates a new value object containing the specified CoreGraphics point structure.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(CGPoint point: CGPoint)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(cgPoint point: CGPoint)
```

## Parameters

- `point` — The value for the new object.

## Return Value

A new value object that contains the point information.

## See Also

### Related Documentation

- [CGPoint](../../corefoundation/cgpoint.md)

### Working with CoreGraphics Geometry Values

- [+ valueWithCGVector:](<init(cgvector_).md>) — Creates a new value object containing the specified CoreGraphics vector structure.
- [+ valueWithCGSize:](<init(cgsize_).md>) — Creates a new value object containing the specified CoreGraphics size structure.
- [+ valueWithCGRect:](<init(cgrect_).md>) — Creates a new value object containing the specified CoreGraphics rectangle structure.
- [+ valueWithCGAffineTransform:](<init(cgaffinetransform_).md>) — Creates a new value object containing the specified CoreGraphics affine transform structure.
- [CGPointValue](cgpointvalue.md) — Returns the CoreGraphics point structure representation of the value.
- [CGVectorValue](cgvectorvalue.md) — Returns the CoreGraphics vector structure representation of the value.
- [CGSizeValue](cgsizevalue.md) — Returns the CoreGraphics size structure representation of the value.
- [CGRectValue](cgrectvalue.md) — Returns the CoreGraphics rectangle structure representation of the value.
- [CGAffineTransformValue](cgaffinetransformvalue.md) — Returns the CoreGraphics affine transform representation of the value.

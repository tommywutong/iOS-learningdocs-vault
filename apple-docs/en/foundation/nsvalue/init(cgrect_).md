---
title: 'init(CGRect:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/init(cgrect:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/init(cgrect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/init%28cgrect%3A%29.json'
content_hash: 'sha256:42f78a195f3980ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# init(CGRect:)

<sub>Initializer</sub>

Creates a new value object containing the specified CoreGraphics rectangle structure.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(CGRect rect: CGRect)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(cgRect rect: CGRect)
```

## Parameters

- `rect` — The value for the new object.

## Return Value

A new value object that contains the rectangle information.

## See Also

### Related Documentation

- [CGRect](../../corefoundation/cgrect.md)

### Working with CoreGraphics Geometry Values

- [+ valueWithCGPoint:](<init(cgpoint_).md>) — Creates a new value object containing the specified CoreGraphics point structure.
- [+ valueWithCGVector:](<init(cgvector_).md>) — Creates a new value object containing the specified CoreGraphics vector structure.
- [+ valueWithCGSize:](<init(cgsize_).md>) — Creates a new value object containing the specified CoreGraphics size structure.
- [+ valueWithCGAffineTransform:](<init(cgaffinetransform_).md>) — Creates a new value object containing the specified CoreGraphics affine transform structure.
- [CGPointValue](cgpointvalue.md) — Returns the CoreGraphics point structure representation of the value.
- [CGVectorValue](cgvectorvalue.md) — Returns the CoreGraphics vector structure representation of the value.
- [CGSizeValue](cgsizevalue.md) — Returns the CoreGraphics size structure representation of the value.
- [CGRectValue](cgrectvalue.md) — Returns the CoreGraphics rectangle structure representation of the value.
- [CGAffineTransformValue](cgaffinetransformvalue.md) — Returns the CoreGraphics affine transform representation of the value.

---
title: 'vectorWithX:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/civector/vectorwithx:'
source_url: 'https://developer.apple.com/documentation/coreimage/civector/vectorwithx:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/civector/vectorwithx%3A.json'
content_hash: 'sha256:af2741fa87238655'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIVector](../civector.md)

# vectorWithX:

<sub>Type Method</sub>

Create a Core Image vector object that is initialized with one value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (instancetype) vectorWithX:(CGFloat) x;
```

## Parameters

- `x` — The value for the first position in the vector.

## Return Value

An autoreleased [CIVector](../civector.md) object of length 1.

## See Also

### Creating a Vector

- [vectorWithValues:count:](vectorwithvalues_count_.md) — Create a Core Image vector object that is initialized with the specified values.
- [vectorWithX:Y:](vectorwithx_y_.md) — Create a Core Image vector object that is initialized with two values.
- [vectorWithX:Y:Z:](vectorwithx_y_z_.md) — Create a Core Image vector object that is initialized with three values.
- [vectorWithX:Y:Z:W:](vectorwithx_y_z_w_.md) — Create a Core Image vector object that is initialized with four values.
- [vectorWithString:](vectorwithstring_.md) — Create a Core Image vector object with values provided in a string representation.
- [+ vectorWithCGAffineTransform:](<init(cgaffinetransform_)-59e4k.md>) — Create a Core Image vector object that is initialized with six values provided by a `CGAffineTransform` structure.
- [+ vectorWithCGPoint:](<init(cgpoint_)-3mobm.md>) — Create a Core Image vector object that is initialized with two values provided by a `CGPoint` structure.
- [+ vectorWithCGRect:](<init(cgrect_)-3undj.md>) — Create a Core Image vector object that is initialized with four values provided by a `CGRect` structure.

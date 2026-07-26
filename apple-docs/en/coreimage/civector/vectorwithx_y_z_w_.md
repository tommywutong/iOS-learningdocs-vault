---
title: 'vectorWithX:Y:Z:W:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/civector/vectorwithx:y:z:w:'
source_url: 'https://developer.apple.com/documentation/coreimage/civector/vectorwithx:y:z:w:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/civector/vectorwithx%3Ay%3Az%3Aw%3A.json'
content_hash: 'sha256:0cd4bc9dbd9d4281'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIVector](../civector.md)

# vectorWithX:Y:Z:W:

<sub>Type Method</sub>

Create a Core Image vector object that is initialized with four values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (instancetype) vectorWithX:(CGFloat) x Y:(CGFloat) y Z:(CGFloat) z W:(CGFloat) w;
```

## Parameters

- `x` — The value for the first position in the vector.

- `y` — The value for the second position in the vector.

- `z` — The value for the third position in the vector.

- `w` — The value for the forth position in the vector.

## Return Value

An autoreleased [CIVector](../civector.md) object of length 4.

## See Also

### Creating a Vector

- [vectorWithValues:count:](vectorwithvalues_count_.md) — Create a Core Image vector object that is initialized with the specified values.
- [vectorWithX:](vectorwithx_.md) — Create a Core Image vector object that is initialized with one value.
- [vectorWithX:Y:](vectorwithx_y_.md) — Create a Core Image vector object that is initialized with two values.
- [vectorWithX:Y:Z:](vectorwithx_y_z_.md) — Create a Core Image vector object that is initialized with three values.
- [vectorWithString:](vectorwithstring_.md) — Create a Core Image vector object with values provided in a string representation.
- [+ vectorWithCGAffineTransform:](<init(cgaffinetransform_)-59e4k.md>) — Create a Core Image vector object that is initialized with six values provided by a `CGAffineTransform` structure.
- [+ vectorWithCGPoint:](<init(cgpoint_)-3mobm.md>) — Create a Core Image vector object that is initialized with two values provided by a `CGPoint` structure.
- [+ vectorWithCGRect:](<init(cgrect_)-3undj.md>) — Create a Core Image vector object that is initialized with four values provided by a `CGRect` structure.

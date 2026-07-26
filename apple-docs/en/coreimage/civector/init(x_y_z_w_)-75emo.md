---
title: 'init(x:y:z:w:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/civector/init(x:y:z:w:)-75emo'
source_url: 'https://developer.apple.com/documentation/coreimage/civector/init(x:y:z:w:)-75emo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/civector/init%28x%3Ay%3Az%3Aw%3A%29-75emo.json'
content_hash: 'sha256:37caf23f57ec59d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIVector](../civector.md)

# init(x:y:z:w:)

<sub>Initializer</sub>

Initialize a Core Image vector object with four values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(x: CGFloat, y: CGFloat, z: CGFloat, w: CGFloat)
```

## Parameters

- `x` — The value for the first position in the vector.

- `y` — The value for the second position in the vector.

- `z` — The value for the third position in the vector.

- `w` — The value for the forth position in the vector.

## Return Value

An initialized [CIVector](../civector.md) object of length 4.

## See Also

### Initializing a Vector

- [- initWithValues:count:](<init(values_count_).md>) — Initialize a Core Image vector object with the specified the values.
- [- initWithX:](<init(x_).md>) — Initialize a Core Image vector object with one value.
- [- initWithX:Y:](<init(x_y_)-4grr.md>) — Initialize a Core Image vector object with two values.
- [- initWithX:Y:Z:](<init(x_y_z_)-zais.md>) — Initialize a Core Image vector object with three values.
- [- initWithString:](<init(string_).md>) — Initialize a Core Image vector object with values provided in a string representation.
- [- initWithCGAffineTransform:](<init(cgaffinetransform_)-6o8gl.md>) — Initialize a Core Image vector object with six values provided by a `CGAffineTransform` structure.
- [- initWithCGPoint:](<init(cgpoint_)-8cf9j.md>) — Initialize a Core Image vector object with two values provided by a `CGPoint` structure.
- [- initWithCGRect:](<init(cgrect_)-6bolw.md>) — Initialize a Core Image vector object with four values provided by a `CGRect` structure.

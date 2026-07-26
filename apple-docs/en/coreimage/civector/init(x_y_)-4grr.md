---
title: 'init(x:y:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/civector/init(x:y:)-4grr'
source_url: 'https://developer.apple.com/documentation/coreimage/civector/init(x:y:)-4grr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/civector/init%28x%3Ay%3A%29-4grr.json'
content_hash: 'sha256:a0ae94824a2cef65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIVector](../civector.md)

# init(x:y:)

<sub>Initializer</sub>

Initialize a Core Image vector object with two values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(x: CGFloat, y: CGFloat)
```

## Parameters

- `x` — The value for the first position in the vector.

- `y` — The value for the second position in the vector.

## Return Value

An initialized [CIVector](../civector.md) object of length 2.

## See Also

### Initializing a Vector

- [- initWithValues:count:](<init(values_count_).md>) — Initialize a Core Image vector object with the specified the values.
- [- initWithX:](<init(x_).md>) — Initialize a Core Image vector object with one value.
- [- initWithX:Y:Z:](<init(x_y_z_)-zais.md>) — Initialize a Core Image vector object with three values.
- [- initWithX:Y:Z:W:](<init(x_y_z_w_)-75emo.md>) — Initialize a Core Image vector object with four values.
- [- initWithString:](<init(string_).md>) — Initialize a Core Image vector object with values provided in a string representation.
- [- initWithCGAffineTransform:](<init(cgaffinetransform_)-6o8gl.md>) — Initialize a Core Image vector object with six values provided by a `CGAffineTransform` structure.
- [- initWithCGPoint:](<init(cgpoint_)-8cf9j.md>) — Initialize a Core Image vector object with two values provided by a `CGPoint` structure.
- [- initWithCGRect:](<init(cgrect_)-6bolw.md>) — Initialize a Core Image vector object with four values provided by a `CGRect` structure.

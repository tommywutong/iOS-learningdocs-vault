---
title: 'init(cgRect:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/civector/init(cgrect:)-6bolw'
source_url: 'https://developer.apple.com/documentation/coreimage/civector/init(cgrect:)-6bolw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/civector/init%28cgrect%3A%29-6bolw.json'
content_hash: 'sha256:15b9f5874b91d39a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIVector](../civector.md)

# init(cgRect:)

<sub>Initializer</sub>

Initialize a Core Image vector object with four values provided by a `CGRect` structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
convenience init(cgRect r: CGRect)
```

## Parameters

- `r` — The `CGRect` structure.

## Return Value

An initialized [CIVector](../civector.md) object of length 4.

## Discussion

The `CGRect` structure’s `x`, `y`, `height` and `width` values are stored in the vector’s four values.

## See Also

### Initializing a Vector

- [- initWithValues:count:](<init(values_count_).md>) — Initialize a Core Image vector object with the specified the values.
- [- initWithX:](<init(x_).md>) — Initialize a Core Image vector object with one value.
- [- initWithX:Y:](<init(x_y_)-4grr.md>) — Initialize a Core Image vector object with two values.
- [- initWithX:Y:Z:](<init(x_y_z_)-zais.md>) — Initialize a Core Image vector object with three values.
- [- initWithX:Y:Z:W:](<init(x_y_z_w_)-75emo.md>) — Initialize a Core Image vector object with four values.
- [- initWithString:](<init(string_).md>) — Initialize a Core Image vector object with values provided in a string representation.
- [- initWithCGAffineTransform:](<init(cgaffinetransform_)-6o8gl.md>) — Initialize a Core Image vector object with six values provided by a `CGAffineTransform` structure.
- [- initWithCGPoint:](<init(cgpoint_)-8cf9j.md>) — Initialize a Core Image vector object with two values provided by a `CGPoint` structure.

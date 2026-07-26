---
title: 'init(cgAffineTransform:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/civector/init(cgaffinetransform:)-6o8gl'
source_url: 'https://developer.apple.com/documentation/coreimage/civector/init(cgaffinetransform:)-6o8gl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/civector/init%28cgaffinetransform%3A%29-6o8gl.json'
content_hash: 'sha256:612724f50a9abf2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIVector](../civector.md)

# init(cgAffineTransform:)

<sub>Initializer</sub>

Initialize a Core Image vector object with six values provided by a `CGAffineTransform` structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
convenience init(cgAffineTransform t: CGAffineTransform)
```

## Parameters

- `t` — The `CGAffineTransform` structure.

## Return Value

An initialized [CIVector](../civector.md) object of length 6.

## Discussion

The `CGAffineTransform` structure’s `a`, `b`, `c`, `c`, `tx` and `ty` values are stored in the vector’s six values.

## See Also

### Initializing a Vector

- [- initWithValues:count:](<init(values_count_).md>) — Initialize a Core Image vector object with the specified the values.
- [- initWithX:](<init(x_).md>) — Initialize a Core Image vector object with one value.
- [- initWithX:Y:](<init(x_y_)-4grr.md>) — Initialize a Core Image vector object with two values.
- [- initWithX:Y:Z:](<init(x_y_z_)-zais.md>) — Initialize a Core Image vector object with three values.
- [- initWithX:Y:Z:W:](<init(x_y_z_w_)-75emo.md>) — Initialize a Core Image vector object with four values.
- [- initWithString:](<init(string_).md>) — Initialize a Core Image vector object with values provided in a string representation.
- [- initWithCGPoint:](<init(cgpoint_)-8cf9j.md>) — Initialize a Core Image vector object with two values provided by a `CGPoint` structure.
- [- initWithCGRect:](<init(cgrect_)-6bolw.md>) — Initialize a Core Image vector object with four values provided by a `CGRect` structure.

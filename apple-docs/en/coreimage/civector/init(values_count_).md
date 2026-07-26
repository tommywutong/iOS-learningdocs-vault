---
title: 'init(values:count:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/civector/init(values:count:)'
source_url: 'https://developer.apple.com/documentation/coreimage/civector/init(values:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/civector/init%28values%3Acount%3A%29.json'
content_hash: 'sha256:9319c3c30fc889d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIVector](../civector.md)

# init(values:count:)

<sub>Initializer</sub>

Initialize a Core Image vector object with the specified the values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(values: UnsafePointer<CGFloat>, count: Int)
```

## Parameters

- `values` — A pointer `CGFloat` values for vector.

- `count` — The number of `CGFloats` specified by the `values` parameter.

## Return Value

An initialized [CIVector](../civector.md) object of length `count`.

## See Also

### Initializing a Vector

- [- initWithX:](<init(x_).md>) — Initialize a Core Image vector object with one value.
- [- initWithX:Y:](<init(x_y_)-4grr.md>) — Initialize a Core Image vector object with two values.
- [- initWithX:Y:Z:](<init(x_y_z_)-zais.md>) — Initialize a Core Image vector object with three values.
- [- initWithX:Y:Z:W:](<init(x_y_z_w_)-75emo.md>) — Initialize a Core Image vector object with four values.
- [- initWithString:](<init(string_).md>) — Initialize a Core Image vector object with values provided in a string representation.
- [- initWithCGAffineTransform:](<init(cgaffinetransform_)-6o8gl.md>) — Initialize a Core Image vector object with six values provided by a `CGAffineTransform` structure.
- [- initWithCGPoint:](<init(cgpoint_)-8cf9j.md>) — Initialize a Core Image vector object with two values provided by a `CGPoint` structure.
- [- initWithCGRect:](<init(cgrect_)-6bolw.md>) — Initialize a Core Image vector object with four values provided by a `CGRect` structure.

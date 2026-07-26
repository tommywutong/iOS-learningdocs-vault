---
title: 'float4(_:_:_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shader/argument/float4(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shader/argument/float4(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shader/argument/float4%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0439d8b5ab78a42c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Shader](../../shader.md) · [Argument](../argument.md)

# float4(_:_:_:_:)

<sub>Type Method</sub>

Returns an argument value representing the MSL value `float4(x, y, z, w)`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@export(implementation) static func float4<T>(_ x: T, _ y: T, _ z: T, _ w: T) -> Shader.Argument where T : BinaryFloatingPoint
```

## See Also

### Creating argument values

- [boundingRect](boundingrect.md) — Returns an argument value representing the bounding rect of the shape or view that the shader is attached to, as `float4(x, y, width, height)`. This value is undefined for shaders that do not have a natural bounding rect (e.g. filter effects drawn into `GraphicsContext`).
- [color(_:)](<color(__).md>) — Returns an argument value representing `color`. When passed to a MSL function it will convert to a `half4` value, as a premultiplied color in the target color space.
- [colorArray(_:)](<colorarray(__).md>) — Returns an argument value defined by the provided array of color values. When passed to an MSL function it will convert to a `device const half4 *ptr, int count` pair of parameters.
- [data(_:)](<data(__).md>) — Returns an argument value defined by the provided data value. When passed to an MSL function it will convert to a `device const void *ptr, int size_in_bytes` pair of parameters.
- [float(_:)](<float(__).md>) — Returns an argument value representing the MSL value `float(x)`.
- [float2(_:)](<float2(__).md>) — Returns an argument value representing the MSL value `float2(point.x, point.y)`.
- [float2(_:_:)](<float2(____).md>) — Returns an argument value representing the MSL value `float2(x, y)`.
- [float3(_:_:_:)](<float3(______).md>) — Returns an argument value representing the MSL value `float3(x, y, z)`.
- [floatArray(_:)](<floatarray(__).md>) — Returns an argument value defined by the provided array of floating point numbers. When passed to an MSL function it will convert to a `device const float *ptr, int count` pair of parameters.
- [image(_:)](<image(__).md>) — Returns an argument value defined by the provided image. When passed to an MSL function it will convert to a `texture2d<half>` value. Currently only one image parameter is supported per `Shader` instance.

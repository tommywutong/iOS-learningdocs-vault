---
title: Shader.Argument
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shader/argument
source_url: 'https://developer.apple.com/documentation/swiftui/shader/argument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shader/argument.json'
content_hash: 'sha256:1284a901425646f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shader](../shader.md)

# Shader.Argument

<sub>Structure</sub>

A single uniform argument value to a shader function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct Argument
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating argument values

- [boundingRect](argument/boundingrect.md) — Returns an argument value representing the bounding rect of the shape or view that the shader is attached to, as `float4(x, y, width, height)`. This value is undefined for shaders that do not have a natural bounding rect (e.g. filter effects drawn into `GraphicsContext`).
- [color(_:)](<argument/color(__).md>) — Returns an argument value representing `color`. When passed to a MSL function it will convert to a `half4` value, as a premultiplied color in the target color space.
- [colorArray(_:)](<argument/colorarray(__).md>) — Returns an argument value defined by the provided array of color values. When passed to an MSL function it will convert to a `device const half4 *ptr, int count` pair of parameters.
- [data(_:)](<argument/data(__).md>) — Returns an argument value defined by the provided data value. When passed to an MSL function it will convert to a `device const void *ptr, int size_in_bytes` pair of parameters.
- [float(_:)](<argument/float(__).md>) — Returns an argument value representing the MSL value `float(x)`.
- [float2(_:)](<argument/float2(__).md>) — Returns an argument value representing the MSL value `float2(point.x, point.y)`.
- [float2(_:_:)](<argument/float2(____).md>) — Returns an argument value representing the MSL value `float2(x, y)`.
- [float3(_:_:_:)](<argument/float3(______).md>) — Returns an argument value representing the MSL value `float3(x, y, z)`.
- [float4(_:_:_:_:)](<argument/float4(________).md>) — Returns an argument value representing the MSL value `float4(x, y, z, w)`.
- [floatArray(_:)](<argument/floatarray(__).md>) — Returns an argument value defined by the provided array of floating point numbers. When passed to an MSL function it will convert to a `device const float *ptr, int count` pair of parameters.
- [image(_:)](<argument/image(__).md>) — Returns an argument value defined by the provided image. When passed to an MSL function it will convert to a `texture2d<half>` value. Currently only one image parameter is supported per `Shader` instance.

## See Also

### Creating a shader

- [init(function:arguments:)](<init(function_arguments_).md>) — Creates a new shader from a function and the uniform argument values to bind to the function.

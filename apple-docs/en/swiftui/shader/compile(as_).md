---
title: 'compile(as:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shader/compile(as:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shader/compile(as:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shader/compile%28as%3A%29.json'
content_hash: 'sha256:74a6ed507a0f5129'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shader](../shader.md)

# compile(as:)

<sub>Instance Method</sub>

Attempts to asynchronously compile a shader function, to minimize the chance of stalling when it is first used for rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func compile(as type: Shader.UsageType) async throws
```

## Parameters

- `type` — How the shader will eventually be used.

## Discussion

Before being available for rendering each shader must be compiled for the current GPU. By default this happens on first use, but that may cause that frame to be delayed waiting for the compiler, i.e. cause a visible “glitch” in animations.

Calling this method for each shader before it’s first used allows the necessary compilation to happen ahead of time, eliminating the delay on the first actual use (provided `compile()` completes before the first use of the shader).

For compilation to be successful the specified usage type must match how the shader is eventually used to render, and its current argument values must match the types of the arguments used when rendering (however array and data sizes may be empty).

For example, to compile a fill shader asynchronously when your app launches:

```swift
Task {
    let shader = ShaderLibrary.example(.color(.clear), .float(0))
    try! await shader.compile(as: .shapeStyle)
}
```

Here the MSL shader function `example` takes two uniform arguments: a color and a numeric value. The placeholder values are replaced with actual values when using the shader, in this case to fill a circle:

```swift
Circle().fill(
    ShaderLibrary.example(.color(.orange), .float(32)))
```

> [!danger] Throws
> An error describing why compilation failed.

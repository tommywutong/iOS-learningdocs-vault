---
title: 'dynamicallyCall(withArguments:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shaderfunction/dynamicallycall(witharguments:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shaderfunction/dynamicallycall(witharguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shaderfunction/dynamicallycall%28witharguments%3A%29.json'
content_hash: 'sha256:118a43fc8a278b41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShaderFunction](../shaderfunction.md)

# dynamicallyCall(withArguments:)

<sub>Instance Method</sub>

Returns a new shader by applying the provided argument values to the referenced function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func dynamicallyCall(withArguments args: [Shader.Argument]) -> Shader
```

## Discussion

Typically this subscript is used implicitly via function-call syntax, for example:

```swift
let shader = ShaderLibrary.default.myFunction(.float(42))
```

which creates a shader passing the value `42` to the first unbound parameter of `myFunction()`.

## See Also

### Configuring a function

- [library](library.md) — The shader library storing the function.
- [name](name.md) — The name of the shader function in the library.

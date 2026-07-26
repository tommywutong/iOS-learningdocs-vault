---
title: ShaderFunction
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shaderfunction
source_url: 'https://developer.apple.com/documentation/swiftui/shaderfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shaderfunction.json'
content_hash: 'sha256:bbfe2d3c25e0e4b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ShaderFunction

<sub>Structure</sub>

A reference to a function in a Metal shader library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@dynamicCallable struct ShaderFunction
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a shader function

- [init(library:name:)](<shaderfunction/init(library_name_).md>) — Creates a new function reference from the provided shader library and function name string.

### Configuring a function

- [library](shaderfunction/library.md) — The shader library storing the function.
- [name](shaderfunction/name.md) — The name of the shader function in the library.
- [dynamicallyCall(withArguments:)](<shaderfunction/dynamicallycall(witharguments_).md>) — Returns a new shader by applying the provided argument values to the referenced function.

## See Also

### Accessing Metal shaders

- [colorEffect(_:isEnabled:)](<view/coloreffect(__isenabled_).md>) — Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [distortionEffect(_:maxSampleOffset:isEnabled:)](<view/distortioneffect(__maxsampleoffset_isenabled_).md>) — Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [layerEffect(_:maxSampleOffset:isEnabled:)](<view/layereffect(__maxsampleoffset_isenabled_).md>) — Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
- [Shader](shader.md) — A reference to a function in a Metal shader library, along with its bound uniform argument values.
- [ShaderLibrary](shaderlibrary.md) — A Metal shader library.

---
title: ShaderLibrary
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shaderlibrary
source_url: 'https://developer.apple.com/documentation/swiftui/shaderlibrary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shaderlibrary.json'
content_hash: 'sha256:9ff794ed44e44412'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ShaderLibrary

<sub>Structure</sub>

A Metal shader library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@dynamicMemberLookup struct ShaderLibrary
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the default shader library

- [default](shaderlibrary/default.md) — The default shader library of the main (i.e. app) bundle.
- [bundle(_:)](<shaderlibrary/bundle(__).md>) — Returns the default shader library of the specified bundle.

### Creating a shader library

- [init(url:)](<shaderlibrary/init(url_).md>) — Creates a new Metal shader library from the contents of `url`, which must be the location  of precompiled Metal library. Functions compiled from the returned library will only be cached as long as the returned library exists.
- [init(data:)](<shaderlibrary/init(data_).md>) — Creates a new Metal shader library from `data`, which must be the contents of precompiled Metal library. Functions compiled from the returned library will only be cached as long as the returned library exists.

### Access shader functions

- [subscript(dynamicMember:)](<shaderlibrary/subscript(dynamicmember_)-swift.type.subscript.md>) — Returns a new shader function representing the stitchable MSL function called `name` in the default shader library.

### Subscripts

- [subscript(dynamicMember:)](<shaderlibrary/subscript(dynamicmember_)-swift.subscript.md>) — Returns a new shader function representing the stitchable MSL function in the library called `name`.

## See Also

### Accessing Metal shaders

- [colorEffect(_:isEnabled:)](<view/coloreffect(__isenabled_).md>) — Returns a new view that applies `shader` to `self` as a filter effect on the color of each pixel.
- [distortionEffect(_:maxSampleOffset:isEnabled:)](<view/distortioneffect(__maxsampleoffset_isenabled_).md>) — Returns a new view that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [layerEffect(_:maxSampleOffset:isEnabled:)](<view/layereffect(__maxsampleoffset_isenabled_).md>) — Returns a new view that applies `shader` to `self` as a filter on the raster layer created from `self`.
- [Shader](shader.md) — A reference to a function in a Metal shader library, along with its bound uniform argument values.
- [ShaderFunction](shaderfunction.md) — A reference to a function in a Metal shader library.

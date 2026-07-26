---
title: 'blur(radius:opaque:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/blur(radius:opaque:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/blur(radius:opaque:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/blur%28radius%3Aopaque%3A%29.json'
content_hash: 'sha256:05ee1b820355196a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# blur(radius:opaque:)

<sub>Instance Method</sub>

Applies a Gaussian blur to the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func blur(radius: CGFloat, opaque: Bool = false) -> some VisualEffect

```

## Parameters

- `radius` — The radial size of the blur. A blur is more diffuse when its radius is large.

- `opaque` — A Boolean value that indicates whether the blur renderer permits transparency in the blur output. Set to `true` to create an opaque blur, or set to `false` to permit transparency.

## Return Value

An effect that blurs the view.

## Discussion

Use `blur(radius:opaque:)` to apply a gaussian blur effect to the rendering of the view.

## See Also

### Applying other effects

- [distortionEffect(_:maxSampleOffset:isEnabled:)](<distortioneffect(__maxsampleoffset_isenabled_).md>) — Returns a new visual effect that applies `shader` to `self` as a geometric distortion effect on the location of each pixel.
- [layerEffect(_:maxSampleOffset:isEnabled:)](<layereffect(__maxsampleoffset_isenabled_).md>) — Returns a new visual effect that applies `shader` to `self` as a filter on the raster layer created from `self`.

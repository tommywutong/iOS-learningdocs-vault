---
title: Gradient.ColorSpace
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gradient/colorspace
source_url: 'https://developer.apple.com/documentation/swiftui/gradient/colorspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gradient/colorspace.json'
content_hash: 'sha256:6a3632023312df4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Gradient](../gradient.md)

# Gradient.ColorSpace

<sub>Structure</sub>

A method of interpolating between the colors in a gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ColorSpace
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting an interpolation method

- [device](colorspace/device.md) — Interpolates gradient colors in the output color space.
- [perceptual](colorspace/perceptual.md) — Interpolates gradient colors in a perceptual color space.

## See Also

### Working with color spaces

- [colorSpace(_:)](<colorspace(__).md>) — Returns a version of the gradient that will use a specified color space for interpolating between its colors.

---
title: Color.ResolvedHDR
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/color/resolvedhdr
source_url: 'https://developer.apple.com/documentation/swiftui/color/resolvedhdr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/resolvedhdr.json'
content_hash: 'sha256:4dd1369faa24ff5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# Color.ResolvedHDR

<sub>Structure</sub>

A concrete color value, including HDR headroom information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct ResolvedHDR
```

## Overview

`Color.ResolvedHDR` is a set of RGBA values that represent a color that can be shown. The color components are stored in the extended sRGB color space and may contain a “headroom” value describing how the color is rendered for displays with different dynamic ranges. This is a low-level type, most colors are represented by the `Color` type.

> [!info] See Also
> `Color.Resolved`, `Color`.

## Relationships

- **Conforms To**: [Animatable](../animatable.md), [BitwiseCopyable](../../swift/bitwisecopyable.md), [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [ShapeStyle](../shapestyle.md)

## Topics

### Creating a concrete color value

- [init(_:headroom:)](<resolvedhdr/init(__headroom_).md>) — Initializes a new resolved color value.

### Getting color properties

- [red](resolvedhdr/red.md) — The amount of red in the color in the extended sRGB color space.
- [green](resolvedhdr/green.md) — The amount of green in the color in the extended sRGB color space.
- [blue](resolvedhdr/blue.md) — The amount of blue in the color in the extended sRGB color space.
- [linearRed](resolvedhdr/linearred.md) — The amount of red in the color in the extended sRGB color space variant with linear gamma.
- [linearGreen](resolvedhdr/lineargreen.md) — The amount of green in the color in the extended sRGB color space variant with linear gamma.
- [linearBlue](resolvedhdr/linearblue.md) — The amount of blue in the color in the extended sRGB color space variant with linear gamma.
- [opacity](resolvedhdr/opacity.md) — The opacity of the color, in the range `0` to `1`.
- [headroom](resolvedhdr/headroom.md) — The content headroom of the color.

## See Also

### Working with high dynamic range (HDR) colors

- [resolveHDR(in:)](<resolvehdr(in_).md>) — Evaluates this color to a resolved color with content headroom, given a set of environment values.
